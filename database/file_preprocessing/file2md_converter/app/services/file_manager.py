import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai
import time
import random
from .utils.file_manager_utils import get_files_paths, check_missing_conversions, files_for_preload, get_mime_type, get_balanced_shuffled_files
from . import myconstants

load_dotenv()
try:
    api_key = os.getenv("API_KEY")
except KeyError:
    print("Error: API_KEY environment variable not set.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name='gemini-1.5-pro-latest'
)

class FILE():
    def __init__(self, file_path: str, md_files_folder_path: str, uploaded: bool = False):

        p = Path(file_path)

        self.filename = p.stem
        self.file_extension = p.suffix
        self.folder = p.parent.name
        self.original_file_path = file_path
        self.size = os.path.getsize(file_path)
        self.uploaded = uploaded
        self.gemini_obj = None

        # Path to the converted version of the file
        md_base_path = Path(md_files_folder_path)
        new_filename = f"{p.name}.md"
        self.md_file_path: str = str(md_base_path / self.folder / new_filename)
    
    def on_cloud(self, file_obj):
        self.uploaded = True
        self.gemini_obj = file_obj
    
    def off_cloud(self):
        self.uploaded = False
        self.gemini_obj = None

class FILE_MANAGER():

    def __init__(self, original_files_folder_path: str, md_files_folder_path: str, unprocessed_files_folder_path: str):
        self.storage_limit = 18 # Gigabytes / The real limit is 20GB but we decided to leave some free space
        self.file_size_limit = 2 # Gigabytes
        self.file_lifetime_in_cloud = 48 # Hours
        self.total_used_memory = 0
        self.original_files_folder_path = original_files_folder_path
        self.md_files_folder_path = md_files_folder_path
        self.unprocessed_files_folder_path = unprocessed_files_folder_path
        self.files = {} # Map: folder -> Map: filename -> FILE_OBJECT

        # Check if directories for the files are valid
        if not os.path.isdir(self.original_files_folder_path):
            raise FileNotFoundError(f"Directory for the original files not found: {self.original_files_folder_path}")
        if not os.path.isdir(self.md_files_folder_path):
            raise FileNotFoundError(f"Directory for the markdown version of the files not found: {self.md_files_folder_path}")
        
        # Get the paths to every file in both directories
        original_files_paths = get_files_paths(self.original_files_folder_path)
        md_files_paths = get_files_paths(self.md_files_folder_path)

        # Check which if there are files without the conversion stored
        files_converted, need_conversion_files, md_files_without_original = check_missing_conversions(original_files_paths, md_files_paths)

        # Delete the md files with no original version
        for f in md_files_without_original:
            self.delete_example_file(f)

        # Store the info about the converted files
        for path in files_converted:

            # Create a new File instance
            file_obj = self.FILE(path, self.md_files_folder_path)

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
        for file in need_conversion_files:
            status = self.convert_file(file)

        # Get the paths for the files in the unprocessed files folder
        unprocessed_files = [os.path.join(self.unprocessed_files_folder_path, file)
                       for file in os.listdir(self.unprocessed_files_folder_path) 
                       if os.path.isfile(file)]

    
    def delete_example_file(self, file_path: str) -> bool:

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
                for file_obj in folder_dict[folder].values():
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
        other_unloaded = self.get_unloaded_examples(exclude_folder=template_folder)
        _fill_from_source(get_balanced_shuffled_files(other_unloaded))

        return selected_examples

    def upload_file_to_gemini(self, file_path: str, mime_type: str = None):
        """
        Upload a file to Gemini and return the file object.
        
        Args:
            file_path: Path to the file to upload
            mime_type: MIME type of the file (optional, will be auto-detected)
        
        Returns:
            genai.File: The uploaded file object
        """
        try:
            file = genai.upload_file(file_path, mime_type=mime_type)
            print(f"Uploaded file: {file.name}")
            
            # Wait for the file to be processed
            while file.state.name == "PROCESSING":
                print("Processing file...")
                time.sleep(2)
                file = genai.get_file(file.name)
            
            if file.state.name == "FAILED":
                raise ValueError(f"File processing failed: {file.state}")

            return file
            
        except Exception as e:
            print(f"Error uploading file {file_path}: {e}")
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

        if self.total_used_memory + needed_space < self.storage_limit:
            return
        else:

            # Randomly remove files from the cloud until enough space is available
            missing_space = self.total_used_memory + needed_space - self.storage_limit
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
        file_obj = self.upload_file_to_gemini(file.original_file_path, mime_type)

        # Update the file info
        if file_obj:
            file.on_cloud(file_obj)
            self.add_memory(file.size)
    
    def convert_file(self, file: FILE) -> bool:

        folder_name = Path(file).parent.name
        loaded_examples = self.get_loaded_examples()
        examples_to_use = self.find_examples(self.files, loaded_examples, folder_name)

        # Ensure there are enough free memory in the cloud available
        self.manage_memory(loaded_examples, examples_to_use)

        # Upload the examples that are not in the cloud
        for f in examples_to_use:
            self.upload_file(f)
        
