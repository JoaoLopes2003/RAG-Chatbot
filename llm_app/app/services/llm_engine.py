import ollama
import os
from typing import List, Dict, Optional

# Set base_url to Docker service name defined in docker-compose
host = os.getenv("OLLAMA_HOST")
if not host:
    raise ValueError("OLLAMA_HOST environment variable is not set.")
ollama.base_url = host

def generate_response(
    prompt: str, 
    model: str = "llama3.2:3b", 
    temperature: float = 0.7,
    history: Optional[List[Dict[str, str]]] = None,
    documents: Optional[List[str]] = None
) -> str:
    """
    Generate response with conversation history and document context
    
    Args:
        prompt: User's current message
        model: Ollama model to use
        temperature: Response creativity (0.0-2.0)
        history: Previous conversation messages [{"role": "user/assistant", "content": "..."}]
        documents: List of relevant documents to include as context
    
    Returns:
        Generated response string
    """
    # Initialize history if None
    if history is None:
        history = []
    
    # Build the current user message
    current_message = prompt
    
    # Add document context if provided
    if documents and len(documents) > 0:
        document_context = "\n\n".join([f"Document {i+1}:\n{doc}" for i, doc in enumerate(documents)])
        current_message = f"Context documents:\n{document_context}\n\nUser question: {prompt}"
    
    # Build messages list: history + current message
    messages = history + [{"role": "user", "content": current_message}]
    
    response = ollama.chat(
        model=model, 
        messages=messages,
        options={
            "temperature": temperature,
            # You can add other parameters here too:
            # "top_p": 0.9,
            # "top_k": 40,
            # "repeat_penalty": 1.1,
            # "num_predict": 512,
        }
    )
    return response['message']['content']