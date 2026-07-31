import { useState } from 'react'
import { Link, useParams, useSearchParams } from 'react-router-dom'
import { api } from './api'
import type { Confidence, Crosswalk, Lineage, NodeBrief, NodeDetail, Ontology, Stats } from './api'
import { useAsync } from './useAsync'
import {
  AsOfControl, ConfMark, Count, Empty, ErrorBox, EvidenceList, LegalNote, Loading,
  NodeRef, PageHead, Rich, Section, TierMark, confLabel,
} from './components'
import { Graph } from './Graph'
import { Strata } from './Brand'
import { AsOfContrast, CrosswalkPreview, DelegationChain } from './Explain'
import { JurChip } from './Jur'
import { IconArrow, IconSearch } from './Icons'

const TRAVEL_RULE = 'OBL:x-travel-rule-originator'
const ROOT_PROV = 'PROV:kr-tfia-art5-3'

const LAYER_KO: Record<string, string> = {
  semantic: 'L1 명사',
  dynamic: 'L2 시간',
  kinetic: 'L3 동사',
  funnel: '유입',
}

/**
 * 속성값 한 칸. 값이 노드 ID 면 링크로 만든다.
 * `parent_typology: TYP:x-onchain-layering` 처럼 다른 노드를 가리키는
 * 속성이 맨 텍스트로 남으면 거기서 탐색이 끊긴다 — 관계 목록에서는
 * 눌러 갈 수 있는 대상이 속성 칸에서만 막다른 길이 될 이유가 없다.
 */
const NODE_ID = /^[A-Z]{3,7}:[a-z0-9][a-z0-9-]*$/

