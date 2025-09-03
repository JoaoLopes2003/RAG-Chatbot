import os
import shutil
from fastapi import APIRouter, UploadFile, HTTPException, status, Form, Body
from fastapi.responses import FileResponse
from pathlib import Path
from services.file_manager import FILE_MANAGER
from schemas.messages import UploadFileResponse, DeleteFileRequest, GetFileRequest
from services import myconstants
from services.utils.sanitize_filename import secure_filename, sanitize_upload_request

router = APIRouter()

file_manager = FILE_MANAGER()

UNPROCESSED_BASE_DIR = Path(myconstants.UNPROCESS_FILES_DIR)

ALLOWED_CONTENT_TYPES = [
    "application/pdf"
]

@router.get("/getFile")
def delete_file(request_data: GetFileRequest):

    folder = request_data.folder
    filename = request_data.filename
    converted = request_data.converted
    relative_path = str(Path(folder) / filename)
    file_obj = file_manager.get_file_obj(relative_path)

    # Throw an error in case the file with the given folder and filename doesn't exist
    if not file_obj:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Folder and/or filename are invalid."
        )
    
    if converted:
        file_path = file_obj.md_file_path
    else:
        file_path = file_obj.original_file_path

    return FileResponse(path=file_path, filename=filename)

@router.post("/uploadfile", response_model=UploadFileResponse)
def upload_file(file: UploadFile, template_folder: str = Form("undefined")):
    
    s_template_folder, s_filename = sanitize_upload_request(file, template_folder, ALLOWED_CONTENT_TYPES)
    
    try:
        # Resolve the path to ensure it's within our base directory
        path_to_folder = UNPROCESSED_BASE_DIR.joinpath(s_template_folder).resolve()
        
        # Security check: Ensure the final path is still inside the intended base directory
        if UNPROCESSED_BASE_DIR not in path_to_folder.parents:
             raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid template_folder specified."
            )
            
        path_to_folder.mkdir(parents=True, exist_ok=True)
        
        # Correctly construct the final file path
        path_to_file = path_to_folder / s_filename

        # Use binary write mode ('wb') and process the file in chunks
        with open(path_to_file, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    except HTTPException as http_exc:
        # Re-raise HTTPExceptions so FastAPI can handle them
        raise http_exc
    except Exception as e:
        # Log the detailed error for debugging
        print(f"Failed to upload file '{s_filename}': {e}", flush=True)
        # Return a generic error to the user
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing the file.",
        )
    finally:
        file.file.close()

    # Let the file manager process the file
    try:
        file_manager.post_new_file(str(path_to_file))
    except Exception as e:
        print(f"File '{path_to_file}' was saved but processing failed: {e}", flush=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="File was uploaded but could not be processed."
        )

    return UploadFileResponse(uploaded=True, error="")

@router.post("/updatefile", response_model=UploadFileResponse)
def update_file(file: UploadFile, template_folder: str = Form("undefined")):
    
    s_template_folder, s_filename = sanitize_upload_request(file, template_folder, ALLOWED_CONTENT_TYPES)
    
    try:
        # Resolve the path to ensure it's within our base directory
        path_to_folder = UNPROCESSED_BASE_DIR.joinpath(s_template_folder).resolve()
        
        # Security check: Ensure the final path is still inside the intended base directory
        if UNPROCESSED_BASE_DIR not in path_to_folder.parents:
             raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid template_folder specified."
            )
            
        path_to_folder.mkdir(parents=True, exist_ok=True)
        
        # Correctly construct the final file path
        path_to_file = path_to_folder / s_filename

        # Use binary write mode ('wb') and process the file in chunks
        with open(path_to_file, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    except HTTPException as http_exc:
        # Re-raise HTTPExceptions so FastAPI can handle them
        raise http_exc
    except Exception as e:
        # Log the detailed error for debugging
        print(f"Failed to upload file '{s_filename}': {e}", flush=True)
        # Return a generic error to the user
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing the file.",
        )
    finally:
        file.file.close()

    # Let the file manager process the file
    try:
        file_manager.post_new_file(str(path_to_file), modify_file=True)
    except Exception as e:
        print(f"File '{path_to_file}' was saved but processing failed: {e}", flush=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="File was uploaded but could not be processed."
        )

    return UploadFileResponse(uploaded=True, error="")

@router.post("/deleteFile", status_code=status.HTTP_204_NO_CONTENT)
def delete_file(request_data: DeleteFileRequest):

    folder = request_data.folder
    filename = request_data.filename
    relative_path = str(Path(folder) / filename)
    file_obj = file_manager.get_file_obj(relative_path)

    if not file_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="File not found at the specified path."
        )
    
    try:
        success = file_manager.delete_file_from_server(file_obj)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to delete file from server storage."
            )
    except Exception as e:
        # Catch any unexpected errors from the file manager
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred during file deletion: {e}"
        )