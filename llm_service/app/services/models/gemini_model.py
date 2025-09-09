import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

import services.prompts.gemini_model as gemini_prompts

SYSTEM_INSTRUCTIONS_COMPLETE_FILES  = gemini_prompts.SYSTEM_INSTRUCTIONS_COMPLETE_FILES
SYSTEM_INSTRUCTIONS_CHUNKS = gemini_prompts.SYSTEM_INSTRUCTIONS_CHUNKS
PROMPT_PREFIX_COMPLETE_FILES = gemini_prompts.PROMPT_PREFIX_COMPLETE_FILES
PROMPT_PREFIX_CHUNKS = gemini_prompts.PROMPT_PREFIX_CHUNKS

load_dotenv()
try:
    api_key = os.getenv("GEMINI_API_KEY")
except KeyError:
    print("Error: GEMINI_API_KEY environment variable not set.")

genai.configure(api_key=api_key)

# Model configured for the "complete files" workflow
model_complete_files = genai.GenerativeModel(
    model_name='gemini-1.5-pro-latest',
    system_instruction=SYSTEM_INSTRUCTIONS_COMPLETE_FILES
)

# Model configured for the "chunks" workflow
model_chunks = genai.GenerativeModel(
    model_name='gemini-1.5-pro-latest',
    system_instruction=SYSTEM_INSTRUCTIONS_CHUNKS
)

def build_final_prompt(prompt_prefix: str, current_task_string: str) -> str:
    """
    Takes the appropriate prompt prefix and the current task string,
    and wraps it with the final prompt structure.
    """
    final_prompt = f"""\
{prompt_prefix}

##### BEGIN CURRENT TASK #####

{current_task_string}
"""
    return final_prompt

def generate_response(
    prompt_with_docs: str,
    temperature: float = 0.7,
    chunking: bool = False
) -> dict:
    
    # Setting the parameters for the model
    generation_config = genai.types.GenerationConfig(
        temperature=temperature,
        response_mime_type="application/json"
    )

    if not chunking:
        active_model = model_complete_files
        prompt_prefix = PROMPT_PREFIX_COMPLETE_FILES
    else:
        active_model = model_chunks
        prompt_prefix = PROMPT_PREFIX_CHUNKS
    
    final_prompt = build_final_prompt(prompt_prefix, prompt_with_docs)

    # Sending the prompt to the model
    try:
        response = active_model.generate_content(
            contents=final_prompt,
            generation_config=generation_config
        )
        return json.loads(response.text)
    
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from model response. Error: {e}")
        print(f"Model's raw response was:\n---\n{response.text}\n---")
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