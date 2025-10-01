# Vector Database Service

# Overview

This directory contains the implementation of a vector database service that utilizes FAISS for efficient similarity search and retrieval of vector embeddings. The service is designed to handle operations such as adding, searching, and deleting vectors, as well as managing collections of vectors.

## Setup Instructions

If the user wants to only use the vector database service, they can follow these steps:

1. Navigate to the `database/vector_db` directory.

2. Run the docker-compose command to start the service:
   ```bash
   docker-compose up
   ```

3. The vector database service will be accessible at `http://localhost:3006`.

4. To stop the service, use:
   ```bash
   docker-compose down
   ```

## Technologies Used

The vector database service is built using the following technologies:

- **FastAPI** as the web framework;
- **Uvicorn** as the ASGI server.
- **FAISS** for vector similarity search;
- **Beanie** and **Motor** for MongoDB interactions;
- **Pydantic** for data validation;
- **LangChain** for chunking and text splitting;
- **Google Generative AI** for embedding generation.
- **Python-Multipart** for handling file uploads.

## Project Structure

The project is organized as follows:

```
vector_db/
├── app/
│   ├── config/                # Configuration files
│   ├── controllers/           # MongoDB controllers
│   ├── models/                # MongoDB models
│   ├── routes/                # API route definitions
│   ├── schemas/               # Pydantic schemas for request and response validation
│   ├── services/              # Business logic and services
│       ├── utils/             # Utility functions
│   ├── dependencies.py        # File to resolve dependencies
│   ├── main.py                # Main application entry point
├── modify_files/              # Directory for storing files that need to be updated
├── unprocessed_files/         # Directory for storing unprocessed files
├── Dockerfile                 # Dockerfile for building the service image
├── docker-compose.yml         # Docker Compose configuration file
├── requirements.txt           # Python dependencies
└── README.md                  # This README file
```

## Environment Variables

The vector database service uses environment variables for configuration. You can set these variables in a `.env` file in the `vector_db` directory if you intend to run the service independently. (if running as part of the full project, the `.env` file in the root directory will be used).

The following environment variables are used:
- `API_KEY`: Your Google Generative AI API key.
- `MONGO_DB_HOST`: The hostname of the MongoDB server.
- `MONGO_DB_PORT`: The port number of the MongoDB server.
- `MONGO_DB_NAME`: The name of the MongoDB database to use.

## API Endpoints

The vector database service exposes the following API endpoints:
- `POST /uploadfile`: Upload a file to be processed and added to the vector database.
- `POST /updatefile`: Update an existing file in the vector database.
- `POST /deletefile`: Delete a file from the vector database.
- `POST /retrievefiles`: Retrieve relevant files based on a query.
- `POST /retrievechunks`: Retrieve relevant chunks of text based on a query.

## API Documentation

In the following subsections we explore in detail the API endpoints exposed by the vector database service, detailing their purpose, request and response formats, and any relevant notes.

### POST /uploadfile

This endpoint allows users to generate and store vector embeddings for a Markdown file.

#### Request

- **Content-Type**: `multipart/form-data`
- **Parameters**:
    - `file` (required): The Markdown file to be uploaded.
    - `template_folder` (optional): The folder where the file should be stored. Defaults to "undefined".

#### Response

- **Status Code**: `201 Created` on success.
- **Body**: Empty

#### Request Processing

When a request is made to this endpoint, the service performs the following steps:
1. Validates the uploaded file and saves it to the specified folder within the `unprocessed_files` directory.
2. Processes the file to generate vector embeddings using Google Generative AI.
    - From the Markdown, it generates a hierarchical structure based on the headings. The resulting data structure as the effect of a tree;
    - It then chunks the text of each  leaf/node of the tree into smaller pieces, ensuring that each chunk does not exceed a predefined token limit (e.g., 500 tokens). This is done using LangChain's text splitting capabilities.
    - Finally, it generates embeddings for each chunk using the Google Generative AI embeddings model.
3. Stores the generated embeddings in the vector database. It stores both in the permanent memory (mongoDB) and in the temporary memory (FAISS index and in-memory data structures).
4. Finally, we generate a summary for the document using the Google Generative AI model, which is also stored in the database. This is useful for keeping context about the document, in case the user asks for only chunks of it.

It's important to mention that we have two approachs for the embeddings generation, and both are stored in both the permanent and temporary memory:

1. **Smart Chunking**: It's related to the process mentioned above in step 2, where the text is chunked based on the document's structure and a token limit. In addition, it uses a bottom up approach, where we not only generate the embedding for each leaf/node but also for the concatenation of each parent and its children. This way, we can capture the context of larger sections of the document, which can be beneficial for retrieval tasks that require understanding broader topics or themes within the document.

2. **Naive Chunking**: In this approach, the entire text of the document is treated as a single block without considering its structure. The text is then chunked into smaller pieces based solely on the token limit, without any hierarchical context. Embeddings are generated for each of these chunks. This method is simpler and faster but may not capture the nuances of the document's structure and context as effectively as the smart chunking approach.

### POST /updatefile

