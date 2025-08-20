from __future__ import annotations
from pydantic import BaseModel
from typing import List, Optional, Literal, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from image import Image
    from table import Table

class Text(BaseModel):
    type: Literal["text"]
    value: str
    children: Optional[List[Union["Text", "Image", "Table"]]] = None