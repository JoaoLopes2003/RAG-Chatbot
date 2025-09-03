from typing import List
from pydantic import Field
from beanie import Document

class File(Document):
    id: str = Field(..., alias="_id") # filename (folder + filename)
    chunks_ids: List[int] # Ids of chunks
    
    class Settings:
        name = "files"