from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from .app.api import api as api_router
from .app.schemas import TaskCreate, TaskRead, SubTaskCreate, SubTaskRead, CostCreate, EarnedValueCreate, MindMapNodeCreate, MindMapNodeRead, CalendarEventCreate, CalendarEventRead

app = FastAPI(title="PMQ Backend Skeleton")
app.include_router(api_router, prefix="/api")

# In-memory stores (simple MVP database)
projects_store: dict = {}
tasks_store: dict = {}
subtasks_store: dict = {}
costs_store: dict = {}
earned_store: dict = {}
mindmaps_store: dict = {}
calendar_store: dict = {}


def to_task_read(data: dict) -> TaskRead:
    return TaskRead(**data)

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/projects")
def create_project():
    import uuid
    p = {"id": str(uuid.uuid4()), "name": "New Project"}
    projects_store[p["id"]] = p
    return p



@app.get("/version")
def version():
    return {"version": "0.1.0"}


@app.post("/api/projects/{project_id}/tasks")
def create_task(project_id: str, payload: TaskCreate):
    import uuid
    t = payload.dict()
    t["id"] = str(uuid.uuid4())
    t["project_id"] = project_id
    tasks_store[t["id"]] = t
    return t


@app.get("/api/projects/{project_id}/tasks")
def list_tasks(project_id: str):
    return [t for t in tasks_store.values() if t.get("project_id") == project_id]



@app.post("/api/projects/{project_id}/tasks/{task_id}/subtasks")
def create_subtask(project_id: str, task_id: str, payload: SubTaskCreate):
    import uuid
    st = payload.dict()
    st["id"] = str(uuid.uuid4())
    st["task_id"] = task_id
    subtasks_store[st["id"]] = st
    return st


@app.get("/api/projects/{project_id}/tasks/{task_id}/subtasks")
def list_subtasks(project_id: str, task_id: str):
    return [s for s in subtasks_store.values() if s.get("task_id") == task_id]
