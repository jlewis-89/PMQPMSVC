Sync Adapter: Overview
- A pluggable adapter interface for syncing local offline data with a cloud provider.
- Google Drive is the starter provider. Other providers can be plugged in with minimal changes.

Structure
- ts/SyncAdapter.ts: Core interface and types used by frontend adapters
- ts/adapters/: Provider-specific adapters
- ts/index.ts: Barrel exports

Usage (non-technical)
- Open the app, navigate to Sync settings, choose a provider, and grant permissions.
- The app will automatically push local changes when online and pull remote changes when online or on demand.
