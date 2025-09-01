import google.generativeai as genai

def list_uploaded_files():
    """List all uploaded files in Gemini."""
    files = genai.list_files()
    for file in files:
        print(f"File: {file.name} | Display Name: {file.display_name} | State: {file.state.name}")

def cleanup_all_files():
    """Delete all uploaded files from Gemini."""
    files = genai.list_files()
    for file in files:
        try:
            genai.delete_file(file.name)
            print(f"Deleted: {file.display_name}")
        except Exception as e:
            print(f"Error deleting {file.display_name}: {e}")