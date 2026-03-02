# Phase 1 MVP Sprint 1 Backlog (Expanded)

Sprint Goal
- Validate core MVP flows across backend, frontend, and sync adaptor; establish per-user PMQ templates and AI starter; ensure CI scaffold is in place.

Epic mapping
- MVP Core API (Backend): tasks, subtasks, costs, earned value, mind maps, calendar (in-memory)
- UI Skeleton: WBS, Gantt, Mind Map, Calendar, PMQ templates
- Sync: Google Drive scaffold and extension path for other providers
- PMQ: per-user starter templates (Stakeholders, Budgeting, Scheduling)
- AI Starter: rule-based prompt support
- Handover: Markdown handover export scaffold
- CI: linting and test scaffolding

User Stories (expanded with acceptance criteria)
- US-01 Authenticate and create local profile (Google/GitHub)
  - Acceptance: OAuth flow completes; profile is stored; user appears in per-project member list
- US-02 Create project with at least one member and RBAC
  - Acceptance: project created; member added with role; per-project RBAC enforced
- US-03 Create task and subtask; set dates and estimates
  - Acceptance: hierarchical WBS created; dates/estimates persisted
- US-04 Backend MVP endpoints: /tasks, /subtasks, /costs, /earned-value, /mindmaps, /calendar
  - Acceptance: endpoints respond with payloads, in-memory persistence within session
- US-05 Frontend skeleton: routes for WBS, Gantt, Mind Map, Calendar, PMQ
  - Acceptance: routes render; basic navigation works; components mount
- US-06 Google Drive sync scaffold: connect and basic push/pull interfaces (mocked)
  - Acceptance: adapter scaffold compiles; extension notes present
- US-07 PMQ starter templates: Stakeholders, Budgeting, Scheduling; per-user storage
  - Acceptance: templates exist and can be edited; saved per user
- US-08 AI Starter: rule-based prompts for task creation and path suggestions
  - Acceptance: natural-language-like prompts yield actionable actions
- US-09 Handover: Markdown handover export
  - Acceptance: markdown export available; sample handover renders
- US-10 CI/Testing: scaffolding for lint/tests
  - Acceptance: CI config present; tests scaffolds invoked

Deliverables by end of Sprint 1
- phase-1-mvp/SPRINT1_BACKLOG_DETAILED.md fleshed out with acceptance criteria and owners
- phase-1-mvp/backlog.json updated as needed
- phase-1-mvp/SPRINT1_PLAN.md and phase-1-mvp/SPRINT1_TASKS.md aligned with the expanded backlog
- CI scaffolding in .github/workflows/ci.yml energized with tests scaffolding

Exit Criteria
- All Sprint 1 US implemented or clearly moved to Sprint 2; acceptance criteria documented
- A PR-ready state for MVP features
