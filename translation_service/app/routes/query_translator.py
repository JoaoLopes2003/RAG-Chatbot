from fastapi import APIRouter
from services.ro2en import generate_response
from schemas.messages import PromptRequest, PromptResponse

router = APIRouter()

@router.post("/", response_model=PromptResponse)
def query_search_engine(query_req: PromptRequest):

    query = query_req.query
    origin_language = query_req.origin
    target_language = query_req.target

    response = generate_response(query_req.query, origin_language, target_language)

    print(f"The query response was the following: {response}")

    return PromptResponse(response=response)