import { useEffect, useState } from 'react'

/** 비동기 조회 한 건. 언마운트 후 setState 를 하지 않는다. */
export function useAsync<T>(fn: () => Promise<T>, deps: unknown[]) {
  const [state, set] = useState<{ data?: T; error?: unknown; loading: boolean }>({ loading: true })
  useEffect(() => {
    let alive = true
    set({ loading: true })
    fn().then(
      (d) => alive && set({ data: d, loading: false }),
      (e) => alive && set({ error: e, loading: false }),
    )
    return () => {
      alive = false
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps)
  return state
}
