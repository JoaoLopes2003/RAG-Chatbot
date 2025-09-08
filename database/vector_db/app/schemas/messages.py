from pydantic import BaseModel
from typing import Optional

class UploadFileResponse(BaseModel):
    uploaded: bool
    error: str

class GetRelevantDocumentsResponse(BaseModel):
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