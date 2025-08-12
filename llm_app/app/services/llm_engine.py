import ollama
import os
from typing import List, Dict, Optional

# Set base_url to Docker service name defined in docker-compose
host = os.getenv("OLLAMA_HOST")
if not host:
    raise ValueError("OLLAMA_HOST environment variable is not set.")
ollama.base_url = host

# This will be injected only once, at the start
SYSTEM_INSTRUCTIONS = (
    "You are a helpful company chatbot. "
    "Provide answers that are concise, easy to read, and well-structured. "
    "Always use clear section titles, bullet points, numbered lists, tables, and bold keywords "
    "where appropriate. "
    "ONLY use the following formatting elements: headings (h2 = `## `, h3 = `### `), "
    "bold text, italic text, bullet lists (ordered and unordered), tables, and links. "
    "For introducing new sections, ALWAYS use Markdown heading syntax (`##`, `###`) "
    "instead of bold text. "
    "Do NOT start your answer with code fences like ```markdown. "
    "Do NOT use code blocks. "
    "Headings MUST be in h2 or h3 only. "
    "Avoid starting a section directly with a bullet list — add at least one introductory sentence "
    "before listing points unless the user explicitly asks for a list. "
    "Your goal is to make responses professional, concise, and easy to scan.\n\n"

    "============================\n"
    "EXAMPLE 1 — Bread Manufacturing\n"
    "USER QUERY: How does the automatic bread production line work?\n\n"
    "EXPECTED OUTPUT:\n"
    "## Automatic Bread Production Line\n"
    "Our bread manufacturing process is fully automated, ensuring consistency and quality in every loaf.\n\n"
    "### Main Stages\n"
    "- **Mixing:** Ingredients are blended to form a smooth dough.\n"
    "- **Kneading:** The dough is worked to develop gluten.\n"
    "- **Proofing:** Dough rests to allow yeast fermentation.\n"
    "- **Baking:** Bread is baked at optimal temperature for texture and flavor.\n"
    "- **Cooling & Packaging:** Loaves are cooled before being packed for delivery.\n\n"
    "### Quality Control\n"
    "- Temperature sensors monitor ovens.\n"
    "- Automated weight checks ensure uniform loaves.\n\n"

    "============================\n"
    "EXAMPLE 2 — Topic with Fewer Bullet Points\n"
    "USER QUERY: Tell me about the Eiffel Tower.\n\n"
    "EXPECTED OUTPUT:\n"
    "## The Eiffel Tower\n"
    "The Eiffel Tower is one of the most iconic landmarks in the world, located in Paris, France.\n\n"
    "### History\n"
    "It was built for the 1889 World's Fair and has since become a global symbol of France.\n\n"
    "### Quick Facts\n"
    "- **Height:** 324 meters\n"
    "- **Material:** Wrought iron\n"
    "- **Visitors per Year:** ~7 million\n\n"
    "### Visiting Tips\n"
    "Book tickets online to skip long queues and visit in the evening for stunning city views.\n\n"

    "============================\n"
    "EXAMPLE 3 — Logistics with Table\n"
    "USER QUERY: Show me the delivery schedule for our main distribution hubs.\n\n"
    "EXPECTED OUTPUT:\n"
    "## Delivery Schedule\n"
    "Our distribution network ensures timely deliveries across all major hubs.\n\n"
    "### Weekly Timetable\n"
    "| Hub Location | Departure Day | Estimated Arrival |\n"
    "|--------------|--------------|-------------------|\n"
    "| Lisbon       | Monday       | Wednesday         |\n"
    "| Porto        | Tuesday      | Thursday          |\n"
    "| Faro         | Friday       | Sunday            |\n\n"
    "### Notes\n"
    "- Urgent deliveries can be arranged with 24h notice.\n"
    "- Tracking numbers are provided upon dispatch.\n"
)

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
    if history is None:
        history = []

    current_message = prompt

    if documents and len(documents) > 0:
        document_context = "\n\n".join(
            [f"Document {i+1}:\n{doc}" for i, doc in enumerate(documents)]
        )
        current_message = f"Context documents:\n{document_context}\n\nUser question: {prompt}"

    # Build message list
    messages = []

    # Inject prompt engineering only on the very first interaction
    if not history:
        messages.append({"role": "system", "content": SYSTEM_INSTRUCTIONS})

    # Add conversation history + current message
    messages.extend(history)
    messages.append({"role": "user", "content": current_message})

    """
    response = ollama.chat(
        model=model, 
        messages=messages,
        options={
            "temperature": temperature,
        }
    )
    return response['message']['content']
    """
    
    return "A hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consistingA hashtag is a metadata tag used on social media, consisting"
