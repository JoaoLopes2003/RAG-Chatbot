from pydantic import BaseModel

class UploadFileResponse(BaseModel):
    uploaded: bool
    error: str