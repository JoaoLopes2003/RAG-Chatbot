from typing import List
from beanie import Document

class DefaultChunk(Document):
    embedding: List[float]
    file_id: str
    start_pos: int | None
    end_pos: int | None
    
    class Settings:
        name = "default_chunks"