"""
Translation engine core module.
This handles API calls to translation services and response processing.
"""

import requests
import os

# Load API key from environment variable
API_KEY = os.getenv('3b1e8b3a-382d-4bfe-aea2-13c2234b4854:fx', '')

def translate_text(text, target_language="en"):
    """
    Translate sanitized text to target language.
    
    My family speaks Ewe, French, and English. 
    I want this to eventually auto-detect which one 
    my mom is typing in so she doesn't have to select it.
    """
    if not text:
        return ""
    
    # TODO: I need to handle missing API key better — maybe warn the user
    if not API_KEY:
        # Fallback: return original text if no API key
        return text
    
    try:
        url = "https://api-free.deepl.com/v2/translate"
        headers = {
            'Authorization': f'DeepL-Auth-Key {API_KEY}'
        }
        data = {
            'text': text,
            'target_lang': target_language.upper()
        }
        response = requests.post(url, headers=headers, data=data, timeout=10)
        result = response.json()
        
        if 'translations' in result and len(result['translations']) > 0:
            return result['translations'][0]['text']
        else:
            return text
            
    except Exception as e:
        # TODO: I need to handle this better; I could probably log it somewhere
        return text

def detect_language(text):
    """
    Detect the language of input text.

    """
    if not text:
        return "en"
    
    # TODO: DeepL doesn't have a free detect endpoint
    # I'll need to use a different service or implement basic detection
    # For now, return auto and let DeepL handle it
    return "auto"
