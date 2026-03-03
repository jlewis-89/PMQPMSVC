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

@app.get("/api/projects")
def list_projects():
    return list(projects_store.values())

@app.put("/api/projects/{project_id}")
def update_project(project_id: str, payload: dict):
    if project_id not in projects_store:
        raise HTTPException(status_code=404, detail="Project not found")
    proj = projects_store[project_id]
    proj.update(payload or {})
    return proj

@app.delete("/api/projects/{project_id}")
def delete_project(project_id: str):
    if project_id in projects_store:
        del projects_store[project_id]
        return {"status": "deleted"}
    raise HTTPException(status_code=404, detail="Project not found")


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

@app.post("/api/projects/{project_id}/costs")
def create_cost(project_id: str, payload: CostCreate):
    import uuid
    c = payload.dict()
    c["id"] = str(uuid.uuid4())
    c["project_id"] = project_id
    costs_store[c["id"]] = c
    return c


@app.get("/api/projects/{project_id}/costs")
def list_costs(project_id: str):
    return [c for c in costs_store.values() if c.get("project_id") == project_id]


@app.post("/api/projects/{project_id}/earned-value")
def create_earned_value(project_id: str, payload: EarnedValueCreate):
    import uuid
    ev = payload.dict()
    ev["id"] = str(uuid.uuid4())
    ev["project_id"] = project_id
    earned_store[ev["id"]] = ev
    return ev


@app.get("/api/projects/{project_id}/earned-value")
def list_earned_value(project_id: str):
    return [e for e in earned_store.values() if e.get("project_id") == project_id]


@app.post("/api/projects/{project_id}/mindmaps")
def create_mindmap(project_id: str, payload: MindMapNodeCreate):
    import uuid
    node = payload.dict()
    node["id"] = str(uuid.uuid4())
    node["project_id"] = project_id
    mindmaps_store[node["id"]] = node
    return node


@app.get("/api/projects/{project_id}/mindmaps")
def list_mindmaps(project_id: str):
    return [m for m in mindmaps_store.values() if m.get("project_id") == project_id]


@app.post("/api/projects/{project_id}/calendar")
def create_calendar_event(project_id: str, payload: CalendarEventCreate):
    import uuid
    ev = payload.dict()
    ev["id"] = str(uuid.uuid4())
    ev["project_id"] = project_id
    calendar_store[ev["id"]] = ev
    return ev


@app.get("/api/projects/{project_id}/calendar")
def list_calendar_events(project_id: str):
    return [c for c in calendar_store.values() if c.get("project_id") == project_id]

@app.get("/api/projects/{project_id}/calendar/ics")
def calendar_ics(project_id: str):
    # Minimal ICS export placeholder for a per-project calendar
    ics = (
        "BEGIN:VCALENDAR\r\n"
        "VERSION:2.0\r\n"
        "PRODID:-//PMQPMSVC//Calendar//EN\r\n"
        "BEGIN:VEVENT\r\n"
        "DTSTART:20260316T090000Z\r\n"
        "DTEND:20260316T100000Z\r\n"
        "SUMMARY:Kickoff\r\n"
        "LOCATION:Online\r\n"
        "DESCRIPTION:Project kickoff\r\n"
        "END:VEVENT\r\n"
        "END:VCALENDAR\r\n"
    )
    from fastapi.responses import Response
    return Response(ics, media_type="text/calendar")
