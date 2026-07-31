import { useEffect, useState } from 'react'
import type { ReactNode } from 'react'
import { Link } from 'react-router-dom'
import type { Confidence, Evidence, NodeBrief } from './api'
import { IconAuto, IconMoon, IconSun, IconTime, IconWarn } from './Icons'

/* ═══ 섹션 ═══════════════════════════════════════════════════════════
   참고서의 조판: 번호 · 표제 · 방주. 제목만 반복해서 쌓지 않는다. */

export function Section({
  num,
  title,
  note,
  children,
}: {
  num?: ReactNode
  title: string
  note?: ReactNode
  children: ReactNode
}) {
  return (
    <section className="sec">
      <div className="sec-head">
        {num && <span className="sec-num">{num}</span>}
        <h2>{title}</h2>
        {note && <p className="sec-note">{note}</p>}
      </div>
      {children}
    </section>
  )
}

export function PageHead({
  title,
  lead,
  aside,
}: {
  title: string
  lead?: ReactNode
  aside?: ReactNode
}) {
  return (
    <header className="phead">
      <div>
        <h1>{title}</h1>
        {lead && <p>{lead}</p>}
      </div>
      {aside && <div className="phead-aside">{aside}</div>}
    </header>
  )
}

/* ═══ 본문 ═══════════════════════════════════════════════════════════
   KB 원문은 마크다운 강조를 쓴다. 별표를 화면에 그대로 흘리지 않는다. */

export function Rich({ text }: { text?: string | null }) {
  const t = (text ?? '').replace(/\s+$/, '')
  if (!t) return null
  return (
    <>
      {t.split(/(\*\*[^*]+\*\*)/g).map((p, i) =>
        p.startsWith('**') && p.endsWith('**') ? <strong key={i}>{p.slice(2, -2)}</strong> : p,
      )}
    </>
  )
}

/* ═══ 신뢰 표식 ══════════════════════════════════════════════════════
   확신도·출처등급은 **문자와 형태**가 1차 부호다. 색은 거들 뿐이며
   색을 못 보는 사람에게도 등급이 그대로 전달되어야 한다. */

const CONF_LABEL: Record<Confidence, string> = {
  A: '원문 직접 확인',
  B: '복수 출처 또는 간접 확인',
  C: '단일 매체 출처',
  D: '미검증 또는 상충',
}

export function ConfMark({ value }: { value: Confidence | null | undefined }) {
  if (!value) return null
  return (
    <span className={`mark mark-${value}`} title={`확신도 ${value} — ${CONF_LABEL[value]}`}>
      {value}
      <span className="sr-only"> 확신도 {CONF_LABEL[value]}</span>
    </span>
  )
}

export const confLabel = (c: Confidence) => CONF_LABEL[c]

/** 출처 등급은 서열이다 — 색조가 아니라 눈금 개수로 말한다. T1 이 가장 높다. */
export function TierMark({ tier, title }: { tier: string; title?: string }) {
  const n = Number(tier.replace(/\D/g, '')) || 5
  const filled = Math.max(1, 6 - n)
  return (
    <span className="tier" title={title ? `${tier} — ${title}` : tier}>
      {tier}
      <span className="tier-steps" aria-hidden>
        {[0, 1, 2, 3, 4].map((i) => (
          <i key={i} className={i < filled ? 'on' : ''} />
        ))}
      </span>
    </span>
  )
}

/* ═══ 노드 참조 ══════════════════════════════════════════════════════
   테두리 친 칩 대신 '타입 코드 + 제목'. 왼쪽 2px 눈금이 계층을 말한다.
   문서 어디에 놓여도 본문 흐름을 끊지 않는다. */

export function NodeRef({ node }: { node: NodeBrief & { missing?: boolean } }) {
  if (node.missing) {
    return (
      <span className="nref missing" title="이 ID 는 아직 등재되지 않았습니다">
        <span className="tcode">없음</span>
        <span className="nref-name mono">{node.id}</span>
      </span>
    )
  }
  const style = node.layer ? { ['--lc' as string]: `var(--layer-${node.layer})` } : undefined
  return (
    <Link className="nref" to={`/n/${encodeURIComponent(node.id)}`} style={style}>
      <span className="tcode">{node.type}</span>
      <span className="nref-name">{node.title}</span>
    </Link>
  )
}

/* ═══ 증거 ═══════════════════════════════════════════════════════════ */

export function EvidenceList({ items, empty }: { items?: Evidence[]; empty?: string }) {
  if (!items?.length) {
    return empty ? <p className="ev-empty">{empty}</p> : null
  }
  return (
    <ul className="ev">
      {items.map((e, i) => (
        <li key={i}>
          <div className="ev-head">
            <ConfMark value={e.confidence} />
            <Link to={`/n/${encodeURIComponent(e.doc)}`}>{e.doc}</Link>
            {e.locator && <span className="loc">{e.locator}</span>}
            {e.retrieved && <span>확인 {e.retrieved}</span>}
          </div>
          {e.quote && <blockquote>{e.quote}</blockquote>}
        </li>
      ))}
    </ul>
  )
}

