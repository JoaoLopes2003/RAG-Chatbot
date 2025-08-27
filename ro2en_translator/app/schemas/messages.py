from pydantic import BaseModel

class PromptRequest(BaseModel):
    query: str

class PromptResponse(BaseModel):
    response: str