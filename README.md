PMQ MVP — Running, Testing, and Deploying

Overview
- This repository contains a planning-to-build project: a modern, offline-first project management tool with a work breakdown structure (WBS), Gantt chart, mind map for critical path, earned value management, and PMQ-aligned templates. It targets a two-sprint MVP (Sprint 1: baseline scaffolds; Sprint 2: MVP surface; Sprint 3: packaging and finish).
- Core stack: frontend (React + TypeScript) + backend (Python FastAPI) + optional Electron desktop wrapper; offline-first with IndexedDB; Webhooks and JSON data export; a pluggable sync adapter (Google Drive as default).
- Documentation links are provided in-line; see links at the end for deeper technical details.

Getting started
- Prereqs: Node.js, Python 3.x, npm, virtualenv (optional but recommended)
- Initialize and run locally:
  1) Backend
     - Create a Python virtual environment (optional): python -m venv venv
     - Activate the environment: venv\Scripts\activate on Windows or source venv/bin/activate on Unix
     - Install dependencies: pip install -r backend/requirements.txt
     - Run the API: uvicorn backend.main:app --reload
     - Backend tests: pytest -q (after installing test requirements)
  2) Frontend
     - cd frontend
     - npm install
     - npm run start
     - Open http://localhost:5173
  3) Optional Electron
     - If you want desktop packaging, follow Sprint 3 Electron packaging guidance
- Quick test sequence (sanity tests):
  - Access health: http://localhost:8000/health
  - Create a project: POST http://localhost:8000/api/projects
  - Create a task: POST http://localhost:8000/api/projects/{project_id}/tasks
  - List tasks: GET http://localhost:8000/api/projects/{project_id}/tasks
  - ICS export: GET /api/projects/{project_id}/calendar/ics
  - JSON export: GET /api/export/json

What to test in Sprint 2 and Sprint 3
- Sprint 2: Validate MVP surface; ensure CRUD operations for core entities; ICS export; per-user PMQ templates; AI intents; patch/test CI
- Sprint 3: Packaging (Electron), finalize polish, security & GDPR, finalize data portability, closeout docs

Project structure and key docs
- Frontend: frontend/ (React code), with components wired to MVP endpoints
- Backend: backend/ (FastAPI), with in-memory MVP endpoints and auth scaffolding
- Common: common/ (shared types)
- Sync Adapters: sync-adapter/ (Google Drive default adapter scaffolding)
- Phase-1 MVP planning: phase-1-mvp/ (SPRINT1_PLAN_FINAL.md, SPRINT2_PLAN_FINAL.md, SPRINT3_PLAN_FINAL.md, etc)
- Documentation: docs/ (API_CONTRACT_MVP_COMBINED.md, API_DETAILED.md, SyncAdaptor.md)
- Tests: backend/tests/ (test_api.py and __init__.py)

Save Point / Snapshot
- To save your current work, run the included savepoint script to archive a snapshot of the repo state.
- Script: scripts/savepoint.sh (or scripts/savepoint.ps1 on Windows)
- Usage (Linux/macOS): ./scripts/savepoint.sh
- Usage (Windows): powershell -ExecutionPolicy Bypass -File scripts/savepoint.ps1
- The script will create a compressed archive in artifacts/pmq-savepoint-YYYYMMDD-HHMM.tar.gz (or zip on Windows if tar is unavailable).

Where to find more information
- API contract (A): docs/API_CONTRACT_MVP_COMBINED.md
- MVP detailed planning: phase-1-mvp/SPRINT1_BACKLOG_DETAILED.md, phase-1-mvp/SPRINT2_BACKLOG_DETAILED.md, phase-1-mvp/SPRINT3_BACKLOG_DETAILED.md
- Sprint plans: phase-1-mvp/SPRINT2_PLAN_FINAL.md, phase-1-mvp/SPRINT3_PLAN_FINAL.md
- Spark docs for SyncAdaptor: docs/SyncAdaptor.md
- Test references: backend/tests/test_api.py
- Handover and data portability: phase-1-mvp/SPRINT3_ELECTRON_PACKAGING.md, phase-1-mvp/TEST_SUMMARY.md, phase-1-mvp/SPRINT1_COMPLETION_SUMMARY.md, phase-1-mvp/SPRINT2_COMPLETION_SUMMARY.md, phase-1-mvp/SPRINT3_COMPLETION_SUMMARY.md

Notes
- This readme is intended as a stable, single source of truth for anyone picking up the project later. When sprint patches land, this file may be augmented with new commands or deployment steps as needed.

Save state and next steps
- A read-only snapshot at any given sprint can be kept by archiving the repository state via the savepoint script. When you resume later, simply clone the repo, restore the savepoint, and start the appropriate sprint scripts.
- For a new session later, start by installing dependencies, running the backend, and then the frontend, and finally hooking up the Electron packaging in Sprint 3.

References
- Docs: docs/API_CONTRACT_MVP_COMBINED.md, docs/SyncAdaptor.md, docs/API_DETAILED.md
- MVP planning: phase-1-mvp/SPRINT1_PLAN.md, phase-1-mvp/SPRINT2_PLAN_FINAL.md, phase-1-mvp/SPRINT3_PLAN_FINAL.md
- Phase 1 artifacts: phase-1-mvp/SPRINT1_MVP_BACKLOG_FINAL.md, phase-1-mvp/SPRINT2_BACKLOG_DETAILED.md, phase-1-mvp/SPRINT3_BACKLOG_DETAILED.md
