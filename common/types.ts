// Shared TypeScript types for frontend-backend data contracts

export interface User {
  id: string
  name: string
  email: string
  avatar?: string
  oauth_provider: string
  roles: string[]
}

export interface Task {
  id: string
  project_id: string
  parent_task_id?: string | null
  name: string
  description?: string
  start_date?: string
  end_date?: string
  duration_days?: number
  estimate_hours?: number
  priority: 'low'|'medium'|'high'
  status: 'pending'|'in_progress'|'completed'
  assignee_id?: string
}

export interface SubTask {
  id: string
  task_id: string
  name: string
  start_date?: string
  end_date?: string
  duration_days?: number
  estimate_hours?: number
  status: 'pending'|'in_progress'|'completed'
}

export interface Milestone {
  id: string
  project_id: string
  name: string
  date?: string
}

export interface Dependency {
  id: string
  before_task_id: string
  after_task_id: string
  type: 'FS'|'SS'|'FF'|'SF'
}

export interface Cost {
  id: string
  project_id: string
  task_id?: string
  planned_cost: number
  actual_cost: number
  date?: string
}

export interface EarnedValue {
  id: string
  project_id: string
  date: string
  planned_value: number
  earned_value: number
  actual_cost: number
}

export interface MindMapNode {
  id: string
  project_id: string
  parent_id?: string | null
  label: string
  data?: any
}

export interface CalendarEvent {
  id: string
  project_id: string
  title: string
  start: string
  end?: string
  location?: string
  description?: string
}

export interface HandoverDoc {
  id: string
  project_id: string
  title: string
  content_md?: string
  pdf_generated?: boolean
}

export interface Webhook {
  id: string
  project_id: string
  event_type: string
  endpoint_url: string
  auth_method?: string
  last_payload_hash?: string
}
