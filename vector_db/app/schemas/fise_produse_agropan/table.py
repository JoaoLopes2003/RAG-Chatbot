from __future__ import annotations
from pydantic import BaseModel
from typing import List, Literal, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from image import Image
    from text import Text

# Defining the structure of a table and it's elements
class TableHeaderEl(BaseModel):
    column: int
    el: Union["Text", "Image"]

class tableContentEl(BaseModel):
    row: int
    column: int
    el: Union["Text", "Image"]

class Table(BaseModel):
    type: Literal["table"]
    n_rows: int
    n_columns: int
    header: List[TableHeaderEl]
    body: List[List[tableContentEl]]