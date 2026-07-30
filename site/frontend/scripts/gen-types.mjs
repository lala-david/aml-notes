// kb/schema/*.json → src/types/kb.gen.ts
//
// 스키마가 바뀌면 프론트 컴파일이 깨진다. 이것이 "프론트가 온톨로지와
// 어긋날 수 없다"의 구현이다. (docs/architecture/03-site-blueprint.md §5.1)
import { compileFromFile } from 'json-schema-to-typescript'
import { mkdir, writeFile } from 'node:fs/promises'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const here = dirname(fileURLToPath(import.meta.url))
const kbSchema = resolve(here, '../../../kb/schema')
const outFile = resolve(here, '../src/types/kb.gen.ts')

const banner = `/* eslint-disable */
// 🤖 자동 생성 — 직접 편집하지 마세요.
// 원본: kb/schema/{node,edge}.schema.json
// 재생성: npm run gen:types
`

const opts = { bannerComment: '', additionalProperties: false, style: { singleQuote: true } }

const parts = []
for (const [file, name] of [['node.schema.json', 'KBNode'], ['edge.schema.json', 'KBEdge']]) {
  parts.push(await compileFromFile(resolve(kbSchema, file), { ...opts, customName: () => name }))
}

await mkdir(dirname(outFile), { recursive: true })
await writeFile(outFile, banner + '\n' + parts.join('\n'), 'utf8')
console.log(`생성: ${outFile}`)
