"""
Translation engine core module.
This handles API calls to translation services and response processing.
"""

import os

# Load API key from environment variable for production use
# Set this in your terminal: $env:TRANSLATION_API_KEY="your-key"
API_KEY = os.getenv('TRANSLATION_API_KEY', '')

def translate_text(text, target_language="en"):
    """
    Translate sanitized text to target language.
    
    TODO: I need to integrate a real translation API (DeepL, Google Cloud, etc.)
    For now this returns the original text as a placeholder.
    """
    if not text:
        return ""
    
    #  Once I get a reliable API key, I'll uncomment this block
    # try:
    #     import requests
    #     url = "https://api-free.deepl.com/v2/translate"
    #     headers = {'Authorization': f'DeepL-Auth-Key {API_KEY}'}
    #     data = {'text': text, 'target_lang': target_language.upper()}
    #     response = requests.post(url, headers=headers, data=data, timeout=10)
    #     result = response.json()
    #     if 'translations' in result:
    #         return result['translations'][0]['text']
    # except Exception:
    #     pass
    
    # Placeholder: return text as-is until API is connected
    return text

def detect_language(text):
    """
    Detect the language of input text.
    
    For now I'll hardcode common languages my family uses: Ewe, French, English
    """
    if not text:
        return "en"
    
    # TODO: I'll implement real detection once I integrate a translation service
    # For now, default to English
    return "en"
