from typing import List
from beanie import Document

class File(Document):
    filename: str # filename (folder + filename)
    summary: str # Summary of the file, for context
    chunks_ids_default_parsing: List[str] # Ids of chunks
    chunks_ids_smart_parsing: List[str] # Ids of chunks
    
    class Settings:
        name = "files"