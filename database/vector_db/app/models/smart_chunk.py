from typing import List
from beanie import Document

class SmartChunk(Document):
    embedding: List[float]
    file_id: str
    start_pos: int
    end_pos: int
    
    class Settings:
        name = "smart_chunks"