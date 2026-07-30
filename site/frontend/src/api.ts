const BASE = import.meta.env.VITE_API_BASE ?? 'http://localhost:8000'

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
  const res = await fetch(`${BASE}${path}`)
  if (!res.ok) {
    const body = await res.json().catch(() => ({}))
    throw new Error((body as { detail?: string }).detail ?? `${res.status} ${res.statusText}`)
  }
  return res.json() as Promise<T>
}

const asOf = (d?: string | null) => (d ? `?as_of=${d}` : '')

export const api = {
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
    return get<{ total: number; items: NodeBrief[] }>(`/api/nodes?${s}`)
  },
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
