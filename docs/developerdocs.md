# developerdocs.md

Overview
- Purpose: Provide entry-level developers with a full understanding of the project structure, decisions, and how to contribute.
- Scope: Architecture, data models, API contracts, sync adaptor, PMQ modules, security, tests, and deployment.

Repository structure
- frontend/ : React + TS SPA
- backend/ : FastAPI app
- common/ : shared types and contracts
- sync-adapter/ : pluggable adapters (TS frontend; Python adapters optional)
- apps/ : Electron wiring and wrappers
- docs/ : this documentation
- tests/ : tests and utilities

Getting started
- Prereqs, environment setup, and run commands for frontend and backend
- How to run in offline mode with IndexedDB and the sync adaptor

Code layout details
- Data models: Task, SubTask, Milestone, Dependency, Cost, EarnedValue, MindMapNode, CalendarEvent, HandoverDoc, Webhook
- API contracts: endpoints, payload schemas, authentication
- Sync adaptor: interface, delta schema, provider adapters
- PMQ templates: default templates and customization flow

Contribution guidelines
- Coding standards, linting, testing, PR process, and issue templates

Security and privacy practices
- RBAC, data minimization, encryption, and GDPR considerations
