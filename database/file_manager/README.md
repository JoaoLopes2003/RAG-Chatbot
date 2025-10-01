# File Manager Service

## Overview

This directory contains the file manager service, which is responsible for handling file uploads, storage, and retrieval. It provides APIs to upload files, list stored files, and download files.

## Setup Instructions

If the user wants to only run the file manager service, they can follow these steps:

1. Navigate to the `database/file_manager` directory.

2. Run the docker-compose command to start the service:
   ```bash
   docker-compose up
   ```

3. The file manager service will be accessible at `http://localhost:3005`.

4. To stop the service, run:
   ```bash
   docker-compose down
   ```

## Technologies Used

The file manager service is built using the following technologies:

- **FastAPI** as the web framework;
- **Uvicorn** as the ASGI server;
- **Python-dotenv** for environment variable management;
- **Pydantic** for data validation;
- **Google Generative AI** for AI functionalities;
- **Python-multipart** for handling file uploads.

## Project Structure

The project structure is as follows:

```
file_manager/
├── app/
│   ├── routes/            # API route definitions
│   ├── schemas/           # Pydantic models for request and response validation
│   ├── services/          # Business logic and service implementations
│   ├── main.py            # Entry point for the FastAPI application
├── converted_files/       # Directory for storing converted files
├── modify_files/          # Directory for storing files that need to be updated
├── original_files/        # Directory for storing the original versions of files
├── unprocessed_files/     # Directory for storing unprocessed files
├── Dockerfile             # Dockerfile for building the service image
├── docker-compose.yml     # Docker Compose configuration file
├── requirements.txt       # Python dependencies
└── README.md              # This README file
```

## Environment Variables

The file manager service uses environment variables for configuration. You can set these variables in a `.env` file in the `file_manager` directory if you intend to run the service independently. (if running as part of the full application stack, the main `.env` file in the root directory will be used).

The following environment variables are used:
- `API_KEY`: API key for accessing Google Generative AI services.

Here is an example `.env` file:

```
API_KEY=your_google_generative_ai_api_key
```

## API Endpoints

The file manager service exposes the following API endpoints:
- `GET /getfile`: Retrieve a file from the server.
- `POST /uploadfile`: Upload a new file to the server.
- `POST /updatefile`: Update an existing file on the server.
- `POST /deletefile`: Delete a file from the server.
- `GET /getallfiles`: List all files stored on the server.
- `POST /getfilescontents`: Retrieve the contents of specified files.
- `POST /getchunkscontents`: Retrieve the contents of specified file chunks.

## API Documentation

In the following subsections we explore in detail the API endpoints exposed by the file manager service, detailing their purpose, request and response formats, and any relevant notes.

### GET /getfile

This endpoint retrieves a file from the server.

#### Request

- **Method**: GET
- **Query Parameters**:
  - `folder` (str): The folder where the file is located.
  - `filename` (str): The name of the file to retrieve.
  - `converted` (bool, optional): Whether to retrieve the Markdown converted version of the file. Defaults to `True`, which retrieves the converted file. If set to `False`, retrieves the original file.

#### Response

- **Status Code**: `200 OK` on success.
- **Content**: The requested file as a binary stream.

#### Request Processing

When a request is made to this endpoint, the server performs the following steps:
1. It constructs the relative path to the file using the provided `folder` and `filename`.
2. It checks if the file exists in the file manager's records.
3. If the file does not exist, it returns a `400 Bad Request` error indicating that the folder and/or filename are invalid.
4. If the file exists, it checks the `converted` parameter:
   - If `converted` is `True`, it retrieves the path to the Markdown converted version of the file.
   - If `converted` is `False`, it retrieves the path to the original file.
5. Finally, it returns the file as a `FileResponse`, allowing the client to download it.

### GET /getallfiles

This endpoint lists all files stored on the server.

#### Request

- **Method**: GET

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

When a request is made to this endpoint, the server performs the following steps:
1. It retrieves all files from the file manager's records.
2. It constructs a response object containing the list of filenames organized by their respective folders.

### POST /uploadfile

This endpoint uploads a new file to the server.

#### Request

- **Method**: POST
- **Form Data**:
    - `file` (UploadFile): The file to be uploaded.
    - `template_folder` (str, optional): The folder where the file should be stored. Defaults to `"undefined"`.

#### Response

- **Status Code**: `201 Created` on success.
- **Content**: None.

#### Request Processing

When a request is made to this endpoint, the server performs the following steps:
1. It sanitizes the `template_folder` and filename to prevent directory traversal attacks and ensure valid filenames.
2. It constructs the path to the target folder within the `unprocessed_files` directory and ensures it exists.
3. It writes the uploaded file to the unprocessed files directory.
4. It invokes the file manager to process the newly uploaded file, converting it to Markdown and storing it appropriately.

### POST /updatefile

This endpoint updates an existing file on the server.

#### Request

