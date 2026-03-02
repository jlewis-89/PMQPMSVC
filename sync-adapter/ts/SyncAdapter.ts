export type ChangeAction = 'create'|'update'|'delete'

export interface ChangeRecord {
  id: string
  project_id: string
  record_type: string
  action: ChangeAction
  payload: any
  timestamp: string
  version: number
}

export interface ChangeSet {
  changes: ChangeRecord[]
  schemaVersion: number
}

export interface SyncAdapter {
  connect(providerConfig: any): Promise<void>
  disconnect(): Promise<void>
  pushChanges(changes: ChangeSet): Promise<void>
  pullChanges(): Promise<ChangeSet>
  resolveConflict(localChange: ChangeRecord, remoteChange: ChangeRecord): Promise<ChangeRecord>
  status(): string
  getLastSync(): string
}
