import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

import services.prompts.gemini_model as gemini_prompts

SYSTEM_INSTRUCTIONS = gemini_prompts.SYSTEM_INSTRUCTIONS
PROMPT_PREFIX = gemini_prompts.PROMPT_PREFIX

load_dotenv()
try:
    api_key = os.getenv("GEMINI_API_KEY")
except KeyError:
    print("Error: GEMINI_API_KEY environment variable not set.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    model_name='gemini-1.5-pro-latest',
    system_instruction=SYSTEM_INSTRUCTIONS
)

def build_final_prompt(current_task_string: str) -> str:
    """
    Takes the pre-formatted string of documents and the current query,
    and wraps it with the prompt structure.
    """
    final_prompt = f"""\
{PROMPT_PREFIX}

##### BEGIN CURRENT TASK #####

{current_task_string}
"""
    return final_prompt

def generate_response(
    prompt_with_docs: str,
    temperature: float = 0.7,
) -> dict:
    
    # Setting the parameters for the model
    generation_config = genai.types.GenerationConfig(
        temperature=temperature,
        response_mime_type="application/json"
    )

    final_prompt  = build_final_prompt(prompt_with_docs)

    # Sending the prompt to the model
    try:
        response = model.generate_content(
            contents=final_prompt,
            generation_config=generation_config
        )
        return json.loads(response.text)
    
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from model response. Error: {e}")
        print(f"Model's raw response was:\n---\n{response.text}\n---")
        # Return a structured error that your application can handle
        return {
            "answer": "I'm sorry, I encountered a technical issue while formatting my response. Please try your query again.",
            "sources": []
        }
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {
            "answer": "I'm sorry, an unexpected error occurred. Please try again later.",
            "sources": []
        }