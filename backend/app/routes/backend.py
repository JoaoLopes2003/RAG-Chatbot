import os
import httpx
from dotenv import load_dotenv
from fastapi import APIRouter, UploadFile, HTTPException, Body, status
from pathlib import Path

router = APIRouter()

load_dotenv()
FILE_DATABASE_ENTRYPOINT = os.getenv("FILE_DATABASE_ENTRYPOINT")
VECTOR_DATABASE_ENTRYPOINT = os.getenv("VECTOR_DATABASE_ENTRYPOINT")
# LLM_url = os.getenv("LLM_ENTRYPOINT") # Not used in this function

@router.post("/uploadfile", status_code=status.HTTP_201_CREATED)
async def upload_file(
    file: UploadFile,
    template_folder: str = Body("undefined"),
):
    """
    Orchestrates the file upload and processing workflow:
    1. Uploads the original file to the File Database service.
    2. Retrieves the translated/converted Markdown version from the File Database.
    3. Uploads the Markdown version to the Vector Database for embedding.
    """
    if not FILE_DATABASE_ENTRYPOINT or not VECTOR_DATABASE_ENTRYPOINT:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server configuration error: service URLs are not set."
        )

    try:
        # Read the file content into memory once
        file_content = await file.read()
        
        async with httpx.AsyncClient(timeout=60.0) as client:
            
            # 1. Send the new document to the file database
            print(f"Step 1: Uploading '{file.filename}' to File Database...", flush=True)
            files_payload = {
                'file': (file.filename, file_content, file.content_type)
            }
            data_payload = {'template_folder': template_folder}
            
            response_file_db_upload = await client.post(
                f"{FILE_DATABASE_ENTRYPOINT}/uploadfile",
                files=files_payload,
                data=data_payload
            )

            if response_file_db_upload.status_code != status.HTTP_201_CREATED:
                raise HTTPException(
                    status_code=response_file_db_upload.status_code,
                    detail=f"Failed to upload to File Database: {response_file_db_upload.text}"
                )
            print("Step 1: Success.", flush=True)


            # 2. Ask the file database for the converted (.md) version
            print(f"Step 2: Retrieving converted Markdown for '{file.filename}'...", flush=True)
            get_file_params = {  # Renamed for clarity
                "folder": template_folder,
                "filename": file.filename,
                "converted": True
            }
            
            response_get_md = await client.get(
                f"{FILE_DATABASE_ENTRYPOINT}/getfile",
                params=get_file_params
            )
            
            if response_get_md.status_code != status.HTTP_200_OK:
                raise HTTPException(
                    status_code=response_get_md.status_code,
                    detail=f"Failed to retrieve converted file from File Database: {response_get_md.text}"
                )
            
            md_content = response_get_md.content
            md_filename = Path(file.filename).with_suffix(".md").name
            print("Step 2: Success.", flush=True)

            
            # 3. Send the converted version to the vector database
            print(f"Step 3: Uploading '{md_filename}' to Vector Database...", flush=True)
            vector_db_files_payload = {
                'file': (md_filename, md_content, 'text/markdown')
            }
            vector_db_data_payload = {'template_folder': template_folder}

            response_vector_db_upload = await client.post(
                f"{VECTOR_DATABASE_ENTRYPOINT}/uploadfile",
                files=vector_db_files_payload,
                data=vector_db_data_payload
            )

            if response_vector_db_upload.status_code != status.HTTP_201_CREATED:
                raise HTTPException(
                    status_code=response_vector_db_upload.status_code,
                    detail=f"Failed to upload to Vector Database: {response_vector_db_upload.text}"
                )
            print("Step 3: Success.", flush=True)

    except httpx.RequestError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Failed to connect to an upstream service: {e}"
        )
    except HTTPException as e:
        # Re-raise known HTTP exceptions
        raise e
    except Exception as e:
        print(f"An unexpected error occurred: {e}", flush=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred during file processing."
        )
    finally:
        await file.close()

    return {"message": f"File '{file.filename}' was successfully uploaded and processed by all services."}
