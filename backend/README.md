# Backend Service

## Overview

This directory contains the backend service for our application. **The backend is the only service the frontend communicates with** directly, incapsulating all business logic and data management.

## Setup Instructions

If the user wants to only run the backend service, they can follow these steps:

1. Run the docker compose file located in the backend directory:
   ```bash
   docker compose up
   ```

2. The backend service will be accessible at `http://localhost:3007`.

3. To stop the backend service, use:
   ```bash
   docker compose down
   ```

It's important to note that the backend service is designed to work in conjunction with all the other services in the project. This way, it will not work as expected if run in isolation. We recommend running the entire project using the main `docker-compose.yml` file located in the root directory of the project.

## Technologies Used

The project is built using the following technologies:
- **FastAPI** as the web framework;
- **Uvicorn** as the ASGI server;
- **HTTPX** for making HTTP requests.
- **python-dotenv** for environment variable management;
- **python-multipart** for handling file uploads.

## Project Structure

The project is organized as follows:

```
backend/
├── app/
│   ├── routes/          # API route definitions
│       ├── utils/       # Utility functions and helpers for routes
│   ├── schemas/         # Pydantic models for request and response validation
│   ├── services/        # Business logic and service layer
│   ├── main.py          # Entry point for the FastAPI application
├── Dockerfile           # Dockerfile for building the backend service image
├── docker-compose.yml   # Docker Compose file for the backend service
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Environment Variables

The backend service uses environment variables for configuration. You can define these variables in a `.env` file located in the `backend` directory if you intend on running the backend service independently. (if you run the entire project using the main `docker-compose.yml`, the environment variables will be managed there).

The following environment variables are used:
- `FILE_DATABASE_ENTRYPOINT`: URL of the file management service.
- `VECTOR_DATABASE_ENTRYPOINT`: URL of the vector database service.
- `LLM_ENTRYPOINT`: URL of the language model service.
- `TRANSLATION_SERVICE_ENTRYPOINT`: URL of the translation service.

Here is an example of a `.env` file:

```
FILE_DATABASE_ENTRYPOINT=http://file_manager:3005
VECTOR_DATABASE_ENTRYPOINT=http://vector_db:3006
LLM_ENTRYPOINT=http://llm_service:3002
TRANSLATION_SERVICE_ENTRYPOINT=http://translation_service:3004
```

## API Endpoints

The backend service exposes the following API endpoints:
- `GET /getfile`: Retrieve a file from the file database.
- `GET /getallfiles`: Retrieve a list of all files from the file database.
- `POST /answerprompt`: Answer a user prompt by orchestrating multiple services.
- `POST /uploadfile`: Upload a new file to the system.
- `POST /updatefile`: Update an existing file in the system.
- `POST /deletefile`: Delete a file from the system.

## API Documentation

In the following subsections we explore in detail the API endpoints exposed by the backend service, detailing their purpose, request and response formats, and any relevant notes.

### GET /getfile

This endpoint retrieves a file from the file database service. It streams the file content directly to the client.

#### Request

- **Method**: `GET`
- **Query Parameters**:
  - `filename` (str): The name of the file to retrieve, including its folder name.

#### Response

- **Status Code**: `200 OK` on success.
- **Content**: The file content is streamed directly to the client. The `Content-Type` header reflects the file's MIME type.

#### Request Processing

The endpoint performs the following steps:
1. Sanitizes the provided filename to prevent directory traversal attacks.
2. Constructs a request to the file database service with the sanitized filename.
3. Streams the response from the file database service directly to the client using `StreamingResponse`.

### GET /getallfiles

This endpoint retrieves a list of all filenames from the file database service.

#### Request

- **Method**: `GET`

#### Response

- **Status Code**: `200 OK` on success.
- **Content**: A JSON object containing a list of filenames.
```json
{
  "filenames": {
    "folder1": ["file1.txt", "file2.txt"],
    "folder2": ["file3.txt"]
  }
}
```

#### Request Processing

The endpoint performs the following steps:
1. Sends a request to the file database service to fetch all filenames.
2. Validates the response format to ensure it contains the expected `filenames` key.
3. Returns the list of filenames to the client.

### POST /uploadfile

This endpoint orchestrates the file upload and processing workflow. It uploads the original file to the file database, retrieves the translated/converted Markdown version, and uploads it to the vector database for embedding.

#### Request

- **Method**: `POST`
- **Body Parameters**:
    - `file` (UploadFile): The file to be uploaded.
    - `template_folder` (str, optional): The folder where the file should be stored. Defaults to "undefined".

#### Response

- **Status Code**: `201 Created` on success.
- **Content**: None.

#### Request Processing

The endpoint performs the following steps:
1. Reads the file content into memory.
2. Sends the file to the file database service for storage.
3. Requests the converted Markdown version of the file from the file database.
4. Sends the Markdown file to the vector database service for embedding.

### POST /updatefile

This endpoint orchestrates the file updating and processing workflow. It updates the original file in the file database, retrieves the translated/converted Markdown version, and updates it in the vector database for embedding.

#### Request

- **Method**: `POST`
- **Body Parameters**:
    - `file` (UploadFile): The file to be updated.
    - `template_folder` (str, optional): The folder where the file is stored.

#### Response

- **Status Code**: `201 Created` on success.
- **Content**: None.

#### Request Processing

The endpoint performs the following steps:
1. Reads the file content into memory.
2. Sends the updated file to the file database service.
3. Requests the converted Markdown version of the file from the file database.
4. Sends the Markdown file to the vector database service for updating embedding.

### POST /deletefile

This endpoint orchestrates the file deletion workflow. It deletes the original file from the file database and removes its information from the vector database.

#### Request

- **Method**: `POST`
- **Body Parameters**:
    - `filename` (str): The name of the file to be deleted.
    - `folder` (str): The folder where the file is stored.

#### Response

- **Status Code**: `204 No Content` on success.
- **Content**: None.

#### Request Processing

The endpoint performs the following steps:
1. Sends a request to the file database service to delete the specified file if it exists.
2. Sends a request to the vector database service to remove the file's information if it exists.

It's important to mention that this is not an atomic operation. If the file is deleted from the file database but fails to be deleted from the vector database (or vice-versa), the system may end up in an inconsistent state. Future improvements could include implementing a more robust transaction mechanism to ensure atomicity across services.

### POST /answerprompt

This endpoint orchestrates the query answering workflow across multiple services. It handles prompt translation, document retrieval, content fetching, and answer generation.

#### Request

- **Method**: `POST`
- **Body Parameters**:
    - `prompt` (str): The user prompt to be answered.
    - `retrieve_limit` (int, optional): The maximum number of documents/chunks to retrieve. Defaults to 10.
    - `smart_chunking` (bool, optional): Whether to use smart chunking for retrieval. Defaults to True.
    - `retrieve_only_chunks` (bool, optional): Whether to retrieve only chunks instead of full documents. Defaults to True.
    - `source_files` (list[str], optional): Specific source files to consider for retrieval. Defaults to None (all files).
    - `input_language` (str, optional): The language of the input prompt. Can be "en" or "ro". Defaults to "en".
    - `output_language` (str, optional): The desired language of the output answer. Can be "en" or "ro". Defaults to "en".

#### Response

- **Status Code**: `200 OK` on success.
- **Content**: A JSON object containing the answer and its sources.
```json
{
    "answer": "The generated answer to the prompt.",
    "sources": [
        {"document_name": "file1.txt", "quote": "Relevant context from file1."},
        {"document_name": "file2.txt", "quote": "Relevant context from file2."}
    ]
}
```

#### Request Processing

1. If the input language is Romanian, translates the prompt to English using the translation service.
2. Retrieves relevant document or chunk IDs from the vector database based on the prompt.
3. Fetches the text content of the retrieved documents or chunks from the file database.
4. Constructs a final prompt combining the user prompt and the retrieved context.
5. Sends the final prompt to the LLM service to generate an answer.
6. If the desired output language is Romanian, translates the answer back to Romanian using the translation service.
7. Returns the final answer and its sources to the client.

## Important Notes

It's important to note that for the prompt answering we use:

- **RAG (Retrieval-Augmented Generation)**: We retrieve relevant documents or chunks from a vector database to provide context for the LLM, enhancing the quality and accuracy of the generated answers. Be careful when setting the `retrieve_limit` parameter, as a very high value may lead to performance issues or exceed token limits of the LLM. A balance in accuracy and performance should be sought.