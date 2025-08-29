from .upload_file_to_gemini import upload_file_to_gemini
from .read_markdown_content import read_markdown_content
from .get_mime_type import get_mime_type

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