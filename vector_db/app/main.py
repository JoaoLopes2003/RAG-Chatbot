import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("API_KEY")

# Configure the API key
genai.configure(api_key=API_KEY)

# Generate embeddings (not a model instance)
response = genai.embed_content(
    model="models/text-embedding-004",
    content="What is the meaning of life?"
)

# Print the embeddings
print(response['embedding'])
