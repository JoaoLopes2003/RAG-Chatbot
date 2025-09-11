import os
import httpx
from dotenv import load_dotenv
from fastapi import APIRouter, UploadFile, HTTPException, Body, status
from fastapi.responses import StreamingResponse
from starlette.background import BackgroundTask
from pathlib import Path
from schemas.messages import DeleteFileRequest, AnswerPromptRequest, AnswerPromptResponse, GetRelevantDocumentsResponse, GetRelevantChunksResponse, GetRelevantDocumentsContents, GetPromptAnswerLLMAnswer, GetAllFilesResponse
from .utils.utils import build_prompt_from_files, build_prompt_from_chunks, sanitize_filename

router = APIRouter()

load_dotenv()
FILE_DATABASE_ENTRYPOINT = os.getenv("FILE_DATABASE_ENTRYPOINT")
VECTOR_DATABASE_ENTRYPOINT = os.getenv("VECTOR_DATABASE_ENTRYPOINT")
LLM_ENTRYPOINT = os.getenv("LLM_ENTRYPOINT")

def check_connections():
    if not FILE_DATABASE_ENTRYPOINT or not VECTOR_DATABASE_ENTRYPOINT:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server configuration error: service URLs are not set."
        )

@router.get("/getfile", status_code=status.HTTP_200_OK)
async def get_file(
    filename: str
):
    print("-"*30, flush=True)
    print(filename, flush=True)
    print("-"*30, flush=True)

    folder, clean_filename = sanitize_filename(filename)

    params_payload = {
        "folder": folder,
        "filename": clean_filename,
        "converted": False
    }

    client = httpx.AsyncClient(timeout=120.0)

    try:
        # 1. Build the request but don't send it yet
        req = client.build_request(
            "GET",
            f"{FILE_DATABASE_ENTRYPOINT}/getfile",
            params=params_payload
        )
        
        # 2. Send the request and open a stream.
        #    The response object `r` is now available, but the content is not yet downloaded.
        r = await client.send(req, stream=True)
        
        # 3. Check for errors from the downstream service
        r.raise_for_status()

        # 4. Return a StreamingResponse.
        #    - Pass the async byte iterator to stream the content.
        #    - Create a BackgroundTask to close the stream (`r.aclose`) AFTER the response is finished.
        return StreamingResponse(
            r.aiter_bytes(),
            headers=r.headers,
            media_type=r.headers.get("content-type"),
            background=BackgroundTask(r.aclose)
        )
    
    except httpx.HTTPStatusError as e:
        # It's important to manually close the client in case of an error
        # before raising the exception.
        await client.aclose()
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"File service error: {e.response.text}"
        )
    except httpx.RequestError as e:
        await client.aclose()
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Failed to connect to the file service: {e}"
        )
    except Exception as e:
        # Ensure the client is closed in any unexpected error scenario
        await client.aclose()
        print(f"An unexpected error occurred: {e}", flush=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected server error occurred."
        )

@router.get(
    "/getallfiles",
    status_code=status.HTTP_200_OK,
    response_model=GetAllFilesResponse
)
async def get_all_files():
    """
    Acts as a client to fetch all filenames from the file database service.
    """
    try:

        async with httpx.AsyncClient(timeout=120.0) as client:

            response = await client.get(
                f"{FILE_DATABASE_ENTRYPOINT}/getallfiles"
            )

            # Check for HTTP errors (e.g., 404, 500) from the target service
            response.raise_for_status()

            data = response.json()
            filenames = data.get("filenames")

            if filenames is None:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="File database service returned an invalid response format: 'filenames' key missing."
                )

        return GetAllFilesResponse(filenames=filenames)

    except httpx.RequestError as e:
        # Handles network errors, like connection refused
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Could not connect to the file database service: {e}"
        )
    except httpx.HTTPStatusError as e:
        # Handles non-2xx responses from the target service
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"File database service returned an error: {e.response.text}"
        )
    except Exception as e:
        # Catches any other unexpected errors, including JSON parsing issues
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {e}"
        )
    
