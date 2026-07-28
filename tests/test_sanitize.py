from src.api.sanitize import sanitize_text

def test_sanitize_removes_extra_spaces():
    assert sanitize_text("hello   world") == "hello world"

def test_sanitize_strips_leading_trailing():
    assert sanitize_text("  hello  ") == "hello"

def test_sanitize_empty_string():
    assert sanitize_text("") == ""
