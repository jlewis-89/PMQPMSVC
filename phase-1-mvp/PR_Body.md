Phase 1 MVP: Scaffold and backlog baseline

Summary of changes in this PR
- Consolidated API contract MVP (docs/API_CONTRACT_MVP_COMBINED.md)
- Expanded Phase 1 MVP backlog and planning artifacts (SPRINT1_BACKLOG_DETAILED.md, backlog.json, SPRINT1_PLAN.md, SPRINT1_TASKS.md, PROJECT_PLAN.md)
- UI scaffolds for MVP: WBS, Gantt, MindMap, Calendar, PMQTemplates (frontend)
- MVP backend scaffolds: in-memory endpoints for Task, SubTask, Cost, EarnedValue, MindMap, Calendar
- Sync adaptor scaffold: core SyncAdapter interface and Google Drive starter adapter
- Living development log: development_log.md
- Phase 1 MVP planning artifacts added (SPRINT1_MVP_BACKLOG.md placeholder, SPRINT1_BACKLOG_DETAILED.md expanded)
- Documentation: expanded SyncAdaptor.md; detailed MVP API docs in API_DETAILED.md

Rationale
- Establish a solid baseline for Phase 1 MVP, enabling two-week sprints and measurable DoD. All critical scaffolds are in place to start implementing MVP features without blocking dependencies.

How to test locally (high level)
- Ensure you have Node.js and Python installed
- Start backend: uvicorn backend.main:app --reload
- Start frontend: cd frontend; npm install; npm run start
- Open app at http://localhost:5173
- Interact with WBS, Gantt, MindMap, Calendar skeletons; verify basic data flow through the MVP endpoints

Files touched (high level)
- docs/API_CONTRACT_MVP_COMBINED.md
- phase-1-mvp/SPRINT1_BACKLOG_DETAILED.md
- phase-1-mvp/backlog.json
- phase-1-mvp/SPRINT1_PLAN.md
- phase-1-mvp/SPRINT1_TASKS.md
- phase-1-mvp/PROJECT_PLAN.md
- phase-1-mvp/SPRINT1_MVP_BACKLOG.md
- phase-1-mvp/SPRINT1_BACKLOG_DETAILED.md
- development_log.md
- docs/SyncAdaptor.md
- backend/app/schemas.py
- backend/main.py
- frontend/* skeleton components

Next steps
- Finalize Sprint 1 backlog with explicit owners and acceptance criteria (patch updates in phase-1-mvp/SPRINT1_BACKLOG_DETAILED.md)
- Kick off Sprint 1 execution on phase-1-mvp branch; push updates frequently
- If desired, add PR body notes for reviewers and stakeholders
