from fastapi import APIRouter
from schemas.llm import PromptRequest, PromptResponse
from services.llm_engine import generate_response

router = APIRouter()

@router.post("/", response_model=PromptResponse)
def get_llm_response(prompt_req: PromptRequest):
    answer = generate_response(prompt=prompt_req.prompt, history=prompt_req.history, documents=prompt_req.documents)
    return PromptResponse(response=answer)