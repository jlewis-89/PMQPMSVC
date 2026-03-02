# Phase 1 MVP Detailed Sprint Backlog

- Sprint 1 (Week 1): Foundation
  - User Story: Create a project with basic metadata and add first member; acceptance: API returns project id; project lists include new item.
  - Tasks: Scaffold pages for PMQ modules; set up OAuth scaffolding; initialize IndexedDB schema book-keeping; implement health endpoint check.
  - Acceptance: Backend stores a minimal project; frontend can display it after API call; OAuth login route exists.

- Sprint 2 (Week 2-3): WBS and Subtasks + Basic Gantt
  - User Story: Create tasks and subtasks; dates and estimates persist; Gantt renders bars; dependencies stub.
  - Acceptance: REST endpoints return correct data; UI shows task bars; drag to edit dates wired to state changes.

- Sprint 3 (Week 4): Mind Map and PMQ templates
  - User Story: Mind map nodes linked to tasks; starter PMQ templates editable and stored per-user profile.
  - Acceptance: Mind map links to tasks; templates saved per-user; templates applied to a new project.

- Sprint 4 (Week 5-6): AI starter + Sync adaptor (Google Drive)
  - User Story: Rule-based AI can suggest next actions and create tasks from textual prompts; Google Drive sync ready.
  - Acceptance: AI returns actionable results; connect/push/pull flows execute; encryption in transit.

- Sprint 5 (Week 7-8): Offline merge, RBAC, and Handover export
  - User Story: Offline edits merge on sync; per-project RBAC enforced; Markdown handover exported as MD and PDF.
  - Acceptance: Two offline edits on separate devices merge; user prompts for conflicts; handover MD/PDF exports succeed.

- Sprint 6 (Week 9): Polish, docs, and packaging
  - Tasks: Finalize docs; add CI scaffolding; produce Electron packaging skeleton; ensure GDPR controls in UI.
  - Acceptance: All critical paths covered; CI runs; Electron builds succeed.

Note: This backlog will be adjusted as we break down features into precise tasks with estimates during sprint planning.
