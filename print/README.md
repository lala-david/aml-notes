# 🖨 AML Notes — Print Packets (A4)

> 60-Day 챌린지용 **A4 프린트 전용 학습 패킷**. Task Sheet 1장 + 그날 필요한 모든 읽기 본문을 하나로 묶었습니다.

## 📁 구조

```
print/
├── index.html            ← 허브 (브라우저에서 이걸 먼저 열기)
├── README.md             ← 이 파일
├── assets/
│   └── print.css         ← 공통 A4 프린트 스타일
├── days/
│   ├── day_01.html       ← Day 1 완전 패킷 (Task + Reading)
│   ├── day_02.html
│   ├── ...
│   └── day_60.html
└── generator.py          ← MD → HTML 자동 변환기
```

## 🚀 지금 Day 1 프린트하는 법 (3스텝)

1. 브라우저로 `print/index.html` 열기
2. **Day 01** 카드 클릭
3. 우상단 **🖨 Print A4** 버튼 (또는 <kbd>Ctrl</kbd>+<kbd>P</kbd> / <kbd>⌘</kbd>+<kbd>P</kbd>)

## 🖨 브라우저 프린트 대화상자 설정 권장

| 항목 | 값 |
|---|---|
| 용지 | **A4** |
| 여백 | **None** 또는 **Minimum** (페이지 내부 18mm 여백) |
| 배경 그래픽 | **체크 ✓** (헤더 구분선·강조색 인쇄용) |
| 배율 | **100%** 또는 **Default** |
| 헤더·푸터 | **체크 해제** (페이지 번호·URL 불필요) |

## 📄 Day 패킷 구성

각 Day는 아래 구조로 구성됩니다.

### 1. Task Sheet (1페이지)

- 큰 **DAY 넘버**, Week 진척 점, 오늘의 테마
- 제목 + 리드 + 예상 시간
- 🎯 핵심 질문 / 📖 읽기 / 🌐 외부 자료 / 🛠 미니 챌린지
- ✅ 체크포인트 (손으로 채우는 □ 박스)
- 💭 오늘의 한 줄 (괘선 2줄)
- 더 깊이 + Date 기입란

### 2. Reading Articles (여러 페이지)

Task Sheet의 📖 읽기·더 깊이에서 참조하는 **내부 노트(`.md`) 전체 본문**이 이어집니다.

- 각 노트 시작에 **표지 페이지**(Divider)
- 본문은 A4 최적화된 타이포그래피로 포매팅 (Pretendard 변형체, 10.2pt, 행간 1.72)
- 표·콜아웃·코드블록 모두 프린트 대응

## 🛠 생성기 재실행

커리큘럼 `.md`나 링크된 노트가 바뀌면 다시 실행:

```bash
# Day 1만
python print/generator.py 1

# 특정 범위
python print/generator.py 1 2 3
python print/generator.py 1-7

# 전체 60일
python print/generator.py all
```

필수: `pip install markdown`

## 🎨 디자인 원칙

- **A4 정확한 크기** (210×297 mm)
- **Pretendard Variable** 본문 / **IBM Plex Serif** 숫자 / **IBM Plex Mono** 레이블
- **잉크 절약형** 흑백 기본 + 차콜 네이비 단일 액센트(`#1a2e4a`)
- **한글 끊어읽기 방지** (word-break: keep-all)
- **직접 쓰는 공간** — 체크박스·괘선·날짜 기입란

## 📎 팁

- **여러 날 묶어 프린트**하고 싶으면 PDF로 각각 저장 후 PDF 편집기에서 병합
- **모바일에서 볼 때**는 브라우저 세로모드에서 자연스럽게 스케일됨
- **오프라인 저장**: 각 `day_NN.html`은 외부 자원(폰트·CSS) 외엔 독립적 — 폴더 통째로 USB에 복사해도 작동

## 🔄 업데이트 시

커리큘럼이나 노트를 수정한 뒤:

```bash
python print/generator.py all
```

한 번에 재생성됩니다. 변경된 날만 재생성하려면 번호 지정.
