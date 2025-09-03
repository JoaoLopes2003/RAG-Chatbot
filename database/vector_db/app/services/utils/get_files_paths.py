import os

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
                       if os.path.isfile(os.path.join(folder_path, file))]
        file_paths.extend(folder_files)
    
    return file_paths