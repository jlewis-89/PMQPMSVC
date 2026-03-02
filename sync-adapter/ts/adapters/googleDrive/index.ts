import { SyncAdapter, ChangeSet, ChangeRecord } from '../SyncAdapter'

export class GoogleDriveAdapter implements SyncAdapter {
  async connect(config: any): Promise<void> {
    // Placeholder: initialize Google Drive API client with PKCE tokens
  }

  async disconnect(): Promise<void> {
    // Placeholder: cleanup tokens
  }

  async pushChanges(changes: ChangeSet): Promise<void> {
    // Placeholder: upload encrypted delta blob to Google Drive
  }

  async pullChanges(): Promise<ChangeSet> {
    // Placeholder: fetch remote changes and decrypt
    return { changes: [], schemaVersion: 1 } as ChangeSet
  }

  async resolveConflict(localChange: ChangeRecord, remoteChange: ChangeRecord): Promise<ChangeRecord> {
    // Simple last-write-wins strategy by default
    return localChange.timestamp > remoteChange.timestamp ? localChange : remoteChange
  }

  status(): string {
    return 'idle'
  }

  getLastSync(): string {
    return new Date().toISOString()
  }
}

export default GoogleDriveAdapter
