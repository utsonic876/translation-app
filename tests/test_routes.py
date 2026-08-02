# tests/test_routes.py

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from api.routes import app

def test_sanitize_endpoint():
    """This tests the /sanitize endpoint returns cleaned text."""
    client = app.test_client()
    
    response = client.post('/sanitize', 
                          json={'text': '  hello   world  '})
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['original'] == '  hello   world  '
    assert data['cleaned'] == 'hello world'

def test_translate_endpoint():
    """This tests the /translate endpoint returns expected structure."""
    client = app.test_client()
    
    response = client.post('/translate',
                          json={'text': 'hello', 'target_lang': 'fr'})
    
    assert response.status_code == 200
    data = response.get_json()
    assert 'original' in data
    assert 'cleaned' in data
    assert 'translated' in data
    assert 'target_language' in data
    assert data['target_language'] == 'fr'

def test_translate_empty_text():
    """This tests /translate handles empty text gracefully."""
    client = app.test_client()
    
    response = client.post('/translate',
                          json={'text': '', 'target_lang': 'en'})
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['cleaned'] == ''
    assert data['translated'] == ''
