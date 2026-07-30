import { Link } from 'react-router-dom'
import type { Confidence, Evidence, NodeBrief } from './api'

const CONF_LABEL: Record<Confidence, string> = {
  A: '원문 직접 확인',
  B: '복수 출처 또는 간접 확인',
  C: '단일 매체 출처',
  D: '미검증 또는 상충',
}

/** 확신도 배지. C·D 는 시각적으로 구분된다 — 지식베이스가 구별해 둔 것을 화면이 뭉개면 안 된다. */
export function ConfidenceBadge({ value }: { value: Confidence | null | undefined }) {
  if (!value) return null
  return (
    <span className={`conf conf-${value}`} title={CONF_LABEL[value]}>
      {value}
    </span>
  )
}

export function NodeChip({ node }: { node: NodeBrief & { missing?: boolean } }) {
  if (node.missing) return <span className="chip chip-missing">{node.id} (없음)</span>
  return (
    <Link className="chip" to={`/n/${encodeURIComponent(node.id)}`}>
      <span className="chip-type">{node.type}</span>
      {node.title}
    </Link>
  )
}

export function EvidenceList({ items }: { items?: Evidence[] }) {
  if (!items?.length) return null
  return (
    <ul className="evidence">
      {items.map((e, i) => (
        <li key={i}>
          <ConfidenceBadge value={e.confidence} />
          <Link to={`/n/${encodeURIComponent(e.doc)}`}>{e.doc}</Link>
          {e.locator && <span className="loc">{e.locator}</span>}
          {e.quote && <blockquote>{e.quote}</blockquote>}
        </li>
      ))}
    </ul>
  )
}

/** 시점 슬라이더. 전 화면의 질의에 as_of 를 주입한다 — 이 사이트의 차별 기능. */
export function AsOfControl({
  value,
  onChange,
}: {
  value: string | null
  onChange: (v: string | null) => void
}) {
  const presets = ['2019-06-21', '2020-01-01', '2022-03-25', '2024-12-30', '2026-07-30']
  return (
    <div className="asof">
      <label>
        기준 시점
        <input
          type="date"
          value={value ?? ''}
          max="2030-12-31"
          onChange={(e) => onChange(e.target.value || null)}
        />
      </label>
      <div className="asof-presets">
        {presets.map((p) => (
          <button key={p} className={value === p ? 'on' : ''} onClick={() => onChange(p)}>
            {p}
          </button>
        ))}
        <button className={value === null ? 'on' : ''} onClick={() => onChange(null)}>
          전체
        </button>
      </div>
    </div>
  )
}

export function Loading() {
  return <div className="muted">불러오는 중…</div>
}

export function ErrorBox({ error }: { error: unknown }) {
  return <div className="error">{error instanceof Error ? error.message : String(error)}</div>
}

export function Disclaimer() {
  return (
    <p className="disclaimer">
      학습·참조용이며 <strong>법률 자문이 아닙니다.</strong> 확신도 <code>C</code>·<code>D</code> 와{' '}
      <code>proposed</code> 상태는 그대로 인용하지 마십시오. 실무 적용 시 원문 재확인이 필요합니다.
    </p>
  )
}
