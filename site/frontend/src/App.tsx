import { BrowserRouter, Link, NavLink, Route, Routes } from 'react-router-dom'
import {
  AlogPage, ContradictionsPage, CrosswalkPage, FactsPage, Home, LineagePage,
  NodePage, OntologyPage, SearchPage, SourcesPage,
} from './pages'
import './App.css'

export default function App() {
  return (
    <BrowserRouter>
      <header className="top">
        <Link className="brand" to="/">🛡️ AML KB</Link>
        <nav>
          <NavLink to="/search">탐색</NavLink>
          <NavLink to="/obl/OBL:x-travel-rule-originator">크로스워크</NavLink>
          <NavLink to="/facts">사실</NavLink>
          <NavLink to="/sources">출처</NavLink>
          <NavLink to="/contradictions">상충</NavLink>
          <NavLink to="/ontology">온톨로지</NavLink>
          <NavLink to="/alog">이력</NavLink>
        </nav>
      </header>

      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/search" element={<SearchPage />} />
          <Route path="/n/:id" element={<NodePage />} />
          <Route path="/obl/:id" element={<CrosswalkPage />} />
          <Route path="/lineage/:id" element={<LineagePage />} />
          <Route path="/facts" element={<FactsPage />} />
          <Route path="/sources" element={<SourcesPage />} />
          <Route path="/contradictions" element={<ContradictionsPage />} />
          <Route path="/ontology" element={<OntologyPage />} />
          <Route path="/alog" element={<AlogPage />} />
          <Route path="*" element={<p className="muted">페이지를 찾을 수 없습니다.</p>} />
        </Routes>
      </main>

      <footer>
        문서 CC BY 4.0 · 코드 MIT · <a href="https://github.com/lala-david/aml-notes">저장소</a>
      </footer>
    </BrowserRouter>
  )
}
