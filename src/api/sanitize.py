def sanitize_text(text):
    """
    This function cleans and normalizes input text before translation.
    """
    if not text:
        return ""
    
    cleaned = " ".join(text.split())
    cleaned = cleaned.strip()
    
    return cleaned
