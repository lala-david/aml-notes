import { useEffect, useState } from 'react'
import { Link, useParams, useSearchParams } from 'react-router-dom'
import { api } from './api'
import type { Crosswalk, Lineage, NodeBrief, NodeDetail, Stats } from './api'
import {
  AsOfControl, ConfidenceBadge, Disclaimer, ErrorBox, EvidenceList, Loading, NodeChip,
} from './components'

function useAsync<T>(fn: () => Promise<T>, deps: unknown[]) {
  const [state, set] = useState<{ data?: T; error?: unknown; loading: boolean }>({ loading: true })
  useEffect(() => {
    let alive = true
    set({ loading: true })
    fn().then(
      (d) => alive && set({ data: d, loading: false }),
      (e) => alive && set({ error: e, loading: false }),
    )
    return () => {
      alive = false
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps)
  return state
}

/** URL 쿼리로 as_of 를 유지 — 링크를 공유하면 시점도 함께 간다. */
function useAsOf(): [string | null, (v: string | null) => void] {
  const [sp, setSp] = useSearchParams()
  const value = sp.get('as_of')
  return [
    value,
    (v) => {
      const next = new URLSearchParams(sp)
      if (v) next.set('as_of', v)
      else next.delete('as_of')
      setSp(next, { replace: true })
    },
  ]
}

// ─────────────────────────────────────────────────────────

export function Home() {
  const { data, error, loading } = useAsync<Stats>(() => api.stats(), [])
  if (loading) return <Loading />
  if (error) return <ErrorBox error={error} />
  const s = data!
  return (
    <div className="stack">
      <section className="hero">
        <h1>가상자산 AML 지식베이스</h1>
        <p>
          조문 하나를 클릭하면 그 의무가 <strong>어디서 왔고</strong>,{' '}
          <strong>누가 바꿀 수 있고</strong>, <strong>언제부터 그랬는지</strong>를 따라갈 수 있습니다.
        </p>
        <div className="cta">
          <Link className="btn primary" to="/obl/OBL:x-travel-rule-originator">
            트래블룰 관할 비교 →
          </Link>
          <Link className="btn" to="/search">
            노드 탐색
          </Link>
        </div>
      </section>

      <section>
        <h2>현황</h2>
        <div className="stats">
          <Stat n={s.nodes} label="노드" />
          <Stat n={s.facts} label="원자적 사실" />
          <Stat n={s.contradictions} label="상충" sub={`미판정 ${s.unresolved_contradictions}`} />
          <Stat n={s.action_log} label="액션 로그" />
        </div>
        <div className="confbar">
          {(['A', 'B', 'C', 'D'] as const).map((c) => (
            <span key={c} className={`conf conf-${c}`}>
              {c} {s.confidence[c] ?? 0}
            </span>
          ))}
        </div>
        <div className="typegrid">
          {Object.entries(s.by_type).map(([t, n]) => (
            <Link key={t} to={`/search?type=${t}`} className="typecell">
              <b>{t}</b>
              <span>{n}</span>
            </Link>
          ))}
        </div>
      </section>
      <Disclaimer />
    </div>
  )
}

function Stat({ n, label, sub }: { n: number; label: string; sub?: string }) {
  return (
    <div className="stat">
      <b>{n.toLocaleString()}</b>
      <span>{label}</span>
      {sub && <em>{sub}</em>}
    </div>
  )
}

// ─────────────────────────────────────────────────────────

export function CrosswalkPage() {
  const { id = '' } = useParams()
  const [at, setAt] = useAsOf()
  const { data, error, loading } = useAsync<Crosswalk>(() => api.crosswalk(id, at), [id, at])

  return (
    <div className="stack">
      <AsOfControl value={at} onChange={setAt} />
      {loading && <Loading />}
      {error ? <ErrorBox error={error} /> : null}
      {data && (
        <>
          <h1>{data.obligation.title}</h1>
          {data.obligation.summary && <p className="muted">{data.obligation.summary}</p>}
          <p className="asof-note">
            {at ? (
              <>
                <b>{at}</b> 시점 기준 — 그날 유효했던 조문만 표시됩니다.
              </>
            ) : (
              '전체 기간'
            )}
          </p>

          <table className="cw">
            <thead>
              <tr>
                <th>관할</th>
                <th>근거 조문</th>
                <th className="num">임계값</th>
                <th>유효기간</th>
                <th>확신도</th>
              </tr>
            </thead>
            <tbody>
              {data.rows.map((r) => (
                <tr key={r.provision.id}>
                  <td>{r.jurisdiction_label}</td>
                  <td>
                    <NodeChip node={r.provision} />
                    {r.regulation && <div className="sub">{r.regulation.title}</div>}
                  </td>
                  <td className="num">
                    {r.threshold != null ? (
                      <>
                        {r.threshold.toLocaleString()} <small>{r.currency}</small>
                      </>
                    ) : (
                      <span className="muted">임계값 없음</span>
                    )}
                    {r.scope_note && <div className="sub">{r.scope_note}</div>}
                  </td>
                  <td className="sub">
                    {r.valid_from ?? '?'} ~ {r.valid_to ?? '현재'}
                  </td>
                  <td>
                    <ConfidenceBadge value={r.confidence} />
                  </td>
                </tr>
              ))}
              {!data.rows.length && (
                <tr>
                  <td colSpan={5} className="muted">
                    이 시점에 유효한 조문이 없습니다.
                  </td>
                </tr>
              )}
            </tbody>
          </table>

          {data.missing_jurisdictions.length > 0 && (
            <p className="muted">
              미등재 관할: {data.missing_jurisdictions.map((m) => m.label).join(' · ')}
            </p>
          )}
        </>
      )}
      <Disclaimer />
    </div>
  )
}

// ─────────────────────────────────────────────────────────

export function LineagePage() {
  const { id = '' } = useParams()
  const [at, setAt] = useAsOf()
  const { data, error, loading } = useAsync<Lineage>(() => api.lineage(id, at), [id, at])

  return (
    <div className="stack">
      <AsOfControl value={at} onChange={setAt} />
      {loading && <Loading />}
      {error ? <ErrorBox error={error} /> : null}
      {data && (
        <>
          <h1>계보 — {data.root.title}</h1>
          {data.root.summary && <p className="muted">{data.root.summary}</p>}
          {data.paths.map((path, i) => (
            <ol className="lineage" key={i}>
              <li>
                <NodeChip node={path[0].from} />
              </li>
              {path.map((s, j) => (
                <li key={j}>
                  <span className="pred">{s.predicate}</span>
                  <NodeChip node={s.to} />
                  {Object.keys(s.qualifiers ?? {}).length > 0 && (
                    <span className="sub">
                      {Object.entries(s.qualifiers)
                        .filter(([, v]) => v != null)
                        .map(([k, v]) => `${k}=${v}`)
                        .join(' · ')}
                    </span>
                  )}
                </li>
              ))}
            </ol>
          ))}
          {!data.paths.length && <p className="muted">상위 경로가 없습니다.</p>}
        </>
      )}
    </div>
  )
}

// ─────────────────────────────────────────────────────────

export function NodePage() {
  const { id = '' } = useParams()
  const [at, setAt] = useAsOf()
  const { data, error, loading } = useAsync<NodeDetail>(() => api.node(id, at), [id, at])

  if (loading) return <Loading />
  if (error) return <ErrorBox error={error} />
  const n = data!
  const skip = new Set([
    'id', 'type', 'layer', 'label', 'title', 'path', 'edges_out', 'edges_in',
    'facts', 'states', 'evidence', 'summary', 'curator_note', 'created_at', 'updated_at',
  ])

  return (
    <div className="stack">
      <AsOfControl value={at} onChange={setAt} />
      <header className="nodehead">
        <span className="chip-type big">{n.type}</span>
        <h1>{n.title}</h1>
        <code className="muted">{n.id}</code>
        {n.type === 'OBL' && (
          <Link className="btn primary" to={`/obl/${encodeURIComponent(n.id)}`}>
            관할 비교 →
          </Link>
        )}
        {n.type === 'PROV' && (
          <Link className="btn" to={`/lineage/${encodeURIComponent(n.id)}`}>
            계보 보기 →
          </Link>
        )}
      </header>

      {n.summary && <p className="lead">{n.summary}</p>}

      <section>
        <h2>속성</h2>
        <dl className="props">
          {Object.entries(n)
            .filter(([k, v]) => !skip.has(k) && v != null && typeof v !== 'object')
            .map(([k, v]) => (
              <div key={k}>
                <dt>{k}</dt>
                <dd>{String(v)}</dd>
              </div>
            ))}
        </dl>
      </section>

      {n.evidence?.length ? (
        <section>
          <h2>증거</h2>
          <EvidenceList items={n.evidence} />
        </section>
      ) : null}

      {n.facts.length > 0 && (
        <section>
          <h2>사실 {n.facts.length}</h2>
          {n.facts.map((f) => (
            <div className="fact" key={f.id}>
              <ConfidenceBadge value={f.confidence} />
              <p>{f.claim}</p>
              {f.note && <p className="sub">{f.note}</p>}
              <EvidenceList items={f.evidence} />
            </div>
          ))}
        </section>
      )}

      <section>
        <h2>관계</h2>
        <EdgeTable title="나가는" edges={n.edges_out} />
        <EdgeTable title="들어오는" edges={n.edges_in} />
      </section>

      {n.curator_note && (
        <section>
          <h2>큐레이터 메모</h2>
          <pre className="note">{n.curator_note}</pre>
        </section>
      )}
      <p className="muted src">원본: {n.path}</p>
    </div>
  )
}

function EdgeTable({ title, edges }: { title: string; edges: NodeDetail['edges_out'] }) {
  if (!edges.length) return null
  return (
    <>
      <h3>{title}</h3>
      <ul className="edges">
        {edges.map((e, i) => (
          <li key={i}>
            <span className="pred">{e.predicate}</span>
            <NodeChip node={e.node} />
            <ConfidenceBadge value={e.confidence} />
            {(e.valid_from || e.valid_to) && (
              <span className="sub">
                {e.valid_from ?? '?'} ~ {e.valid_to ?? '현재'}
              </span>
            )}
          </li>
        ))}
      </ul>
    </>
  )
}

// ─────────────────────────────────────────────────────────

export function SearchPage() {
  const [sp, setSp] = useSearchParams()
  const q = sp.get('q') ?? ''
  const type = sp.get('type') ?? ''
  const { data, error, loading } = useAsync(
    () => api.search({ q: q || undefined, type: type || undefined, limit: 200 }),
    [q, type],
  )

  const setParam = (k: string, v: string) => {
    const next = new URLSearchParams(sp)
    if (v) next.set(k, v)
    else next.delete(k)
    setSp(next, { replace: true })
  }

  return (
    <div className="stack">
      <h1>탐색</h1>
      <div className="filters">
        <input
          placeholder="ID · 제목 · 요약 · 별칭 검색"
          defaultValue={q}
          onKeyDown={(e) => e.key === 'Enter' && setParam('q', (e.target as HTMLInputElement).value)}
        />
        <input
          placeholder="타입 (REG · PROV · OBL …)"
          defaultValue={type}
          onKeyDown={(e) =>
            e.key === 'Enter' && setParam('type', (e.target as HTMLInputElement).value.toUpperCase())
          }
        />
      </div>
      {loading && <Loading />}
      {error ? <ErrorBox error={error} /> : null}
      {data && (
        <>
          <p className="muted">{data.total}건</p>
          <ul className="results">
            {data.items.map((n: NodeBrief) => (
              <li key={n.id}>
                <NodeChip node={n} />
                {n.summary && <p className="sub">{n.summary}</p>}
              </li>
            ))}
          </ul>
        </>
      )}
    </div>
  )
}

// ─────────────────────────────────────────────────────────

export function ContradictionsPage() {
  const { data, error, loading } = useAsync(() => api.contradictions(), [])
  if (loading) return <Loading />
  if (error) return <ErrorBox error={error} />
  return (
    <div className="stack">
      <h1>상충 레지스트리</h1>
      <p className="muted">
        출처가 엇갈릴 때 어느 쪽도 삭제하지 않습니다. 판정과 근거를 함께 기록합니다.
      </p>
      {data!.items.map((c) => {
        const r = c as Record<string, string>
        const unresolved = r.resolution === 'unresolved'
        return (
          <article className={`ctr ${unresolved ? 'ctr-open' : ''}`} key={r.id}>
            <header>
              <code>{r.id}</code>
              <span className={`tag ${unresolved ? 'tag-warn' : 'tag-ok'}`}>{r.resolution}</span>
            </header>
            <h3>{r.issue}</h3>
            <p>{r.analysis}</p>
            {r.action && (
              <p className="sub">
                <b>조치</b> {r.action}
              </p>
            )}
          </article>
        )
      })}
    </div>
  )
}

export function FactsPage() {
  const [sp, setSp] = useSearchParams()
  const conf = sp.get('confidence') ?? ''
  const { data, error, loading } = useAsync(
    () => api.facts({ confidence: conf || undefined, limit: 500 }),
    [conf],
  )
  return (
    <div className="stack">
      <h1>원자적 사실</h1>
      <p className="muted">
        주어 1 · 술어 1 · 값 1 · 시점 1. 모든 사실이 원문 인용까지 추적됩니다.
      </p>
      <div className="filters">
        {['', 'A', 'B', 'C', 'D'].map((c) => (
          <button
            key={c || 'all'}
            className={conf === c ? 'on' : ''}
            onClick={() => {
              const n = new URLSearchParams(sp)
              if (c) n.set('confidence', c)
              else n.delete('confidence')
              setSp(n, { replace: true })
            }}
          >
            {c || '전체'}
          </button>
        ))}
      </div>
      {loading && <Loading />}
      {error ? <ErrorBox error={error} /> : null}
      {data && (
        <>
          <p className="muted">{data.total}건</p>
          {data.items.map((f) => (
            <article className="fact" key={f.id}>
              <header>
                <ConfidenceBadge value={f.confidence} />
                <code>{f.id}</code>
                {f.subject && <NodeChip node={{ id: f.subject, type: f.subject.split(':')[0], layer: '', title: f.subject, label: {} }} />}
              </header>
              <p>{f.claim}</p>
              {f.value != null && (
                <p className="sub">
                  <b>{f.attribute}</b> = {String(f.value)} {f.unit ?? ''}
                  {f.valid_from && ` · ${f.valid_from} ~ ${f.valid_to ?? '현재'}`}
                </p>
              )}
              {f.note && <p className="sub note-inline">{f.note}</p>}
              <EvidenceList items={f.evidence} />
            </article>
          ))}
        </>
      )}
      <Disclaimer />
    </div>
  )
}

export function SourcesPage() {
  const { data, error, loading } = useAsync(() => api.search({ type: 'SRC', limit: 300 }), [])
  const tiers = ['T1', 'T2', 'T3', 'T4', 'T5']
  if (loading) return <Loading />
  if (error) return <ErrorBox error={error} />
  const items = data!.items
  return (
    <div className="stack">
      <h1>출처 레지스트리</h1>
      <p className="muted">
        등급은 출처의 권위이며 확신도와 별개입니다. T1 은 법령 원문·감독기관 공식 발간물입니다.
      </p>
      {tiers.map((t) => {
        const group = items.filter((n) => (n as unknown as { tier?: string }).tier === t)
        if (!group.length) return null
        return (
          <section key={t}>
            <h2>
              <span className={`tier tier-${t}`}>{t}</span> {group.length}
            </h2>
            <ul className="results">
              {group.map((n) => (
                <li key={n.id}>
                  <NodeChip node={n} />
                  {n.summary && <p className="sub">{n.summary}</p>}
                </li>
              ))}
            </ul>
          </section>
        )
      })}
      <section>
        <h2>등급 미상 {items.filter((n) => !(n as unknown as { tier?: string }).tier).length}</h2>
        <ul className="results">
          {items
            .filter((n) => !(n as unknown as { tier?: string }).tier)
            .map((n) => (
              <li key={n.id}>
                <NodeChip node={n} />
              </li>
            ))}
        </ul>
      </section>
    </div>
  )
}

export function OntologyPage() {
  const { data, error, loading } = useAsync(() => api.ontology(), [])
  if (loading) return <Loading />
  if (error) return <ErrorBox error={error} />
  const o = data!
  const layers: Record<string, string> = {
    semantic: 'L1 SEMANTIC — 명사 · 무엇이 존재하는가',
    dynamic: 'L2 DYNAMIC — 시간 · 언제 참이었는가',
    kinetic: 'L3 KINETIC — 동사 · 무엇을 바꿀 수 있는가',
    funnel: 'FUNNEL — 계층 아님 · 유입 인프라',
  }
  return (
    <div className="stack">
      <h1>온톨로지 v{o.version}</h1>
      <p className="muted">
        이 사이트의 화면은 손으로 만들지 않았습니다. 아래 정의를 읽어 렌더링합니다.
      </p>

      {Object.entries(layers).map(([layer, title]) => {
        const cls = Object.entries(o.classes).filter(([, c]) => c.layer === layer)
        if (!cls.length) return null
        return (
          <section key={layer}>
            <h2>{title}</h2>
            <div className="typegrid">
              {cls.map(([code, c]) => (
                <Link key={code} to={`/search?type=${code}`} className="typecell">
                  <b>{code}</b>
                  <span>{c.label?.ko}</span>
                </Link>
              ))}
            </div>
          </section>
        )
      })}

      <section>
        <h2>술어 {Object.keys(o.predicates).length}</h2>
        <ul className="preds">
          {Object.entries(o.predicates).map(([p, spec]) => (
            <li key={p}>
              <span className="pred">{p}</span>
              <span className="sub">
                {(spec.from ?? ['*']).join('|')} → {(spec.to ?? ['*']).join('|')}
                {spec.symmetric ? ' · 대칭' : ''}
              </span>
            </li>
          ))}
        </ul>
      </section>

      <section>
        <h2>확신도</h2>
        <dl className="props">
          {Object.entries(o.confidence_levels).map(([k, v]) => (
            <div key={k}>
              <dt>
                <span className={`conf conf-${k}`}>{k}</span>
              </dt>
              <dd>{v}</dd>
            </div>
          ))}
        </dl>
        <h2>출처 등급</h2>
        <dl className="props">
          {Object.entries(o.source_tiers).map(([k, v]) => (
            <div key={k}>
              <dt>
                <span className={`tier tier-${k}`}>{k}</span>
              </dt>
              <dd>{v}</dd>
            </div>
          ))}
        </dl>
      </section>
    </div>
  )
}

export function AlogPage() {
  const { data, error, loading } = useAsync(() => api.alog(), [])
  if (loading) return <Loading />
  if (error) return <ErrorBox error={error} />
  return (
    <div className="stack">
      <h1>액션 로그</h1>
      <p className="muted">지식이 언제 누구에 의해 어떤 근거로 바뀌었는지의 기록입니다.</p>
      <ul className="alog">
        {data!.items.map((a) => {
          const r = a as Record<string, string>
          return (
            <li key={r.id}>
              <code>{r.executed_at}</code>
              <span className="pred">{r.action}</span>
              <span className="sub">{r.actor}</span>
              {r.note && <p>{r.note}</p>}
            </li>
          )
        })}
      </ul>
    </div>
  )
}
