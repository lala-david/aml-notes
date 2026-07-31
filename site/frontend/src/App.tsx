import { BrowserRouter, Link, Navigate, Route, Routes, useLocation } from 'react-router-dom'
import {
  AuditPage, CrosswalkIndex, CrosswalkPage, FactsPage, Home, LineagePage,
  NodePage, NotFound, OntologyPage, SearchPage, SourcesPage,
} from './pages'
import { Mark } from './Brand'
import { BackendNotice, ThemeToggle } from './components'
import './App.css'

/**
 * 화면 여섯. 이전에는 일곱 개가 아이콘을 달고 나란히 있었다.
 * 상충과 이력은 성격이 같다 — "무엇이 다투고 무엇이 바뀌었는가" — 그래서
 * 「검토」 하나로 합쳤다. 아이콘은 뗐다. 여섯 개의 낱말이 여섯 개의
 * 그림보다 빨리 읽힌다.
 */
const NAV = [
  { to: '/search', label: '탐색', match: ['/search', '/n/'] },
  { to: '/crosswalk', label: '관할 비교', match: ['/crosswalk', '/obl/', '/lineage/'] },
  { to: '/facts', label: '사실', match: ['/facts'] },
  { to: '/sources', label: '출처', match: ['/sources'] },
  { to: '/audit', label: '검토', match: ['/audit'] },
  { to: '/ontology', label: '체계', match: ['/ontology'] },
]

function TopNav() {
  const { pathname } = useLocation()
  return (
    <nav aria-label="주요 화면">
      {NAV.map((n) => {
        const on = n.match.some((m) => (m.endsWith('/') ? pathname.startsWith(m) : pathname === m))
        return (
          <Link key={n.to} to={n.to} className={on ? 'active' : undefined} aria-current={on ? 'page' : undefined}>
            {n.label}
          </Link>
        )
      })}
    </nav>
  )
}

export default function App() {
  return (
    <BrowserRouter>
      <div className="shell">
        <header className="masthead">
          <Link className="wordmark" to="/">
            <Mark size={20} />
            가상자산 AML
            <em>규제 지식베이스</em>
          </Link>
          <TopNav />
          <div className="mast-tools">
            <ThemeToggle />
          </div>
        </header>

        <BackendNotice />

        <main className="page">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/search" element={<SearchPage />} />
            <Route path="/n/:id" element={<NodePage />} />
            <Route path="/crosswalk" element={<CrosswalkIndex />} />
            <Route path="/obl/:id" element={<CrosswalkPage />} />
            <Route path="/lineage/:id" element={<LineagePage />} />
            <Route path="/facts" element={<FactsPage />} />
            <Route path="/sources" element={<SourcesPage />} />
            <Route path="/audit" element={<AuditPage />} />
            <Route path="/ontology" element={<OntologyPage />} />
            {/* 이전 주소는 살려 둔다 — 공유된 링크가 죽지 않게 */}
            <Route path="/contradictions" element={<Navigate to="/audit?tab=conflict" replace />} />
            <Route path="/alog" element={<Navigate to="/audit?tab=log" replace />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </main>

        <footer className="foot">
          <div>
            <Mark size={16} />
            <span>가상자산 자금세탁방지 규제 지식베이스</span>
            <span>문서 CC BY 4.0 · 코드 MIT</span>
            <a href="https://github.com/lala-david/aml-notes">저장소</a>
          </div>
        </footer>
      </div>
    </BrowserRouter>
  )
}
