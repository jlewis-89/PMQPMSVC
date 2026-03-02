Phase 1 MVP Plan

Scope
- Backend MVP: Tasks, SubTasks, Costs, Earned Value, MindMap, Calendar (in-memory)
- Frontend MVP: WBS, Gantt scaffold, Mind Map scaffold, Calendar scaffold, PMQ template scaffolds
- Sync Adapter: Google Drive starter, pluggable pattern for additional providers
- AI: Rule-based starter AI for task creation and path suggestions
- Authentication: OAuth (Google, GitHub) with per-user profiles
- Data: In-memory MVP; database strategy defined for Phase 2
- Handover docs: Markdown handover generation with MD/PDF export

Phases and milestones
- Phase 1: MVP core implementation (weeks 1-4)
- Phase 2: Automation and PMQ depth expansion (weeks 5-8)
- Phase 3: Offline packaging (Electron), polish, and security hardening (weeks 9-12)

Sprint cadence
- 2-week sprints (adjustable)
- Sprint planning with acceptance criteria per US in backlog.json

Definition of Done (DoD)
- All MVP US are implemented and tested; unit tests for backend, smoke tests for frontend
- Sync adaptor functioning for Google Drive (connect, push, pull, conflict resolution)
- PMQ templates editable and stored per user
- Handover doc generation working in Markdown export and PDF export path
- CI checks pass (lint, typecheck, tests)

Risks and mitigations
- Adapter complexity: keep Google Drive starter minimal; design for plug-and-play extension
- Offline merge: define deterministic merge rules and prompt on conflicts
- Data portability: ensure all data can be exported as JSON/MD/PDF
