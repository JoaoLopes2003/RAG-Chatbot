def read_markdown_content(file_path: str, max_chars: int = 8000) -> str:
    """
    Read markdown file content and truncate if necessary.
    
    Args:
        file_path: Path to the markdown file
        max_chars: Maximum characters to include
    
    Returns:
        str: Markdown content (truncated if needed)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if len(content) > max_chars:
            content = content[:max_chars] + "\n\n... [content truncated for brevity]"
            
        return content
        
    except Exception as e:
        return f"[Error reading markdown file: {e}]"