import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  forceCenter, forceCollide, forceLink, forceManyBody, forceSimulation, forceX, forceY,
} from 'd3-force'
import type { SimulationLinkDatum, SimulationNodeDatum } from 'd3-force'
import { LAYER_LABEL, radiusFor, shapeFor, shapePath } from './theme'
import type { Layer } from './theme'

export type GraphNode = { id: string; type: string; layer: string; title: string }
export type GraphLink = { source: string; target: string; predicate: string }

type SimNode = GraphNode & SimulationNodeDatum & { deg: number; r: number }
type SimLink = SimulationLinkDatum<SimNode> & { predicate: string }

const LAYERS: Layer[] = ['semantic', 'dynamic', 'kinetic', 'funnel']

export function Graph({
  nodes,
  links,
  height = 520,
  focusId,
}: {
  nodes: GraphNode[]
  links: GraphLink[]
  height?: number
  focusId?: string
}) {
  const nav = useNavigate()
  const wrap = useRef<HTMLDivElement>(null)
  const [w, setW] = useState(900)
  const [hover, setHover] = useState<string | null>(null)
  const [muted, setMuted] = useState<Set<Layer>>(new Set())
  const [view, setView] = useState({ k: 1, x: 0, y: 0 })

  useEffect(() => {
    if (!wrap.current) return
    const ro = new ResizeObserver(([e]) => setW(e.contentRect.width))
    ro.observe(wrap.current)
    return () => ro.disconnect()
  }, [])

  const { simNodes, simLinks } = useMemo(() => {
    const deg = new Map<string, number>()
    for (const l of links) {
      deg.set(l.source, (deg.get(l.source) ?? 0) + 1)
      deg.set(l.target, (deg.get(l.target) ?? 0) + 1)
    }
    const ns: SimNode[] = nodes.map((n, i) => {
      const d = deg.get(n.id) ?? 0
      const a = (i / Math.max(1, nodes.length)) * Math.PI * 2
      return { ...n, deg: d, r: radiusFor(d), x: 450 + Math.cos(a) * 190, y: 260 + Math.sin(a) * 150 }
    })
    const ids = new Set(ns.map((n) => n.id))
    const ls: SimLink[] = links
      .filter((l) => ids.has(l.source) && ids.has(l.target))
      .map((l) => ({ source: l.source, target: l.target, predicate: l.predicate }))
    return { simNodes: ns, simLinks: ls }
  }, [nodes, links])

  // 레이아웃을 **동기적으로** 확정한다.
  //  · rAF 애니메이션에 의존하면 탭이 백그라운드일 때 한 틱도 굴지 않는다.
  //  · 노드가 날아다니는 연출은 그래프를 불안정해 보이게 한다. 처음부터 정돈된 상태로 보여준다.
  //  · 매 틱 리렌더가 없으므로 렌더러가 멈출 위험도 사라진다.
  const laid = useMemo(() => {
    if (!simNodes.length) return { nodes: simNodes, links: simLinks }
    const sim = forceSimulation<SimNode>(simNodes)
      .force('link', forceLink<SimNode, SimLink>(simLinks).id((d) => d.id).distance(74).strength(0.35))
      .force('charge', forceManyBody().strength(-280))
      .force('collide', forceCollide<SimNode>((d) => d.r + 8))
      .force('center', forceCenter(w / 2, height / 2))
      // 계층을 세로 밴드로 — 색만이 아니라 위치로도 계층이 읽힌다
      .force('y', forceY<SimNode>((d) => {
        const i = LAYERS.indexOf(d.layer as Layer)
        return height * (0.2 + (i < 0 ? 1.5 : i) * 0.2)
      }).strength(0.2))
      .force('x', forceX(w / 2).strength(0.035))
      .stop()

    const n = Math.ceil(Math.log(sim.alphaMin()) / Math.log(1 - sim.alphaDecay()))
    for (let i = 0; i < n; i++) sim.tick()
    return { nodes: simNodes, links: simLinks }
  }, [simNodes, simLinks, w, height])

  const onWheel = useCallback((e: React.WheelEvent) => {
    e.preventDefault()
    setView((v) => ({ ...v, k: Math.min(3, Math.max(0.4, v.k * (e.deltaY < 0 ? 1.12 : 0.89))) }))
  }, [])

  const drag = useRef<{ x: number; y: number; vx: number; vy: number } | null>(null)

  const neighborOf = useMemo(() => {
    if (!hover) return null
    const s = new Set<string>([hover])
    for (const l of simLinks) {
      const a = typeof l.source === 'object' ? (l.source as SimNode).id : String(l.source)
      const b = typeof l.target === 'object' ? (l.target as SimNode).id : String(l.target)
      if (a === hover) s.add(b)
      if (b === hover) s.add(a)
    }
    return s
  }, [hover, simLinks])

  const byId = useMemo(() => new Map(simNodes.map((n) => [n.id, n])), [simNodes])

  const isMuted = (n: SimNode) =>
    muted.has(n.layer as Layer) || (neighborOf ? !neighborOf.has(n.id) : false)

  return (
    <div className="graph" ref={wrap}>
      <div className="graph-legend">
        {LAYERS.map((l) => (
          <button
            key={l}
            className={`lg ${muted.has(l) ? 'off' : ''}`}
            onClick={() =>
              setMuted((m) => {
                const n = new Set(m)
                n.has(l) ? n.delete(l) : n.add(l)
                return n
              })
            }
          >
            <span className="lg-dot" style={{ background: `var(--layer-${l})` }} />
            {LAYER_LABEL[l]}
          </button>
        ))}
        <span className="graph-hint">휠 확대 · 드래그 이동 · 노드 클릭</span>
      </div>

      <svg
        width={w}
        height={height}
        onWheel={onWheel}
        onPointerDown={(e) => {
          drag.current = { x: e.clientX, y: e.clientY, vx: view.x, vy: view.y }
          ;(e.target as Element).setPointerCapture?.(e.pointerId)
        }}
        onPointerMove={(e) => {
          if (!drag.current) return
          setView((v) => ({
            ...v,
            x: drag.current!.vx + (e.clientX - drag.current!.x),
            y: drag.current!.vy + (e.clientY - drag.current!.y),
          }))
        }}
        onPointerUp={() => (drag.current = null)}
        className="graph-svg"
      >
        <defs>
          <marker id="arw" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="5" markerHeight="5" orient="auto">
            <path d="M0,0 L8,4 L0,8 z" fill="var(--edge)" />
          </marker>
          <filter id="soft" x="-40%" y="-40%" width="180%" height="180%">
            <feDropShadow dx="0" dy="1.5" stdDeviation="2.5" floodOpacity="0.16" />
          </filter>
        </defs>

        <g transform={`translate(${view.x},${view.y}) scale(${view.k})`}>
          <g className="edges">
            {laid.links.map((l, i) => {
              // 첫 렌더에서는 source/target 이 아직 문자열이다 (d3 가 시뮬레이션 시작 시 객체로 바꾼다).
              // null 을 반환하면 DOM 에 line 이 안 생겨 rAF 갱신 대상이 사라진다 — 항상 그린다.
              const sid = typeof l.source === 'object' ? (l.source as SimNode).id : String(l.source)
              const tid = typeof l.target === 'object' ? (l.target as SimNode).id : String(l.target)
              const s = byId.get(sid)
              const tg = byId.get(tid)
              const dim = neighborOf ? !(neighborOf.has(sid) && neighborOf.has(tid)) : false
              return (
                <line
                  key={`${sid}|${tid}|${i}`}
                  x1={s?.x ?? 0} y1={s?.y ?? 0} x2={tg?.x ?? 0} y2={tg?.y ?? 0}
                  className={`edge ${dim ? 'dim' : ''}`}
                  markerEnd="url(#arw)"
                />
              )
            })}
          </g>

          <g className="nodes">
            {laid.nodes.map((n) => {
              if (n.x == null || n.y == null) return null
              const dim = isMuted(n)
              const shape = shapeFor(n.type)
              const focus = n.id === focusId
              return (
                <g
                  key={n.id}
                  data-id={n.id}
                  transform={`translate(${n.x},${n.y})`}
                  className={`gnode ${dim ? 'dim' : ''} ${focus ? 'focus' : ''}`}
                  onPointerEnter={() => setHover(n.id)}
                  onPointerLeave={() => setHover(null)}
                  onClick={() => nav(`/n/${encodeURIComponent(n.id)}`)}
                >
                  {focus && <circle r={n.r + 8} className="focus-ring" />}
                  {shape === 'circle' ? (
                    <circle r={n.r} style={{ fill: `var(--layer-${n.layer})` }} filter="url(#soft)" />
                  ) : (
                    <path
                      d={shapePath(shape, n.r)}
                      style={{ fill: `var(--layer-${n.layer})` }}
                      filter="url(#soft)"
                    />
                  )}
                  {(hover === n.id || focus || n.deg >= 6) && (
                    <text y={-n.r - 8} className="glabel">
                      {n.title.length > 22 ? n.title.slice(0, 21) + '…' : n.title}
                    </text>
                  )}
                </g>
              )
            })}
          </g>
        </g>
      </svg>
    </div>
  )
}
