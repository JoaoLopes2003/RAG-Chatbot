from typing import List
from beanie import Document

class Chunk(Document):
    vector_db_id: int
    embedding: List[float]
    file_id: str
    
    class Settings:
        name = "chunks"