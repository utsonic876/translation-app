"""
Translation engine core module.
This handles API calls to translation services (Google Translate) and response processing.
"""

from googletrans import Translator

# This will initialize the translator once so we don't create a new instance every call
translator = Translator()

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
        result = translator.translate(text, dest=target_language)
        return result.text
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
        result = translator.detect(text)
        return result.lang
    except Exception as e:
        # TODO: I'll need to handle this better too
        return "en"
