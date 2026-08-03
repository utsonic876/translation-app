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
    
    # Need to check if JSON was actually sent
    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400
    
    text = data.get('text', '')
    
    # Can't translate nothing — need text to work with
    if text is None or text == '':
        return jsonify({'error': 'Text field is required'}), 400
    
    target_lang = data.get('target_lang', 'en')
    
    # Clean up the input before translating
    clean_text = sanitize_text(text)
    
    # Figure out what language they sent (placeholder for now)
    source_lang = detect_language(clean_text)
    
    # Do the actual translation
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
    
    # Need to check if JSON was actually sent
    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400
    
    text = data.get('text', '')
    
    # Can't sanitize nothing — need text to work with
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
