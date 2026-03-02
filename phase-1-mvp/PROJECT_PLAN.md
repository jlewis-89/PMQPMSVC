# Phase 1 MVP: Project Plan

- Objective: Deliver a minimal but functional MVP with offline-first, pluggable sync, and full PMQ template depth.
- Scope: Backend MVP (tasks, subtasks, costs, EV, mindmaps, calendar) + Frontend skeleton + Google Drive sync adaptor scaffold + PMQ templates + AI starter + OAuth flow.
- Milestones:
  1) Branch and repo readiness (done)
  2) MVP API contracts aligned (docs/API_CONTRACT_MVP.md) and in-memory endpoints implemented (backend)
  3) Frontend skeleton screens and data flows wired (to be implemented)
  4) Google Drive sync adaptor scaffold and docs (SyncAdaptor.md) + encryption notes
  5) Phase 1 MVP sprint backlog fleshed out (PHASE1_MVP_SPRINT_BACKLOG.md) and detailed backlog (PHASE1_MVP_SPRINT_BACKLOG_DETAILED.md)
  6) CI scaffolding and basic tests (CI workflow in .github/workflows/ci.yml)
- Roles:
  - Frontend lead
  - Backend lead
  - Sync adaptor lead
  - PMQ templates lead
  - QA and DevOps
- Risks & mitigations:
  - Scope creep: enforce DoD and sprint backlog discipline
  - Data migration: plan for Phase 2 DB design
  - Security: iterate RBAC and encryption as design advances
- KPIs:
  - MVP API coverage: 90% of MVP endpoints implemented
  - Offline merge: successful merges across two devices in a single project
  - PMQ templates: at least 3 starter templates editable by users
- Next actions: lock in sprint backlog, assign owners, and start implementation sprints
