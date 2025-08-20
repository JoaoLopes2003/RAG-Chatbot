from __future__ import annotations
from pydantic import BaseModel
from typing import List, Optional, Literal, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from text import Text
    from image import Image
    from table import Table

class Metadata(BaseModel):
    schema: str
    file_name: str
    file_extension: str
    folder_path: str

class File_schema(BaseModel):
    metadata: Metadata
    content: Optional[Union[List[Union["Text", "Image", "Table"]], Union["Text", "Image", "Table"]]] = None