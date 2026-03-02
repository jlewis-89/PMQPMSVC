# Phase 1 MVP Sprint 1 - Final Backlog (Completed Baseline)

Sprint Outcome: Sprint 1 completed; baseline MVP scaffolds in place; move into Sprint 2 for fleshing out features, tests, and polish.

MVP Scope covered in Sprint 1:
- Back-end MVP: core endpoints for Task, SubTask, Cost, EarnedValue, MindMap, Calendar; in-memory data stores; basic validation scaffolds.
- Front-end MVP: skeleton UI for WBS, Gantt, MindMap, Calendar, PMQ templates; basic navigation.
- Sync: pluggable SyncAdapter interface with Google Drive starter adapter scaffold; initial docs on extension points.
- PMQ: starter templates for Stakeholders, Budgeting, Scheduling; per-user storage and editing scaffolds.
- AI Starter: rule-based intents for creating tasks and suggesting next actions.
- Handover: Markdown handover export scaffold; PDF path outline in plan docs.
- CI: scaffolding for linting, type checks, and tests; unit test stubs for MVP endpoints.

Tasks and status (high-level):
- US-01 OAuth login and user profile creation: Complete
- US-02 Project creation with at least one member and RBAC: Complete
- US-03 Task and SubTask creation with dates and estimates: Complete
- US-04 MVP endpoints for costs, EV, mindmaps, calendar: Complete (in-memory)
- US-05 UI skeletons wired to endpoints: Complete (skeletons present)
- US-06 SyncAdapter scafolding: Complete (interface + googleDrive scaffold)
- US-07 PMQ templates: Complete (storage per-user scaffold)
- US-08 AI starter: Complete (rule-based intents basics)
- US-09 Handover Markdown: Complete (scaffold exists)
- US-10 CI scaffolding: Complete (pytest scaffolds included)

Carry-Over (Sprint 2):
- Harden validations; implement full CRUD; add ICS export; expand templates; improve AI intents; finalize handover PDFs; strengthen CI
