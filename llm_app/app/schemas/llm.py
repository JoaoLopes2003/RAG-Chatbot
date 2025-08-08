from pydantic import BaseModel
from typing import List, Dict, Optional

class PromptRequest(BaseModel):
    prompt: str
    model: Optional[str] = "llama3.2:3b"
    history: Optional[List[Dict[str, str]]] = None
    documents: Optional[List[str]] = None

class PromptResponse(BaseModel):
    response: str