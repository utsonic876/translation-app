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
    # Placeholder returns original text; I'll it update once real API is integrated
    assert data['translated'] == 'hello'

def test_translate_empty_text():
    """This tests /translate returns 400 when empty text is provided."""
    client = app.test_client()
    
    response = client.post('/translate',
                          json={'text': '', 'target_lang': 'en'})
    
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_translate_no_json():
    """This tests /translate returns 400 when empty JSON is provided."""
    client = app.test_client()
    
    response = client.post('/translate', json={})
    
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_translate_missing_text():
    """This tests /translate returns 400 when text field is missing."""
    client = app.test_client()
    
    response = client.post('/translate',
                          json={'target_lang': 'fr'})
    
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_health_check():
    """This tests the /health endpoint returns ok."""
    client = app.test_client()
    
    response = client.get('/health')
    
    assert response.status_code == 200
    data = response.get_json()
    assert 'status' in data
    assert data['status'] == 'ok'
