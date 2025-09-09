from pydantic import BaseModel
from typing import List, Dict, Optional

class PromptRequest(BaseModel):
    prompt: str
    model: Optional[str] = "gemini"
    temperature: Optional[int] = 0.7

class PromptResponse(BaseModel):
    answer: str
    sources: list[dict[str, str]]