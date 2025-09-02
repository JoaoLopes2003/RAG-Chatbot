import google.generativeai as genai

def list_uploaded_files():
    """List all uploaded files in Gemini."""
    files = genai.list_files()
    for file in files:
        print(f"File: {file.name} | Display Name: {file.display_name} | State: {file.state.name}")

def cleanup_all_files():
    """Delete all uploaded files from Gemini."""
    print("--- Cleaning up all files ---", flush=True)
    files = genai.list_files()
    if not list(files): # Check if the iterator is empty
        print("No files to delete.", flush=True)
        return
        
    # Re-initialize the iterator after checking if it's empty
    files = genai.list_files() 
    for file in files:
        try:
            genai.delete_file(file.name)
            print(f"Deleted: {file.display_name} (ID: {file.name})", flush=True)
        except Exception as e:
            print(f"Error deleting {file.display_name}: {e}", flush=True)
    print("--- Cleanup complete ---", flush=True)


def cleanup_file(gemini_file):
    """
    Deletes a specific uploaded file from Gemini.

    This function receives the file object that is returned by
    genai.upload_file() or is an item from genai.list_files().

    Args:
        gemini_file: The File object to be deleted.
    """
    if not gemini_file:
        print("No file object provided to cleanup_file.", flush=True)
        return

    try:
        print(f"Attempting to delete: {gemini_file.display_name} (ID: {gemini_file.name})", flush=True)
        genai.delete_file(gemini_file.name)
        print(f"Successfully deleted file.", flush=True)
    except Exception as e:
        print(f"Error deleting file {gemini_file.display_name}: {e}", flush=True)