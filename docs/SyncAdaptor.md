# SyncAdaptor.md

Sync Adapter: Expanded Guide

Overview
- The SyncAdapter provides a single, pluggable interface to sync offline-first project data with cloud storage providers.
- Google Drive is the initial provider; the design is provider-agnostic and pluggable.

Architecture
- Core interface: connect, disconnect, pushChanges, pullChanges, resolveConflict, status, getLastSync
- Data delta model: ChangeRecord and ChangeSet with per-record versioning and last_modified timestamps
- Security: client-side encryption for blob storage; token storage and refresh handling; per-provider isolation
- Adapters: one module per provider; all adapters implement the SyncAdapter interface

Adding a new provider adapter
- Create a new adapter under sync-adapter/ts/adapters/newProvider
- Implement the SyncAdapter interface methods; reuse the change delta model
- Update export barrel (sync-adapter/ts/index.ts) to expose the new adapter
- Add high-level docs in SyncAdaptor.md for a quick start

User flow (end-to-end)
1) User selects the provider in app Settings and authorizes access (OAuth where needed)
2) App initializes the adapter and creates the initial sync blob (encrypted)
3) Local changes are queued; when online, pushChanges uploads the delta blob and pullChanges fetches remote changes
4) In case of conflicts, the user is shown a conflict resolver; user can choose local, remote, or merge
5) User can export/import the encrypted blob for portability; data residency options are documented

Security and encryption
- The app uses WebCrypto for encryption at rest in the cloud blob
- Tokens stored securely in the app; PKCE ensures limited exposure
- All transport is TLS-protected

Troubleshooting and QA
- Common errors and recommended fixes
- How to verify a working adapter against a sample project

Appendix: data formats
- ChangeRecord: { id, project_id, record_type, action, payload, timestamp, version }
- ChangeSet: { changes: ChangeRecord[], schemaVersion }
