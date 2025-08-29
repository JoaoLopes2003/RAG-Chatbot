import os
import random
from .. import myconstants

PROMPT_ENGINEERING_CONVERTED_EXAMPLES = myconstants.PROMPT_ENGINEERING_CONVERTED_EXAMPLES
ORIGINAL_FILES_FOLDER = myconstants.ORIGINAL_FILES_FOLDER
EXAMPLES_PER_PROMPT = myconstants.EXAMPLES_PER_PROMPT

def get_examples_unconstrained(
    file_extension: str,
    ignore_template_folder: bool,
    originals_dir: str = '',
    necessary_examples: int = EXAMPLES_PER_PROMPT
):
    original_files = []
    converted_files = []

    # Get the folder names
    folders_original_files = [f for f in os.listdir(ORIGINAL_FILES_FOLDER) 
                             if os.path.isdir(os.path.join(ORIGINAL_FILES_FOLDER, f))]
    if ignore_template_folder and originals_dir in folders_original_files:
        folders_original_files.remove(originals_dir)
    
    folders_converted_files = [f for f in os.listdir(PROMPT_ENGINEERING_CONVERTED_EXAMPLES) 
                              if os.path.isdir(os.path.join(PROMPT_ENGINEERING_CONVERTED_EXAMPLES, f))]
    if ignore_template_folder and originals_dir in folders_converted_files:
        folders_converted_files.remove(originals_dir)
    
    # Build a mapping of basenames to full converted file paths
    converted_file_map = {}  # Maps "folder/basename" -> full_converted_path
    
    for folder in folders_converted_files:
        folder_path = os.path.join(PROMPT_ENGINEERING_CONVERTED_EXAMPLES, folder)
        for file in os.listdir(folder_path):
            if file.endswith('.md'):
                basename = os.path.splitext(file)[0]  # Remove .md extension
                relative_key = os.path.join(folder, basename)  # "folder/basename"
                full_path = os.path.join(folder_path, file)
                converted_file_map[relative_key] = full_path
    
    # Get the files from each folder
    filenames_per_folder = []
    for folder in folders_original_files:
        folder_path = os.path.join(ORIGINAL_FILES_FOLDER, folder)
        # Store as relative paths: "folder/filename_without_extension"
        folder_files = [os.path.join(folder, os.path.splitext(file)[0])
                       for file in os.listdir(folder_path) 
                       if file.endswith(file_extension)]
        filenames_per_folder.append(folder_files)

    # Randomize the files order from each folder to reduce bias
    for files_list in filenames_per_folder:
        random.shuffle(files_list)

    # Concatenate the files from each folder, intercalating them
    filenames_intercalated = []
    max_files = max(len(files) for files in filenames_per_folder) if filenames_per_folder else 0
    
    for i in range(max_files):
        for folder_files in filenames_per_folder:
            if i < len(folder_files):
                filenames_intercalated.append(folder_files[i])
    
    # Select the examples that have matching converted files
    for relative_path in filenames_intercalated:
        if necessary_examples <= 0:
            break
            
        if relative_path in converted_file_map:
            # Build full original file path
            folder, basename = os.path.split(relative_path)
            original_full_path = os.path.join(ORIGINAL_FILES_FOLDER, folder, basename + file_extension)
            
            original_files.append(original_full_path)
            converted_files.append(converted_file_map[relative_path])
            necessary_examples -= 1
    
    return original_files, converted_files

def get_examples(file_extension: str, dir_exists: bool, originals_dir: str = '', outputs_dir: str = ''):
    
    original_files = []
    converted_files = []
    necessary_examples = EXAMPLES_PER_PROMPT

    if dir_exists and originals_dir and outputs_dir:

        # Get filenames from the directories
        originals_dir_files = [f for f in os.listdir(originals_dir) 
                                  if os.path.isfile(os.path.join(originals_dir, f))]
        outputs_dir_files = [f for f in os.listdir(outputs_dir) 
                            if os.path.isfile(os.path.join(outputs_dir, f))]
        
        # Create a set of converted file basenames for quick lookup
        converted_basenames = set()
        for filename in outputs_dir_files:
            if filename.endswith('.md'):
                base_name = os.path.splitext(filename)[0]
                converted_basenames.add(base_name)

        # Iterate through original files and find matching converted files
        for filename in originals_dir_files:
            if necessary_examples <= 0:
                break
                
            name, ext = os.path.splitext(filename)
            if ext == file_extension and name in converted_basenames:
                original_files.append(os.path.join(originals_dir, filename))
                converted_files.append(os.path.join(outputs_dir, name + '.md'))
                necessary_examples -= 1
        
        # Get examples from other folders in case we didn't find enough
        if necessary_examples > 0:

            extra_original_files, extra_converted_files = get_examples_unconstrained(
                file_extension, 
                True,
                originals_dir, 
                necessary_examples
            )

            original_files.extend(extra_original_files)
            converted_files.extend(extra_converted_files)

    else:

        # Get random examples from all folders
        original_files, converted_files = get_examples_unconstrained(file_extension, False)

    # Sort to ensure proper pairing
    original_files.sort()
    converted_files.sort()

    return original_files, converted_files