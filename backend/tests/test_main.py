from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Agreement Repository API"}

def test_login():
    response = client.post(
        "/login",
        json={"username": "testuser", "password": "testpassword"}  # Use `json` instead of `data`
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
