# Contributing to aml-notes

> 가상자산 AML 학습 노트에 기여해주셔서 감사합니다. 이 문서는 **어떤 기여가 환영받고, 어떻게 제출하면 되는지**를 안내합니다.

## 어떤 기여가 환영받나

### ✅ 환영 (우선순위 높음)

- **사실 오류 교정** — 조문 번호·시행일·금액 한도·벌금 액수 등 **감독당국 검사에 인용 가능한 정확도**를 목표로 하므로 작은 숫자 하나도 소중합니다
- **규제 업데이트** — FATF 개정, 특금법 개정, MiCA·AMLR·AMLA·GENIUS Act 시행 관련 최신 내용
- **외부 링크 교정** — 404 또는 리다이렉트된 링크의 최신 URL
- **Mermaid·다이어그램 오류** — 문법 오류·한글 깨짐·렌더 실패
- **한국 VASP 실무 관점 보강** — KoFIU 검사·ISMS·본인확인기관·DAXA 관련 구체 경험
- **용어 한국어 번역 통일** — 같은 영어 용어가 문서마다 다르게 번역된 경우

### ⚠️ 논의 후 반영 (Issue 먼저)

- **새 토픽 추가** — 폴더 구조·커리큘럼 흐름과 맞아야 하므로 Issue로 방향 논의 선행
- **산문 스타일 전면 재작성** — 2026-04 prose-revamp에서 정한 톤·구조가 있으므로 대규모 재작성은 합의 필요
- **벤더 평가 의견** — 사실(라이선스·고객사·가격 대)은 환영, 주관적 평가(좋다/나쁘다)는 출처 필요

### ❌ 받지 않음

- **투자 권유 / 특정 코인 홍보** — 학습 노트의 중립성 유지
- **특정 벤더 마케팅 자료 그대로 복붙** — 팩트 + 비교 관점 필요
- **정치적 프레이밍** — 제재·규제의 정치적 논쟁은 범위 밖
- **AI 생성 원문을 검증 없이 PR** — 2차 출처·링크·번호 검증 필수

## PR 제출 절차

1. **Issue 먼저 열기** (사소한 오타·링크 수정은 건너뛰어도 OK)
   - 큰 변경일수록 사전 합의가 시간을 절약합니다
2. **Fork → branch** — `fix/travel-rule-threshold`, `docs/add-mica-update` 같이 의미 있는 브랜치명
3. **변경 범위 최소화** — 한 PR에 한 주제. "폴더 전체 재작성" PR은 리뷰 지연
4. **산문 노트 추가 시 체크리스트**:
   - [ ] `> 도입 blurb` (1~2문장) 포함
   - [ ] `## TL;DR` 섹션 존재
   - [ ] 용어를 처음 등장시킬 때 한국어 괄호 병기 (예: "Beneficial Owner(실소유자)")
   - [ ] 관련 문서 `## 더 읽을거리` 링크 최소 3개
   - [ ] `마지막 업데이트: YYYY-MM-DD` 포함
5. **Mermaid 추가/변경 시**:
   - [ ] `charts/validate_mermaid.py` 통과
   - [ ] 파이프 레이블에 괄호 `()` 넣지 않기 (mmdc 파서 오류)
   - [ ] 한국어는 `<br/>` 개행 OK, `\n`은 금지
6. **링크 추가/변경 시**:
   - [ ] `charts/validate_links.py` 통과 (내부 링크)
   - [ ] `charts/check_external_urls.py` 통과 (외부 URL)
7. **커밋 메시지 형식**:
   ```
   <scope>: <요지>

   예)
   notes/travel-rule: FATF R.16 2025-06 개정 금액 반영
   curriculum/day_17: 💭 한 줄 메모 섹션 누락 복구
   charts: regulation_timeline 2027-07-10 AMLR 적용일 추가
   ```
8. **PR 템플릿에 인용 출처 제시** — 특히 숫자·조문 변경 시 감독당국 1차 출처 링크 필수

