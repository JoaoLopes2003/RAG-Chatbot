import os
from dotenv import load_dotenv
import google.generativeai as genai
import time
import random
from pathlib import Path

UNPROCESS_FILES_DIR = "/tmp/unprocessed_files/"
MD_FORMATTED_FILE = "/tmp/md_formatted_file/"
PROMPT_ENGINEERING_CONVERTED_EXAMPLES = "/app/prompt_examples/"
ORIGINAL_FILES_FOLDER = "/original_files/"
EXAMPLES_PER_PROMPT = 10

load_dotenv()
try:
    api_key = os.getenv("API_KEY")
except KeyError:
    print("Error: API_KEY environment variable not set.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name='gemini-1.5-pro-latest'
)

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

def read_markdown_content(file_path: str, max_chars: int = 8000) -> str:
    """
    Read markdown file content and truncate if necessary.
    
    Args:
        file_path: Path to the markdown file
        max_chars: Maximum characters to include
    
    Returns:
        str: Markdown content (truncated if needed)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if len(content) > max_chars:
            content = content[:max_chars] + "\n\n... [content truncated for brevity]"
            
        return content
        
    except Exception as e:
        return f"[Error reading markdown file: {e}]"

def create_prompt(
    target_file,
    file_extension: str,
    original_files: list, 
    converted_files: list, 
    target_format: str = "Markdown"
) -> tuple:
    """
    Create a hybrid prompt with uploaded original files and concatenated markdown content.
    
    Args:
        original_files: List of original file paths to upload
        converted_files: List of converted markdown file paths to read
        target_format: Target conversion format
    
    Returns:
        tuple: (content_parts_list, uploaded_files_for_cleanup)
    """
    if not original_files:
        return [], []
    
    uploaded_files = []
    
    # Create the system prompt
    system_prompt = f"""You are an expert at converting {file_extension} files to {target_format}.

I will show you example pairs where:
1. First, you'll see the original {file_extension} file (uploaded)
2. Then, you'll see the expected {target_format} conversion (as text)

After the example pairs, I am going to provide another file with the {file_extension} extension and I want you to convert it to {target_format}. Give only the conversion, and no extra commentary, formatting, or chattiness. Convert the file from {file_extension} format to {target_format}.
"""
    
    content_parts = [system_prompt]
    
    # Add each example pair
    for orig_file, conv_file in zip(original_files, converted_files):
        example_mime_type = get_mime_type(orig_file)
        if not example_mime_type:
             print(f"Warning: Could not determine MIME type for example file {orig_file}. Skipping.")
             continue # Skip this example if the type is unknown

        # Upload original file
        uploaded_file = upload_file_to_gemini(orig_file, mime_type=example_mime_type)
        uploaded_files.append(uploaded_file)
        
        # Read converted markdown content
        markdown_content = read_markdown_content(conv_file)
        
        # Add to content parts
        content_parts.extend([
            f"Original file: ",
            uploaded_file,
            f"\n{target_format}:\n{markdown_content}\n",
        ])

    # Add to content parts
    content_parts.extend([
        f"Original file: ",
        target_file,
        f"\n{target_format}:",
    ])
    
    return content_parts, uploaded_files

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

def get_mime_type(file_path: str) -> str:
    """Gets the MIME type for a given file path based on its extension."""
    extension = Path(file_path).suffix.lower()
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

def convert_file(
    file_path: str,
    template_folder: str = "",
    temperature: float = 1.0,
) -> bool:
    
    # Setting the parameters for the model
    generation_config = genai.types.GenerationConfig(
        temperature=temperature
    )

    # Defining the necessary paths
    full_file_path = os.path.join(UNPROCESS_FILES_DIR, file_path)
    input_template_folder_dir = os.path.join(ORIGINAL_FILES_FOLDER, template_folder)
    output_template_folder_dir = os.path.join(PROMPT_ENGINEERING_CONVERTED_EXAMPLES, template_folder)

    # Check if file exists
    if not os.path.isfile(full_file_path):
        raise FileNotFoundError(f"File not found: {full_file_path}")
    
    # Extract file extension
    filename, file_extension = os.path.splitext(file_path)

    # Check if the template folder exists
    if len(template_folder) and os.path.isdir(input_template_folder_dir) and os.path.isdir(output_template_folder_dir):
        original_files, converted_files = get_examples(file_extension, True, input_template_folder_dir, output_template_folder_dir)
    else:
        original_files, converted_files = get_examples(file_extension, False)

    uploaded_files_for_cleanup = []

    try:

        # Determine the MIME type for the target file
        target_mime_type = get_mime_type(full_file_path)
        if not target_mime_type:
            raise ValueError(f"Unsupported file type or unknown MIME type for {full_file_path}")

        # Upload the target file
        print(f"Uploading target file: {full_file_path}")
        target_file = upload_file_to_gemini(full_file_path, mime_type=target_mime_type)

        # Create the prompt
        if original_files and converted_files:
            content_parts, uploaded_files = create_prompt(target_file, file_extension, original_files, converted_files)
            uploaded_files_for_cleanup.extend(uploaded_files)
        else:
            content_parts = [
                f"Convert the following {file_extension} file to Markdown format. ",
                f"Give only the Markdown conversion, no extra commentary.\n",
                f"{file_extension.upper()} file:\n",
                target_file
            ]

        # Generate conversion
        print("Generating conversion...")
        response = model.generate_content(
            contents=content_parts,
            generation_config=generation_config
        )

        # Save the output
        output_file_path = os.path.join(MD_FORMATTED_FILE, f"{Path(file_path).stem}.md")
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print(f"Conversion saved to: {output_file_path}")
        return 200, output_file_path
        
    except Exception as e:
        print(f"Error during conversion: {e}")
        return 500, ""

    finally:
        # Clean up uploaded files
        print("Cleaning up uploaded files...")
        for file in uploaded_files_for_cleanup:
            try:
                genai.delete_file(file.name)
                print(f"Deleted: {file.display_name}")
            except Exception as e:
                print(f"Error deleting {file.display_name}: {e}")
                return 500, ""