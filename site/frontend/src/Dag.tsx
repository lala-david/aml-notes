import { useMemo } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  Background, BackgroundVariant, Controls, Handle, Position,
  ReactFlow, ReactFlowProvider, type Edge, type Node, type NodeProps,
} from '@xyflow/react'
import dagre from '@dagrejs/dagre'
import '@xyflow/react/dist/style.css'

/**
 * 계층 DAG — React Flow + dagre.
 *
 * 위임 계보는 방향이 있는 사슬이므로 힘기반 배치가 맞지 않는다. 단계를
 * 열로 고정하면 "어디까지 내려가는가"가 배치 자체로 읽힌다.
 * 배치 계산은 dagre 가, 상호작용(확대·이동·선택)은 React Flow 가 맡는다.
 *
 * 겉모습은 라이브러리 기본값을 쓰지 않는다 — 이 사이트의 색·활자 토큰으로
 * 다시 칠한다(App.css `.rf` 절). 라이브러리를 쓰되 라이브러리처럼 보이지
 * 않게 하는 것이 목적이다.
 */

export type DagNode = {
  id: string
  /** 클래스 한글명 — 상자 위 작은 줄 */
  type: string
  layer: string
  title: string
  /** 상자 아래 작은 줄. 건수 같은 부가 수치. */
  note?: string | null
  /** 사슬의 끝. 굵게 그린다. */
  terminal?: boolean
}

export type DagEdge = {
  from: string
  to: string
  /** 관계 이름 */
  label?: string | null
  /** 그 관계에 붙은 값(임계값 등). 조문이 아니라 관계가 가진 수치다. */
  value?: string | null
  confidence?: string | null
}

const W = 196
const H = 74
/** 축 도해처럼 이름과 건수만 필요한 경우. 6칸이 한 화면에 들어간다. */
const CW = 132
const CH = 56

type KbData = {
  kind: string
  title: string
  note?: string | null
  layer: string
  terminal?: boolean
  compact?: boolean
}

function KbNode({ data }: NodeProps<Node<KbData>>) {
  return (
    <div className={`kbn${data.terminal ? ' term' : ''}${data.compact ? ' compact' : ''}`}>
      <Handle type="target" position={Position.Left} />
      <span className="kbn-bar" style={{ background: `var(--layer-${data.layer})` }} />
      <span className="kbn-kind">{data.kind}</span>
      <span className="kbn-title">{data.title}</span>
      {data.note && <span className="kbn-note">{data.note}</span>}
      <Handle type="source" position={Position.Right} />
    </div>
  )
}

const nodeTypes = { kb: KbNode }

/** dagre 로 좌→우 계층 배치. 순수 계산이므로 매번 같은 그림이 나온다. */
function layout(nodes: DagNode[], edges: DagEdge[], compact: boolean) {
  const w = compact ? CW : W
  const h = compact ? CH : H
  const g = new dagre.graphlib.Graph()
  g.setDefaultEdgeLabel(() => ({}))
  // ranksep 은 관계 라벨이 들어갈 자리다. 좁으면 라벨이 상자 위로 올라앉는다.
  g.setGraph({
    rankdir: 'LR', nodesep: compact ? 18 : 26,
    ranksep: compact ? 80 : 128, marginx: 12, marginy: 12,
  })
  for (const n of nodes) g.setNode(n.id, { width: w, height: h })
  for (const e of edges) if (e.from !== e.to) g.setEdge(e.from, e.to)
  dagre.layout(g)

  const rf: Node<KbData>[] = nodes.map((n) => {
    const p = g.node(n.id)
    return {
      id: n.id,
      type: 'kb',
      // dagre 는 중심 좌표를, React Flow 는 좌상단을 쓴다.
      position: { x: (p?.x ?? 0) - w / 2, y: (p?.y ?? 0) - h / 2 },
      // 크기를 명시한다. 없으면 React Flow 가 DOM 을 잰 뒤에야 범위를
      // 알 수 있어 첫 fitView 가 헛돈다 — 그림이 잘린 채로 그려진다.
      width: w,
      height: h,
      data: {
        kind: n.type, title: n.title, note: n.note,
        layer: n.layer, terminal: n.terminal, compact,
      },
      draggable: false,
      connectable: false,
    }
  })

  const re: Edge[] = edges.map((e, i) => ({
    id: `e${i}`,
    source: e.from,
    target: e.to,
    type: 'smoothstep',
    // SVG text 는 개행을 무시한다. 한 줄로 잇되 값은 뒤에 붙인다.
    label: e.value ? `${e.label ?? ''} · ${e.value}` : (e.label ?? undefined),
    labelShowBg: true,
    labelBgPadding: [6, 3] as [number, number],
    labelBgBorderRadius: 2,
    animated: false,
    className: e.value ? 'has-value' : undefined,
  }))
  return { rf, re }
}

function Canvas({ nodes, edges, height, compact }: {
  nodes: DagNode[]; edges: DagEdge[]; height: number; compact: boolean
}) {
  const nav = useNavigate()
  const { rf, re } = useMemo(() => layout(nodes, edges, compact), [nodes, edges, compact])

  return (
    <div className="rf" style={{ height }}>
      <ReactFlow
        nodes={rf}
        edges={re}
        nodeTypes={nodeTypes}
        fitView
        // 글자가 읽히는 선 아래로는 줄이지 않는다. 그보다 넓으면 밀어서 본다.
        fitViewOptions={{ padding: 0.14, minZoom: 0.75, maxZoom: 1 }}
        minZoom={0.3}
        maxZoom={1.6}
        nodesDraggable={false}
        nodesConnectable={false}
        elementsSelectable={false}
        proOptions={{ hideAttribution: false }}
        onNodeClick={(_, n) => nav(`/n/${encodeURIComponent(n.id)}`)}
      >
        <Background variant={BackgroundVariant.Dots} gap={22} size={1} />
        <Controls showInteractive={false} />
      </ReactFlow>
    </div>
  )
}

export function Dag({ nodes, edges, height = 320, compact = false }: {
  nodes: DagNode[]
  edges: DagEdge[]
  height?: number
  /** 이름과 건수만 보이면 되는 도해. 상자를 줄여 한 화면에 담는다. */
  compact?: boolean
}) {
  if (!nodes.length) return null
  return (
    <ReactFlowProvider>
      <Canvas nodes={nodes} edges={edges} height={height} compact={compact} />
    </ReactFlowProvider>
  )
}
