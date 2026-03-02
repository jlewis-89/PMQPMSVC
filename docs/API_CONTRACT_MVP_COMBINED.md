# API Contract MVP - Python Pydantic & TypeScript Frontend (Consolidated)

Overview
- A single source of truth for MVP API contracts linking backend models to frontend interfaces.
- Ensures compatibility between Python FastAPI endpoints and React TypeScript data contracts.
- Conventions: Dates are ISO-8601 strings; IDs are UUIDs; monetary values are floats with two decimals for display.

1) Python (Pydantic) MVP models
- TaskCreate: project_id, parent_task_id, name, description, start_date, end_date, duration_days, estimate_hours, priority, status, assignee_id
- TaskRead: id, project_id, parent_task_id, name, description, start_date, end_date, duration_days, estimate_hours, priority, status, assignee_id
- SubTaskCreate: task_id, name, start_date, end_date, duration_days, estimate_hours, status
- SubTaskRead: id, task_id, name, start_date, end_date, duration_days, estimate_hours, status
- CostCreate: project_id, task_id, planned_cost, actual_cost, date
- EarnedValueCreate: project_id, date, planned_value, earned_value, actual_cost
- MindMapNodeCreate: project_id, parent_id, label, data
- MindMapNodeRead: id, project_id, parent_id, label, data
- CalendarEventCreate: project_id, title, start, end, location, description
- CalendarEventRead: id, project_id, title, start, end, location, description

2) TypeScript Frontend contracts (Interfaces)
- User: id, name, email, avatar, oauth_provider, roles
- Task: id, project_id, parent_task_id, name, description, start_date, end_date, duration_days, estimate_hours, priority, status, assignee_id
- SubTask: id, task_id, name, start_date, end_date, duration_days, estimate_hours, status
- Cost: id, project_id, task_id, planned_cost, actual_cost, date
- EarnedValue: id, project_id, date, planned_value, earned_value, actual_cost
- MindMapNode: id, project_id, parent_id, label, data
- CalendarEvent: id, project_id, title, start, end, location, description

3) Payload Examples (JSON)
- TaskCreate: { "project_id": "proj-1", "parent_task_id": null, "name": "Design UI", "description": "Initial UI", "start_date": "2026-03-02", "end_date": "2026-03-10", "duration_days": 8, "estimate_hours": 40, "priority": "high", "status": "pending", "assignee_id": "user-1" }
- TaskRead: { "id": "task-uuid", "project_id": "proj-1", "parent_task_id": null, "name": "Design UI", "description": "Initial UI", "start_date": "2026-03-02", "end_date": "2026-03-10", "duration_days": 8, "estimate_hours": 40, "priority": "high", "status": "pending", "assignee_id": "user-1" }
- SubTaskCreate: { "task_id": "task-uuid", "name": "Wireframe", "start_date": "2026-03-02", "end_date": "2026-03-04", "duration_days": 2, "estimate_hours": 8, "status": "pending" }
- SubTaskRead: { "id": "subtask-uuid", "task_id": "task-uuid", "name": "Wireframe", "start_date": "2026-03-02", "end_date": "2026-03-04", "duration_days": 2, "estimate_hours": 8, "status": "pending" }
- CostCreate: { "project_id": "proj-1", "task_id": "task-uuid", "planned_cost": 1200, "actual_cost": 0, "date": "2026-03-02" }
- EarnedValueCreate: { "project_id": "proj-1", "date": "2026-03-02", "planned_value": 1500, "earned_value": 0, "actual_cost": 0 }
- MindMapNodeCreate: { "project_id": "proj-1", "parent_id": null, "label": "Phase 1", "data": {"notes": "planning"} }
- MindMapNodeRead: { "id": "node-uuid", "project_id": "proj-1", "parent_id": null, "label": "Phase 1", "data": {"notes": "planning"} }
- CalendarEventCreate: { "project_id": "proj-1", "title": "Kickoff", "start": "2026-03-02T09:00:00Z", "end": "2026-03-02T10:00:00Z", "location": "Online", "description": "Project kickoff" }
- CalendarEventRead: { "id": "ev-uuid", "project_id": "proj-1", "title": "Kickoff", "start": "2026-03-02T09:00:00Z", "end": "2026-03-02T10:00:00Z", "location": "Online", "description": "Project kickoff" }

4) Endpoints mapping (MVP)
- POST /api/projects -> create project
- GET /api/projects -> list projects
- POST /api/projects/{project_id}/tasks -> create task
- GET /api/projects/{project_id}/tasks -> list tasks
- POST /api/projects/{project_id}/tasks/{task_id}/subtasks -> create subtask
- GET /api/projects/{project_id}/tasks/{task_id}/subtasks -> list subtasks
- POST /api/projects/{project_id}/costs -> create cost
- GET /api/projects/{project_id}/costs -> list costs
- POST /api/projects/{project_id}/earned-value -> create EV
- GET /api/projects/{project_id}/earned-value -> list EV
- POST /api/projects/{project_id}/mindmaps -> create mind map node
- GET /api/projects/{project_id}/mindmaps -> list mind map nodes
- POST /api/projects/{project_id}/calendar -> create calendar event
- GET /api/projects/{project_id}/calendar -> list calendar events
- GET /health, /version

5) Validation & errors
- 422 Unprocessable Entity for validation errors; 404 for not-found; 400 for bad requests

6) Security & testing notes
- Basic token handling and PKCE approach defined elsewhere in docs; tests should verify payload validation and error behavior
