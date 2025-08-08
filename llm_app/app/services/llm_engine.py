import ollama
import os

# Set base_url to Docker service name defined in docker-compose
host = os.getenv("OLLAMA_HOST")
if not host:
    raise ValueError("OLLAMA_HOST environment variable is not set.")
ollama.base_url = host

def generate_response(prompt: str, model: str = "llama3.2:3b", temperature: float = 0.7) -> str:
    response = ollama.chat(
        model=model, 
        messages=[{"role": "user", "content": prompt}],
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