/**
 * 기본값은 빈 문자열 — 같은 출처로 `/api` 를 부른다.
 * 개발에서는 Vite 가 프록시로 백엔드에 넘긴다(vite.config.ts).
 * 그래서 브라우저가 백엔드 포트를 알 필요가 없다. 포트를 손으로
 * 맞추다 어긋나면 모든 화면이 한꺼번에 죽는데, 그 연결 자체를 끊었다.
 * 다른 호스트에 배포할 때만 VITE_API_BASE 로 절대주소를 준다.
 */
const BASE = import.meta.env.VITE_API_BASE ?? ''

/** 백엔드에 닿지 못한 상태. HTTP 오류(404·422)와 성격이 다르다 —
 *  고칠 사람도, 고칠 방법도 다르므로 타입을 나눈다. */
export class ApiUnreachable extends Error {
  constructor() {
    super('백엔드에 연결하지 못했습니다')
    this.name = 'ApiUnreachable'
  }
}

export type NodeBrief = {
  id: string
  type: string
  layer: string
  title: string
  label: Record<string, string>
  status?: string
  summary?: string | null
  tags?: string[]
  jurisdiction?: string | null
}

export type Confidence = 'A' | 'B' | 'C' | 'D'

export type EdgeView = {
  predicate: string
  direction: 'in' | 'out'
  node: NodeBrief & { missing?: boolean }
  qualifiers: Record<string, unknown>
  valid_from: string | null
  valid_to: string | null
  confidence: Confidence | null
  evidence: Evidence[]
}

export type Evidence = {
  doc: string
  confidence: Confidence
  locator?: string
  quote?: string
  retrieved?: string
}

export type NodeDetail = Record<string, unknown> & {
  id: string
  type: string
  layer: string
  title: string
  path: string
  summary?: string
  curator_note?: string
  evidence?: Evidence[]
  edges_out: EdgeView[]
  edges_in: EdgeView[]
  facts: Fact[]
  states: Record<string, unknown>[]
}

export type Fact = {
  id: string
  claim: string
  confidence: Confidence
  subject?: string
  attribute?: string
  value?: unknown
  unit?: string
  valid_from?: string | null
  valid_to?: string | null
  note?: string
  evidence: Evidence[]
}

export type CrosswalkRow = {
  provision: NodeBrief
  citation: string
  regulation: NodeBrief | null
  namespace: string
  jurisdiction_label: string
  threshold: number | null
  currency: string | null
  scope_note?: string
  valid_from: string | null
  valid_to: string | null
  confidence: Confidence | null
  evidence: Evidence[]
}

export type Crosswalk = {
  obligation: NodeBrief & { summary?: string }
  as_of: string | null
  rows: CrosswalkRow[]
  missing_jurisdictions: { namespace: string; label: string }[]
}

export type LineageStep = {
  predicate: string
  from: NodeBrief
  to: NodeBrief
  qualifiers: Record<string, unknown>
  confidence: Confidence | null
}

export type Lineage = {
  root: NodeBrief & { summary?: string }
  as_of: string | null
  paths: LineageStep[][]
}

export type Stats = {
  loaded_at: string
  nodes: number
  by_type: Record<string, number>
  by_layer: Record<string, number>
  facts: number
  states: number
  contradictions: number
  unresolved_contradictions: number
  action_log: number
  confidence: Record<Confidence, number>
}

export type Ontology = {
  version: string
  updated: string
  classes: Record<string, { layer: string; label: { ko: string; en: string }; dir?: string }>
  predicates: Record<string, { from?: string[]; to?: string[]; symmetric?: boolean }>
  confidence_levels: Record<string, string>
  source_tiers: Record<string, string>
  lifecycle_states: string[]
}

async function get<T>(path: string): Promise<T> {
  let res: Response
  try {
    res = await fetch(`${BASE}${path}`)
  } catch {
    // fetch 가 throw 하는 경우는 네트워크 단절뿐이다 — 백엔드가 안 떠 있다.
    throw new ApiUnreachable()
  }
  if (!res.ok) {
    const body = await res.json().catch(() => null)
    // 프록시 대상이 죽어 있으면 Vite 가 JSON 이 아닌 5xx 를 돌려준다.
    // 그것도 결국 "백엔드가 없다" 는 뜻이다.
    if (body === null && res.status >= 500) throw new ApiUnreachable()
    throw new Error((body as { detail?: string } | null)?.detail ?? `${res.status} ${res.statusText}`)
  }
  return res.json() as Promise<T>
}

const asOf = (d?: string | null) => (d ? `?as_of=${d}` : '')

export const api = {
  health: () => get<{ ok: boolean; nodes: number }>('/api/health'),
  stats: () => get<Stats>('/api/stats'),
  ontology: () => get<Ontology>('/api/ontology'),
  node: (id: string, at?: string | null) =>
    get<NodeDetail>(`/api/nodes/${encodeURIComponent(id)}${asOf(at)}`),
  search: (p: { q?: string; type?: string; jurisdiction?: string; limit?: number }) => {
    const s = new URLSearchParams()
    if (p.q) s.set('q', p.q)
    if (p.type) s.set('type', p.type)
    if (p.jurisdiction) s.set('jurisdiction', p.jurisdiction)
    s.set('limit', String(p.limit ?? 100))
    return get<{
      total: number
      items: NodeBrief[]
      /** 클래스 필터 적용 전 결과 수 — 「검색어는 맞는데 이 클래스에 없다」를 구분한다. */
      matched: number
      /** 현재 검색어 기준 클래스별 개수. 전체 개수가 아니다. */
      facets: Record<string, number>
    }>(`/api/nodes?${s}`)
  },
  graph: (p: { layer?: string; min_degree?: number; limit?: number } = {}) => {
    const s = new URLSearchParams()
    if (p.layer) s.set('layer', p.layer)
    s.set('min_degree', String(p.min_degree ?? 0))
    s.set('limit', String(p.limit ?? 400))
    return get<{
      nodes: { id: string; type: string; layer: string; title: string; degree: number }[]
      links: { source: string; target: string; predicate: string }[]
      truncated: boolean
      total_nodes: number
    }>(`/api/graph?${s}`)
  },
  neighbors: (id: string, depth = 1) =>
    get<{
      root: string
      nodes: { id: string; type: string; layer: string; title: string }[]
      links: { source: string; target: string; predicate: string }[]
    }>(`/api/nodes/${encodeURIComponent(id)}/neighbors?depth=${depth}`),
  facts: (p: { subject?: string; confidence?: string; limit?: number }) => {
    const s = new URLSearchParams()
    if (p.subject) s.set('subject', p.subject)
    if (p.confidence) s.set('confidence', p.confidence)
    s.set('limit', String(p.limit ?? 200))
    return get<{ total: number; items: Fact[] }>(`/api/facts?${s}`)
  },
  crosswalk: (oblId: string, at?: string | null) =>
    get<Crosswalk>(`/api/crosswalk/${encodeURIComponent(oblId)}${asOf(at)}`),
  lineage: (id: string, at?: string | null) =>
    get<Lineage>(`/api/lineage/${encodeURIComponent(id)}${asOf(at)}`),
  contradictions: () =>
    get<{ total: number; items: Record<string, unknown>[] }>('/api/contradictions'),
  alog: () => get<{ total: number; items: Record<string, unknown>[] }>('/api/alog'),
}
