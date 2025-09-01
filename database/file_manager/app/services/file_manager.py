import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai
import time
import random
from .utils.file_manager_utils import check_missing_conversions, files_for_preload, get_balanced_shuffled_files, create_prompt
from . import myconstants
from .utils.get_files_paths import get_files_paths
from .utils.get_mime_type import get_mime_type
from . import myconstants
from .file import FILE
from .utils.manage_genai_storage import cleanup_all_files

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
        self.files = {} # Map: folder -> Map: filename -> FILE_OBJECT

        # Check if directories for the files are valid
        if not os.path.isdir(self.original_files_folder_path):
            raise FileNotFoundError(f"Directory for the original files not found: {self.original_files_folder_path}")
        if not os.path.isdir(self.md_files_folder_path):
            raise FileNotFoundError(f"Directory for the markdown version of the files not found: {self.md_files_folder_path}")
        
        print("CREATING FILE MANAGER.", flush=True)

        # Get the paths to every file in both directories
        original_files_paths = get_files_paths(self.original_files_folder_path)
        md_files_paths = get_files_paths(self.md_files_folder_path)

        # Check which if there are files without the conversion stored
        files_converted, need_conversion_files, md_files_without_original = check_missing_conversions(original_files_paths, md_files_paths)

        # Delete the md files with no original version
        for f in md_files_without_original:
            self.delete_file(f)

        # Store the info about the converted files
        for path in files_converted:

            # Create a new File instance
            file_obj = FILE(path, self.md_files_folder_path, converted=True)

            # Add it to the files dict
            parent_folder = file_obj.folder
            if parent_folder not in self.files:
                self.files[parent_folder] = {}
            file_key = file_obj.filename + file_obj.file_extension
            self.files[parent_folder][file_key] = file_obj
        
        # Preload files to the gemini cloud
        files_to_upload = files_for_preload(self.files)
        for f in files_to_upload:
            self.upload_file(f)
        
        # Convert the files that needed conversion found before
        self.convert_files(need_conversion_files)

        # Get the paths for the files in the unprocessed files folder
        unprocessed_files = get_files_paths(self.unprocessed_files_folder_path)

        # Convert the unprocessed files
        self.convert_files(unprocessed_files)

    
    def delete_file(self, file_path: str) -> bool:

        # Check if path exists and is a file
        if not os.path.isfile(file_path):
            print(f"The given path was not found or is not a file: {file_path}", flush=True)
            return False
        
        try:
            # Get the path of the parent directory before deleting the file
            parent_dir = os.path.dirname(file_path)

            # Delete the file
            print(f"Deleting file: {file_path}", flush=True)
            os.remove(file_path)
            
            # Delete the parent directory if empty
            if not os.listdir(parent_dir):
                print(f"Parent directory '{parent_dir}' is now empty. Deleting it.", flush=True)
                os.rmdir(parent_dir)
            else:
                print(f"Parent directory '{parent_dir}' is not empty. Leaving it.", flush=True)
            
            return True

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
            print(f"Found {len(remote_file_ids)} files on the cloud.", flush=True)
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
                            print(f"Sync issue: File '{file_obj.original_file_path}' "
                                f"(ID: {gemini_id}) is marked as uploaded but not found on cloud. Updating status.", flush=True)
                            file_obj.off_cloud()
                            self.free_memory(file_obj.size)
                    else:
                        print(f"Sync issue: File '{file_obj.original_file_path}' "
                            f"is marked as uploaded but has no valid cloud ID. Updating status.", flush=True)
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
            print(file.filename, flush=True)
            file.on_cloud(file_obj)
            self.add_memory(file.size)
    
    def convert_file(self, file: FILE) -> bool:

        folder_name = file.folder
        loaded_examples = self.get_loaded_examples()
        examples_to_use = self.find_examples(loaded_examples, folder_name)

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
            return False
        
        # Write the conversion to a file
        with open(file.md_file_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print(f"Conversion saved to: {file.md_file_path}", flush=True)
        return True
    
    def convert_files(self, paths_files: list[str]):

        for path in paths_files:
            file = FILE(path, self.md_files_folder_path)
            
            number_tries = 0
            status = False
            while not status and number_tries < 3:
                status = self.convert_file(file)
                number_tries += 1
            
            if not status:
                self.delete_file(path)

        

        
