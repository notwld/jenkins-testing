from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_read_item():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "query_param": None}

def test_read_item_with_query_param():
    response = client.get("/items/42?query_param=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "query_param": "test"}
