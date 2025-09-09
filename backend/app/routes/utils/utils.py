from pathlib import Path

def build_prompt_from_files(user_prompt: str, documents: dict[str, str]) -> str:
    
    prompt = ""
    index = 1
    for path, content in documents.items():
        
        # Obtain the name of the file
        prompt += f"""\
Document: {index}
Document Name: {path}
Document Content:
{content}
-------------
"""

        index += 1
    
    # Add the user question
    prompt += f"""\
Query: {user_prompt}
Answer:\
"""
    
    return prompt

def build_prompt_from_chunks(user_prompt: str, documents: dict[str, dict], files_chunks: dict) -> str:
    
    prompt = ""
    doc_index = 1
    print(documents, flush=True)
    for path, chunks in documents.items():

        file_summary = files_chunks[path].summary

        prompt += f"""\
Document: {doc_index}
Document Name: {path}
Document Summary: {file_summary}
Document Chunks:
"""

        chunk_index = 1
        for chunk in chunks:
            
            prompt += f"""\
Chunk: {chunk_index}
Chunk Content:
{chunk}
"""
            
            chunk_index += 1
        
        prompt += """\
-------------
"""

        doc_index += 1
    
    # Add the user question
    prompt += f"""\
Query: {user_prompt}
Answer:
"""
    
    return prompt