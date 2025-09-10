from pydantic import BaseModel
from typing import Optional

class UploadFileResponse(BaseModel):
    uploaded: bool
    error: str

class GetRelevantFilesResponse(BaseModel):
    docs_paths: list[str]
    number_docs: int

class Chunk(BaseModel):
    start_pos: int
    end_pos: int

class FileChunks(BaseModel):
    summary: str
    chunks: list[Chunk]

class GetRelevantChunksResponse(BaseModel):
    files_chunks: dict[str, FileChunks]
    chunk_count: int

class DeleteFileRequest(BaseModel):
    filename: str
    folder: Optional[str] = "undefined"

class getRelevantFilesRequest(BaseModel):
    query: str
    retrieve_limit: Optional[int] = 10
    smart_chunking: Optional[bool] = False
    source_files: Optional[list[str]] = None

class GetRelevantChunksRequest(BaseModel):
    query: str
    retrieve_limit: Optional[int] = 10
    smart_chunking: Optional[bool] = False
    source_files: Optional[list[str]] = None