@router.post("/answerprompt", response_model=AnswerPromptResponse, status_code=status.HTTP_200_OK)
async def answer_prompt(request: AnswerPromptRequest):
    """
    Orchestrates the query answering workflow across multiple services.
    """

    check_connections()

    prompt = request.prompt.strip()
    retrieve_limit = request.retrieve_limit
    smart_chunking = request.smart_chunking
    retrieve_only_chunks = request.retrieve_only_chunks
    source_files = request.source_files
    input_language = request.input_language
    output_language = request.output_language

    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            
            # Step 1: Get relevant document/chunk IDs from the Vector Database
            print(f"Step 1: Getting relevant IDs for query '{request.prompt}'...", flush=True)
            
            # Define parameters for the GET request
            vector_db_payload = {
                'query': prompt,
                'retrieve_limit': retrieve_limit,
                'smart_chunking': smart_chunking,
                'source_files': source_files
            }

            # Select the correct endpoint based on the request
            endpoint = "/retrievechunks" if retrieve_only_chunks else "/retrievefiles"
            
            response_vector_db = await client.post(
                f"{VECTOR_DATABASE_ENTRYPOINT}{endpoint}",
                json=vector_db_payload
            )
            
            if response_vector_db.status_code != status.HTTP_200_OK:
                raise HTTPException(
                    status_code=response_vector_db.status_code,
                    detail=f"Failed to retrieve from Vector DB: {response_vector_db.text}"
                )

            # Parse the JSON
            vector_db_data = response_vector_db.json()
            print("Step 1: Success.", flush=True)


            # Step 2: Get the text content from the File Database
            print("Step 2: Getting content from File Database...", flush=True)
            
            if not retrieve_only_chunks:
                retrieved_docs = GetRelevantDocumentsResponse(**vector_db_data)
                file_db_payload = {'files': retrieved_docs.docs_paths}
                file_db_endpoint = "/getfilescontents"
            else:
                retrieved_chunks = GetRelevantChunksResponse(**vector_db_data)
                
                chunks = []
                for path, file_chunks in retrieved_chunks.files_chunks.items():
                    for chunk in file_chunks.chunks:

                        chunks.append({
                            "path": path,
                            "start_pos": chunk.start_pos,
                            "end_pos": chunk.end_pos
                        })

                file_db_payload = {'chunks': chunks}
                file_db_endpoint = "/getchunkscontents"
            
            response_file_db = await client.post(
                f"{FILE_DATABASE_ENTRYPOINT}{file_db_endpoint}",
                json=file_db_payload
            )

            if response_file_db.status_code != status.HTTP_200_OK:
                raise HTTPException(
                    status_code=response_file_db.status_code,
                    detail=f"Failed to get content from File Database: {response_file_db.text}"
                )
            
            file_contents_data = response_file_db.json()
            print("Step 2: Success.", flush=True)
            

            # Step 3: Get the final answer from the LLM service
            print("Step 3: Sending context to LLM service...", flush=True)
            
            if not retrieve_only_chunks:
                final_prompt = build_prompt_from_files(request.prompt, file_contents_data["documents"])
            else:
                final_prompt = build_prompt_from_chunks(request.prompt, file_contents_data["documents"], retrieved_chunks.files_chunks)
            llm_payload = {'prompt': final_prompt, "chunking": retrieve_only_chunks}
            
            response_llm = await client.post(
                f"{LLM_ENTRYPOINT}/answerprompt",
                json=llm_payload
            )
            
            if response_llm.status_code != status.HTTP_200_OK:
                raise HTTPException(
                    status_code=response_llm.status_code,
                    detail=f"Failed to get answer from LLM Service: {response_llm.text}"
                )

            llm_data = response_llm.json()
            print("Step 3: Success.", flush=True)

            answer = llm_data["answer"]
            sources = llm_data["sources"]
            
            return AnswerPromptResponse(answer=answer, sources=sources)

    except httpx.RequestError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Failed to connect to an upstream service: {e}"
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}", flush=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred during the answering process."
        )

# Upload a new file to the system
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

    print("-"*30, flush=True)
    print(template_folder, flush=True)
    print("-"*30, flush=True)

    check_connections()

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
            md_filename = file.filename + ".md"
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

