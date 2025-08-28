from fastapi import APIRouter
from services.convert2md import convert_file
from schemas.messages import PromptRequest, PromptResponse

router = APIRouter()

@router.post("/", response_model=PromptResponse)
def convert2md(query_req: PromptRequest):

    status, path = convert_file(file_path=query_req.file_path, template_folder=query_req.template_folder)

    if status==200:
        print(f"The file was converted successfully to Markdown format and stored in the following path: {path}.")
        return PromptResponse(req_status=200, file_path=path)
    else:
        print("There was an error converting the file to Markdown.")
        return PromptResponse(req_status=400,file_path="")