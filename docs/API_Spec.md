# API Spec (MVP)

This document outlines the MVP REST API for the backend. It is designed as a planning guide and should be expanded with full validation, error handling, and pagination in subsequent iterations.

Base URL: http://localhost:8000/api

Authentication: PKCE-based OAuth flow via frontend; for MVP this API is public and uses in-memory stores.

Endpoints
- POST /projects
  - Create a new project
  - Response: { id, name }
- GET /projects
  - List all projects
- POST /projects/{project_id}/tasks
  - Create a new task under a project
  - Body: TaskCreate payload
  - Response: TaskRead
- GET /projects/{project_id}/tasks
  - List tasks for a project
- POST /projects/{project_id}/tasks/{task_id}/subtasks
  - Create a subtask under a task
  - Body: SubTaskCreate payload
  - Response: SubTaskRead
- GET /projects/{project_id}/tasks/{task_id}/subtasks
  - List subtasks for a task
- POST /projects/{project_id}/costs
  - Create a cost entry
  - Body: CostCreate
- GET /projects/{project_id}/costs
  - List costs for a project
- POST /projects/{project_id}/earned-value
  - Create an EV record
  - Body: EarnedValueCreate
- GET /projects/{project_id}/earned-value
  - List EV records
- POST /api/projects/{project_id}/tasks (duplicate path kept for MVP simplicity)
- GET /health
- GET /version

Notes
- This MVP uses in-memory stores; replace with database-backed storage in Phase 1.
