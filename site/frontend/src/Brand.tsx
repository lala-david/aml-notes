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
/* 이름은 질문으로, 코드는 뒤에 작게. 「L1 SEMANTIC」 을 앞세우면
   읽는 사람은 그 줄에서 멈춘다 — 코드가 뜻을 가로막는다. */
const STRATA = [
  {
    k: 'funnel',
    id: 'FUNNEL',
    name: '어디서 들어왔는가',
    desc: '자동 수집 장치. 사실 후보까지만 만들고, 확정은 사람이 한다.',
    types: ['FEED', 'RUN', 'ITEM', 'SIG', 'TASK'],
  },
  {
    k: 'kinetic',
    id: 'L3',
    name: '무엇을 바꾸는가',
    desc: '사람이 하는 일과 그 기록.',
    types: ['ACTION', 'FUNC', 'ROLE', 'ALOG'],
  },
  {
    k: 'dynamic',
    id: 'L2',
    name: '언제 그랬는가',
    desc: '언제부터 언제까지 참이었는지가 붙은 주장. 시점을 되감을 수 있는 근거.',
    types: ['FACT', 'EVT', 'STATE', 'METRIC'],
  },
  {
    k: 'semantic',
    id: 'L1',
    name: '무엇이 있는가',
    desc: '관할 · 기관 · 법령 · 조문 · 의무.',
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
