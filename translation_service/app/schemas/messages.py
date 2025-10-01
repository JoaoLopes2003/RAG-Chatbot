from pydantic import BaseModel

class PromptRequest(BaseModel):
    query: str
    origin: str
    target: str

class PromptResponse(BaseModel):
    response: str