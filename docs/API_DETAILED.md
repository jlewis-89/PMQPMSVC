# API Detailed Shapes (MVP)

This document defines concrete JSON shapes for key MVP resources used by the backend API. It is intended as a precise contract for frontend and backend teams and to guide validation logic.

Base formatting notes:
- Dates are ISO 8601 strings: YYYY-MM-DD
- Monetary values are floats in the project currency unit; always use two decimals in UI when displaying
- IDs are UUID strings

1) TaskCreate (POST /api/projects/{project_id}/tasks)
Payload:
```
{
  "parent_task_id": null,
  "name": "Design UI",
  "description": "Create initial UI designs",
  "start_date": "2026-03-02",
  "end_date": "2026-03-10",
  "duration_days": 8,
  "estimate_hours": 40,
  "priority": "high",
  "status": "pending",
  "assignee_id": "user-123"
}
```

Response: TaskRead

2) TaskRead
```
{
  "id": "task-uuid",
  "project_id": "project-uuid",
  "parent_task_id": null,
  "name": "Design UI",
  "description": "Create initial UI designs",
  "start_date": "2026-03-02",
  "end_date": "2026-03-10",
  "duration_days": 8,
  "estimate_hours": 40,
  "priority": "high",
  "status": "pending",
  "assignee_id": "user-123"
}
```

3) SubTaskCreate (POST /api/projects/{project_id}/tasks/{task_id}/subtasks)
Payload:
```
{
  "name": "Create wireframes",
  "start_date": "2026-03-02",
  "end_date": "2026-03-04",
  "duration_days": 2,
  "estimate_hours": 8,
  "status": "pending",
  "task_id": "task-uuid" // server derives task_id from path; included here for clarity
}
```
Response: SubTaskRead

4) SubTaskRead
```
{
  "id": "subtask-uuid",
  "task_id": "task-uuid",
  "name": "Create wireframes",
  "start_date": "2026-03-02",
  "end_date": "2026-03-04",
  "duration_days": 2,
  "estimate_hours": 8,
  "status": "pending"
}
```

5) CostCreate
Payload:
```
{
  "project_id": "project-uuid",
  "task_id": "task-uuid", // optional
  "planned_cost": 1200.00,
  "actual_cost": 0.00,
  "date": "2026-03-02"
}
```

6) EarnedValueCreate
Payload:
```
{
  "project_id": "project-uuid",
  "date": "2026-03-02",
  "planned_value": 1500.00,
  "earned_value": 0.00,
  "actual_cost": 0.00
}
```

7) MindMapNodeCreate
Payload:
```
{
  "project_id": "project-uuid",
  "parent_id": null,
  "label": "Phase 1 Initiation",
  "data": {"notes": "Initial planning"}
}
```

8) CalendarEventCreate
Payload:
```
{
  "project_id": "project-uuid",
  "title": "Kickoff",
  "start": "2026-03-02T09:00:00Z",
  "end": "2026-03-02T10:00:00Z",
  "location": "Online",
  "description": "Project kickoff meeting with stakeholders"
}
```

9) HandoverDoc
Payload:
```
{
  "project_id": "project-uuid",
  "title": "Phase 1 Handover",
  "content_md": "# Handover\nDetails...",
  "pdf_generated": false
}
```

Notes
- This spec is MVP-focused and will evolve with real validation logic.
