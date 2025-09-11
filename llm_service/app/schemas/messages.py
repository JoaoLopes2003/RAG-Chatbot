from pydantic import BaseModel
from typing import List, Dict, Optional

class PromptRequest(BaseModel):
    prompt: str
    model: Optional[str] = "gemini"
    temperature: Optional[int] = 0.7
    chunking: Optional[bool] = False

class PromptResponse(BaseModel):
    answer: str
    sources: list[dict[str, str]]