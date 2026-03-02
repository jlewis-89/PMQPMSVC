# Phase 1 Sprint Backlog

- User Story 1: As a user, I can create a project with basic metadata and invite members.
- Acceptance Criteria: Project created; respond with ID; list projects shows new one.
- User Story 2: As a user, I can create tasks and subtasks under a project; dates, estimates, priorities stored.
- Acceptance Criteria: Task and SubTask created; hierarchical relation preserved; list endpoints return data.
- User Story 3: Gantt view MVP: Tasks appear as bars with start/end dates; can drag to adjust dates (UI scaffolding).
- Acceptance Criteria: Bar positions reflect task dates; drag events update internal state.
- User Story 4: Mind map MVP: Node entries link to tasks; clicking node opens task details (UI scaffolding).
- Acceptance Criteria: Node <-> Task linkage works.
- User Story 5: PMQ templates: provide starter templates for Stakeholders, Budgeting, Scheduling; allow customization and per-user storage.
- Acceptance Criteria: Templates stored per user; UI to edit placeholders.
- User Story 6: AI assistant: rule-based assistant can propose next actions and create tasks via natural-language-like prompts.
- Acceptance Criteria: AI parses simple commands and outputs an action payload.
- User Story 7: Sync Adapter: Google Drive adapter pluggable; connect, push, pull flows documented; encryption basics in place.
- Acceptance Criteria: Adapter interface works; connect workflow documented; push/pull run.
- User Story 8: Offline-First: app works offline; changes merge on sync; conflict resolution prompts when needed.
- Acceptance Criteria: Merge logic runs; user is prompted on conflicts.
- User Story 9: Handover docs: Markdown handover generated; export to MD/PDF.
- Acceptance Criteria: Handovers generate; MD export works; PDF export path documented.
- User Story 10: Security & GDPR: data export/erasure and per-project RBAC.
- Acceptance Criteria: Per-project access control in place; can export data.
- User Story 11: Electron packaging: scaffolding present; offline parity.
- Acceptance Criteria: Electron app launches UI; offline data works.

This backlog will be refined with more detailed acceptance criteria and task estimates as we begin sprint planning.
