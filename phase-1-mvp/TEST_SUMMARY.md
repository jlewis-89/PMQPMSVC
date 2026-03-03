# Sprint 2-3 Test Summary

Overview
- Sprint 2: Flesh MVP surface (CRUD, ICS, templates, AI intents, handover, CI scaffolding)
- Sprint 3: Packaging (Electron), polish, final QA, data portability closeout

Coverage
- Backend: Task, SubTask, Cost, EarnedValue, MindMap, Calendar; export JSON
- Frontend: MVP views wired; per-user templates; navigation
- Sync: Google Drive delta flow scaffolding; extension points documented
- AI Starter: expanded intents, local execution
- Handover/Docs: Markdown handover export; PDF planning
- CI/Testing: unit tests, integration tests, frontend smoke tests planned

Test Plan (how to execute locally)
- Backend
  - Setup: python -m venv venv; activate; pip install -r backend/requirements.txt
  - Run: uvicorn backend.main:app --reload
  - Tests: pytest -q
  - Endpoints to verify: /health, /api/projects, /api/projects/{id}/tasks, /api/export/json, /api/export/json
- Frontend
  - Setup: cd frontend; npm install
  - Run: npm run start
  - Access: http://localhost:5173; verify WBS, Gantt, MindMap, Calendar, PMQ templates
- Sync Adaptor
  - Validate Google Drive path with mocked provider; ensure delta creation and delta application paths exist
- Handover & Docs
  - Generate Markdown handover; attempt PDF export when available
- CI/Tests
  - Run CI checks locally: lint, unit tests, and basic TS checks when wired

Known Issues / Risks
- OAuth gating is scaffolded; if you want to enable end-to-end OAuth, provide credentials and scopes in a follow-up sprint
- Electron packaging is staged for Sprint 3; ensure any platform-specific issues are handled in QA
