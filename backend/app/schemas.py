from typing import Optional, List
from pydantic import BaseModel


class UserBase(BaseModel):
    id: str
    name: str
    email: str
    oauth_provider: str
    roles: List[str] = []


class TaskCreate(BaseModel):
    project_id: str
    parent_task_id: Optional[str] = None
    name: str
    description: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    duration_days: Optional[int] = None
    estimate_hours: Optional[float] = None
    priority: str = 'medium'
    status: str = 'pending'
    assignee_id: Optional[str] = None


class TaskRead(BaseModel):
    id: str
    project_id: str
    parent_task_id: Optional[str] = None
    name: str
    description: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    duration_days: Optional[int] = None
    estimate_hours: Optional[float] = None
    priority: str
    status: str
    assignee_id: Optional[str] = None


class SubTaskCreate(BaseModel):
    task_id: str
    name: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    duration_days: Optional[int] = None
    estimate_hours: Optional[float] = None
    status: str = 'pending'


class SubTaskRead(BaseModel):
    id: str
    task_id: str
    name: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    duration_days: Optional[int] = None
    estimate_hours: Optional[float] = None
    status: str


class CostCreate(BaseModel):
    project_id: str
    task_id: Optional[str] = None
    planned_cost: float
    actual_cost: float
    date: Optional[str] = None


class EarnedValueCreate(BaseModel):
    project_id: str
    date: str
    planned_value: float
    earned_value: float
    actual_cost: float


class MindMapNodeCreate(BaseModel):
    project_id: str
    parent_id: Optional[str] = None
    label: str
    data: Optional[dict] = None


class MindMapNodeRead(BaseModel):
    id: str
    project_id: str
    parent_id: Optional[str] = None
    label: str
    data: Optional[dict] = None


class CalendarEventCreate(BaseModel):
    project_id: str
    title: str
    start: str
    end: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None


class CalendarEventRead(BaseModel):
    id: str
    project_id: str
    title: str
    start: str
    end: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
