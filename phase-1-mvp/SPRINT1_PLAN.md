# Phase 1 MVP — Sprint 1 Plan

- Duration: 2 weeks
- Goals: Set up MVP core, wire backend endpoints, scaffold frontend, initialize sync adaptor, and implement PMQ starter templates.
- Sprint 1 User Stories:
  - US1: As a user, I can authenticate via Google or GitHub and create a local profile.
  - US2: As a user, I can create a project and add at least one member with a role.
  - US3: As a user, I can create a task and a subtask under a project; set dates and estimates.
  - US4: Backend exposes endpoints for tasks, subtasks, costs, EV, mindmaps, and calendar; with in-memory storage.
  - US5: Frontend skeleton routes/pages for WBS, Gantt, Mind Map, Calendar, and PMQ modules.
  - US6: Google Drive SyncAdapter scaffold exists; can connect and push/pull changes (no real API calls yet).
  - US7: PMQ starter templates created and stored per-user profile; editable templates.
  - US8: AI starter (rule-based) can generate a new task from a natural-language-like command.

- Deliverables by end of Sprint 1:
  - Backend MVP endpoints wired up with in-memory storage
  - Frontend skeleton with basic navigations
  - Sync adaptor scaffold and Google Drive starter adapter in place
  - PMQ templates stored per user and editable
  - Phase 1 MVP backlog concrete and in phase-1-mvp/backlog.json
  - CI scaffolding and basic tests outline

- Exit criteria: All US in Sprint 1 marked done, basic tests run, and PR ready for review.
