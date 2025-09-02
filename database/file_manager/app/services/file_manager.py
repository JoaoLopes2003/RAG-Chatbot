import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai
import time
import shutil
import random
from .utils.file_manager_utils import check_missing_conversions, files_for_preload, get_balanced_shuffled_files, create_prompt
from . import myconstants
from .utils.get_files_paths import get_files_paths
from .utils.get_mime_type import get_mime_type
from . import myconstants
from .file import FILE
from .utils.manage_genai_storage import cleanup_all_files, cleanup_file

load_dotenv()
try:
    api_key = os.getenv("API_KEY")
except KeyError:
    print("Error: API_KEY environment variable not set.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name='gemini-1.5-pro-latest'
)

class FILE_MANAGER():

    def __init__(self):
        self.storage_limit = 18 # Gigabytes / The real limit is 20GB but we decided to leave some free space
        self.file_size_limit = 2 # Gigabytes
        self.file_lifetime_in_cloud = 48 # Hours
        self.total_used_memory = 0
        self.original_files_folder_path = myconstants.ORIGINAL_FILES_FOLDER
        self.md_files_folder_path = myconstants.CONVERTED_FILES
        self.unprocessed_files_folder_path = myconstants.UNPROCESS_FILES_DIR
        self.modify_files_folder_path = myconstants.MODIFY_FILES_DIR
        self.files = {} # Map: folder -> Map: filename -> FILE_OBJECT

        print("Initializing file manager...", flush=True)

        # Delete any existing files in the cloud
        print("=> Cleaning the gemini cloud storage... ", flush=True, end="")
        cleanup_all_files()
        print("(DONE)", flush=True)

        # Check if directories for the files are valid
        if not os.path.isdir(self.original_files_folder_path):
            raise FileNotFoundError(f"Directory for the original files not found: {self.original_files_folder_path}")
        if not os.path.isdir(self.md_files_folder_path):
            raise FileNotFoundError(f"Directory for the markdown version of the files not found: {self.md_files_folder_path}")

        # Get the paths to every file in both directories
        print("=> Getting original files paths... ", flush=True, end="")
        original_files_paths = get_files_paths(self.original_files_folder_path)
        print("(DONE)", flush=True)
        print("=> Getting converted files paths... ", flush=True, end="")
        md_files_paths = get_files_paths(self.md_files_folder_path)
        print("(DONE)", flush=True)

        # Check which if there are files without the conversion stored
        print("=> Checking files conversion status... ", flush=True, end="")
        files_converted, need_conversion_files, md_files_without_original = check_missing_conversions(original_files_paths, md_files_paths)
        print("(DONE)", flush=True)

        # Delete the md files with no original version
        print("=> Deleting md files with no original version... ", flush=True, end="")
        for f in md_files_without_original:
            self.delete_single_file(f)
        print("(DONE)", flush=True)

        # Store the info about the converted files
        print("=> Storing info about converted files... ", flush=True, end="")
        for path in files_converted:

            # Create a new File instance
            file_obj = FILE(path, self.md_files_folder_path, converted=True)

            # Add it to the files dict
            parent_folder = file_obj.folder
            if parent_folder not in self.files:
                self.files[parent_folder] = {}
            file_key = file_obj.filename + file_obj.file_extension
            self.files[parent_folder][file_key] = file_obj
        print("(DONE)", flush=True)
        
        # Preload files to the gemini cloud
        print("=> Preload files to Gemini API... ", flush=True, end="")
        files_to_upload = files_for_preload(self.files)
        for f in files_to_upload:
            self.upload_file(f)
        print("(DONE)", flush=True)
        
        # Convert the files that needed conversion found before
        print("=> Converting stored files without md conversion... ", flush=True, end="")
        self.convert_files(need_conversion_files)
        print("(DONE)", flush=True)

        # Get the paths for the files in the unprocessed files folder
        print("=> Getting unprocessed files paths... ", flush=True, end="")
        unprocessed_files = get_files_paths(self.unprocessed_files_folder_path)
        print("(DONE)", flush=True)

        # Convert the unprocessed files
        print("=> Converting the unprocessed files... ", flush=True, end="")
        self.convert_files(unprocessed_files, new_files_flag=True)
        print("(DONE)", flush=True)

        # Get the paths for the files in the files to modify folder
        print("=> Getting unprocessed files paths... ", flush=True, end="")
        modify_files = get_files_paths(self.modify_files_folder_path)
        print("(DONE)", flush=True)

        # Convert the files that need modification
        print("=> Converting the files that need modification... ", flush=True, end="")
        self.convert_files(modify_files, new_files_flag=True, allow_override=True)
        print("(DONE)", flush=True)

    
    def delete_single_file(self, file_path: str):
        """Low-level file and empty parent directory deletion.
           Raises exceptions on failure."""
        if not file_path or not os.path.isfile(file_path):
            print(f"File not found or path is invalid, skipping deletion: {file_path}", flush=True)
            return # Not an error, just nothing to do

        try:
            parent_dir = os.path.dirname(file_path)
            print(f"Deleting file: {file_path}", flush=True)
            os.remove(file_path)
            
            # Attempt to remove parent directory if it's empty
            if not os.listdir(parent_dir):
                print(f"Parent directory '{parent_dir}' is empty, deleting.", flush=True)
                os.rmdir(parent_dir)
        except OSError as e:
            print(f"OS error during deletion of {file_path}: {e}", flush=True)
            raise e

        except OSError as e:
            # Catch potential file system errors (e.g., permissions denied)
            print(f"An error occurred while deleting: {e}", flush=True)
            return False
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}", flush=True)
            return False
    
    # Retrieve the files that are loaded in the cloud
    def get_loaded_examples(self) -> list[FILE]:

        try:
            remote_files = genai.list_files()
            remote_file_ids = {f.name for f in remote_files}
        except Exception as e:
            print(f"Could not retrieve files from the cloud API: {e}", flush=True)
            # Return an empty list in case of error
            return []
    
        confirmed_loaded_files = []
        for folder_dict in self.files.values():
            for file_obj in folder_dict.values():
                if file_obj.uploaded:
                    # Check if the file's stored gemini_obj and name exist
                    if file_obj.gemini_obj and hasattr(file_obj.gemini_obj, 'name'):
                        gemini_id = file_obj.gemini_obj.name
                        
                        if gemini_id in remote_file_ids:
                            confirmed_loaded_files.append(file_obj)
                        else:
                            file_obj.off_cloud()
                            self.free_memory(file_obj.size)
                    else:
                        file_obj.off_cloud()
                        self.free_memory(file_obj.size)
        
        return confirmed_loaded_files
    
    # Retrieve the files that are not loaded in the cloud
    def get_unloaded_examples(self, folder: str = None) -> list[FILE]:

        unloaded_files = []

        # Check if only files from a specific folder are to be retrieved
        if folder:
            if folder in self.files.keys():
                for file_obj in self.files[folder].values():
                    if not file_obj.uploaded:
                        unloaded_files.append(file_obj)
            else:
                print(f"The folder was not found: {folder}", flush=True)
                return []
        else:
            for folder_dict in self.files.values():
                for file_obj in folder_dict.values():
                    if not file_obj.uploaded:
                        unloaded_files.append(file_obj)
        
        return unloaded_files
    
    # Find relevant examples for some reference file
    def find_examples(self, loaded_examples: list[FILE], template_folder: str = None, examples_needed: int = myconstants.EXAMPLES_PER_PROMPT) -> list[FILE]:

        selected_examples = []
        selected_ids = set()

        def _fill_from_source(candidate_files: list[FILE]):
            nonlocal selected_examples, selected_ids, examples_needed
            
            # Stop if we already have enough examples
            if examples_needed <= 0:
                return

            for file in candidate_files:
                # Check if this file has already been added
                if file.original_file_path not in selected_ids:
                    selected_examples.append(file)
                    selected_ids.add(file.original_file_path)
                    examples_needed -= 1
                    if examples_needed <= 0:
                        return

        if template_folder and (template_folder in self.files):
            
            # Priority 1: Loaded files from the template folder
            template_loaded = [f for f in loaded_examples if f.folder == template_folder]
            _fill_from_source(template_loaded)

            # Priority 2: Unloaded files from the template folder
            template_unloaded = self.get_unloaded_examples(folder=template_folder)
            _fill_from_source(template_unloaded)

        # Priority 3: All other LOADED examples (shuffled and balanced)
        other_loaded = [f for f in loaded_examples if f.folder != template_folder]
        _fill_from_source(get_balanced_shuffled_files(other_loaded))
        
        # Priority 4: All other UNLOADED examples (shuffled and balanced)
        other_unloaded = self.get_unloaded_examples()
        _fill_from_source(get_balanced_shuffled_files(other_unloaded))

        return selected_examples

    def upload_file_to_gemini(self, file: FILE, mime_type: str = None):
        """
        Upload a file to Gemini and return the file object.
        
        Args:
            file_path: Path to the file to upload
            mime_type: MIME type of the file (optional, will be auto-detected)
        
        Returns:
            genai.File: The uploaded file object
        """

        # 1. VERIFY: Check if we have a record of a previous upload.
        if file.gemini_obj and hasattr(file.gemini_obj, 'name'):
            print(f"File '{file.original_file_path}' has a known cloud ID. Verifying its existence...", flush=True)
            try:
                # Attempt a fast, targeted retrieval of the file by its unique name.
                verified_file_obj = genai.get_file(file.gemini_obj.name)
                print("Verification successful. File is already on the cloud. Skipping upload.", flush=True)
                
                # Update the local state in case it was wrong
                file.on_cloud(verified_file_obj) 
                return verified_file_obj

            except Exception as e:
                # The file was deleted from the cloud.
                print(f"Verification failed: {e}. File no longer on cloud. Proceeding with fresh upload.", flush=True)
                # Clear the old, invalid state before re-uploading.
                file.off_cloud()
        
        file_path = file.original_file_path
        print(f"Uploading file to cloud: {file_path}", flush=True)

        try:
            file = genai.upload_file(file_path, mime_type=mime_type)
            print(f"Uploaded file: {file.name}", flush=True)
            
            # Wait for the file to be processed
            while file.state.name == "PROCESSING":
                print("Processing file...", flush=True)
                time.sleep(2)
                file = genai.get_file(file.name)
            
            if file.state.name == "FAILED":
                raise ValueError(f"File processing failed: {file.state}")

            return file
            
        except Exception as e:
            print(f"Error uploading file {file_path}: {e}", flush=True)
            raise
    
    def add_memory(self, value: int):
        self.total_used_memory += value
    
    def free_memory(self, value: int):
        self.total_used_memory -= value
    
    def file_batch_size(self, files: list[FILE]) -> int:
        
        total = sum(file.size for file in files)
        return total
    
    def manage_memory(self, loaded_examples: list[FILE], examples_to_upload: list[FILE]):

        # Determine which elements are not uploaded yet
        loaded_examples_set = set(loaded_examples)
        examples_to_upload_set = set(examples_to_upload)
        not_uploaded = list(examples_to_upload_set - loaded_examples_set)

        needed_space = self.file_batch_size(not_uploaded)

        storage_limit = self.storage_limit * 10**9

        if self.total_used_memory + needed_space < storage_limit:
            return
        else:

            # Randomly remove files from the cloud until enough space is available
            missing_space = self.total_used_memory + needed_space - storage_limit
            uploads_not_needed = list(loaded_examples_set - examples_to_upload_set)
            random.shuffle(uploads_not_needed)
            while missing_space > 0:
                file = uploads_not_needed.pop()
                size = file.size
                self.free_memory(size)
                missing_space -= size
            
            return
    
    def upload_file(self, file: FILE):
        mime_type = get_mime_type(file.file_extension)
        file_obj = self.upload_file_to_gemini(file, mime_type)

        # Update the file info
        if file_obj:
            file.on_cloud(file_obj)
            self.add_memory(file.size)
    
    def convert_file(self, file: FILE, allow_override: bool = False) -> int:
        """
        Converts a pdf file to Markdown.
        
        Args:
            file: a file object with the info of the file we want to convert
            allow_override: a flag that determines if we can override an existing file
        
        Returns:
            int: A value that determines how the operation went. The options are:
                - 0: Error converting
                - 1: The operation went well
                - 2: The file already exists and the allow_override is false
        """

        print(f"Starting to convert the file: {file.original_file_path}", flush=True)

        # Check if it's ok to remove the file
        file_exists = self.already_stored(file)
        if file_exists and not allow_override:
            return 2

        folder_name = file.folder
        loaded_examples = self.get_loaded_examples()
        print("-"*30, flush=True)
        print("Loaded Examples:", flush=True)
        for f in loaded_examples:
            print(f.filename, flush=True)
        print("-"*30, flush=True)
        examples_to_use = self.find_examples(loaded_examples, folder_name)
        print("-"*30, flush=True)
        print("Examples to Use:", flush=True)
        for f in examples_to_use:
            print(f.filename, flush=True)
        print("-"*30, flush=True)

        # Ensure there are enough free memory in the cloud available
        self.manage_memory(loaded_examples, examples_to_use)

        # Upload the examples that are not in the cloud
        for f in examples_to_use:
            self.upload_file(f)
        
        # Upload the file we want to convert
        self.upload_file(file)
        
        # Create prompt
        prompt = create_prompt(file, examples_to_use)

        # Generate the conversion
        print("Generating conversion...", flush=True)
        try:
            response = model.generate_content(
                contents=prompt,
            )
            file.file_converted()
        except Exception as e:
            print(f"Could not convert the file {file.filename}: {e}", flush=True)
            return 0
        
        if file_exists and allow_override:
            # Delete all info about the previous version of the file
            self.delete_file_from_server(file)
        
        # Write the conversion to a file
        md_base_path = Path(self.md_files_folder_path)
        new_folder = str(md_base_path / file.folder)
        Path(new_folder).mkdir(parents=True, exist_ok=True)
        with open(file.md_file_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print(f"Conversion saved to: {file.md_file_path}", flush=True)

        # Add the new file to the dictionary
        self.update_files_dict(file)

        return 1
    
    def convert_files(self, paths_files: list[str], new_files_flag: bool = False, allow_override: bool = False):

        for path in paths_files:
            file = FILE(path, self.md_files_folder_path)
            
            number_tries = 0
            status = 0
            while status == 0 and number_tries < 3:
                status = self.convert_file(file, allow_override)
                number_tries += 1
            
            if status == 0 or status == 2:
                self.delete_single_file(path)
                if status == 0:
                    print(f"ERROR: Could not convert the file: {file.filename}", flush=True)
                elif status == 2:
                    print(f"ERROR: That file already exists and you can't override it this way: {file.filename}", flush=True)
            elif new_files_flag:
                # Store the unprocessed file in the original_files folder
                self.unprocessed_to_processed(file)
    
    def update_files_dict(self, file: FILE):

        if file.folder not in self.files:
            self.files[file.folder] = {}
        key_file = file.filename + file.file_extension
        self.files[file.folder][key_file] = file
    
    def unprocessed_to_processed(self, file: FILE):
        orig_base_path = Path(self.original_files_folder_path)
        filename = f"{file.filename}{file.file_extension}"
        new_folder = str(orig_base_path / file.folder)
        new_file_path = str(orig_base_path / file.folder / filename)

        # Switch to the new location
        Path(new_folder).mkdir(parents=True, exist_ok=True)
        shutil.move(file.original_file_path, new_file_path)

        # Update the object info
        previous_path = file.original_file_path
        file.update_orig_location(new_file_path)

        # Delete the original unprocessed folder if it's empty
        folder_path = Path(previous_path).parent

        if len(os.listdir(folder_path)) == 0:
            os.rmdir(folder_path)
    
    # Checks if a file is already stored
    def already_stored(self, file: FILE) -> bool:

        folder = file.folder
        filename = file.filename + file.file_extension

        if folder in self.files and filename in self.files[folder]:
            return True
        return False
    
    # Upload a new file
    def post_new_file(self, file_path: str, modify_file: bool = False) -> bool:

        # Create the complete path to the file
        if modify_file:
            folder_path = Path(self.modify_files_folder_path)
        else:
            folder_path = Path(self.unprocessed_files_folder_path)
        file_path = str(folder_path / file_path)

        # Check if the file exists
        if not os.path.isfile(file_path):
            raise Exception("File doesn't exist")

        # Create a new file instance
        file = FILE(file_path, self.md_files_folder_path)

        number_tries = 0
        status = 0
        while status == 0 and number_tries < 3:
            status = self.convert_file(file, modify_file)
            number_tries += 1
        
        if status == 0 or status == 2:
            self.delete_single_file(file_path)
            if status == 0:
                raise Exception(f"Could not convert the file: {file.filename}")
            elif status == 2:
                raise Exception(f"The file already exists and you can't override it this way: {file.filename}")
        
        self.unprocessed_to_processed(file)
        return 200

    def delete_file_from_server(self, file: FILE) -> bool:
        """Orchestrates deletion from disk, cloud, and memory.
           Returns True on success, raises exception on failure."""
        try:
            # 1. Delete original file from disk
            orig_base_path = Path(self.original_files_folder_path)
            filename_with_ext = f"{file.filename}{file.file_extension}"
            original_file_path = str(orig_base_path / file.folder / filename_with_ext)
            self.delete_single_file(original_file_path)

            # 2. Delete converted file from disk
            self.delete_single_file(file.md_file_path)

            # 3. Delete from the cloud
            if file.gemini_obj:
                cleanup_file(file.gemini_obj)

            # 4. If all previous steps succeeded, remove from in-memory state
            del self.files[file.folder][filename_with_ext]
            
            print(f"Successfully deleted all artifacts for {filename_with_ext}", flush=True)
            return True

        except Exception as e:
            print(f"Failed to fully delete file {file.filename}: {e}", flush=True)
            # Re-raise the exception so the router can return a 500 error
            raise e
    
    def get_file_obj(self, relative_path: str) -> FILE | None:
        path = Path(relative_path)
        folder = path.parent.name
        filename = path.name

        return self.files.get(folder, {}).get(filename)