import pytest
from src.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_greet_endpoint(client):
    response = client.get("/api/greet/Alice")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Alice!"}
