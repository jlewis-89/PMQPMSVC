import React, { useState } from 'react'
import WBS from './components/WBS'
import Gantt from './components/Gantt'
import MindMap from './components/MindMap'
import CalendarView from './components/Calendar'
import PMQTemplates from './components/PMQTemplates'

type Tab = 'WBS'|'Gantt'|'MindMap'|'Calendar'|'PMQ'

const App: React.FC = () => {
  const [tab, setTab] = useState<Tab>('WBS')

  return (
    <div style={{ padding: 16 }}>
      <header style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 12 }}>
        <h1 style={{ margin: 0 }}>PMQ Offline-First Planner</h1>
        <nav>
          {(['WBS','Gantt','MindMap','Calendar','PMQ'] as Tab[]).map(t => (
            <button key={t} onClick={() => setTab(t)} style={{ marginRight: 6, padding: '8px 12px' }}>{t}</button>
          ))}
        </nav>
      </header>
      <main>
        {tab === 'WBS' && <WBS/>}
        {tab === 'Gantt' && <Gantt/>}
        {tab === 'MindMap' && <MindMap/>}
        {tab === 'Calendar' && <CalendarView/>}
        {tab === 'PMQ' && <PMQTemplates/>}
      </main>
    </div>
  )
}

export default App
