import os
from dotenv import load_dotenv
import google.generativeai as genai
from pathlib import Path
from . import myconstants

from .utils.get_examples import get_examples
from .utils.get_mime_type import get_mime_type
from .utils.upload_file_to_gemini import upload_file_to_gemini
from .utils.create_prompt import create_prompt

UNPROCESS_FILES_DIR = myconstants.UNPROCESS_FILES_DIR
MD_FORMATTED_FILE = myconstants.MD_FORMATTED_FILE
PROMPT_ENGINEERING_CONVERTED_EXAMPLES = myconstants.PROMPT_ENGINEERING_CONVERTED_EXAMPLES
ORIGINAL_FILES_FOLDER = myconstants.ORIGINAL_FILES_FOLDER
EXAMPLES_PER_PROMPT = myconstants.EXAMPLES_PER_PROMPT

load_dotenv()
try:
    api_key = os.getenv("API_KEY")
except KeyError:
    print("Error: API_KEY environment variable not set.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name='gemini-1.5-pro-latest'
)

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