- **Method**: POST
- **Form Data**:
    - `file` (UploadFile): The file to be updated.
    - `template_folder` (str, optional): The folder where the file is located. Defaults to `"undefined"`.

#### Response

- **Status Code**: `200 OK` on success.
- **Content**: None.

#### Request Processing

When a request is made to this endpoint, the server performs the following steps:
1. It sanitizes the `template_folder` and filename to prevent directory traversal attacks and ensure valid filenames.
2. It constructs the path to the target folder within the `unprocessed_files` directory and ensures it exists.
3. It writes the uploaded file to the modify files directory.
4. It invokes the file manager to process the updated file, converting it to Markdown and updating it appropriately.

## POST /deletefile

This endpoint deletes a file from the server.

#### Request

- **Method**: POST
- **Body**: A JSON object containing the folder and filename of the file to be deleted.
```json
{
  "folder": "folder_name",
  "filename": "file_name.txt"
}
```

#### Response

- **Status Code**: `204 No Content` on success.
- **Content**: None.

#### Request Processing

When a request is made to this endpoint, the server performs the following steps:
1. It constructs the relative path to the file using the provided `folder` and `filename`.
2. It checks if the file exists in the file manager's records.
3. If the file does not exist, it returns a `404 Not Found` error indicating that the file was not found at the specified path.
4. If the file exists, it invokes the file manager to delete the file from the server storage.
5. If the deletion is successful, it returns a `204 No Content` response. If the deletion fails, it returns a `500 Internal Server Error`.

### POST /getfilescontents

This endpoint retrieves the entire contents of specified files.

#### Request
- **Method**: POST
- **Body**: A JSON object containing a list of file paths.
```json
{
  "files": ["folder1/file1.txt", "folder2/file3.txt"]
}
```

#### Response

- **Status Code**: `200 OK` on success.
- **Content**: A JSON object containing the contents of the requested files.
```json
{
    "folder1/file1.txt": "Content of file 1...",
    "folder2/file3.txt": "Content of file 3..."
}
```

#### Request Processing

When a request is made to this endpoint, the server performs the following steps:
1. Iterates over the list of file paths provided in the request.
2. For each file path, it retrieves the content of the file using the file manager, in case the file exists.
3. It constructs a response object containing the contents of the requested files.

### POST /getchunkscontents

This endpoint retrieves the portions (chunks) of text from specified files.

#### Request

- **Method**: POST
- **Body**: A JSON object containing a list of chunk identifiers.
```json
{
  "chunks": [
    {
      "path": "folder1/file1.txt",
      "start_pos": 0,
      "end_pos": 100
    },
    {
        "path": "folder1/file1.txt",
        "start_pos": 150,
        "end_pos": 250
    },
    {
      "path": "folder2/file3.txt",
      "start_pos": 50,
      "end_pos": 150
    }
  ]
}
```

#### Response

- **Status Code**: `200 OK` on success.
- **Content**: A JSON object containing the contents of the requested chunks.
```json
{
    "folder1/file1.txt": [
        "Content of chunk 1...",
        "Content of chunk 2..."
    ],
    "folder2/file3.txt": [
        "Content of chunk 1..."
    ]
}
```

#### Request Processing

When a request is made to this endpoint, the server performs the following steps:
1. Iterates over the list of chunk identifiers provided in the request.
2. For each chunk identifier, it retrieves the specified portion of text from the corresponding file using the file manager, in case the file exists.
3. It constructs a response object containing the contents of the requested chunks, organized by their respective file paths.

## Aditional Notes

### Markdown Conversion Process

As mentioned above the server stores files in both their original format and a converted Markdown format. The conversion process is handled by the file manager service and involves the following steps:
1. The file to be converted is read from the `unprocessed_files` or `modify_files` directory.
2. The file is uploaded to the Google Generative AI cloud storage.
3. Relevant examples are selected from the existing files to guide the conversion process.
    - The selection prioritizes files from the same folder as the file being converted, followed by other loaded and unloaded files.
4. The selected examples are also uploaded to the cloud if they are not already present.
5. A prompt is created using the file to be converted and the selected examples.
6. The prompt is sent to the Google Generative AI model to generate the Markdown conversion and the response is saved to the `converted_files` directory.

### Server Booting Process

When the file manager service starts, it performs the following initialization steps:
1. It cleans up any existing files in the Google Generative AI cloud storage to ensure a fresh state.
2. It verifies the existence of the directories for original and converted files.
3. It check for any inconsistencies between original files and their converted versions, deleting any converted files that do not have a corresponding original file. In addition, it converts any original files that do not have a converted version.
4. It preloads a subset of files to the cloud storage to optimize performance for future conversions.

## Important Notes

It's important to note the following:

- The more and better examples already loaded in the service memory, the better the conversion results will be. For instance, if a user uploads a file to a folder with already many similar files, the conversion will be of higher quality. On the other hand, if a user uploads a file to a new folder or a folder with few files, the conversion quality may be lower.
- For now, the service only supports PDF files for conversion.