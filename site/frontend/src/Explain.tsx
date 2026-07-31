import { Link } from 'react-router-dom'
import type { CrosswalkRow } from './api'
import { ConfMark, NodeRef } from './components'
import { JurChip } from './Jur'

/* ═══════════════════════════════════════════════════════════════════════
   첫 화면의 설명 장치.

   구조도(그래프·계층·클래스 수)로 시작하면 아무것도 전달되지 않는다.
   사람이 실제로 갖는 질문 하나를 던지고, 그 답을 끝까지 따라가는 과정
   자체가 이 사이트가 무엇을 하는지의 설명이 된다.
   ═══════════════════════════════════════════════════════════════════════ */

type Step = {
  idx: string
  kind: string
  rel?: string
  to: string
  title: string
  body: string
  quote?: string
  cite?: string
  val?: string
  unit?: string
  result?: boolean
}

const STEPS: Step[] = [
  {
    idx: '01',
    kind: '법률',
    to: '/n/PROV:kr-tfia-art5-3',
    title: '특금법 제5조의3',
    body:
      '전신송금 시 정보제공 의무의 법률상 근거입니다. 그런데 이 조문은 기준금액을 스스로 정하지 않습니다. ' +
      '500만원이라는 상한만 긋고 나머지를 대통령령에 넘깁니다.',
    quote: '대통령령으로 정하는 금액 이상의 전신송금',
    cite: '특금법 제5조의3 · 위임 상한 500만원',
    val: '5,000,000',
    unit: 'KRW 상한',
  },
  {
    idx: '02',
    kind: '법률',
    rel: '위임',
    to: '/n/PROV:kr-tfia-art6-p3',
    title: '제6조 제3항',
    body:
      '가상자산사업자에게 제5조의3을 어떻게 적용할지를 다시 시행령으로 넘깁니다. ' +
      '법률만 읽어서는 여기서 더 갈 곳이 없습니다.',
    val: '—',
    unit: '미확정',
  },
  {
    idx: '03',
    kind: '시행령',
    rel: '위임',
    to: '/n/PROV:kr-tfia-sd-art10-10',
    title: '시행령 제10조의10 제1호',
    body:
      '실무 기준은 여기 있습니다. 법률을 한 글자도 고치지 않고 이 조문만 바꿔도 ' +
      '내일부터 적용 기준이 달라집니다.',
    quote: '100만원 이상',
    cite: '특금법 시행령 제10조의10 제1호',
    val: '1,000,000',
    unit: 'KRW',
    result: true,
  },
]

export function DelegationChain() {
  return (
    <>
      <ol className="chain">
        {STEPS.map((s) => (
          <li key={s.idx} className="chain-step" data-result={s.result ? '' : undefined}>
            <span className="chain-node" aria-hidden>
              {s.idx}
            </span>

            <div className="chain-body">
              <span className="chain-kind">
                {s.kind}
                {s.rel && <span className="chain-rel">{s.rel}</span>}
              </span>
              <Link className="chain-title" to={s.to}>
                {s.title}
              </Link>
              <p className="chain-text">{s.body}</p>
              {s.quote && (
                <p className="chain-quote">
                  {s.quote}
                  {s.cite && <cite>{s.cite}</cite>}
                </p>
              )}
            </div>

            <p className="chain-val">
              <b>{s.val}</b>
              <span>{s.unit}</span>
            </p>
          </li>
        ))}
      </ol>

      <p className="chain-close">
        법률만 읽으면 100만원이라는 숫자는 나오지 않습니다. 이 지식베이스는 세 조문 사이의 위임
        관계를 그래프로 들고 있어서, 조문 하나에서 시작해 끝까지 따라갈 수 있습니다.
      </p>
    </>
  )
}

/* ═══ 관할 비교 미리보기 — 실제 API 응답으로 그린다 ═══════════════════ */

export function CrosswalkPreview({ rows }: { rows: CrosswalkRow[] }) {
  return (
    <div className="tablewrap">
      <table className="data">
        <thead>
          <tr>
            <th>관할</th>
            <th>근거 조문</th>
            <th className="num">기준금액</th>
            <th>확신도</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r) => (
            <tr key={r.provision.id}>
              <td>
                <JurChip ns={r.namespace} label={r.jurisdiction_label} />
              </td>
              <td>
                <NodeRef node={r.provision} />
                {r.regulation && <span className="sub">{r.regulation.title}</span>}
              </td>
              <td className="num">
                {r.threshold != null ? (
                  <>
                    <b>{r.threshold.toLocaleString()}</b>
                    <small>{r.currency}</small>
                  </>
                ) : (
                  <span className="dim">임계값 없음</span>
                )}
              </td>
              <td>
                <ConfMark value={r.confidence} />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

/* ═══ 시점 대조 — 같은 질의를 두 시점에 던진 결과 ════════════════════ */

const CUT = '2021-12-31'

const inForce = (r: CrosswalkRow, at: string) =>
  (!r.valid_from || r.valid_from <= at) && (!r.valid_to || r.valid_to > at)

export function AsOfContrast({ rows }: { rows: CrosswalkRow[] }) {
  const past = rows.filter((r) => inForce(r, CUT))
  return (
    <div className="astwo">
      <div className="astwo-col">
        <h4>
          <span className="mono">{CUT}</span> 시점
          <small>유효 {past.length}건</small>
        </h4>
        <ul>
          {rows.map((r) => {
            const on = inForce(r, CUT)
            return (
              <li key={r.provision.id} className={on ? '' : 'absent'}>
                <span className="astwo-name">{r.provision.title}</span>
                <time>{on ? (r.valid_from ?? '?') : '미시행'}</time>
              </li>
            )
          })}
        </ul>
      </div>

      <div className="astwo-col">
        <h4>
          전체 기간
          <small>유효 {rows.length}건</small>
        </h4>
        <ul>
          {rows.map((r) => (
            <li key={r.provision.id}>
              <span className="astwo-name">{r.provision.title}</span>
              <time>{r.valid_from ?? '?'}</time>
            </li>
          ))}
        </ul>
      </div>
    </div>
  )
}
