from pydantic import BaseModel

class PromptRequest(BaseModel):
    file_path: str

class PromptResponse(BaseModel):
    response: str