This endpoint allows users to update an existing Markdown file in the vector database, as well as all its associated data.

#### Request

- **Content-Type**: `multipart/form-data`
- **Parameters**:
    - `file` (required): The updated Markdown file.
    - `template_folder` (optional): The folder where the file is stored. Defaults to "undefined".

#### Response

- **Status Code**: `200 OK` on success.
- **Body**: Empty

#### Request Processing

The requesting process is similar to the `/uploadfile` endpoint, with the key difference being that it updates the existing file and its associated data in the vector database. The additional steps just comprehend deleting the previous data associated with the file (embeddings, chunks, document structure, and summary) before processing and storing the new data. Similarly, the deletion process can be found in the Request Processing section of the `/deletefile` endpoint.

### POST /deletefile

This endpoint allows users to delete a Markdown file and all its associated data from the vector database.

#### Request

- **Content-Type**: `application/json`
- **Body**:
    - `folder` (string, required): The folder where the file is stored.
    - `filename` (string, required): The name of the file to be deleted (without the `.md` extension).

#### Response

- **Status Code**: `204 No Content` on success.
- **Body**: Empty

#### Request Processing

When a request is made to this endpoint, the service performs the following steps:
1. Constructs the relative path of the file using the provided folder and filename.
2. Searches the vector database for the file using the constructed path.
3. If the file is found, it deletes the file and all its associated data, including:
    - The file itself from the storage.
    - All vector embeddings related to the file from both the permanent (MongoDB).
    - The document structure and chunks associated
    - The summary of the document.
4. If the file is not found, it returns a `404 Not Found` error.

It's important to note that since the FAISS index does not allow for direct deletion of individual vectors, the service marks the vectors associated with the deleted file as inactive in a separate data structure. This ensures that these vectors are ignored in future retrieval operations, effectively removing them from active use without physically deleting them from the FAISS index. They only disappear from the FAISS index when the service is restarted and the index is rebuilt from the permanent memory (MongoDB).

Future work could involve implementing a method that regenerates the FAISS index periodically or upon certain triggers, to permanently remove inactive vectors and optimize the index.

### POST /retrievefiles

This endpoint allows users to retrieve relevant files based on a query. This retrieves entire files, not chunks of text.

#### Request

- **Content-Type**: `application/json`
- **Body**:
    - `query` (string, required): The query string to search for relevant files.
    - `retrieve_limit` (integer, optional): The maximum number of relevant files to retrieve. Defaults to 10.
    - `smart_chunking` (boolean, optional): Whether to use smart chunking for retrieval. Defaults to True.
    - `source_files` (list of strings, optional): A list of specific file paths to limit the search. If empty or not provided, the search will include all files.

#### Response

- **Status Code**: `200 OK` on success.
- **Body**:
    - `docs_paths` (list of strings): A list of paths to the relevant files.
    - `number_docs` (integer): The number of relevant files retrieved.
```json
{
  "docs_paths": [
    "folder1/relevant_file1.md",
    "folder1/relevant_file2.md"
  ],
  "number_docs": 2
}
```

#### Request Processing

When a request is made to this endpoint, the service performs the following steps:

1. Generates an embedding for the query using the same method as for the document chunks.
2. Searches the FAISS index for the most similar document embeddings to the query embedding, up to the specified `retrieve_limit`.
    - In case the `source_files` parameter is provided, the system instantiates a temporary FAISS index containing only the embeddings related to the specified files. The search is then performed on this temporary index.
3. Retrieves the paths of the files associated with the most similar embeddings.
4. Returns the list of relevant file paths and the count of retrieved files.

### POST /retrievechunks

This endpoint allows users to retrieve relevant chunks of text based on a query. This retrieves chunks of text, not entire files.

#### Request

- **Content-Type**: `application/json`
- **Body**:
    - `query` (string, required): The query string to search for relevant chunks.
    - `retrieve_limit` (integer, optional): The maximum number of relevant chunks to retrieve. Defaults to 10.
    - `smart_chunking` (boolean, optional): Whether to use smart chunking for retrieval. Defaults to True.
    - `source_files` (list of strings, optional): A list of specific file paths to limit the search. If empty or not provided, the search will include all files.

#### Response

- **Status Code**: `200 OK` on success.
- **Body**:
    - `files_chunks` (dictionary): A dictionary where keys are file paths and values are lists of relevant chunks from those files. It includes also a summary of the document.
    - `chunk_count` (integer): The total number of relevant chunks retrieved.
```json
{
    "files_chunks": {
        "folder1/relevant_file1.md": {
            "summary": "This is a summary of the document.",
            "chunks": [
                "Relevant chunk 1 from file 1.",
                "Relevant chunk 2 from file 1."
            ]
        },
        "folder2/relevant_file2.md": {
            "summary": "This is a summary of the document.",
            "chunks": [
                "Relevant chunk 1 from file 2."
            ]
        }
    },
    "chunk_count": 3
}
```

#### Request Processing

The request processing for this endpoint is similar to the `/retrievefiles` endpoint, with the key difference being that it retrieves a summary of the document and chunks of text instead of entire files.