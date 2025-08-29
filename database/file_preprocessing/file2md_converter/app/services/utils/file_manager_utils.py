import os
from pathlib import Path
import google.generativeai as genai
import time
import random
from typing import Tuple
from ..file_manager import FILE
from .. import myconstants

EXAMPLES_PER_PROMPT = myconstants.EXAMPLES_PER_PROMPT

def get_files_paths(root: str) -> list[str]:

    # Get the folders
    folders_of_files = [f for f in os.listdir(root) 
                             if os.path.isdir(os.path.join(root, f))]

    #  Get the files inside each folder
    file_paths = []
    for folder in folders_of_files:
        folder_path = os.path.join(root, folder)
        folder_files = [os.path.join(folder_path, file)
                       for file in os.listdir(folder_path) 
                       if os.path.isfile(file)]
        file_paths.extend(folder_files)
    
    return file_paths

def check_missing_conversions(paths: list[str], converted_paths: list[str]) -> Tuple[list[str], list[str]]:
    """
    Compares source paths with converted paths that have an extra extension.

    Args:
        paths: List of full paths to original files (e.g., '.../folder1/file1.txt').
        converted_paths: List of full paths to converted files (e.g., '.../folder1/file1.txt.md').

    Returns:
        A tuple of (files_to_convert, files_to_delete).
    """

    # 1. Create lookup maps from a consistent key to the full path.
    source_map = {f"{Path(p).parent.name}/{Path(p).name}": p for p in paths}
    converted_map = {f"{Path(p).parent.name}/{Path(p).stem}": p for p in converted_paths}

    # 2. Get the sets of keys from our maps.
    source_keys = set(source_map.keys())
    converted_keys = set(converted_map.keys())

    # 3. Find the differences using set operations.
    keys_to_convert = source_keys - converted_keys
    keys_to_delete = converted_keys - source_keys

    # 4. Use the keys to retrieve the original full paths from our maps.
    files_to_convert = [source_map[key] for key in keys_to_convert]
    files_to_delete = [converted_map[key] for key in keys_to_delete]
    files_converted = [source_map[key] for key in converted_keys]

    return files_converted, files_to_convert, files_to_delete

def files_per_folder_for_preload(folders_info: dict[str, dict], storage_limit_per_folder) -> Tuple[list, dict[str, list], int]:

    files_to_upload = []
    folders_to_remove = []
    used_storage = 0
    for folder, info in folders_info.items():

        # Get folder info
        n_files = info["n_files"]
        sorted_files = info["sorted_files"]

        current_size_sum = 0
        files_added = 0
        for f in sorted_files:
            # Check if has surpassed the available space
            f_size = f.size
            if current_size_sum + f_size > storage_limit_per_folder:
                break
            files_to_upload.append(f.original_file_path)
            current_size_sum += f_size
            files_added += 1
        
        # Remove the added filesfrom the list to add
        if n_files==files_added:
            folders_to_remove.append(folder)
        else:
            info["sorted_files"] = info["sorted_files"][files_added:]
        
        # Check for left storage that wasn't needed
        used_storage += current_size_sum
    
    # Remove folders, which files could all be added
    for folder in folders_to_remove:
        folders_info.pop(folder)
    
    return files_to_upload, folders_info, used_storage

def files_for_preload(files_dict: dict[str, dict[str, FILE]], storage_limit: int = 5, max_file_size: int = 2) -> list[FILE]:

    # Convert the storage limit to bytes
    storage_limit *= 10**9
    max_file_size *= 10**9

    # Determine the number of files per folder and create a list with the files sorted in ascending order by file size. Also calculate how much space the first EXAMPLES_PER_PROMPT occupy
    folders_info = {}
    for folder, files in files_dict.items():

        # Sort the files by file size in ascending order
        sorted_files = list(files.values())
        sorted_files.sort(key=lambda f: f.size)

        # Filter files above the max size limit for files
        sorted_files = [f for f in sorted_files if f.size <= max_file_size]
        
        # Truncate considering the max number of examples
        sorted_files = sorted_files[:EXAMPLES_PER_PROMPT]

        # Number of files in the folder
        n_files = len(sorted_files)

        # Calculate the total size of the first EXAMPLES_PER_PROMPT elements
        total_size = sum(file.size for file in sorted_files)
        folders_info[folder] = {
            "n_files": n_files,
            "total_size": total_size,
            "sorted_files": sorted_files
        }

    storage_full = False
    files_to_upload = []
    while len(folders_info) > 0 and not storage_full:

        # Determine how much space we have for each folder
        n_folders = len(folders_info)
        storage_limit_per_folder = storage_limit / n_folders

        selected_files, folders_info, used_storage = files_per_folder_for_preload(folders_info, storage_limit_per_folder)

        storage_limit = storage_limit - used_storage
        files_to_upload.extend(selected_files)

        # Check if the smallest file is bigger than the remaining space
        size_smallest_file = max_file_size + 1
        for folders in folders_info.values():
            for f in folders["sorted_files"]:
                if f.size < size_smallest_file:
                    size_smallest_file = f.size
        
        if size_smallest_file == max_file_size + 1 or size_smallest_file > storage_limit:
            storage_full = True
    
    return files_to_upload

def get_mime_type(extension: str) -> str:
    """Gets the MIME type for a given file path based on its extension."""
    # A map of common extensions to their MIME types
    mime_type_map = {
        ".pdf": "application/pdf",
        ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
        ".mp3": "audio/mpeg",
        ".wav": "audio/wav",
        ".mp4": "video/mp4",
        ".txt": "text/plain",
    }
    return mime_type_map.get(extension)

# Shuffle a list of file object, returning a list where the files from each folder are intercalated
def get_balanced_shuffled_files(files: list[FILE]) -> list[FILE]:

    filenames_per_folder = {}
    for file in files:
        if file.folder not in filenames_per_folder.keys():
            filenames_per_folder[file.folder] = []
        filenames_per_folder[file.folder].append(file)
    
    # Randomize the files order from each folder to introduce variability
    for files_list in filenames_per_folder.values():
        random.shuffle(files_list)
    
    # Concatenate the files from each folder, intercalating them
    filenames_intercalated = []
    max_files = max(len(files) for files in filenames_per_folder) if filenames_per_folder else 0
    
    for i in range(max_files):
        for folder_files in filenames_per_folder:
            if i < len(folder_files):
                filenames_intercalated.append(folder_files[i])
    
    return filenames_intercalated