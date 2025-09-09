from .models.gemini_model import generate_response as generate_response_gemini

def generate_response(
    prompt_with_docs: str, 
    model: str = "gemini", 
    temperature: float = 0.7,
    chunking: bool = False
) -> dict:

    if model =="gemini":
        answer_json = generate_response_gemini(prompt_with_docs=prompt_with_docs, temperature=temperature, chunking=chunking)
    else:
        answer_json = {
            "answer": "I'm sorry, we don't have that model available.",
            "sources": []
        }
    
    return answer_json