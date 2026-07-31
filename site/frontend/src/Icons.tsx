/**
 * 아이콘 — 전부 직접 그린다. 이모지·아이콘 폰트·외부 라이브러리 없음.
 *
 * 규격: 20×20 viewBox · stroke 1.5 · round cap/join · currentColor.
 * 아이콘은 색을 갖지 않는다 — 부모의 텍스트 색을 그대로 따른다.
 *
 * 수를 줄였다. 네비게이션마다 아이콘을 붙이면 글자가 안 읽히고
 * "대시보드"처럼 보인다. 아이콘은 글자로 대신할 수 없는 자리에만 남긴다.
 */
type P = { size?: number; className?: string }

const box = (s?: number) => ({ width: s ?? 16, height: s ?? 16, viewBox: '0 0 20 20' })
const S = {
  fill: 'none',
  stroke: 'currentColor',
  strokeWidth: 1.5,
  strokeLinecap: 'round' as const,
  strokeLinejoin: 'round' as const,
}

/** 검색 */
export const IconSearch = ({ size, className }: P) => (
  <svg {...box(size)} className={className} aria-hidden>
    <circle cx="8.8" cy="8.8" r="5.3" {...S} />
    <path d="M12.8 12.8 17 17" {...S} />
  </svg>
)

/** 기준 시점 — 시간축 위의 표식. 시계보다 '축'이 이 제품의 은유에 맞다. */
export const IconTime = ({ size, className }: P) => (
  <svg {...box(size)} className={className} aria-hidden>
    <path d="M2.4 13.4h15.2" {...S} />
    <path d="M5.4 13.4v2.6M14.6 13.4v2.6" {...S} />
    <path d="M10 13.4V4.2" {...S} />
    <path d="M7.2 6.6 10 3.8l2.8 2.8" {...S} />
  </svg>
)

/** 진행 · 이동 */
export const IconArrow = ({ size, className }: P) => (
  <svg {...box(size)} className={className} aria-hidden>
    <path d="M3.6 10h12M11.6 5.8 15.8 10l-4.2 4.2" {...S} />
  </svg>
)

/** 외부 원문 */
export const IconExternal = ({ size, className }: P) => (
  <svg {...box(size)} className={className} aria-hidden>
    <path d="M8.6 4H4v12h12v-4.6" {...S} />
    <path d="M11.8 4h4.2v4.2M16 4l-6.6 6.6" {...S} />
  </svg>
)

/** 주의 — 면책 문구에만 쓴다 */
export const IconWarn = ({ size, className }: P) => (
  <svg {...box(size)} className={className} aria-hidden>
    <path d="M10 3.4 17.6 16.6H2.4z" {...S} />
    <path d="M10 8.2v3.2" {...S} />
    <circle cx="10" cy="13.9" r=".85" fill="currentColor" stroke="none" />
  </svg>
)

/** 확인 */
export const IconCheck = ({ size, className }: P) => (
  <svg {...box(size)} className={className} aria-hidden>
    <path d="M4 10.4 8.1 14.5 16 5.6" {...S} />
  </svg>
)

/* ── 표시 모드 ───────────────────────────────────────────────────── */

export const IconSun = ({ size, className }: P) => (
  <svg {...box(size)} className={className} aria-hidden>
    <circle cx="10" cy="10" r="3.6" {...S} />
    <path d="M10 2.6v1.8M10 15.6v1.8M2.6 10h1.8M15.6 10h1.8M4.8 4.8l1.3 1.3M13.9 13.9l1.3 1.3M15.2 4.8l-1.3 1.3M6.1 13.9l-1.3 1.3" {...S} />
  </svg>
)

export const IconMoon = ({ size, className }: P) => (
  <svg {...box(size)} className={className} aria-hidden>
    <path d="M16.2 12.1A6.8 6.8 0 0 1 7.9 3.8a6.8 6.8 0 1 0 8.3 8.3Z" {...S} />
  </svg>
)

/** 시스템 설정을 따름 — 반쪽 원 */
export const IconAuto = ({ size, className }: P) => (
  <svg {...box(size)} className={className} aria-hidden>
    <circle cx="10" cy="10" r="6.6" {...S} />
    <path d="M10 3.4a6.6 6.6 0 0 1 0 13.2Z" fill="currentColor" stroke="none" />
  </svg>
)
