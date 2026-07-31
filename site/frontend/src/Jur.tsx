/**
 * 관할 표식 — 국기 이모지를 쓰지 않고 직접 그린다.
 *
 * 이모지는 폰트에 따라 렌더링이 갈리고 흑백으로 떨어지는 환경이 있다.
 * 여기서는 2자 코드 타일에 관할군별 색띠를 얹는다. 색은 장식이고
 * 의미는 코드가 진다 — 색만으로 구분하게 두지 않는다.
 */
const GROUP: Record<string, string> = {
  kr: 'ko', jp: 'ap', sg: 'ap', hk: 'ap', au: 'ap',
  us: 'am', eu: 'eu', gb: 'eu', ae: 'me',
  intl: 'gl', x: 'nx',
}

const NAME: Record<string, string> = {
  kr: '한국', us: '미국', eu: 'EU', gb: '영국', jp: '일본',
  sg: '싱가포르', hk: '홍콩', ae: 'UAE', au: '호주',
  intl: '국제기준', x: '무국적',
}

export function JurMark({ ns, size = 18 }: { ns: string; size?: number }) {
  const g = GROUP[ns] ?? 'nx'
  const code = ns === 'intl' ? 'IN' : ns === 'x' ? '—' : ns.toUpperCase()

  // 국제기준은 지구본 격자, 무국적은 점선 사각 — 코드 타일과 형태를 달리한다
  if (ns === 'intl') {
    return (
      <svg className={`jm jm-${g}`} width={size} height={size} viewBox="0 0 20 20" aria-label="국제기준">
        <circle cx="10" cy="10" r="8" className="jm-bg" />
        <circle cx="10" cy="10" r="8" className="jm-ring" />
        <ellipse cx="10" cy="10" rx="3.6" ry="8" className="jm-ring" />
        <path d="M2.4 7.4h15.2M2.4 12.6h15.2" className="jm-ring" />
      </svg>
    )
  }
  if (ns === 'x') {
    return (
      <svg className={`jm jm-${g}`} width={size} height={size} viewBox="0 0 20 20" aria-label="무국적">
        <rect x="2" y="2" width="16" height="16" rx="4" className="jm-dash" />
        <path d="M7 10h6" className="jm-ring" />
      </svg>
    )
  }
  return (
    <svg className={`jm jm-${g}`} width={size} height={size} viewBox="0 0 20 20" aria-label={NAME[ns] ?? ns}>
      <rect x="1.5" y="1.5" width="17" height="17" rx="4.5" className="jm-bg" />
      <rect x="1.5" y="1.5" width="17" height="4.2" rx="4.5" className="jm-band" />
      <text x="10" y="14.4" className="jm-code">{code}</text>
    </svg>
  )
}

export function JurChip({ ns, label }: { ns: string; label?: string }) {
  return (
    <span className="jurchip">
      <JurMark ns={ns} />
      {label ?? NAME[ns] ?? ns}
    </span>
  )
}

export const jurName = (ns: string) => NAME[ns] ?? ns
