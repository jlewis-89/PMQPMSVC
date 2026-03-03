# Sprint 3 Electron Packaging Guide

- Objective: Build and validate a production-like Electron desktop app with offline capability.
- Tools: electron-builder, npm, Node.js, cross-platform installers
- Steps:
 1) Ensure Electron app entry points mirror the web app; share code where possible
 2) Configure electron-builder in apps/electron/package.json for Windows and macOS and Linux targets
 3) Wire the app to the local FastAPI backend when available; support offline IndexedDB usage
 4) Build installers and verify installation flow on Windows, macOS, and Linux
- Validation: launch app, verify UI loads offline, verify API autorun locally if server is bundled, verify data export/import remains functional
