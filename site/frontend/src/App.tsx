import { BrowserRouter, Link, Navigate, Route, Routes, useLocation } from 'react-router-dom'
import {
  AuditPage, CrosswalkIndex, CrosswalkPage, FactsPage, Home, LineagePage,
  NodePage, NotFound, OntologyPage, SearchPage, SourcesPage,
} from './pages'
import { Mark } from './Brand'
import { BackendNotice, ThemeToggle } from './components'
import './App.css'

/**
 * 상단은 셋뿐이다.
 *
 * 이전에는 여섯이었는데 그중 「사실 · 검토 · 체계」 는 전부 KB 자체의
 * 기계장치를 보는 화면이다 — FACT 목록, 상충·변경 로그, 온톨로지.
 * 읽으러 온 사람의 과업이 아니라 만드는 사람의 과업인데 1급 자리
 * 절반을 차지했다. 아래 FOOT_NAV 로 내렸다. 죽이지는 않는다.
 *
 * 남은 셋은 낱말만 보고 무엇이 나올지 예측할 수 있어야 한다.
 */
const NAV = [
  { to: '/search', label: '찾아보기', match: ['/search', '/n/'] },
  { to: '/crosswalk', label: '관할 비교', match: ['/crosswalk', '/obl/', '/lineage/'] },
  { to: '/sources', label: '출처', match: ['/sources'] },
]

const FOOT_NAV = [
  { to: '/facts', label: '사실' },
  { to: '/audit', label: '검토' },
  { to: '/ontology', label: '분류 체계' },
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
          <nav className="foot-nav" aria-label="자료 화면">
            {FOOT_NAV.map((n) => (
              <Link key={n.to} to={n.to}>{n.label}</Link>
            ))}
          </nav>
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
