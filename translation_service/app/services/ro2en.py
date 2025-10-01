import os
from dotenv import load_dotenv
import google.generativeai as genai
import services.translation_examples as translation_examples

def create_prompt_ro2en(query):

    prompt = translation_examples.SYSTEM_INSTRUCTIONS_RO2EN + "Romaian: " + query + "\nEnglish: "

    return prompt

def create_prompt_en2ro(query):

    prompt = translation_examples.SYSTEM_INSTRUCTIONS_EN2RO + "English: " + query + "\nRomaian: "

    return prompt

load_dotenv()
try:
    api_key = os.getenv("API_KEY")
except KeyError:
    print("Error: API_KEY environment variable not set.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name='gemini-2.5-pro'
)

def generate_response(
    query: str,
    origin_language: str,
    target_language: str,
    temperature: float = 1.0,
) -> str:
    
    # Setting the parameters for the model
    generation_config = genai.types.GenerationConfig(
        temperature=temperature
    )

    # Print the user query
    print(f"The user query is: {query}")

    # Append to the prompt template
    if origin_language == 'ro' and target_language == 'en':
        prompt = create_prompt_ro2en(query)
    elif origin_language == 'en' and target_language == 'ro':
        prompt = create_prompt_en2ro(query)
    else:
        prompt = query

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