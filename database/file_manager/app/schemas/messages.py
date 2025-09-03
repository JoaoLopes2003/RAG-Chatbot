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