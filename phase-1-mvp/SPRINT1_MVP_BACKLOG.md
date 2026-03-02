# Phase 1 MVP Sprint 1 - MVP Backlog (detailed)

- US-01 Backend: Validate API contracts; endpoints for Task, SubTask, Cost, EarnedValue, MindMap, Calendar implemented with in-memory stores.
  - Acceptance: endpoint definitions exist; responses match TaskRead/SubTaskRead shapes; in-memory stores persist during session.
- US-02 Backend: Add input validation for all Task/SubTask fields; ensure negative values are rejected; date formats validated.
  - Acceptance: invalid payloads return 422; valid payloads accepted.
- US-03 Backend: Implement GET endpoints for listing all tasks, subtasks, costs, EV, mindmaps, and calendar per project.
  - Acceptance: list endpoints return arrays; items filtered by project_id.
- US-04 Frontend: Wire WBS, Gantt, Mind Map, Calendar, and PMQ templates UIs to call MVP backend; render sample data.
  - Acceptance: fetch calls return expected data; UI components render placeholders.
- US-05 Sync: Implement a minimal Google Drive adapter push/pull path (mocked) and a doc section on how to extend to other providers.
  - Acceptance: adapter compiles; described extension consistently.
- US-06 PMQ Templates: Implement starter templates for Stakeholders, Budgeting, Scheduling; allow editing; templates saved per user.
  - Acceptance: templates exist and persist per user; editing saves JSON payload in user profile.
- US-07 AI Starter: Rule-based AI prompts to create tasks and propose path suggestions; integrate with UI to show guidance.
  - Acceptance: AI returns task payloads and path suggestions in UI mini-windows.
- US-08 Handover: Implement Markdown handover export and outline PDF export workflow (doc templates).
  - Acceptance: Markdown handover exports generate; PDF outline available in future iteration.
- US-09 CI/Testing: Setup basic unit tests for backend, frontend smoke tests, and CI checks.
  - Acceptance: test commands in CI run; lint/type checks pass for MVP subset.

Notes
- The MVP backlog should be aligned with the two-week sprint cadence and adjusted as teams gain clarity.

Sprint Execution (Phase 1 MVP)
- Duration: 2 weeks (Sprint 1) with possible extension as needed
- Deliverables by end of Sprint 1:
  - Backend MVP endpoints implemented for tasks, subtasks, costs, earned value, mind maps, and calendar (in-memory)
  - Frontend skeleton wired to MVP backend: WBS, Gantt, MindMap, Calendar, PMQ templates pages
  - Google Drive SyncAdapter scaffold wired through the core SyncAdapter interface
  - Per-user PMQ starter templates (stakeholders, budgeting, scheduling) created and editable
  - AI Starter: rule-based intents wired to create tasks and suggest next steps
  - Handover Markdown export wired; PDF export outline documented
  - CI scaffolding extended; unit test stubs for backend endpoints
- Acceptance criteria per user story (summarized):
  - US-01: Phase 1 MVP branch exists and sprint artifacts are present; backlog is operational
  - US-02: MVP endpoints exist and respond with correct payload shapes; in-memory storage holds data during session
  - US-03: Frontend skeleton renders WBS, Gantt, MindMap, Calendar views and navigates across tabs
  - US-04: Sync adaptor scaffold compiles; Google Drive extension notes present for future provider expansion
  - US-05: PMQ templates exist and are editable; templates saved per user
  - US-06: AI starter handles a few intents and outputs task payloads
  - US-07: Handover Markdown export generates a sample doc
  - US-08: CI/tests skeleton runs basic checks
- Testing plan: Backend unit tests, Frontend smoke tests, Sync adaptor tests, CI validation
