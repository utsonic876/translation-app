def sanitize_text(text):
    
    if not text:
        return ""
    
   
    cleaned = " ".join(text.split())
    
   
    cleaned = cleaned.strip()
    
    return cleaned
