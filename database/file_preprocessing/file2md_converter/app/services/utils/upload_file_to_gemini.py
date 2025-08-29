import google.generativeai as genai
import time

def upload_file_to_gemini(file_path: str, mime_type: str = None):
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