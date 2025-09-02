from pathlib import Path
from fastapi import UploadFile, HTTPException, status, Form

def secure_filename(filename: str) -> str:
    """
    Sanitizes a filename by removing directory traversal characters.
    This is a basic implementation. For production, consider a more robust library.
    """
    # Remove any path components, leaving only the filename
    return Path(filename).name


def sanitize_upload_request(file: UploadFile, template_folder: str, allowed_content_types: list[str]) -> tuple[str, str]:

    # Sanitize the folder name to prevent path traversal
    s_template_folder = secure_filename(template_folder)
    if not s_template_folder and template_folder != "undefined":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A valid template_folder must be provided."
        )

    # Sanitize the uploaded filename
    s_filename = secure_filename(file.filename)
    if not s_filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Filename is invalid."
        )

    # Validate file content type
    if file.content_type not in allowed_content_types:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=(
                f"File type '{file.content_type}' is not allowed. "
                f"Allowed types are: {', '.join(allowed_content_types)}"
            )
        )
    
    return s_template_folder, s_filename