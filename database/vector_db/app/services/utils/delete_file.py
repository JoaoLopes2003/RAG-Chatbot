import os

def delete_single_file(file_path: str):
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