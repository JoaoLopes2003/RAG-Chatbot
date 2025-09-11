from fastapi import APIRouter
from services.ro2en import generate_response
from schemas.messages import PromptRequest, PromptResponse

router = APIRouter()

@router.post("/", response_model=PromptResponse)
def query_search_engine(query_req: PromptRequest):

    response = generate_response(query_req.query)

    print(f"The query response was the following: {response}")

    return PromptResponse(response=response)