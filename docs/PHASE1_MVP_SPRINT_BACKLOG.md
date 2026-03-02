# Phase 1 MVP Sprint Backlog (Detailed)

Epics:
- E1: Auth & Users
- E2: Data Model Core (Projects, Tasks, SubTasks, Milestones)
- E3: WBS and Task Management
- E4: Gantt Visualization (Phase 1 MVP)
- E5: Mind Map (Phase 1 MVP)
- E6: PMQ Starter Templates (customizable per user)
- E7: AI Starter (rule-based)
- E8: Sync Adapter (Google Drive first) and encryption
- E9: Offline-first & Merge
- E10: Handover Docs (Markdown export, PDF export path)
- E11: Calendar & ICS export (and inline updates)
- E12: RBAC & GDPR controls
- E13: Electron packaging scaffolding
- E14: CI/Testing scaffolding

For each Epic, provide User Stories with acceptance criteria and test plan below.

E1 Auth & Users
- US1: As a user, I can sign in with Google or GitHub (PKCE) and create a local profile.
  - Acceptance: OAuth flow completes; user profile is stored in local storage/profile store.
  - Test: UI login flow; token storage; profile retrieval.
- US2: Per-project access control (Owner, Editor, Viewer).
  - Acceptance: Users can be assigned roles per project; UI shows role; API enforces RBAC.
  - Test: access denied for non-members; role changes propagate.

E2 Data Model Core
- US3: Create a new project with metadata, add first member.
- US4: Create tasks, subtasks, milestones; set dates; link to a project.
- US5: List tasks by project; show hierarchical structure (WBS).
- Acceptance: CRUD flows work; data persists in local store; API returns expected structures.

E3 WBS & Task Management
- US6: Drag-and-drop tasks to reorder dates (Phase 1 MVP scaffolding).
- US7: Subtasks inherit parent dates by default, with override capability.
- Acceptance: UI actions reflect on data model; API state matches UI.

E4 Gantt Visualization
- US8: Render task bars for top-level tasks in Gantt; show dependencies (FS/SS).
- US9: Edit start/end by dragging; update task dates in store.
- Acceptance: Bars update with drag; conflicts logged for later resolution.

E5 Mind Map
- US10: Create mind map nodes linked to tasks; click node shows linked task.
- Acceptance: Node-to-task linkage works; navigation flows.

E6 PMQ Starter Templates
- US11: Provide industry-standard starter templates (Stakeholders, Budgeting, Scheduling).
- US12: Templates are fully customizable; saved to user profile for reuse.
- Acceptance: UI to edit placeholders; saved templates visible across projects for the user.

E7 AI Starter
- US13: Rule-based AI can interpret simple prompts like "Create task..." and propose suggested actions.
- Acceptance: AI returns payloads that can be applied; no external data leakage.

E8 Sync Adapter
- US14: Google Drive adapter wired; connect, push, pull flows documented.
- US15: End-to-end encryption for cloud blob; provider rotation path documented.
- Acceptance: Adapter hook points function; push/pull triggers update.

E9 Offline & Merge
- US16: Offline edits merge on sync; conflict prompts appear when ambiguous.
- Acceptance: Merge algorithm resolves non-conflicting changes; user guidance shown for conflicts.

E10 Handover Docs
- US17: Auto-generate Markdown handover; export to MD and PDF path documented.
- Acceptance: Handover content renders; export works.

E11 Calendar & ICS
- US18: Calendar events stored per project; export ICS; update inline.
- Acceptance: ICS export generated; inline calendar updates reflect tasks/events.

E12 RBAC & GDPR
- US19: Per-project access controls and data export/erasure.
- Acceptance: Data export includes project data; removal purges per user.

E13 Electron Packaging
- US20: Scaffolding in place for desktop packaging; offline parity.
- Acceptance: Electron app builds and runs connected to local backend.

E14 CI/Testing
- US21: CI scaffolding for lint/tests across frontend/backend.
- Acceptance: PRs trigger lint/test run; failures block merges.

Timeline (high-level): Phase 1 MVP complete in ~6–10 weeks, followed by Phase 2 enhancements.
