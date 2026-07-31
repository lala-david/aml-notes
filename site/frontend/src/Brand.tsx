/**
 * 마크와 계층 도해.
 *
 * 마크는 이 지식베이스가 실제로 하는 일 하나를 그린다 —
 * 상위 규범에서 하위 규범으로 **내려가는 위임**. 세 개의 층(막대)이 아래로
 * 갈수록 짧아지고(구체화), 각 층의 끝점을 잇는 사선이 그 경로다.
 * 색은 계층 3색 토큰을 그대로 쓴다. 방패·자물쇠 같은 관용 도상은 쓰지 않는다.
 */
export function Mark({ size = 22 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" aria-hidden>
      <path className="mk-link" d="M20.4 6.2 15.2 12.1 10 18" />
      <rect className="mk-l1" x="3" y="5" width="14.6" height="2.4" rx="1.2" />
      <rect className="mk-l2" x="3" y="10.9" width="9.4" height="2.4" rx="1.2" />
      <rect className="mk-l3" x="3" y="16.8" width="4.6" height="2.4" rx="1.2" />
      <circle className="mk-l1" cx="20.4" cy="6.2" r="1.75" />
      <circle className="mk-l2" cx="15.2" cy="12.1" r="1.75" />
      <circle className="mk-l3" cx="10" cy="18" r="1.75" />
    </svg>
  )
}

/**
 * 계층 도해 — 지층 단면.
 *
 * 카드 네 장을 나열하는 대신 하나의 단면으로 읽히게 한다. 각 층은 색 눈금
 * 하나만 갖고, 나머지는 전부 무채색이다. Funnel 은 층이 아니므로 회색이며
 * 맨 위(유입)에 둔다.
 */
const STRATA = [
  {
    k: 'funnel',
    id: 'FUNNEL',
    name: '유입 — 계층이 아니다',
    desc: '수집 파이프라인. 사실 후보까지만 만든다.',
    types: ['FEED', 'RUN', 'ITEM', 'SIG', 'TASK'],
  },
  {
    k: 'kinetic',
    id: 'L3 KINETIC',
    name: '동사 — 무엇을 바꾸는가',
    desc: '실행·역할·기록.',
    types: ['ACTION', 'FUNC', 'ROLE', 'ALOG'],
  },
  {
    k: 'dynamic',
    id: 'L2 DYNAMIC',
    name: '시간 — 언제 참이었는가',
    desc: '유효기간이 붙은 주장. 시점 질의의 근거.',
    types: ['FACT', 'EVT', 'STATE', 'METRIC'],
  },
  {
    k: 'semantic',
    id: 'L1 SEMANTIC',
    name: '명사 — 무엇이 존재하는가',
    desc: '관할·기관·법령·조문·의무.',
    types: ['JUR', 'ORG', 'REG', 'PROV', 'OBL', 'CTL'],
  },
]

export function Strata({ compact = false }: { compact?: boolean }) {
  return (
    <div className="strata">
      {STRATA.map((s) => (
        <div key={s.k} className="stratum" style={{ ['--c' as string]: `var(--layer-${s.k})` }}>
          <span className="stratum-tick" aria-hidden />
          <div className="stratum-id">
            {s.id}
            <small>{s.name}</small>
          </div>
          <div className="stratum-types">
            {!compact && <p className="stratum-desc">{s.desc}</p>}
            {s.types.map((t) => (
              <span key={t}>{t}</span>
            ))}
          </div>
        </div>
      ))}
    </div>
  )
}
