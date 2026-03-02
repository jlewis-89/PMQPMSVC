# Phase 1 MVP Sprint 2 Backlog (Expanded)

Sprint Goal
- Flesh out MVP surface: complete CRUD for core entities, introduce ICS export groundwork, expand PMQ templates, and extend CI/test coverage.

Epics
- MVP Core API completion: Task/SubTask/Cost/EarnedValue/MindMap/Calendar CRUD with validations
- UI polish: wire WBS/Gantt/MindMap/Calendar/PMQ templates to live endpoints with real data
- Sync: move from scaffold to a working delta push/pull routine with a documented extension path
- PMQ: expand starter templates and per-user editing capabilities
- AI: more intents and safer local execution
- Handover/Docs: finalize Markdown export and begin PDF export scaffolding
- CI/Testing: strengthen tests, ensure CI passes on PRs

Key User Stories (examples; real IDs to be aligned in Sprint 2 planning)
- US-11 Backend: Validate TaskCreate/SubTaskCreate; reject invalid payloads (422)
- US-12 Backend: Implement GET endpoints for all MVP lists per project
- US-13 Frontend: Bind WBS, Gantt, MindMap, Calendar to API data; support editing
- US-14 Sync: Implement functional push/pull; delta application
- US-15 PMQ: Template editor improvements and per-user storage
- US-16 AI: Expand intents; provide safer prompts and results
- US-17 Handover: Markdown export to a finalized structure with template data
- US-18 CI: Full unit/integration test suite for MVP surface

Deliverables for Sprint 2
- Completed MVP surface for CRUD operations and data flows
- ICS export groundwork and calendar integration tapestry
- Expanded templates and per-user storage
- Realistic Sync push/pull with delta application (mock or real depending on provider)
- Expanded AI intents and action surface
- Handover docs exportable in Markdown; initial PDF path skeleton
- CI/test suite enhancements and artifact tests

Assumptions
- Phase 1 MVP scope stays within two-week cadence; no major feature creep
- Google Drive remains core provider with extension path clearly documented
- Local offline-first remains intact; IPC/Service Worker parity blocks not encountered