# Update a file in the system
@router.post("/updatefile", status_code=status.HTTP_201_CREATED)
async def update_file(
    file: UploadFile,
    template_folder: str = Body("undefined"),
):
    """
    Orchestrates the file updating and processing workflow:
    1. Updates the original file on the File Database service.
    2. Retrieves the translated/converted Markdown version from the File Database.
    3. Updates the Markdown version on the Vector Database for embedding.

    Important: In case the file doesn't exist in any of this systems, a new one will be updated.
    """

    print("-"*30, flush=True)
    print(template_folder, flush=True)
    print("-"*30, flush=True)
    
    check_connections()

    try:
        # Read the file content into memory once
        file_content = await file.read()
        
        async with httpx.AsyncClient(timeout=60.0) as client:
            
            # 1. Send the new document to the file database
            print(f"Step 1: Updating '{file.filename}' to File Database...", flush=True)
            files_payload = {
                'file': (file.filename, file_content, file.content_type)
            }
            data_payload = {'template_folder': template_folder}
            
            response_file_db_update = await client.post(
                f"{FILE_DATABASE_ENTRYPOINT}/updatefile",
                files=files_payload,
                data=data_payload
            )

            if response_file_db_update.status_code != status.HTTP_200_OK:
                raise HTTPException(
                    status_code=response_file_db_update.status_code,
                    detail=f"Failed to upload to File Database: {response_file_db_update.text}"
                )
            print("Step 1: Success.", flush=True)


            # 2. Ask the file database for the converted (.md) version
            print(f"Step 2: Retrieving converted Markdown for '{file.filename}'...", flush=True)
            get_file_params = {
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
            print(f"Step 3: Updating '{md_filename}' to Vector Database...", flush=True)
            vector_db_files_payload = {
                'file': (md_filename, md_content, 'text/markdown')
            }
            vector_db_data_payload = {'template_folder': template_folder}

            response_vector_db_update = await client.post(
                f"{VECTOR_DATABASE_ENTRYPOINT}/updatefile",
                files=vector_db_files_payload,
                data=vector_db_data_payload
            )

            if response_vector_db_update.status_code != status.HTTP_200_OK:
                raise HTTPException(
                    status_code=response_vector_db_update.status_code,
                    detail=f"Failed to upload to Vector Database: {response_vector_db_update.text}"
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

# Delete a file from the system
@router.post("/deletefile", status_code=status.HTTP_204_NO_CONTENT)
async def delete_file(
    request: DeleteFileRequest
):
    """
    Orchestrates the file updating and processing workflow:
    1. Deletes the original file from the File Database service.
    3. Deletes the file info from the Vector Database.
    """

    print("-"*30, flush=True)
    print(request, flush=True)
    print("-"*30, flush=True)

    filename = request.filename
    folder = request.folder
    
    check_connections()

    try:
        
        async with httpx.AsyncClient(timeout=60.0) as client:
            
            # 1. Send the request to the File Database service
            print(f"Step 1: Deleting '{filename}' from File Database...", flush=True)
            data_payload = {'filename': filename, 'folder': folder}
            
            response_file_db_delete = await client.post(
                f"{FILE_DATABASE_ENTRYPOINT}/deletefile",
                json=data_payload
            )

            if response_file_db_delete.status_code != status.HTTP_204_NO_CONTENT:
                raise HTTPException(
                    status_code=response_file_db_delete.status_code,
                    detail=f"Failed to delete file from File Database: {response_file_db_delete.text}"
                )
            print("Step 1: Success.", flush=True)
            
            # 3. Delete the file from the Vector Database service
            print(f"Step 2: Deleting '{filename}' from Vector Database...", flush=True)
            vector_db_data_payload = {'filename': filename, 'folder': folder}

            response_vector_db_delete = await client.post(
                f"{VECTOR_DATABASE_ENTRYPOINT}/deletefile",
                json=vector_db_data_payload
            )

            if response_vector_db_delete.status_code != status.HTTP_204_NO_CONTENT:
                raise HTTPException(
                    status_code=response_vector_db_delete.status_code,
                    detail=f"Failed to upload to Vector Database: {response_vector_db_delete.text}"
                )
            print("Step 2: Success.", flush=True)

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
            detail="An unexpected error occurred during file deletion."
        )