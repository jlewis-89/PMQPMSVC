from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"

def test_create_project_and_task_and_list():
    # create a new project
    r = client.post("/api/projects")
    assert r.status_code == 200
    data = r.json()
    project_id = data.get("id")
    assert project_id is not None

    # create a task under the project
    payload = {
        "parent_task_id": None,
        "name": "Sprint 1 Task",
        "description": "MVP task for sprint 1",
        "start_date": "2026-03-16",
        "end_date": "2026-03-18",
        "duration_days": 2,
        "estimate_hours": 8,
        "priority": "high",
        "status": "pending",
        "assignee_id": None
    }
    r = client.post(f"/api/projects/{project_id}/tasks", json=payload)
    assert r.status_code == 200
    task = r.json()
    assert task.get("name") == payload["name"]

    # list tasks for the project
    r = client.get(f"/api/projects/{project_id}/tasks")
    assert r.status_code == 200
    tasks = r.json()
    assert isinstance(tasks, list)
