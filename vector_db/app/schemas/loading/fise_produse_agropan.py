from __future__ import annotations
from pydantic import BaseModel
from typing import List, Optional, Literal, Union, Annotated, TYPE_CHECKING
from pydantic.types import conlist

if TYPE_CHECKING:
    from text import Text
    from image import Image
    from table import Table

class Field_1(Text):
    value: Literal["Denumire produs:"]
    children: Annotated[List[Text], conlist(min_length=1, max_length=1)]

class Field_2(Text):
    value: Literal["Gramaj:"]
    children: Annotated[List[Text], conlist(min_length=1, max_length=1)]


class Content(BaseModel):
    type: Literal["text"]
    value: str
    children: List[Field_1, Field_2, Field_3]

class Fpa_schema(Content):
    content: Content