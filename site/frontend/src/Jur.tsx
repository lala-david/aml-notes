/**
 * 관할 표식 — 국기 이모지를 쓰지 않고 직접 그린다.
 *
 * 이모지는 폰트에 따라 렌더링이 갈리고 흑백으로 떨어지는 환경이 있다.
 *
 * 색은 쓰지 않는다. 이전에는 관할군 7색이었는데 색맹 검증에서 네 항목이
 * 떨어졌다 — 중동 #b07b12 와 미주 #eb6834 가 ΔE 2.1(protan), 무국적과
 * 국제기준은 둘 다 무채라 채도 바닥 미달. 애초에 의미는 2자 코드가
 * 지고 있었으므로, 검증에 걸리는 색축을 떼는 것이 정직하다.
 *
 * 대신 명도와 형태로 가른다 — 한국은 채운 타일(이 저장소의 기준 관할),
 * 다른 나라는 테두리 타일, 국제기준은 지구본, 무국적은 점선. 색조가
 * 아니므로 흑백 인쇄·색맹·강제 대비 모드에서 그대로 살아남는다.
 */
const NAME: Record<string, string> = {
  kr: '한국', us: '미국', eu: 'EU', gb: '영국', jp: '일본',
  sg: '싱가포르', hk: '홍콩', ae: 'UAE', au: '호주',
  intl: '국제기준', x: '무국적',
}

export function JurMark({ ns, size = 18 }: { ns: string; size?: number }) {
  // 국제기준은 지구본 격자, 무국적은 점선 사각 — 코드 타일과 형태를 달리한다
  if (ns === 'intl') {
    return (
      <svg className="jm" width={size} height={size} viewBox="0 0 20 20" aria-label="국제기준">
        <circle cx="10" cy="10" r="8" className="jm-ring" />
        <ellipse cx="10" cy="10" rx="3.6" ry="8" className="jm-ring" />
        <path d="M2.4 7.4h15.2M2.4 12.6h15.2" className="jm-ring" />
      </svg>
    )
  }
  if (ns === 'x') {
    return (
      <svg className="jm" width={size} height={size} viewBox="0 0 20 20" aria-label="무국적">
        <rect x="2" y="2" width="16" height="16" rx="4" className="jm-dash" />
        <path d="M7 10h6" className="jm-ring" />
      </svg>
    )
  }
  const home = ns === 'kr'
  return (
    <svg
      className={home ? 'jm jm-home' : 'jm'}
      width={size}
      height={size}
      viewBox="0 0 20 20"
      aria-label={NAME[ns] ?? ns}
    >
      <rect x="1.5" y="1.5" width="17" height="17" rx="3" className={home ? 'jm-fill' : 'jm-tile'} />
      <text x="10" y="13.5" className="jm-code">{ns.toUpperCase()}</text>
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