## 로컬 검증

```bash
# 의존성 설치 (처음 1회)
pip install -r charts/requirements.txt        # seaborn·matplotlib·markdown
cd charts && npm install && cd ..             # @mermaid-js/mermaid-cli

# Mermaid 컴파일 검증 (전체 114+ 블록)
python charts/validate_mermaid.py

# 내부 링크 검증 (.md·.png·.svg 상대 경로)
python charts/validate_links.py

# 외부 URL 검증 (400+개, 느림 — CI에서만 돌려도 OK)
python charts/check_external_urls.py

# 차트 재생성 (seaborn 8개)
python charts/generate.py

# 프린트 HTML 재생성 (60개 day 패킷)
python print/generator.py
```

## 스타일 가이드

- **산문 우선, 치트시트 지양** — 불릿 나열이 아니라 "왜 이게 중요한지" 문장으로 설명
- **한국어 괄호 병기** — 영어 전문 용어를 처음 등장시킬 때 한국어(또는 그 반대)
- **시각 자료 적극 활용** — 핵심 개념은 Mermaid 또는 seaborn 차트로도 보여주기
- **출처는 1차 자료** — 감독당국·법원·법제처·표준화 기구. 2차 블로그는 보조
- **날짜 형식 통일** — YYYY-MM-DD (예: `2026-04-20`)
- **금액 단위** — 한국 원화는 "100만원", 달러는 "$4.3B" 같이 관습적 표기 허용
- **이모지** — 섹션 헤더·카테고리 구분 용도만. 문장 중간은 지양

## 행동 강령

- **기여자 모두 존중** — 비판은 원고·논리에 하고 사람을 공격하지 않기
- **정치 중립** — 제재·규제 해석에 이념적 색깔 넣지 않기
- **한국어·영어 모두 OK** — 본문은 한국어지만 Issue/PR 토론은 영어도 환영

## 🏆 Recognition

기여하신 분들께 감사드립니다. 다음 경로로 인정합니다:

### Contributor Hall of Fame

5+ accepted PR → README의 "Trusted Contributor" 명단에 등재.

### Reviewer Acknowledgment

분야별 reviewer로 참여하신 분들 (동의 시):
- 법무 Reviewer
- 기술 Reviewer
- 실무 Reviewer
- 번역 Reviewer

### 분기 회고

매 분기 (Q1·Q2·Q3·Q4) GitHub Discussions에 회고 게시. Top contributor 언급.

## 🌱 Good First Issues

처음 기여하실 때 추천:

- [ ] 외부 URL 깨짐 수정 (`charts/check_external_urls.py` 결과 처리)
- [ ] 한국어 → 영어 용어 번역 추가 (`notes/glossary.md`)
- [ ] 새 일자·금액 fact-check (`grep` 후 1차 자료 검증)
- [ ] Mermaid 다이어그램 가독성 개선 (color·layout)
- [ ] 영문 에디션 (`en/`) 자연스러운 영어로 다듬기

각 카테고리에 GitHub Issue `good-first-issue` 라벨로 등록되어 있습니다.

## 📋 규제 변화 신고

새 규제·법령·사건 발견 시 → [Regulatory Update Issue Template](https://github.com/lala-david/aml-notes/issues/new?template=04-regulatory-update.yml)

## 라이선스

기여하는 콘텐츠는 저장소의 [CC BY 4.0](LICENSE) (코드 샘플은 MIT) 라이선스로 공개됩니다. PR 제출은 이 라이선스에 동의하는 것으로 간주합니다.

## 질문·논의

- 🐛 **버그·오류** → [Issues](https://github.com/lala-david/aml-notes/issues) → `오류 보고` 템플릿
- 💡 **토픽 제안** → Issues → `토픽 제안` 템플릿
- 🧭 **방향 논의** → Issues → `Discussion` 라벨

작은 PR이라도 환영합니다. 오탈자 하나도 업계 종사자에게는 소중합니다.
