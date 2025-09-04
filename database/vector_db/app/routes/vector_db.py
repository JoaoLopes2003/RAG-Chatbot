import shutil
from fastapi import APIRouter, UploadFile, HTTPException, Body, status, Depends
from pathlib import Path
from services import myconstants

from dependencies import get_vector_db
from services.vector_db import Vector_db

router = APIRouter()

UNPROCESSED_FILES_DIR = Path(myconstants.UNPROCESSED_FILES_DIR)

@router.post("/uploadfile", status_code=status.HTTP_201_CREATED)
async def upload_file(
    file: UploadFile,
    template_folder: str = Body("undefined"),
    db: Vector_db = Depends(get_vector_db)
):
        
    try:
        # Resolve the path to ensure it's within our base directory
        path_to_folder = UNPROCESSED_FILES_DIR.joinpath(template_folder).resolve()
        
        path_to_folder.mkdir(parents=True, exist_ok=True)
        
        # Correctly construct the final file path
        path_to_file = path_to_folder / file.filename

        # Use binary write mode ('wb') and process the file in chunks
        with open(path_to_file, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    except HTTPException as http_exc:
        # Re-raise HTTPExceptions so FastAPI can handle them
        raise http_exc
    except Exception as e:
        # Log the detailed error for debugging
        print(f"Failed to process file '{file.filename}': {e}", flush=True)
        # Return a generic error to the user
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing the file.",
        )
    finally:
        file.file.close()

    # Let the file manager process the file
    try:
        pass
        # file_manager.post_new_file(str(path_to_file))
    except Exception as e:
        print(f"File '{path_to_file}' was saved but processing failed: {e}", flush=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="File was uploaded but could not be processed."
        )