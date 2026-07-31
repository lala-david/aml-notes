/**
 * 시각 토큰 — 색은 역할로 배정한다.
 *
 * 계층 3색(blue·orange·aqua)은 all-pairs 검증 통과.
 *   light  CVD ΔE 9.2 · normal ΔE 24.0
 *   dark   CVD ΔE 9.4 · normal ΔE 20.9
 * funnel 은 온톨로지 계층이 아니므로 중립 회색이다 — 색을 아끼는 게 아니라 의미가 그렇다.
 *
 * 그래프는 모든 노드가 서로 인접할 수 있으므로 색만으로 구분하지 않는다.
 * 계층 = 색, 클래스군 = 형태. 이중 부호화가 CVD 대비의 안전장치다.
 */

export type Layer = 'semantic' | 'dynamic' | 'kinetic' | 'funnel'

/* 계층 색의 실제 정의는 App.css 의 --layer-* 하나뿐이다.
   여기에 값을 복제해 두면 두 곳이 말없이 어긋난다. */

export const LAYER_LABEL: Record<Layer, string> = {
  semantic: 'L1 의미 · 명사',
  dynamic: 'L2 동적 · 시간',
  kinetic: 'L3 운동 · 동사',
  funnel: 'Funnel · 유입',
}

/** 노드 형태 — 계층 색의 보조 부호화. */
export type Shape = 'circle' | 'square' | 'diamond' | 'hex' | 'triangle'

const SHAPE_BY_TYPE: Record<string, Shape> = {
  // 규범 축 — 사각형 계열 (제도는 각지게)
  JUR: 'hex', ORG: 'hex',
  REG: 'square', PROV: 'square',
  OBL: 'diamond', CTL: 'diamond',
  // 위협 축 — 삼각형 (경고)
  RISK: 'triangle', TYP: 'triangle', TEC: 'triangle', IND: 'triangle',
  // 증거 축 — 원
  SRC: 'circle', DOC: 'circle', FACT: 'circle', EVT: 'circle',
  // 실행 축 — 다이아
  ACTION: 'diamond', FUNC: 'diamond', ROLE: 'hex',
}

export const shapeFor = (type: string): Shape => SHAPE_BY_TYPE[type] ?? 'circle'

/** 노드 반지름 — 중요도(연결 수)에 따라 커진다. */
export const radiusFor = (degree: number) => 5 + Math.min(9, Math.sqrt(degree) * 2.6)

/** SVG 형태 path — 모두 중심 (0,0) 기준. */
export function shapePath(shape: Shape, r: number): string {
  switch (shape) {
    case 'square': {
      const a = r * 0.9
      return `M${-a},${-a}h${a * 2}v${a * 2}h${-a * 2}z`
    }
    case 'diamond':
      return `M0,${-r * 1.2}L${r * 1.2},0L0,${r * 1.2}L${-r * 1.2},0z`
    case 'triangle': {
      const h = r * 1.35
      return `M0,${-h}L${h * 0.92},${h * 0.62}L${-h * 0.92},${h * 0.62}z`
    }
    case 'hex': {
      const pts = Array.from({ length: 6 }, (_, i) => {
        const a = (Math.PI / 3) * i - Math.PI / 2
        return `${(r * 1.1 * Math.cos(a)).toFixed(2)},${(r * 1.1 * Math.sin(a)).toFixed(2)}`
      })
      return `M${pts.join('L')}z`
    }
    default:
      return ''
  }
}
