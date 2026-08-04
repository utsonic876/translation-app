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
        url = "
