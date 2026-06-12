from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_health():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_questions():
    response = client.get("/api/v1/questions")
    assert response.status_code == 200
    assert response.json()["total"] == 5

def test_invalid_question():
    response = client.post(
        "/api/v1/interview",
        json={"question": "Wrong question"}
    )
    assert response.status_code == 400