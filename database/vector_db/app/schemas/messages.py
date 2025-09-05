from pydantic import BaseModel
from typing import Optional

class UploadFileResponse(BaseModel):
    uploaded: bool
    error: str

class GetRelevantDocumentsResponse(BaseModel):
    docs_paths: list[str]
    number_docs: int

class Chunk(BaseModel):
    path: str
    start_pos: int
    end_pos: int

class GetRelevantChunksResponse(BaseModel):
    chunks: list[Chunk]
    chunk_count: int

class DeleteFileRequest(BaseModel):
    filename: str
    folder: Optional[str] = "undefined"