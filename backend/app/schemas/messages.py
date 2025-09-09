from pydantic import BaseModel
from typing import Optional

class AnswerPromptRequest(BaseModel):
    prompt: str
    retrieve_limit: Optional[int] = 30
    smart_chunking: Optional[bool] = True
    retrieve_only_chunks: Optional[bool] = True

class AnswerPromptResponse(BaseModel):
    answer: str
    sources: list[dict[str, str]]

class DeleteFileRequest(BaseModel):
    filename: str
    folder: str

class GetRelevantDocumentsResponse(BaseModel):
    docs_paths: list[str]
    number_docs: int

class Chunk(BaseModel):
    start_pos: int
    end_pos: int

class FileChunks(BaseModel):
    summary: str
    chunks: list[Chunk]

class GetRelevantChunksResponse(BaseModel):
    files_chunks: dict[str, FileChunks]
    chunk_count: int

class GetRelevantDocumentsContents(BaseModel):
    documents: dict[str, list[str]]

class GetPromptAnswerLLMAnswer(BaseModel):
    answer: str