function SpecValue({ value }: { value: unknown }) {
  if (Array.isArray(value)) {
    return (
      <>
        {value.map((v, i) => (
          <span key={i}>
            {i > 0 && ', '}
            <SpecValue value={v} />
          </span>
        ))}
      </>
    )
  }
  if (typeof value === 'string' && NODE_ID.test(value)) {
    return <Link to={`/n/${encodeURIComponent(value)}`} className="spec-ref">{value}</Link>
  }
  if (typeof value === 'boolean') return <>{value ? '예' : '아니오'}</>
  if (value && typeof value === 'object') return <>{JSON.stringify(value)}</>
  return <>{String(value)}</>
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

/* ═══════════════════════════════════════════════════════════════════════
   홈 — 구조 설명이 아니라 질문 하나로 시작한다.
   ═══════════════════════════════════════════════════════════════════════ */

export function Home() {
  const s = useAsync<Stats>(() => api.stats(), [])
  const cw = useAsync<Crosswalk>(() => api.crosswalk(TRAVEL_RULE), [])

  return (
    <>
      <div className="lede">
        <p className="kicker">위임 계보 · 시점 질의 · 원문 증거</p>
        <h1>100만원. 이 숫자는 법률 어디에도 없습니다.</h1>
        <p className="lede-body">
          가상자산을 100만원 넘게 보내면 받는 거래소에 송신인 정보를 넘겨야 합니다. 그런데{' '}
          <strong>특금법 본문에는 이 금액이 없습니다.</strong> 법률은 상한만 긋고 위임했고, 실제
          기준은 두 단계 아래 시행령에 있습니다.
        </p>
      </div>

      {s.data && <Census stats={s.data} />}

      <Section num="§ 01" title="위임은 어디까지 내려가는가" note="조문 셋을 따라가면 숫자가 나옵니다">
        <DelegationChain />
      </Section>

      <Section num="§ 02" title="같은 의무, 다른 조문" note={<>관할 비교<br />크로스워크</>}>
        <p className="sec-lead">
          트래블룰이라는 하나의 의무를 나라마다 다른 조문이 정하고, 기준금액도 제각각입니다. 아래
          표는 손으로 만든 것이 아니라 그래프에서 뽑아낸 결과입니다 — 조문을 등재하면 한 줄이
          자동으로 늘어납니다.
        </p>
        {cw.loading && <Loading rows={4} />}
        {cw.error ? <ErrorBox error={cw.error} /> : null}
        {cw.data && <CrosswalkPreview rows={cw.data.rows} />}
        <div className="btnrow gap-top">
          <Link className="btn btn-key" to={`/obl/${encodeURIComponent(TRAVEL_RULE)}`}>
            전체 비교표
            <IconArrow size={14} />
          </Link>
          <Link className="btn" to={`/lineage/${encodeURIComponent(ROOT_PROV)}`}>
            위임 사슬 전체
          </Link>
        </div>
      </Section>

      <Section num="§ 03" title="2021년에는 어땠는가" note={<>시점 질의<br />as-of</>}>
        <p className="sec-lead">
          규제는 계속 바뀝니다. 이 지식베이스는 모든 사실에 유효기간을 붙여 두어서 과거 어느 날의
          규제 지형을 그대로 재현합니다. 아래는 같은 질의를 두 시점에 던진 결과입니다 — 그날
          시행되지 않았던 조문은 답에서 빠집니다.
        </p>
        {cw.data && <AsOfContrast rows={cw.data.rows} />}
      </Section>

      <Section num="§ 04" title="지식을 담는 세 겹" note="온톨로지">
        <p className="sec-lead">
          무엇이 존재하는가(명사), 언제 참이었는가(시간), 무엇을 바꿀 수 있는가(동사). 수집
          파이프라인은 계층이 아니라 이 세 겹을 채우는 인프라입니다.
        </p>
        <Strata />
        <div className="btnrow gap-top">
          <Link className="btn" to="/ontology">
            클래스 · 술어 전체
            <IconArrow size={14} />
          </Link>
        </div>
      </Section>

      <LegalNote />
    </>
  )
}

/** 수록 현황 — 통계 타일이 아니라 판권장 한 줄. */
function Census({ stats }: { stats: Stats }) {
  const cells: [string, number, string][] = [
    ['노드', stats.nodes, '조문 · 의무 · 기관 · 출처'],
    ['사실', stats.facts, '전부 원문 인용 결속'],
    ['출처', stats.by_type.SRC ?? 0, '등급 T1~T5'],
    [
      '상충',
      stats.contradictions,
      stats.unresolved_contradictions ? `미판정 ${stats.unresolved_contradictions}` : '전부 판정 완료',
    ],
    ['변경 기록', stats.action_log, '누가 · 언제 · 왜'],
  ]
  return (
    <>
      <dl className="census">
        {cells.map(([k, v, n]) => (
          <div className="census-cell" key={k}>
            <dt>{k}</dt>
            <dd>{v.toLocaleString()}</dd>
            <small>{n}</small>
          </div>
        ))}
      </dl>
      <div className="confrow">
        <span className="label">확신도 분포</span>
        {(['A', 'B', 'C', 'D'] as const).map((c) => (
          <span className="confrow-item" key={c}>
            <ConfMark value={c} />
            <b>{stats.confidence[c] ?? 0}</b>
            <span>{confLabel(c)}</span>
          </span>
        ))}
      </div>
    </>
  )
}

/* ═══════════════════════════════════════════════════════════════════════
   관할 비교
   ═══════════════════════════════════════════════════════════════════════ */

export function CrosswalkIndex() {
  const { data, error, loading } = useAsync(() => api.search({ type: 'OBL', limit: 100 }), [])
  return (
    <>
      <PageHead
        title="관할 비교"
        lead="관할에서 탈각된 추상 의무 하나에 각국 조문이 어떻게 걸려 있는지를 나란히 봅니다. 기준 시점을 바꾸면 그날 시행 중이던 조문만 남습니다."
      />
      {loading && <Loading rows={3} />}
      {error ? <ErrorBox error={error} /> : null}
      {data && !data.items.length && <Empty>등재된 추상 의무가 없습니다.</Empty>}
      {data && data.items.length > 0 && (
        <ul className="ledger split">
          {data.items.map((o) => (
            <li key={o.id}>
              <div className="rec-meta">
                <span>{o.id}</span>
              </div>
              <div className="rec-body">
                <Link className="rec-title" to={`/obl/${encodeURIComponent(o.id)}`}>
                  {o.title}
                </Link>
                {o.summary && <p className="rec-note clamp"><Rich text={o.summary} /></p>}
              </div>
            </li>
          ))}
        </ul>
      )}
    </>
  )
}

export function CrosswalkPage() {
  const { id = '' } = useParams()
  const [at, setAt] = useAsOf()
  const { data, error, loading } = useAsync<Crosswalk>(() => api.crosswalk(id, at), [id, at])

  return (
    <>
      <AsOfControl
        value={at}
        onChange={setAt}
        effect="그날 아직 시행되지 않은 조문은 표에서 사라집니다."
      />
      {loading && <Loading rows={5} />}
      {error ? <ErrorBox error={error} /> : null}
      {data && (
        <>
          <PageHead
            title={data.obligation.title}
            lead={<Rich text={data.obligation.summary} />}
            aside={
              <>
                <Count n={data.rows.length} unit="개 관할" />
                <Link className="btn" to={`/n/${encodeURIComponent(data.obligation.id)}`}>
                  의무 노드
                </Link>
              </>
            }
          />

          <div className="tablewrap">
            <table className="data">
              <thead>
                <tr>
                  <th>관할</th>
                  <th>근거 조문 · 원문 증거</th>
                  <th className="num">기준금액</th>
                  <th>시행 기간</th>
                  <th>확신도</th>
                </tr>
              </thead>
              <tbody>
                {data.rows.map((r) => (
                  <tr key={r.provision.id}>
                    <td>
                      <JurChip ns={r.namespace} label={r.jurisdiction_label} />
                    </td>
                    <td>
                      <NodeRef node={r.provision} />
                      {r.regulation && <span className="sub">{r.regulation.title}</span>}
                      {r.evidence.length > 0 && (
                        <details className="disc">
                          <summary>원문 {r.evidence.length}건</summary>
                          <EvidenceList items={r.evidence} />
                        </details>
                      )}
                    </td>
                    <td className="num">
                      {r.threshold != null ? (
                        <>
                          <b>{r.threshold.toLocaleString()}</b>
                          <small>{r.currency}</small>
                        </>
                      ) : (
                        <span className="dim">임계값 없음</span>
                      )}
                      {r.scope_note && <span className="sub">{r.scope_note}</span>}
                    </td>
                    <td>
                      <span className="period">
                        {r.valid_from ?? '?'} ~ {r.valid_to ?? '현재'}
                      </span>
                    </td>
                    <td>
                      <ConfMark value={r.confidence} />
                    </td>
                  </tr>
                ))}
                {!data.rows.length && (
                  <tr>
                    <td colSpan={5} className="dim">
                      이 시점에 유효한 조문이 없습니다.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>

          {data.missing_jurisdictions.length > 0 && (
            <p className="aftertable">
              <span className="label">미등재 관할</span>
              {data.missing_jurisdictions.map((m) => (
                <JurChip key={m.namespace} ns={m.namespace} label={m.label} />
              ))}
            </p>
          )}

          <LegalNote />
        </>
      )}
    </>
  )
}

/* ═══════════════════════════════════════════════════════════════════════
   계보
   ═══════════════════════════════════════════════════════════════════════ */

export function LineagePage() {
  const { id = '' } = useParams()
  const [at, setAt] = useAsOf()
  const { data, error, loading } = useAsync<Lineage>(() => api.lineage(id, at), [id, at])

  return (
    <>
      <AsOfControl value={at} onChange={setAt} effect="그날 유효했던 관계만 이어집니다." />
      {loading && <Loading rows={4} />}
      {error ? <ErrorBox error={error} /> : null}
      {data && (
        <>
          <PageHead
            title={data.root.title}
            lead={<Rich text={data.root.summary} />}
            aside={
              <>
                <Count n={data.paths.length} unit="개 경로" />
                <Link className="btn" to={`/n/${encodeURIComponent(data.root.id)}`}>
                  조문 노드
                </Link>
              </>
            }
          />
          {!data.paths.length && <Empty>이 조문에서 거슬러 올라갈 상위 경로가 없습니다.</Empty>}
          {data.paths.filter((p) => p.length > 0).map((path, i) => (
            <div className="path" key={i}>
              <h4>경로 {String(i + 1).padStart(2, '0')}</h4>
              <ol>
                <li className="origin">
                  <NodeRef node={path[0].from} />
                </li>
                {path.map((s, j) => (
                  <li key={j}>
                    <span className="path-rel">
                      <span className="pred">{s.predicate}</span>
                      <ConfMark value={s.confidence} />
                      {Object.entries(s.qualifiers ?? {})
                        .filter(([, v]) => v != null)
                        .map(([k, v]) => (
                          <span className="path-q" key={k}>
                            {k}={String(v)}
                          </span>
                        ))}
                    </span>
                    <NodeRef node={s.to} />
                  </li>
                ))}
              </ol>
            </div>
          ))}
        </>
      )}
    </>
  )
}

/* ═══════════════════════════════════════════════════════════════════════
   노드 상세 — 본문 + 제원 레일
   ═══════════════════════════════════════════════════════════════════════ */

const HIDDEN_PROPS = new Set([
  'id', 'type', 'layer', 'label', 'title', 'path', 'edges_out', 'edges_in',
  'facts', 'states', 'evidence', 'summary', 'curator_note',
])

export function NodePage() {
  const { id = '' } = useParams()
  const [at, setAt] = useAsOf()
  const { data, error, loading } = useAsync<NodeDetail>(() => api.node(id, at), [id, at])

  if (loading) return <Loading rows={5} />
  if (error) return <ErrorBox error={error} />
  const n = data!
  const tier = typeof n.tier === 'string' ? n.tier : null
  const props = Object.entries(n).filter(
    ([k, v]) => !HIDDEN_PROPS.has(k) && v != null && typeof v !== 'object',
  )

  return (
    <>
      <AsOfControl value={at} onChange={setAt} effect="그 시점에 유효했던 관계·사실만 남습니다." />

      <div className="with-rail">
        <div>
          <header className="nodehead">
            <span className="label">
              {n.type} · {LAYER_KO[n.layer] ?? n.layer}
            </span>
            <h1>{n.title}</h1>
            <code className="nid">{n.id}</code>
            {n.summary && <p className="nodehead-sum"><Rich text={n.summary} /></p>}
          </header>

          {n.evidence?.length ? (
            <Section num="§" title="원문 증거" note={<Count n={n.evidence.length} />}>
              <EvidenceList items={n.evidence} />
            </Section>
          ) : null}

          {n.facts.length > 0 && (
            <Section num="§" title="사실" note={<Count n={n.facts.length} />}>
              <ul className="ledger split">
                {n.facts.map((f) => (
                  <li key={f.id}>
                    <div className="rec-meta">
                      <ConfMark value={f.confidence} />
                      <span>{f.id}</span>
                    </div>
                    <div className="rec-body">
                      <p className="rec-claim"><Rich text={f.claim} /></p>
                      {f.value != null && (
                        <p className="rec-kv">
                          {f.attribute} = <b>{String(f.value)}</b> {f.unit ?? ''}
                          {f.valid_from && ` · ${f.valid_from} ~ ${f.valid_to ?? '현재'}`}
                        </p>
                      )}
                      {f.note && <p className="rec-note"><Rich text={f.note} /></p>}
                      <EvidenceList items={f.evidence} />
                    </div>
                  </li>
                ))}
              </ul>
            </Section>
          )}

          <Section
            num="§"
            title="관계"
            note={<Count n={n.edges_out.length + n.edges_in.length} unit="개" />}
          >
            <EdgeList title="나가는 관계" edges={n.edges_out} />
            <EdgeList title="들어오는 관계" edges={n.edges_in} />
            {!n.edges_out.length && !n.edges_in.length && <Empty>연결된 노드가 없습니다.</Empty>}
          </Section>

          <NeighborGraph id={n.id} />

          {n.curator_note && (
            <Section num="§" title="큐레이터 메모" note="판단의 흔적">
              <pre className="note"><Rich text={n.curator_note} /></pre>
            </Section>
          )}
        </div>

        <aside className="rail">
          {(n.type === 'OBL' || n.type === 'PROV' || tier) && (
            <div>
              <h4>이 노드로 할 수 있는 것</h4>
              <div className="btnrow">
                {n.type === 'OBL' && (
                  <Link className="btn btn-key" to={`/obl/${encodeURIComponent(n.id)}`}>
                    관할 비교
                    <IconArrow size={14} />
                  </Link>
                )}
                {n.type === 'PROV' && (
                  <Link className="btn btn-key" to={`/lineage/${encodeURIComponent(n.id)}`}>
                    위임 계보
                    <IconArrow size={14} />
                  </Link>
                )}
              </div>
              {tier && (
                <p className="rail-tier">
                  <TierMark tier={tier} />
                  <span>{typeof n.tier_basis === 'string' ? n.tier_basis : '출처 등급'}</span>
                </p>
              )}
            </div>
          )}

          {props.length > 0 && (
            <div>
              <h4>속성</h4>
              <dl className="spec">
                {props.map(([k, v]) => (
                  <div key={k}>
                    <dt>{k}</dt>
                    <dd><SpecValue value={v} /></dd>
                  </div>
                ))}
              </dl>
            </div>
          )}

          <div>
            <h4>원본 파일</h4>
            <p className="rail-path">{n.path}</p>
          </div>
        </aside>
      </div>
    </>
  )
}

function EdgeList({ title, edges }: { title: string; edges: NodeDetail['edges_out'] }) {
  if (!edges.length) return null
  return (
    <>
      <h4 className="sub-head">{title}</h4>
      <ul className="rels">
        {edges.map((e, i) => (
          <li key={i}>
            <span className="pred">{e.predicate}</span>
            <NodeRef node={e.node} />
            <span className="rels-side">
              {(e.valid_from || e.valid_to) && (
                <span className="period">
                  {e.valid_from ?? '?'} ~ {e.valid_to ?? '현재'}
                </span>
              )}
              <ConfMark value={e.confidence} />
            </span>
          </li>
        ))}
      </ul>
    </>
  )
}

/**
 * 이웃 그래프. 홈에서 걷어냈다 — 처음 온 사람에게 노드 220개짜리 성운은
 * 아무것도 설명하지 못한다. 여기서는 "이 조문 하나의 주변"이므로 읽힌다.
 */
function NeighborGraph({ id }: { id: string }) {
  const [depth, setDepth] = useState(1)
  const { data, loading } = useAsync(() => api.neighbors(id, depth), [id, depth])
  if (loading) return <Loading rows={2} />
  if (!data || data.nodes.length < 2) return null
  return (
    <Section
      num="§"
      title="주변 연결망"
      note={
        <>
          노드 {data.nodes.length} · 관계 {data.links.length}
        </>
      }
    >
      <div className="btnrow gap-bottom">
        <span className="label">탐색 깊이</span>
        <div className="seg">
          {[1, 2, 3].map((d) => (
            <button key={d} aria-pressed={depth === d} onClick={() => setDepth(d)}>
              {d}단계
            </button>
          ))}
        </div>
      </div>
      <Graph nodes={data.nodes} links={data.links} height={380} focusId={id} />
      <p className="graph-foot">
        색은 계층, 모양은 클래스군입니다. 색을 구분하기 어려워도 모양과 세로 위치로 읽을 수
        있습니다. 노드를 누르면 그 상세로 이동합니다.
      </p>
    </Section>
  )
}

/* ═══════════════════════════════════════════════════════════════════════
   탐색 — 결과 + 타입 패싯
   ═══════════════════════════════════════════════════════════════════════ */

export function SearchPage() {
  const [sp, setSp] = useSearchParams()
  const q = sp.get('q') ?? ''
  const type = sp.get('type') ?? ''
  const stats = useAsync<Stats>(() => api.stats(), [])
  const ont = useAsync<Ontology>(() => api.ontology(), [])
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

  /**
   * 패싯 숫자는 **현재 검색어 기준**이어야 한다. 전체 개수를 그대로 쓰면
   * 「TEC 62」 를 눌러 0 건이 나온다 — 화면이 62 건을 약속하고 0 건을 준다.
   * 검색 중에는 서버가 준 집계를 쓰고, 검색어가 없을 때만 전체 분포를 쓴다.
   * 검색어에 걸리지 않은 클래스도 0 으로 남겨 둔다. 목록에서 사라지면
   * 무엇이 빠졌는지 알 수 없다.
   */
  const base = stats.data?.by_type ?? {}
  // 클래스 목록은 전체 분포에서 얻고(0 건도 남겨 둔다), 숫자는 조회 결과에서 얻는다.
  const counts: Record<string, number> = data
    ? Object.fromEntries(Object.keys(base).map((k) => [k, data.facets[k] ?? 0]))
    : base
  const types = Object.entries(counts).sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
  const totalShown = data ? data.matched : stats.data?.nodes

  return (
    <>
      <PageHead
        title="탐색"
        lead="ID · 제목 · 요약 · 별칭으로 찾습니다. 오른쪽에서 클래스를 눌러 좁힐 수 있습니다."
      />

      <div className="field">
        <IconSearch size={17} />
        <input
          /* key 로 q 를 물린다. 비제어 입력이라 이게 없으면 「초기화」 를 눌러
             주소는 비워졌는데 입력칸에는 옛 검색어가 남는다. */
          key={q}
          placeholder="예: 트래블룰, 특금법, FATF, SRC:"
          defaultValue={q}
          onKeyDown={(e) => e.key === 'Enter' && setParam('q', (e.target as HTMLInputElement).value)}
          aria-label="검색어"
        />
        {(q || type) && (
          <button className="btn btn-quiet" onClick={() => setSp(new URLSearchParams(), { replace: true })}>
            초기화
          </button>
        )}
      </div>

      <div className="with-rail gap-top">
        <div>
          {loading && <Loading rows={5} />}
          {error ? <ErrorBox error={error} /> : null}
          {data && !data.items.length && (
            <div className="noresult">
              {/* 어느 조건이 결과를 죽였는지 말하고, 그 조건만 떼는 길을 준다.
                  「없습니다」 만 남으면 다음에 뭘 할지 알 수 없다. */}
              {type && data.matched > 0 ? (
                <>
                  <p>
                    {q && <>“{q}” 에 <b>{data.matched}건</b>이 있지만, </>}
                    그 중 <code>{type}</code> 클래스는 없습니다.
                  </p>
                  <button className="btn btn-quiet" onClick={() => setParam('type', '')}>
                    클래스 조건 없이 {data.matched}건 보기
                  </button>
                </>
              ) : (
                <>
                  <p>
                    {q ? <>“{q}” 로 찾은 노드가 없습니다.</> : <>조건에 맞는 노드가 없습니다.</>}
                  </p>
                  <p className="dim">
                    제목·요약·별칭·ID 를 글자 그대로 훑습니다. 짧게 줄이거나
                    <code>SRC:</code> 처럼 클래스 앞자리로 찾아 보세요.
                  </p>
                  {(q || type) && (
                    <button
                      className="btn btn-quiet"
                      onClick={() => setSp(new URLSearchParams(), { replace: true })}
                    >
                      조건 모두 지우기
                    </button>
                  )}
                </>
              )}
            </div>
          )}
          {data && data.items.length > 0 && (
            <>
              <p className="resultbar">
                <Count n={data.total} />
                {type && <span className="dim"> · 클래스 {type}</span>}
                {q && <span className="dim"> · “{q}”</span>}
                {/* 245 건이라 적고 200 행만 그리면 나머지가 없는 것처럼 보인다.
                    잘렸으면 잘렸다고 말한다. */}
                {data.items.length < data.total && (
                  <span className="dim"> · 아래 {data.items.length}건만 표시</span>
                )}
              </p>
              <ul className="ledger">
                {data.items.map((n: NodeBrief) => (
                  <li key={n.id}>
                    <NodeRef node={n} />
                    {n.summary && <p className="rec-note clamp"><Rich text={n.summary} /></p>}
                  </li>
                ))}
              </ul>
            </>
          )}
        </div>

        <aside className="rail">
          <div>
            <h4>클래스</h4>
            <ul className="facets">
              <li>
                <button aria-pressed={!type} onClick={() => setParam('type', '')}>
                  전체
                  <span className="n">{totalShown ?? ''}</span>
                </button>
              </li>
              {types.map(([code, n]) => (
                <li key={code}>
                  <button
                    aria-pressed={type === code}
                    /* 0 건인 클래스는 누를 수 없다. 눌러 봐야 빈 화면뿐이다. */
                    disabled={n === 0 && type !== code}
                    onClick={() => setParam('type', code)}
                  >
                    <code>{code}</code>
                    <span className="fname">{ont.data?.classes[code]?.label?.ko ?? ''}</span>
                    <span className="n">{n}</span>
                  </button>
                </li>
              ))}
            </ul>
          </div>
        </aside>
      </div>
    </>
  )
}

/* ═══════════════════════════════════════════════════════════════════════
   사실
   ═══════════════════════════════════════════════════════════════════════ */

export function FactsPage() {
  const [sp, setSp] = useSearchParams()
  const conf = sp.get('confidence') ?? ''
  const { data, error, loading } = useAsync(
    () => api.facts({ confidence: conf || undefined, limit: 500 }),
    [conf],
  )

  const setConf = (c: string) => {
    const n = new URLSearchParams(sp)
    if (c) n.set('confidence', c)
    else n.delete('confidence')
    setSp(n, { replace: true })
  }

  return (
    <>
      <PageHead
        title="원자적 사실"
        lead="주어 하나 · 술어 하나 · 값 하나 · 시점 하나. 쪼갤 수 있는 만큼 쪼개 두어야 어느 부분이 틀렸는지 지목할 수 있습니다. 모든 사실은 원문 인용까지 추적됩니다."
        aside={
          <div className="seg">
            {['', 'A', 'B', 'C', 'D'].map((c) => (
              <button key={c || 'all'} aria-pressed={conf === c} onClick={() => setConf(c)}>
                {c || '전체'}
              </button>
            ))}
          </div>
        }
      />

      {loading && <Loading rows={5} />}
      {error ? <ErrorBox error={error} /> : null}
      {data && !data.items.length && <Empty>해당 확신도의 사실이 없습니다.</Empty>}
      {data && data.items.length > 0 && (
        <>
          <p className="resultbar">
            <Count n={data.total} />
          </p>
          <ul className="ledger split">
            {data.items.map((f) => (
              <li key={f.id}>
                <div className="rec-meta">
                  <ConfMark value={f.confidence} />
                  <span>{f.id}</span>
                  {f.subject && (
                    <Link className="mono" to={`/n/${encodeURIComponent(f.subject)}`}>
                      {f.subject}
                    </Link>
                  )}
                </div>
                <div className="rec-body">
                  <p className="rec-claim"><Rich text={f.claim} /></p>
                  {f.value != null && (
                    <p className="rec-kv">
                      {f.attribute} = <b>{String(f.value)}</b> {f.unit ?? ''}
                      {f.valid_from && ` · ${f.valid_from} ~ ${f.valid_to ?? '현재'}`}
                    </p>
                  )}
                  {f.note && <p className="rec-note"><Rich text={f.note} /></p>}
                  <EvidenceList items={f.evidence} empty="원문 인용이 아직 결속되지 않았습니다." />
                </div>
              </li>
            ))}
          </ul>
        </>
      )}
      <LegalNote />
    </>
  )
}

/* ═══════════════════════════════════════════════════════════════════════
   출처 — 등급별
   ═══════════════════════════════════════════════════════════════════════ */

type SrcRow = NodeBrief & { tier?: string; tier_basis?: string; base_url?: string }

/**
 * 목록 API 는 tier 를 투영하지 않는다. KB 전체가 100여 노드라 상세를 한 번에
 * 끌어와 등급을 채운다. (개선 제안: GET /api/nodes 가 tier 를 함께 내려주면
 * 이 왕복이 사라진다.)
 */
export function SourcesPage() {
  const ont = useAsync<Ontology>(() => api.ontology(), [])
  const { data, error, loading } = useAsync<SrcRow[]>(async () => {
    const list = await api.search({ type: 'SRC', limit: 400 })
    const full = await Promise.all(
      list.items.map((n) =>
        api.node(n.id).then(
          (d) => ({ ...n, tier: d.tier as string | undefined, base_url: d.base_url as string | undefined }),
          () => n as SrcRow,
        ),
      ),
    )
    return full
  }, [])

  const tiers = ['T1', 'T2', 'T3', 'T4', 'T5']
  const unknown = data?.filter((n) => !n.tier) ?? []

  return (
    <>
      <PageHead
        title="출처 등록부"
        lead="등급은 출처의 권위이며 확신도와 다릅니다. 확신도는 “이 주장을 얼마나 믿을 수 있는가”, 등급은 “이 문서가 어떤 종류의 문서인가”입니다. 눈금이 많을수록 상위 등급입니다."
        aside={data ? <Count n={data.length} unit="개 출처" /> : undefined}
      />
      {loading && <Loading rows={6} />}
      {error ? <ErrorBox error={error} /> : null}
      {data &&
        tiers.map((t) => {
          const group = data.filter((n) => n.tier === t)
          if (!group.length) return null
          return (
            <Section
              key={t}
              num={<TierMark tier={t} title={ont.data?.source_tiers[t]} />}
              title={ont.data?.source_tiers[t] ?? t}
              note={<Count n={group.length} unit="개" />}
            >
              <ul className="ledger">
                {group.map((n) => (
                  <li key={n.id}>
                    <NodeRef node={n} />
                    {n.summary && <p className="rec-note clamp"><Rich text={n.summary} /></p>}
                  </li>
                ))}
              </ul>
            </Section>
          )
        })}
      {unknown.length > 0 && (
        <Section num="—" title="등급 미상" note={<Count n={unknown.length} unit="개" />}>
          <ul className="ledger">
            {unknown.map((n) => (
              <li key={n.id}>
                <NodeRef node={n} />
              </li>
            ))}
          </ul>
        </Section>
      )}
    </>
  )
}

/* ═══════════════════════════════════════════════════════════════════════
   검토 — 상충 + 변경 이력. 성격이 같아 한 화면으로 합쳤다.
   ═══════════════════════════════════════════════════════════════════════ */

const RESOLUTION_KO: Record<string, string> = {
  unresolved: '미판정',
  a_correct: 'A 측 채택',
  b_correct: 'B 측 채택',
  both_valid_different_scope: '둘 다 유효 · 적용범위 다름',
  both_wrong: '양측 모두 기각',
}

export function AuditPage() {
  const [sp, setSp] = useSearchParams()
  const tab = sp.get('tab') === 'log' ? 'log' : 'conflict'
  const set = (t: string) => {
    const n = new URLSearchParams(sp)
    n.set('tab', t)
    setSp(n, { replace: true })
  }
  return (
    <>
      <PageHead
        title="검토"
        lead="지식이 무엇과 다투었고, 언제 누구에 의해 어떤 근거로 바뀌었는지의 기록입니다. 출처가 엇갈릴 때 어느 쪽도 지우지 않고 판정과 근거를 함께 남깁니다."
      />
      <div className="tabs" role="tablist">
        <button role="tab" aria-selected={tab === 'conflict'} onClick={() => set('conflict')}>
          상충 레지스트리
        </button>
        <button role="tab" aria-selected={tab === 'log'} onClick={() => set('log')}>
          변경 이력
        </button>
      </div>
      {tab === 'conflict' ? <Contradictions /> : <ActionLog />}
    </>
  )
}

function Contradictions() {
  const { data, error, loading } = useAsync(() => api.contradictions(), [])
  if (loading) return <Loading rows={4} />
  if (error) return <ErrorBox error={error} />
  const items = data!.items as Record<string, string>[]
  const open = items.filter((c) => !c.resolution || c.resolution === 'unresolved')
  const closed = items.filter((c) => c.resolution && c.resolution !== 'unresolved')
  const ordered = [...open, ...closed]

  if (!ordered.length) return <Empty>기록된 상충이 없습니다.</Empty>

  return (
    <ul className="ledger split">
      {ordered.map((c) => {
        const isOpen = !c.resolution || c.resolution === 'unresolved'
        return (
          <li key={c.id} className={isOpen ? 'open' : ''}>
            <div className="rec-meta">
              <span className={`tag ${isOpen ? 'bad' : 'ok'}`}>
                {RESOLUTION_KO[c.resolution] ?? c.resolution ?? '미판정'}
              </span>
              <span>{c.id}</span>
              {c.detected_at && <span>발견 {c.detected_at}</span>}
            </div>
            <div className="rec-body">
              <h3 className="rec-title"><Rich text={c.issue} /></h3>
              <p className="rec-claim"><Rich text={c.analysis} /></p>
              {c.verify_method && (
                <p className="rec-note">
                  <span className="label">검증 방법</span> {c.verify_method}
                </p>
              )}
              {c.action && (
                <p className="rec-note">
                  <span className="label">조치</span> {c.action}
                </p>
              )}
            </div>
          </li>
        )
      })}
    </ul>
  )
}

function ActionLog() {
  const { data, error, loading } = useAsync(() => api.alog(), [])
  if (loading) return <Loading rows={4} />
  if (error) return <ErrorBox error={error} />
  const items = data!.items as Record<string, string>[]
  if (!items.length) return <Empty>기록된 변경이 없습니다.</Empty>
  return (
    <ul className="ledger log">
      {items.map((a) => (
        <li key={a.id}>
          <div className="log-when">
            {String(a.executed_at ?? '').replace('T', ' ').replace('Z', '')}
            <br />
            {a.id}
          </div>
          <div className="rec-body">
            <p className="rec-title-row">
              <span className="pred">{a.action}</span>
              <span className="mono dim">{a.actor}</span>
              {a.result && <span className="tag">{a.result}</span>}
            </p>
            {a.note && <p className="rec-note"><Rich text={a.note} /></p>}
          </div>
        </li>
      ))}
    </ul>
  )
}

/* ═══════════════════════════════════════════════════════════════════════
   체계 — 온톨로지
   ═══════════════════════════════════════════════════════════════════════ */

export function OntologyPage() {
  const { data, error, loading } = useAsync<Ontology>(() => api.ontology(), [])
  if (loading) return <Loading rows={5} />
  if (error) return <ErrorBox error={error} />
  const o = data!
  const layers: [string, string][] = [
    ['semantic', 'L1 SEMANTIC — 명사 · 무엇이 존재하는가'],
    ['dynamic', 'L2 DYNAMIC — 시간 · 언제 참이었는가'],
    ['kinetic', 'L3 KINETIC — 동사 · 무엇을 바꿀 수 있는가'],
    ['funnel', 'FUNNEL — 계층 아님 · 유입 인프라'],
  ]

  return (
    <>
      <PageHead
        title={`온톨로지 v${o.version}`}
        lead="이 사이트의 화면은 손으로 만들지 않았습니다. 아래 정의를 읽어 렌더링합니다. 클래스가 늘면 화면이 늘고, 정의에 어긋난 노드는 검증기가 막습니다."
        aside={
          <span className="count">
            클래스 {Object.keys(o.classes).length} · 술어 {Object.keys(o.predicates).length}
          </span>
        }
      />

      <Section num="§ 01" title="세 겹" note="계층은 색과 세로 위치로도 부호화됩니다">
        <Strata compact />
      </Section>

      <Section num="§ 02" title="클래스" note={<Count n={Object.keys(o.classes).length} unit="개" />}>
        {layers.map(([layer, title]) => {
          const cls = Object.entries(o.classes).filter(([, c]) => c.layer === layer)
          if (!cls.length) return null
          return (
            <div className="classgroup" key={layer}>
              <h4 className="sub-head">{title}</h4>
              <div className="classes" style={{ ['--c' as string]: `var(--layer-${layer})` }}>
                {cls.map(([code, c]) => (
                  <Link key={code} to={`/search?type=${code}`}>
                    <code>{code}</code>
                    <span>{c.label?.ko}</span>
                  </Link>
                ))}
              </div>
            </div>
          )
        })}
      </Section>

      <Section num="§ 03" title="술어" note={<Count n={Object.keys(o.predicates).length} unit="개" />}>
        <ul className="preds">
          {Object.entries(o.predicates).map(([p, spec]) => (
            <li key={p}>
              <span className="pred">{p}</span>
              <span className="sig">
                {(spec.from ?? ['*']).join(' | ')} → {(spec.to ?? ['*']).join(' | ')}
                {spec.symmetric ? ' · 대칭' : ''}
              </span>
            </li>
          ))}
        </ul>
      </Section>

      <Section num="§ 04" title="신뢰 등급" note="색이 아니라 문자와 눈금이 등급을 진다">
        <h4 className="sub-head">확신도 — 주장을 얼마나 믿을 수 있는가</h4>
        <dl className="spec legend">
          {Object.entries(o.confidence_levels).map(([k, v]) => (
            <div key={k}>
              <dt>
                <ConfMark value={k as Confidence} />
              </dt>
              <dd>{v}</dd>
            </div>
          ))}
        </dl>
        <h4 className="sub-head">출처 등급 — 문서가 어떤 종류인가</h4>
        <dl className="spec legend">
          {Object.entries(o.source_tiers).map(([k, v]) => (
            <div key={k}>
              <dt>
                <TierMark tier={k} title={v} />
              </dt>
              <dd>{v}</dd>
            </div>
          ))}
        </dl>
      </Section>
    </>
  )
}

/* ═══════════════════════════════════════════════════════════════════════ */

export function NotFound() {
  return (
    <>
      <PageHead
        title="여기에는 아무것도 없습니다"
        lead="주소가 바뀌었거나, 아직 등재되지 않은 노드일 수 있습니다."
      />
      <div className="btnrow">
        <Link className="btn btn-key" to="/search">
          탐색으로
          <IconArrow size={14} />
        </Link>
        <Link className="btn" to="/">
          첫 화면
        </Link>
      </div>
    </>
  )
}
