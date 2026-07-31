import { useState } from 'react'
import { Link, useParams, useSearchParams } from 'react-router-dom'
import { api } from './api'
import type { Confidence, Crosswalk, Lineage, NodeBrief, NodeDetail, Ontology, Stats } from './api'
import { useAsync } from './useAsync'
import {
  AsOfControl, ConfMark, Count, Empty, ErrorBox, EvidenceList, LegalNote, Loading,
  NodeRef, PageHead, Rich, Section, TierMark,
} from './components'
import { Graph } from './Graph'
import { Strata } from './Brand'
import { AsOfContrast, CrosswalkPreview, DelegationChain } from './Explain'
import { JurChip } from './Jur'
import { IconArrow, IconSearch } from './Icons'

const TRAVEL_RULE = 'OBL:x-travel-rule-originator'
const ROOT_PROV = 'PROV:kr-tfia-art5-3'

/* 노드 상세에서 「TEC · L1 명사」 를 걷어냈다. 처음 온 사람에게 계층
   번호는 아무 뜻도 아니고, 계층은 NodeRef 좌측 2px 색눈금이 이미
   조용히 말한다. 계층 이름이 필요한 곳은 /ontology 뿐이고 거기서는
   Strata 가 자기 라벨을 들고 있다. */

/** 클래스 코드 → 한글. 화면에 나가는 이름은 코드가 아니라 이쪽이다. */
const CLASS_KO: Record<string, string> = {
  ACT: '위협행위자', ACTION: '액션', ALOG: '액션 로그', ASSET: '가상자산',
  CAP: '역량', CASE: '판례·소송', CHAIN: '블록체인', CONCEPT: '개념',
  CTL: '통제', DOC: '문서', ENF: '집행조치', ERA: '국면', EVT: '사건',
  FACT: '사실', FEED: '수집 피드', FUNC: '함수', INC: '사고',
  IND: '지표', ITEM: '원시 항목', JUR: '관할', METRIC: '관측 수치',
  OBL: '의무', ORG: '기관', PROD: '분석 산출물', PROTO: '프로토콜·서비스',
  PROV: '조문', REG: '규범', RISK: '위험요인', ROLE: '역할',
  RUN: '수집 실행', SIG: '변화 신호', SRC: '출처', STATE: '구간 상태',
  TASK: '검증 과제', TEC: '기법', TYP: '유형론', VASP: '가상자산사업자',
  VEND: '솔루션 공급자',
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

/**
 * 속성 이름 한글. 화면에 PARENT_REG · CITATION_PATH 가 그대로 나오면
 * 방문자는 그 줄을 읽을 수 없다. 없는 키는 코드를 그대로 쓴다 —
 * 모르는 것을 아는 척 옮기지 않는다.
 */
const PROP_KO: Record<string, string> = {
  parent_reg: '소속 법령', citation_path: '조문 위치', heading: '조문 제목',
  language: '언어', tier: '출처 등급', tier_basis: '등급 근거',
  publisher_kind: '발행 주체', base_url: '주소', paywall: '유료 여부',
  website: '웹사이트', jurisdiction: '관할', org_kind: '기관 종류',
  reg_kind: '규범 종류', binding: '구속력', citation: '인용 표기',
  src: '출처', url: '주소', accessed: '확인일', doc_kind: '문서 종류',
  published: '발행일', translation: '번역본 여부',
  iso: 'ISO 코드', legal_family: '법계', fatf_member: 'FATF 회원',
  fatf_style_body: '지역기구',
  signal_type: '신호 유형', fp_risk: '오탐 위험', rule_sketch: '판별 규칙',
  parent_typology: '상위 유형', detectability: '탐지 난이도', stage: '단계',
  action_kind: '액션 종류', requires_proposal: '제안 필요', is_agent: '에이전트',
  reversible_by: '되돌리는 액션', vend_kind: '공급자 종류', hq: '본사',
  implements_obligation: '이행 의무', definition_ko: '정의(국문)',
  definition_en: '정의(영문)', contested: '쟁점 여부', ctl_kind: '통제 종류',
  automatable: '자동화 가능', maturity: '성숙도', track: '분류',
  evt_kind: '사건 종류', occurred_on: '발생일', announced_on: '공표일',
  date_precision: '날짜 정밀도', impact: '영향', significance: '중요도',
  func_kind: '함수 종류', output: '산출', deterministic: '결정적',
  implementation: '구현', output_path: '산출 경로',
  obl_kind: '의무 종류', actor_class: '수범자', trigger: '발동 조건',
  text_orig: '원문', license: '이용 허락', attribution: '출처 표시',
  content_hash: '내용 해시', snapshot_path: '보존본 경로',
}

/** 기계 열거값 → 사람 말. threshold_abolished 는 읽을 수 있는 말이 아니다. */
const VALUE_KO: Record<string, string> = {
  threshold_abolished: '기준금액 폐지',
  proposed: '입법 예고 단계 (공포 전)',
  undetermined: '미확정',
  partial: '일부',
  full_history: '전체 이력',
  true: '예',
  false: '아니오',
}

/** 사실의 값. 큰 수는 자릿점을 찍는다 — 1000000 은 눈으로 못 읽는다. */
function factValue(v: unknown): string {
  if (typeof v === 'number') return v.toLocaleString('ko-KR')
  const s = String(v)
  if (VALUE_KO[s]) return VALUE_KO[s]
  if (/^\d{4,}$/.test(s)) return Number(s).toLocaleString('ko-KR')
  return s
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
        <p className="kicker">한국 · FATF · EU 가상자산 자금세탁방지 규제</p>
        <h1>100만원. 이 숫자는 법률 어디에도 없습니다.</h1>
        {/* 점선 친 낱말은 눌러서 뜻을 볼 수 있다. Rich 가 용어를 잡아 준다. */}
        <p className="lede-body">
          <Rich text="가상자산을 100만원 넘게 보내면 받는 거래소에 보내는 사람이 누구인지를 함께 넘겨야 합니다. 그런데 **특금법 본문에는 이 금액이 없습니다.** 법률은 상한만 긋고 위임했고, 실제 기준은 두 단계 아래 시행령에 있습니다." />
        </p>
      </div>

      {/* 표제가 심은 질문을 그대로 문으로 만든다. 기능 이름(위임 계보·크로스워크)이
          아니라 방금 읽은 질문으로 적는다 — 처음 온 사람은 기능 이름을 모른다. */}
      <div className="entry">
        <Link className="btn btn-key" to={`/lineage/${encodeURIComponent(ROOT_PROV)}`}>
          그 숫자는 어느 조문에 있나
          <IconArrow size={14} />
        </Link>
        <Link className="btn" to={`/obl/${encodeURIComponent(TRAVEL_RULE)}`}>
          나라마다 기준이 얼마인가
        </Link>
        <Link className="btn" to="/search">
          조문 · 기관 찾아보기
        </Link>
      </div>

      <Section num="§ 01" title="위임은 어디까지 내려가는가" note="조문 셋을 따라가면 숫자가 나옵니다">
        <DelegationChain />
      </Section>

      {/* 재고 통계는 이야기 뒤에 와야 근거로 읽힌다. 앞에 두면 처음 온 사람이
          아무것도 할 수 없는 숫자 다섯을 두 번째로 읽는다. */}
      {s.data && <Census stats={s.data} />}

      <Section num="§ 02" title="같은 의무, 다른 조문">
        <p className="sec-lead">
          <Rich text="트래블룰이라는 하나의 의무를 나라마다 다른 조문이 정하고, 기준금액도 제각각입니다." />
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

      <Section num="§ 03" title="2021년에는 어땠는가">
        <p className="sec-lead">
          같은 질문을 두 시점에 던진 결과입니다. 그날 시행되지 않았던 조문은 답에서 빠집니다.
        </p>
        {cw.data && <AsOfContrast rows={cw.data.rows} />}
      </Section>

      {/* 곁가지다. 본줄기와 같은 무게를 주지 않는다. */}
      <Section num="§ 04" title="지식을 담는 세 겹" minor>
        <p className="sec-lead">
          무엇이 존재하는가(명사), 언제 참이었는가(시간), 무엇을 바꿀 수 있는가(동사).
        </p>
        <div className="btnrow gap-top">
          <Link className="btn" to="/ontology">
            분류 체계 보기
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
  // 확신도 분포(A~D 막대)는 뺐다 — 처음 온 사람이 두 번째로 읽는 것이
  // KB 품질 지표일 이유가 없다. /ontology 와 /facts 필터에 그대로 있다.
  return (
    <dl className="census">
      {cells.map(([k, v, n]) => (
        <div className="census-cell" key={k}>
          <dt>{k}</dt>
          <dd>{v.toLocaleString()}</dd>
          <small>{n}</small>
        </div>
      ))}
    </dl>
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
        lead="같은 의무를 나라마다 어느 조문이 정하는지 나란히 봅니다. 기준 시점을 바꾸면 그날 시행 중이던 조문만 남습니다."
      />
      {loading && <Loading rows={3} />}
      {error ? <ErrorBox error={error} /> : null}
      {data && !data.items.length && <Empty>등재된 의무가 없습니다.</Empty>}
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
  // 등재 장부용 날짜. TEC 노드에서는 속성 5줄 중 3줄이 이것이었다.
  // 언제 등재했는지는 방문자가 아니라 관리자의 관심사다.
  'created_at', 'updated_at', 'review_due',
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

  // 시간에 결속된 것이 하나도 없는 노드에서는 날짜를 무엇으로 바꿔도
  // 화면이 변하지 않는다. 그런 노드에 조작기를 제목 위에 세워 둘 이유가 없다.
  const temporal =
    at != null ||
    n.facts.some((f) => f.valid_from || f.valid_to) ||
    [...n.edges_out, ...n.edges_in].some((e) => e.valid_from || e.valid_to)

  return (
    <>
      <div className="with-rail">
        <div>
          <header className="nodehead">
            <span className="label">{CLASS_KO[n.type] ?? n.type}</span>
            <h1>{n.title}</h1>
            <code className="nid">{n.id}</code>
            {n.summary && <p className="nodehead-sum"><Rich text={n.summary} /></p>}
          </header>

          {temporal && (
            <AsOfControl value={at} onChange={setAt} effect="그 시점에 유효했던 관계·사실만 남습니다." />
          )}

          {n.evidence?.length ? (
            <Section title="원문 증거" note={<Count n={n.evidence.length} />}>
              <EvidenceList items={n.evidence} />
            </Section>
          ) : null}

          {n.facts.length > 0 && (
            <Section title="사실" note={<Count n={n.facts.length} />}>
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
                        /* 값이 먼저, 기계 이름은 뒤에 작게.
                           travel_rule_threshold = 1000000 KRW 는 사람이 읽는
                           자리에 데이터베이스 열 이름을 세워 둔 것이었다. */
                        <p className="rec-kv">
                          <b>{factValue(f.value)}</b>
                          {f.unit ? ` ${f.unit}` : ''}
                          {f.valid_from && (
                            <span className="dim"> · {f.valid_from}부터 {f.valid_to ?? '현재까지'}</span>
                          )}
                          <code title="기계 판독용 속성명">{f.attribute}</code>
                        </p>
                      )}
                      {f.note && (
                        <p className="rec-note">
                          {/* CTR:00004 로 시작하는 메모가 있다. 설명 없는
                              내부 ID 는 막다른 길이므로 검토 화면으로 잇는다. */}
                          {/^CTR:\d+/.test(f.note) && (
                            <Link to="/audit?tab=conflict" className="ctr-link">
                              상충 기록
                            </Link>
                          )}
                          <Rich text={f.note.replace(/^CTR:\d+\s*—\s*/, '')} />
                        </p>
                      )}
                      <EvidenceList items={f.evidence} />
                    </div>
                  </li>
                ))}
              </ul>
            </Section>
          )}

          <Section
            title="관계"
            note={<Count n={n.edges_out.length + n.edges_in.length} unit="개" />}
          >
            <EdgeList title="나가는 관계" edges={n.edges_out} />
            <EdgeList title="들어오는 관계" edges={n.edges_in} />
            {!n.edges_out.length && !n.edges_in.length && <Empty>연결된 노드가 없습니다.</Empty>}
          </Section>

          <NeighborGraph id={n.id} />

          {/* 245개 중 214개에 있다. 즉 예외가 아니라 기본값인데, 내용은
              「임계값 한정자를 옮겼다」 「OC 발급 후 채울 것」 같은 담당자
              작업 기록이다. 지우지는 않는다 — 판단의 흔적을 남기는 것이
              이 저장소의 원칙이다. 다만 접어서 원하는 사람만 연다. */}
          {n.curator_note && (
            <details className="disc gap-top">
              <summary>등재 · 정정 기록</summary>
              <pre className="note"><Rich text={n.curator_note} /></pre>
              <p className="rail-path">{n.path}</p>
            </details>
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
                    <dt title={k}>{PROP_KO[k] ?? k}</dt>
                    <dd><SpecValue value={v} /></dd>
                  </div>
                ))}
              </dl>
            </div>
          )}
          {/* 원본 파일 경로는 「등재 · 정정 기록」 안으로 옮겼다.
              저장소 경로는 방문자용 정보가 아니다. */}
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
            {/* 한글이 1차, 코드는 작게 뒤에. PART_OF 만 있으면 처음 온
                사람은 이 행이 무슨 관계인지 읽을 수 없다. */}
            <span className="pred">
              {e.predicate_ko ?? e.predicate}
              {e.predicate_ko && <code>{e.predicate}</code>}
            </span>
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
      minor
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
      {/* 그래프 하나에 설명 세 줄이 붙어 있었다. 눌러 보면 아는 것을
          글로 적지 않는다 — 범례만 남긴다. */}
      <Graph nodes={data.nodes} links={data.links} height={380} focusId={id} />
    </Section>
  )
}