/* ═══ 기준 시점 ══════════════════════════════════════════════════════
   이 사이트의 서명 기능. 화면 상단에 붙어 스크롤해도 사라지지 않는다 —
   "지금 보고 있는 것이 어느 시점의 지형인가"를 잊게 두지 않는다. */

const PRESETS: [string, string][] = [
  ['2019-06-21', 'FATF R.15'],
  ['2022-03-25', '한국 시행'],
  ['2024-12-30', 'MiCA 적용'],
]

export function AsOfControl({
  value,
  onChange,
  effect,
}: {
  value: string | null
  onChange: (v: string | null) => void
  effect?: string
}) {
  return (
    <div className="asof">
      <span className="asof-label">
        <IconTime size={14} />
        기준 시점
      </span>
      <input
        type="date"
        value={value ?? ''}
        max="2030-12-31"
        aria-label="기준 시점"
        onChange={(e) => onChange(e.target.value || null)}
      />
      <div className="seg">
        {PRESETS.map(([d, label]) => (
          <button key={d} aria-pressed={value === d} onClick={() => onChange(d)} title={d}>
            {label}
          </button>
        ))}
        <button aria-pressed={value === null} onClick={() => onChange(null)}>
          전체 기간
        </button>
      </div>
      <p className="asof-state">
        {value ? (
          <>
            <b>{value}</b> 시점에 유효했던 조문만 표시됩니다. {effect}
          </>
        ) : (
          <>기간을 제한하지 않았습니다. 날짜를 고르면 그날 시행 중이던 것만 남습니다.</>
        )}
      </p>
    </div>
  )
}

/* ═══ 상태 ═══════════════════════════════════════════════════════════ */

export function Loading({ rows = 3 }: { rows?: number }) {
  return (
    <div className="skel" aria-busy="true" aria-label="불러오는 중">
      {Array.from({ length: rows }, (_, i) => (
        <i key={i} style={{ width: `${94 - i * 13}%` }} />
      ))}
    </div>
  )
}

export function ErrorBox({ error }: { error: unknown }) {
  const msg = error instanceof Error ? error.message : String(error)
  return (
    <p className="err">
      불러오지 못했습니다 — {msg}
    </p>
  )
}

export function Empty({ children }: { children: ReactNode }) {
  return <p className="empty">{children}</p>
}

export function Count({ n, unit = '건' }: { n: number; unit?: string }) {
  return (
    <span className="count">
      {n.toLocaleString()}
      {unit}
    </span>
  )
}

/* ═══ 면책 ═══════════════════════════════════════════════════════════
   상시 노출하되 각주 자리에. 경고 상자로 화면 위쪽을 차지하면
   본문을 밀어내고, 매 페이지 반복되면 아무도 읽지 않는다. */

export function LegalNote() {
  return (
    <p className="legal">
      <IconWarn size={15} />
      <span>
        학습·참조용이며 <strong>법률 자문이 아닙니다.</strong> 확신도 <code>C</code>·<code>D</code>
        와 <code>proposed</code> 상태는 그대로 인용하지 마십시오. 실무 적용 전에는 원문을 다시
        확인해야 합니다.
      </span>
    </p>
  )
}

/* ═══ 표시 모드 ══════════════════════════════════════════════════════ */

type Mode = 'auto' | 'light' | 'dark'
const MODE_LABEL: Record<Mode, string> = { auto: '시스템', light: '밝게', dark: '어둡게' }
const NEXT: Record<Mode, Mode> = { auto: 'light', light: 'dark', dark: 'auto' }

const readMode = (): Mode => {
  try {
    const v = localStorage.getItem('theme')
    return v === 'light' || v === 'dark' ? v : 'auto'
  } catch {
    return 'auto'
  }
}

export function ThemeToggle() {
  const [mode, setMode] = useState<Mode>(readMode)

  useEffect(() => {
    const el = document.documentElement
    if (mode === 'auto') el.removeAttribute('data-theme')
    else el.setAttribute('data-theme', mode)
    try {
      if (mode === 'auto') localStorage.removeItem('theme')
      else localStorage.setItem('theme', mode)
    } catch {
      /* 저장 불가 환경은 세션 한정으로 동작한다 */
    }
  }, [mode])

  const Icon = mode === 'light' ? IconSun : mode === 'dark' ? IconMoon : IconAuto
  return (
    <button
      type="button"
      className="themebtn"
      onClick={() => setMode(NEXT[mode])}
      title={`표시 모드 — ${MODE_LABEL[mode]} (눌러서 전환)`}
      aria-label={`표시 모드 ${MODE_LABEL[mode]}. 눌러서 전환`}
    >
      <Icon size={14} />
      <span>{MODE_LABEL[mode]}</span>
    </button>
  )
}
