# Phase 1 MVP Sprint 2 Plan

Objective: Flesh out MVP scope; complete core CRUD, validation, ICS export, higher fidelity UI, and CI improvements.

Cadence: 2 weeks

Sprint 2 Goals
- Backend: finalize Task/SubTask/Cost/EarnedValue CRUD; add validation; implement per-project RBAC stubs; add basic unit tests
- Frontend: connect UI skeleton to API for all MVP modules; refine Gantt and Mind Map interactions; ICS calendar export groundwork
- Sync: advance Google Drive adapter to real push/pull with simple delta handling; document extension steps for other providers
- PMQ Templates: expand templates (Stakeholders, Budgeting, Scheduling) with additional fields and exportability; store per-user
- AI Starter: expand intents to more actions and ensure privacy-first execution
- Handover/Docs: Markdown handover generation, templates, and PDF path planning
- CI/Testing: automations for unit tests, integration tests, and linting
- Packaging: continue PWA offline support; plan for Electron packaging in Sprint 3

Deliverables for Sprint 2
- Completed MVP endpoints and data models, with validation and tests
- Fully wired UI for MVP modules (WBS, Gantt, MindMap, Calendar, PMQ templates)
- Operational Google Drive sync path with doc-based extension approach
- Expanded PMQ templates with per-user storage
- AI intents more robust; local-first execution
- Handover docs export, including Markdown and PDF path
- CI/tests pass and coverage increases

Risks
- Potential delays in integration between UI and API; mitigation: early API mocks and clear test harness
- Sync adaptor complexity; mitigation: keep to a minimal delta approach and document extension