/* ═══════════════════════════════════════════════════════════════════════
   탐색 — 결과 + 타입 패싯
   ═══════════════════════════════════════════════════════════════════════ */

/**
 * 아무 조건 없이 들어왔을 때 보여줄 시작점.
 *
 * 그냥 두면 245건 중 200건이 쏟아지는데, 그 절반이 IND·TEC(지표·기법)라
 * 홈이 조문 이야기를 해 놓고 첫 목록은 「필체인」 「계단식 감소 선형 체인」
 * 이 된다. 약속과 재고가 어긋난다.
 */
const SEED_NODES = [
  'PROV:kr-tfia-art5-3', 'OBL:x-travel-rule-originator',
  'REG:kr-tfia', 'REG:intl-fatf-r15',
  'JUR:kr', 'ORG:kr-fsc',
]

const FACET_HEAD = 8

export function SearchPage() {
  const [sp, setSp] = useSearchParams()
  const q = sp.get('q') ?? ''
  const type = sp.get('type') ?? ''
  const showAll = sp.has('all')
  const blank = !q && !type && !showAll
  const [moreFacets, setMoreFacets] = useState(false)
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
  // 고른 클래스가 뒤쪽에 있으면 접혀 사라지면 안 된다.
  const selectedHidden = type ? types.findIndex(([c]) => c === type) >= FACET_HEAD : false
  const shownTypes = moreFacets || selectedHidden ? types : types.slice(0, FACET_HEAD)

  return (
    <>
      <PageHead title="찾아보기" lead="제목 · 요약 · ID 로 찾습니다." />

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
          {blank && data ? (
            <div className="seed">
              <h4>여기서 시작</h4>
              <ul className="ledger">
                {SEED_NODES.map((sid) => {
                  const node = data.items.find((x) => x.id === sid)
                  return node ? <li key={sid}><NodeRef node={node} /></li> : null
                })}
              </ul>
              <button className="btn btn-quiet" onClick={() => setParam('all', '1')}>
                전체 {data.total}건 보기
              </button>
            </div>
          ) : null}
          {loading && <Loading rows={5} />}
          {error ? <ErrorBox error={error} /> : null}
          {!blank && data && !data.items.length && (
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
          {!blank && data && data.items.length > 0 && (
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
              {shownTypes.map(([code, n]) => (
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
            {/* 한 자릿수 클래스가 절반이라 다 펴면 레일이 화면 높이를 먹는다. */}
            {types.length > FACET_HEAD && (
              <button className="btn btn-quiet facet-more" onClick={() => setMoreFacets((v) => !v)}>
                {moreFacets ? '접기' : `나머지 ${types.length - FACET_HEAD}개`}
              </button>
            )}
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
        title="사실"
        lead="모든 사실은 원문 인용까지 추적됩니다."
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
  // 이 화면은 체계 자체를 보는 곳이라 구조 어휘가 정당하다. 다만
  // 「L1 SEMANTIC」 처럼 코드를 앞세우지 않고 질문을 앞세운다.
  const layers: [string, string][] = [
    ['semantic', '무엇이 있는가 — 관할 · 기관 · 법령 · 조문 · 의무'],
    ['dynamic', '언제 그랬는가 — 시점이 붙은 사실과 사건'],
    ['kinetic', '무엇을 바꾸는가 — 사람이 하는 일과 그 기록'],
    ['funnel', '어디서 들어왔는가 — 자동 수집 장치'],
  ]

  return (
    <>
      <PageHead
        title={`분류 체계 v${o.version}`}
        lead="등재할 수 있는 것의 종류와, 그것들이 맺을 수 있는 관계의 정의입니다."
        aside={
          <span className="count">
            종류 {Object.keys(o.classes).length} · 관계 {Object.keys(o.predicates).length}
          </span>
        }
      />

      <Section num="§ 01" title="세 겹" note="색과 세로 위치로도 구분됩니다">
        <Strata compact />
      </Section>

      <Section num="§ 02" title="등재할 수 있는 것" note={<Count n={Object.keys(o.classes).length} unit="개" />}>
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

      <Section num="§ 03" title="관계 종류" note={<Count n={Object.keys(o.predicates).length} unit="개" />}>
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
