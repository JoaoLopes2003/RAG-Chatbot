import shutil
from fastapi import APIRouter, UploadFile, HTTPException, Body, status, Depends
from pathlib import Path
from services import myconstants
from schemas.messages import DeleteFileRequest, GetRelevantFilesResponse, GetRelevantChunksResponse, getRelevantFilesRequest, GetRelevantChunksRequest

from dependencies import get_vector_db
from services.vector_db import Vector_db

router = APIRouter()

UNPROCESSED_FILES_DIR = Path(myconstants.UNPROCESSED_FILES_DIR)

@router.post(
    "/retrievefiles",
    response_model=GetRelevantFilesResponse,
    status_code=status.HTTP_200_OK
)
async def retrieve_files(
    request: getRelevantFilesRequest,
    vector_db: Vector_db = Depends(get_vector_db)
):
    
    query = request.query
    retrieve_limit = request.retrieve_limit
    smart_chunking = request.smart_chunking
    source_files = request.source_files

    docs, doc_count = vector_db.get_relevant_docs_paths(query, retrieve_limit, smart_chunking, source_files)

    return GetRelevantFilesResponse(docs_paths=docs, number_docs=doc_count)

@router.post(
    "/retrievechunks",
    response_model=GetRelevantChunksResponse,
    status_code=status.HTTP_200_OK
)
async def retrieve_chunks(
    request: GetRelevantChunksRequest,
    vector_db: Vector_db = Depends(get_vector_db)
):
    
    query = request.query
    retrieve_limit = request.retrieve_limit
    smart_chunking = request.smart_chunking
    source_files = request.source_files

    chunks, chunk_count = vector_db.get_relevant_chunks(query, retrieve_limit, smart_chunking, source_files)
    
    return GetRelevantChunksResponse(files_chunks=chunks, chunk_count=chunk_count)

@router.post("/uploadfile", status_code=status.HTTP_201_CREATED)
async def upload_file(
    file: UploadFile,
    template_folder: str = Body("undefined"),
    vector_db: Vector_db = Depends(get_vector_db)
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

    # Let the vector database process the file
    try:
        await vector_db.process_file(path_to_file)
    except Exception as e:
        print(f"File '{path_to_file}' was saved but processing failed: {e}", flush=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="File was uploaded but could not be processed."
        )

@router.post("/updatefile", status_code=status.HTTP_200_OK)
async def upload_file(
    file: UploadFile,
    template_folder: str = Body("undefined"),
    vector_db: Vector_db = Depends(get_vector_db)
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

    # Let the vector database process the file
    try:
        await vector_db.process_file(path_to_file, update=True)
    except Exception as e:
        print(f"File '{path_to_file}' was saved but updating failed: {e}", flush=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="File was uploaded but could not be updated."
        )

@router.post("/deletefile", status_code=status.HTTP_204_NO_CONTENT)
async def delete_file(
    request_data: DeleteFileRequest,
    vector_db: Vector_db = Depends(get_vector_db)
):

    folder = request_data.folder
    filename = request_data.filename
    relative_path = str(Path(folder) / filename)
    relative_path += ".md"
    
    # Delete teh file from the database
    success = await vector_db.delete_file_from_server(relative_path)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="File not found at the specified path or file could not be deleted."
        )