from pydantic import BaseModel
from typing import Optional, Literal

class Metadata_Img(BaseModel):
    file_name: str
    file_extension: str
    folder_path: str
    alt_text: Optional[str] = None

class Image(BaseModel):
    type: Literal["image"]
    metadata: Metadata_Img