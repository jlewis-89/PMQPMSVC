API Contract MVP - Python (Pydantic) & TypeScript (Frontend)

Overview
- A single source of truth for MVP API contracts, covering backend models and frontend interfaces.
- Ensures compatibility between Python FastAPI endpoints and React TypeScript data contracts.
- Dates: ISO-8601 strings; IDs: UUID strings; monetary values in floats with two decimals for display.

1) Python (Pydantic) models (MV P MVP)
- TaskCreate
  - project_id: str
  - parent_task_id: Optional[str]
  - name: str
  - description: Optional[str]
  - start_date: Optional[str]
  - end_date: Optional[str]
  - duration_days: Optional[int]
  - estimate_hours: Optional[float]
  - priority: str
  - status: str
  - assignee_id: Optional[str]
- TaskRead
  - id: str
  - project_id: str
  - parent_task_id: Optional[str]
  - name: str
  - description: Optional[str]
  - start_date: Optional[str]
  - end_date: Optional[str]
  - duration_days: Optional[int]
  - estimate_hours: Optional[float]
  - priority: str
  - status: str
  - assignee_id: Optional[str]
- SubTaskCreate
  - task_id: str
  - name: str
  - start_date: Optional[str]
  - end_date: Optional[str]
  - duration_days: Optional[int]
  - estimate_hours: Optional[float]
  - status: str
- SubTaskRead
  - id: str
  - task_id: str
  - name: str
  - start_date: Optional[str]
  - end_date: Optional[str]
  - duration_days: Optional[int]
  - estimate_hours: Optional[float]
  - status: str
- CostCreate
  - project_id: str
  - task_id: Optional[str]
  - planned_cost: float
  - actual_cost: float
  - date: Optional[str]
- EarnedValueCreate
  - project_id: str
  - date: str
  - planned_value: float
  - earned_value: float
  - actual_cost: float
- MindMapNodeCreate
  - project_id: str
  - parent_id: Optional[str]
  - label: str
  - data: Optional[dict]
- MindMapNodeRead
  - id: str
  - project_id: str
  - parent_id: Optional[str]
  - label: str
  - data: Optional[dict]
- CalendarEventCreate
  - project_id: str
  - title: str
  - start: str
  - end: Optional[str]
  - location: Optional[str]
  - description: Optional[str]
- CalendarEventRead
  - id: str
  - project_id: str
  - title: str
  - start: str
  - end: Optional[str]
  - location: Optional[str]
  - description: Optional[str]

2) TypeScript Frontend contracts (Interfaces)
- export interface User { id: string; name: string; email: string; avatar?: string; oauth_provider: string; roles: string[] }
- export interface Task { id: string; project_id: string; parent_task_id?: string | null; name: string; description?: string; start_date?: string; end_date?: string; duration_days?: number; estimate_hours?: number; priority: 'low'|'medium'|'high'; status: 'pending'|'in_progress'|'completed'; assignee_id?: string }
- export interface SubTask { id: string; task_id: string; name: string; start_date?: string; end_date?: string; duration_days?: number; estimate_hours?: number; status: string }
- export interface Cost { id: string; project_id: string; task_id?: string; planned_cost: number; actual_cost: number; date?: string }
- export interface EarnedValue { id: string; project_id: string; date: string; planned_value: number; earned_value: number; actual_cost: number }
- export interface MindMapNode { id: string; project_id: string; parent_id?: string | null; label: string; data?: any }
- export interface CalendarEvent { id: string; project_id: string; title: string; start: string; end?: string; location?: string; description?: string }

Payload examples (JSON)
- TaskCreate: see above MVP structure
- TaskRead: { id, project_id, name, start_date, end_date, etc. }
- SubTaskCreate: { task_id, name, start_date, end_date, duration_days, estimate_hours, status }
- SubTaskRead: { id, task_id, name, start_date, end_date, duration_days, estimate_hours, status }
- MindMapNodeCreate: { project_id, parent_id, label, data }
- CalendarEventCreate: { project_id, title, start, end, location, description }

Notes
- This contract is intended to be updated as the PMQ templates expand and as additional fields are introduced in Phase 2.
