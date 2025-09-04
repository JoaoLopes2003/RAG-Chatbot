from pydantic import BaseModel
from typing import Optional

class UploadFileResponse(BaseModel):
    uploaded: bool
    error: str

class GetRelevantDocumentsRequest(BaseModel):
    query: str
    retrieve_limit: Optional[int] = 10
    smart_search: Optional[bool] = False

class GetRelevantDocumentsResponse(BaseModel):
    docs_paths: list[str]
    number_docs: int