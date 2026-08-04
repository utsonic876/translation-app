"""
Translation engine core module.
This handles API calls to translation services and response processing.
"""

import requests

def translate_text(text, target_language="en"):
    """
    Translate sanitized text to target language.
    
    My family speaks Ewe, French, and English. 
    I want this to eventually auto-detect which one 
    my mom is typing in so she doesn't have to select it.
    """
    if not text:
        return ""
    
    try:
        url = "https://api.mymemory.translated.net/get"
        params = {
            'q': text,
            'langpair': f'auto|{target_language}'
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        # Check if we got a valid translation back
        if 'responseData' in data and 'translatedText' in data['responseData']:
            return data['responseData']['translatedText']
        else:
            # TODO: I need to handle API errors better
            return text  # Fallback to original if something goes wrong
            
    except Exception as e:
        # TODO: I need to handle this better; I could probably log it somewhere
        return f"Translation error: {str(e)}"

def detect_language(text):
    """
    Detect the language of input text.
    
    For now I'll hardcode common languages my family uses: Ewe, French, English
    """
    if not text:
        return "en"
    
    try:
        # MyMemory doesn't have a separate detect endpoint, so I'll use their 
        # translation with auto-detect and return the detected source
        url = "https://api.mymemory.translated.net/get"
        params = {
            'q': text,
            'langpair': 'Autodetect|en'
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        if 'responseData' in data and 'detectedLanguage' in data['responseData']:
            return data['responseData']['detectedLanguage']
        else:
            return "en"
            
    except Exception as e:
        # TODO: I'll need to handle this better too
        return "en"
