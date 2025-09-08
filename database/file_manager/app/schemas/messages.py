from pydantic import BaseModel
from typing import Optional

class UploadFileResponse(BaseModel):
    uploaded: bool
    error: str

class DeleteFileRequest(BaseModel):
    filename: str
    folder: Optional[str] = "undefined"

class GetFileRequest(BaseModel):
    filename: str
    folder: Optional[str] = "undefined"
    converted: Optional[bool] = False

class GetAllFilesResponse(BaseModel):
    filenames: dict[str, list[str]]

class GetFilesContentsResponse(BaseModel):
    documents: dict[str, str]

class GetChunksContentsResponse(BaseModel):
    documents: dict[str, list[str]]

class GetFilesContentsRequest(BaseModel):
    files: list[str]

class Chunk(BaseModel):
    path: str
    start_pos: int
    end_pos: int

class GetChunksContentsRequest(BaseModel):
    chunks: list[Chunk]