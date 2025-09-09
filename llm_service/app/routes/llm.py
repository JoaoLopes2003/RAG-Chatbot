from fastapi import APIRouter, status
from schemas.messages import PromptRequest, PromptResponse
from services.llm_engine import generate_response

router = APIRouter()

@router.post("/answerprompt", response_model=PromptResponse, status_code=status.HTTP_200_OK)
def get_llm_response(prompt_req: PromptRequest):

    prompt = prompt_req.prompt
    model = prompt_req.model
    temperature = prompt_req.temperature
    chunking = prompt_req.chunking

    answer_json = generate_response(model=model, prompt_with_docs=prompt, temperature=temperature, chunking=chunking)

    answer = answer_json["answer"]
    sources = answer_json["sources"]
    
    return PromptResponse(answer=answer, sources=sources)