import os
from dotenv import load_dotenv
import google.generativeai as genai
import services.translation_examples as translation_examples

def create_prompt(query):

    prompt = translation_examples.SYSTEM_INSTRUCTIONS + "Romaian: " + query + "\nEnglish: "

    return prompt

load_dotenv()
try:
    api_key = os.getenv("API_KEY")
except KeyError:
    print("Error: API_KEY environment variable not set.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name='gemini-1.5-pro-latest'
)

def generate_response(
    query: str,
    temperature: float = 1.0,
) -> str:
    
    # Setting the parameters for the model
    generation_config = genai.types.GenerationConfig(
        temperature=temperature
    )

    # Print the user query
    print(f"The user query is: {query}")

    # Append to the prompt template
    prompt = create_prompt(query)

    # Print the complete prompt
    print(f"The user query is: {query}")

    # Sending the prompt to the model
    try:
        response = model.generate_content(
            contents=prompt,
            generation_config=generation_config
        )
    except Exception as e:
        print(e)

    return response.text