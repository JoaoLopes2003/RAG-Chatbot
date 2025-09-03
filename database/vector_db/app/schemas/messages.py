from pydantic import BaseModel
from typing import Optional

class UploadFileResponse(BaseModel):
    uploaded: bool
    error: str