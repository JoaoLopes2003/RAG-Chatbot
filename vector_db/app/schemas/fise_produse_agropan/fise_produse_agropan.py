from __future__ import annotations
from pydantic import BaseModel
from typing import List, Optional, Literal, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from text import Text
    from image import Image
    from table import Table

class Metadata(BaseModel):
    file_name: str
    file_extension: str
    folder_path: str

class Content(BaseModel):
    type: Literal["text"]
    value: str
    children: Optional[List[Union["Text", "Image", "Table"]]] = None

class Fpa_schema(BaseModel):
    metadata: Metadata
    content: Content