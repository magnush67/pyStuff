import pytest
from flask import Flask
from src.app import app  # Adjust this import based on your actual file structure

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_greet_with_valid_name(client):
    response = client.get("/api/greet/Alice")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Alice!"}

def test_greet_with_empty_name(client):
    response = client.get("/api/greet/")
    assert response.status_code == 404  # Flask will return 404 for missing path param

def test_greet_with_special_characters(client):
    response = client.get("/api/greet/John%20Doe")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, John Doe!"}

def test_greet_with_numeric_name(client):
    response = client.get("/api/greet/12345")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, 12345!"}

def test_greet_with_unicode_name(client):
    response = client.get("/api/greet/Éowyn")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Éowyn!"}

def test_greet_with_special_chars(client):
    response = client.get("/api/greet/!£$%^&*()_+{]{}")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, !£$%^&*()_+{]{}!"}