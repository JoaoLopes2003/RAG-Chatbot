from typing import List
from beanie import Document

class DefaultChunk(Document):
    embedding: List[float]
    file_id: str
    
    class Settings:
        name = "default_chunks"