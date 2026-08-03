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
    
    # Error handling: check if JSON was provided
    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400
    
    text = data.get('text', '')
    
    # Error handling: validate text exists and is not empty
    if text is None or text == '':
        return jsonify({'error': 'Text field is required'}), 400
    
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
    
    # Error handling: check if JSON was provided
    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400
    
    text = data.get('text', '')
    
    # Error handling: validate text exists and is not empty
    if text is None or text == '':
        return jsonify({'error': 'Text field is required'}), 400
    
    return jsonify({
        'original': text,
        'cleaned': sanitize_text(text)
    })

@app.route('/health', methods=['GET'])
def health_check():
    """
    Simple health check endpoint.
    """
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
