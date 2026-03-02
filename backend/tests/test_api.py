from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_create_project():
    r = client.post("/api/projects")
    assert r.status_code == 200
    data = r.json()
    assert "id" in data
