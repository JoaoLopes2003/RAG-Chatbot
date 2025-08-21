import ollama
import os
from typing import List, Dict, Optional
from services.models.gemini_model import generate_response as generate_response_gemini
from services.models.llama_model import generate_response as generate_response_llama

def generate_response(
    prompt: str, 
    model: str = "llama3.2:3b", 
    temperature: float = 0.7,
    history: Optional[List[Dict[str, str]]] = None,
    documents: str = None
) -> str:
    """
    Generate response with conversation history and document context
    
    Args:
        prompt: User's current message
        model: Model to use
        temperature: Response creativity (0.0-2.0)
        history: Previous conversation messages [{"role": "user/assistant", "content": "..."}]
        documents: A string of relevant documents to include as context
    
    Returns:
        Generated response string
    """
    history = []
    model = "gemini"

    user_query = "<query>" + documents + "</query>\n"
    prompt = user_query + documents

    # Check which model the user wants to use
    if model == "gemini":

        history.append({'role': 'user', 'parts': [{'text': prompt}]})
        response = generate_response_gemini(history)
        print(response)
        return response
    elif model == "llama":

        history.append({"role": "user", "content": prompt})
        response = generate_response_llama(history)
        print(response)
        return response