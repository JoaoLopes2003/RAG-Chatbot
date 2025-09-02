from pydantic import BaseModel

class PromptRequest(BaseModel):
    template_folder: str
    file_path: str

class PromptResponse(BaseModel):
    req_status: int
    file_path: str