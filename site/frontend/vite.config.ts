import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

/**
 * `/api` 는 프록시로 백엔드에 넘긴다.
 *
 * 브라우저가 백엔드 포트를 직접 알면 두 포트가 어긋나는 순간 모든 화면이
 * 동시에 죽는다. 그래서 포트를 아는 곳을 여기 한 군데로 줄였다.
 * 백엔드를 다른 포트에 띄웠다면 VITE_API_TARGET 만 바꾸면 된다.
 */
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '')
  const target = env.VITE_API_TARGET || 'http://127.0.0.1:8000'
  const proxy = { '/api': { target, changeOrigin: true } }
  return {
    plugins: [react()],
    // 5173 이 다른 프로세스에 잡혀 있으면 조용히 다음 포트로 옮긴다.
    server: { strictPort: false, proxy },
    preview: { proxy },
  }
})
