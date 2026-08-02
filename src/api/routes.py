from flask import Flask, request, jsonify
from api.sanitize import sanitize_text
from src.backend.translator import translate_text, detect_language

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    """
    This function receives text and target language; it then returns translated text.
    """
    data = request.get_json()
    text = data.get('text', '')
    target_lang = data.get('target_lang', 'en')
    
    # Sanitizes input
    clean_text = sanitize_text(text)
    
    # Detects source language (placeholder for now)
    source_lang = detect_language(clean_text)
    
    # Translates text
    translated = translate_text(clean_text, target_lang)
    
    return jsonify({
        'original': text,
        'cleaned': clean_text,
        'source_language': source_lang,
        'translated': translated,
        'target_language': target_lang
    })

@app.route('/sanitize', methods=['POST'])
def sanitize():
    """
    Standalone endpoint for text sanitization.
    """
    data = request.get_json()
    text = data.get('text', '')
    
    return jsonify({
        'original': text,
        'cleaned': sanitize_text(text)
    })

if __name__ == '__main__':
    app.run(debug=True)
