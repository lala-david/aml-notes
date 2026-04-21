#!/usr/bin/env python3
"""
AML Notes Print Packet Generator
=================================
day_NN.md 를 읽어 해당 day의 읽기/외부자료/미니챌린지/체크포인트/한 줄/더 깊이를
A4 Task Sheet 1장 + (링크된 notes 모두의 Reading Article 여러 장) HTML 패킷으로 생성.

사용:
  python print/generator.py 1            # Day 1만
  python print/generator.py 1 2 3        # Day 1,2,3
  python print/generator.py all          # 60개 전체
"""

from __future__ import annotations

import hashlib
import os
import re
import subprocess
import sys
import html
from pathlib import Path

try:
    import markdown as md_lib
except ImportError:
    print("Error: pip install markdown", file=sys.stderr)
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent  # aml/
PRINT_ROOT = ROOT / "print"
DAYS_OUT = PRINT_ROOT / "days"
CHARTS_DIR = ROOT / "charts"
MERMAID_CACHE = CHARTS_DIR / "mermaid-cache"
MERMAID_CACHE.mkdir(parents=True, exist_ok=True)

MMDC_BIN = CHARTS_DIR / "node_modules" / ".bin" / (
    "mmdc.cmd" if os.name == "nt" else "mmdc"
)
MERMAID_CONFIG = CHARTS_DIR / "mermaid_config.json"
USE_MMDC = MMDC_BIN.exists() and MERMAID_CONFIG.exists()

WEEK_THEMES = [
    (1, 7, "Week 1", "AML 기초 + 가상자산 특수성"),
    (8, 14, "Week 2", "한국 규제 (특금법 + 이용자보호법)"),
    (15, 21, "Week 3", "FATF + 글로벌 (미국·EU)"),
    (22, 28, "Week 4", "Travel Rule + IVMS101"),
    (29, 35, "Week 5", "온체인 분석 + KYT"),
    (36, 42, "Week 6", "자금세탁 유형 + DeFi·믹서"),
    (43, 49, "Week 7", "컴플라이언스 운영 + 거버넌스"),
    (50, 56, "Week 8", "사례 + 리서치 + AI"),
    (57, 60, "Capstone", "통합 설계 + 90일 로드맵"),
]


def week_for(day: int) -> tuple[str, str, int, int]:
    """Return (week_label, theme, day_in_week_index, week_length)."""
    for start, end, label, theme in WEEK_THEMES:
        if start <= day <= end:
            return label, theme, day - start, end - start + 1
    return "Day", "", 0, 7


# ----- MD parsing helpers ---------------------------------------------------

SECTION_ICONS = {
    "핵심 질문": "🎯",
    "회고 질문": "🎯",
    "읽기": "📖",
    "오늘 뭘 배우나": "📖",
    "외부 자료": "🌐",
    "미니 챌린지": "🛠️",
    "메인 미니 프로젝트": "🛠️",
    "미니 프로젝트": "🛠️",
    "체크포인트": "✅",
    "오늘의 한 줄": "💭",
    "더 깊이": "🔎",
}

LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')


def parse_day_md(text: str) -> dict:
    """Parse day_NN.md into structured blocks."""
    lines = text.splitlines()
    out = {
        "title": "",
        "lead": "",
        "time": "",
        "today": "",      # 📖 오늘 뭘 배우나 paragraph
        "questions": [],  # ordered list items
        "reading_main": [],  # [(text, ref)] — main internal notes
        "reading_extra": [],  # same
        "external": [],   # [(text, url)]
        "challenge": [],  # bullet items
        "checkpoints": [],
        "one_liner_prompt": "",
        "deeper": [],     # [(text, ref)]
        "challenge_raw_md": "",   # full markdown for the 미니 챌린지/프로젝트 section
        "daymap_raw_md": "",      # 🗺 오늘의 지도 Mermaid block
    }

    # Title
    for ln in lines:
        if ln.startswith("# "):
            # "# Day 1 — AML이 뭔가 + 자금세탁 3단계"
            m = re.match(r"^#\s*Day\s*\d+\s*—\s*(.+)$", ln)
            if m:
                out["title"] = m.group(1).strip()
            else:
                out["title"] = ln[2:].strip()
            break

    # Lead (first blockquote > ... ⏱️ ~75분)
    for i, ln in enumerate(lines):
        if ln.startswith("> "):
            lead = ln[2:].strip()
            # Extract time
            m = re.search(r"⏱️\s*(~?\d+분)", lead)
            if m:
                out["time"] = m.group(1).strip()
                lead = re.sub(r"\.\s*⏱️[^.]*\.?\s*$", ".", lead).strip()
            out["lead"] = lead
            break

    # Walk through sections
    current = None
    buffer: list[str] = []

    def commit():
        nonlocal buffer
        if current is None:
            buffer = []
            return
        text = "\n".join(buffer).strip()
        if current == "today":
            out["today"] = text
        elif current == "daymap":
            out["daymap_raw_md"] = text
        elif current in ("questions",):
            items = []
            for bl in buffer:
                m = re.match(r"^\s*\d+\.\s+(.*)$", bl)
                if m:
                    items.append(m.group(1).strip())
            out["questions"] = items
        elif current == "reading":
            for bl in buffer:
                m = re.match(r"^\s*[-*]\s+(.*)$", bl)
                if not m:
                    continue
                item = m.group(1).strip()
                # Strip leading prefix like "메인: " or "보조: "
                is_main = item.startswith("메인")
                item_clean = re.sub(r"^(메인|보조)\s*:\s*", "", item)
                links = LINK_RE.findall(item_clean)
                if links:
                    for label, ref in links:
                        target_list = out["reading_main"] if is_main else out["reading_extra"]
                        target_list.append((
                            re.sub(r"`", "", label).strip(),
                            ref.strip()
                        ))
                else:
                    (out["reading_main"] if is_main else out["reading_extra"]).append(
                        (item_clean, "")
                    )
        elif current == "external":
            for bl in buffer:
                m = re.match(r"^\s*[-*]\s+(.*)$", bl)
                if not m:
                    continue
                item = m.group(1).strip()
                links = LINK_RE.findall(item)
                if links:
                    for label, url in links:
                        out["external"].append((label.strip(), url.strip()))
                else:
                    out["external"].append((item, ""))
        elif current in ("challenge",):
            # Keep raw markdown for full rendering (tables/code/headers)
            out["challenge_raw_md"] = "\n".join(buffer).strip()
            items = []
            for bl in buffer:
                m = re.match(r"^\s*[-*]\s+(.*)$", bl)
                if m:
                    items.append(m.group(1).strip())
            out["challenge"] = items
        elif current == "checkpoints":
            items = []
            for bl in buffer:
                m = re.match(r"^\s*-\s*\[\s*\]\s*(.*)$", bl)
                if m:
                    items.append(m.group(1).strip())
            out["checkpoints"] = items
        elif current == "one_liner":
            # Find "> _직접 작성: ..." style prompt
            for bl in buffer:
                bl = bl.strip()
                if bl.startswith(">"):
                    out["one_liner_prompt"] = re.sub(r"^>\s*_?|_?\s*$", "", bl).strip()
                    break
            if not out["one_liner_prompt"]:
                out["one_liner_prompt"] = "오늘 가장 의외였던 것 한 줄을 직접 작성하세요."
        elif current == "deeper":
            for bl in buffer:
                m = re.match(r"^\s*[-*]\s+(.*)$", bl)
                if not m:
                    continue
                item = m.group(1).strip()
                links = LINK_RE.findall(item)
                if links:
                    for label, ref in links:
                        out["deeper"].append((
                            re.sub(r"`", "", label).strip(),
                            ref.strip()
                        ))
                else:
                    out["deeper"].append((item, ""))
        buffer = []

    for ln in lines:
        h = re.match(r"^##\s+(.+)$", ln)
        if h:
            commit()
            heading = h.group(1).strip()
            heading_plain = re.sub(r"^[^\w가-힣]+", "", heading).strip()
            # Route
            if "오늘 뭘 배우나" in heading_plain:
                current = "today"
            elif "오늘의 지도" in heading_plain:
                current = "daymap"
            elif "핵심 질문" in heading_plain or "회고 질문" in heading_plain or "캡스톤 목표" in heading_plain:
                current = "questions"
            elif heading_plain.startswith("읽기") or "빠른 복습" in heading_plain:
                current = "reading"
            elif "외부 자료" in heading_plain:
                current = "external"
            elif "미니 챌린지" in heading_plain or "미니 프로젝트" in heading_plain or "캡스톤" in heading_plain or "90일 로드맵" in heading_plain or "한국법" in heading_plain:
                current = "challenge"
            elif "체크포인트" in heading_plain:
                current = "checkpoints"
            elif "오늘의 한 줄" in heading_plain or "회고" in heading_plain:
                current = "one_liner"
            elif "더 깊이" in heading_plain:
                current = "deeper"
            else:
                current = None
            continue
        if current is not None:
            buffer.append(ln)

    commit()
    return out


# ----- Note internal link resolution ----------------------------------------

def resolve_ref(ref: str, from_dir: Path) -> Path | None:
    """Resolve a markdown link ref from a given directory to an absolute Path."""
    if not ref or ref.startswith(("http://", "https://", "mailto:", "#")):
        return None
    # strip fragment
    ref = ref.split("#", 1)[0]
    if not ref:
        return None
    target = (from_dir / ref).resolve()
    if target.exists() and target.is_file():
        return target
    return None


def linked_note_files(day_data: dict, day_md_path: Path) -> list[tuple[str, Path]]:
    """Gather internal .md files linked in reading_main + reading_extra + deeper.
    Returns [(kind_label, Path), ...] in order. Deduplicates by path.
    """
    day_dir = day_md_path.parent
    seen: set[Path] = set()
    out: list[tuple[str, Path]] = []

    for label, ref in day_data["reading_main"]:
        p = resolve_ref(ref, day_dir)
        if p and p not in seen and p.suffix == ".md":
            seen.add(p)
            out.append(("메인 읽기", p))

    for label, ref in day_data["reading_extra"]:
        p = resolve_ref(ref, day_dir)
        if p and p not in seen and p.suffix == ".md":
            seen.add(p)
            out.append(("보조 읽기", p))

    for label, ref in day_data["deeper"]:
        p = resolve_ref(ref, day_dir)
        if p and p not in seen and p.suffix == ".md":
            seen.add(p)
            out.append(("더 깊이 (선택)", p))

    return out


# ----- HTML rendering --------------------------------------------------------

def esc(s: str) -> str:
    return html.escape(s, quote=False)


def render_inline(md_text: str) -> str:
    """Inline markdown → HTML (bold/italic/code/links). Used for task sheet items."""
    s = md_text
    # Code first (backticks)
    def code_sub(m):
        return f"<code>{esc(m.group(1))}</code>"
    s = re.sub(r"`([^`]+)`", code_sub, s)
    # Bold
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    # Italic
    s = re.sub(r"(?<![_*])\*([^*\n]+)\*", r"<em>\1</em>", s)
    # Links [t](u) — for display, keep as text + small URL in mono
    def link_sub(m):
        t = m.group(1)
        u = m.group(2)
        # strip backticks in label
        t_clean = re.sub(r"`", "", t)
        if u.startswith(("http://", "https://")):
            short = re.sub(r"^https?://", "", u)
            return f'{esc(t_clean)}<br><span style="font-family:var(--font-mono);font-size:8pt;color:var(--ink-mute);">{esc(short)}</span>'
        else:
            # internal note path
            return f'<span class="ref">{esc(u)}</span> {esc(t_clean)}'
    s = LINK_RE.sub(link_sub, s)
    return s


def render_progress_dots(day_in_week: int, week_len: int) -> str:
    dots = []
    for i in range(week_len):
        cls = "page-meta__dot"
        if i < day_in_week:
            cls += " page-meta__dot--active"
        elif i == day_in_week:
            cls += " page-meta__dot--today"
        dots.append(f'<span class="{cls}"></span>')
    return "\n          ".join(dots)


def render_task_sheet(day: int, day_data: dict) -> str:
    week_label, theme, idx_in_week, week_len = week_for(day)
    dots = render_progress_dots(idx_in_week, week_len)

    # Sections
    sections_html: list[str] = []

    # 🗺 오늘의 지도 (Mermaid)
    if day_data.get("daymap_raw_md", "").strip():
        body_html = split_article_blocks(day_data["daymap_raw_md"])
        sections_html.append(f'''
    <section class="section section--map">
      <div class="section__head">
        <span class="section__icon">🗺</span>
        <h2 class="section__title">오늘의 지도</h2>
      </div>
      <div class="section__body section__body--rich">
{body_html}
      </div>
    </section>''')

    # 🎯 핵심 질문
    if day_data["questions"]:
        lis = "".join(f"<li>{render_inline(q)}</li>\n" for q in day_data["questions"])
        sections_html.append(f'''
    <section class="section">
      <div class="section__head">
        <span class="section__icon">🎯</span>
        <h2 class="section__title">핵심 질문</h2>
      </div>
      <div class="section__body">
        <ol>
{lis}        </ol>
      </div>
    </section>''')

    # 📖 읽기
    if day_data["reading_main"] or day_data["reading_extra"]:
        main_lis = ""
        for label, ref in day_data["reading_main"]:
            if ref:
                main_lis += f'<li>메인 · <span class="ref">{esc(ref)}</span></li>\n'
            else:
                main_lis += f'<li>{esc(label)}</li>\n'
        for label, ref in day_data["reading_extra"]:
            if ref:
                main_lis += f'<li>보조 · <span class="ref">{esc(ref)}</span></li>\n'
            else:
                main_lis += f'<li>{esc(label)}</li>\n'
        sections_html.append(f'''
    <section class="section">
      <div class="section__head">
        <span class="section__icon">📖</span>
        <h2 class="section__title">읽기</h2>
      </div>
      <div class="section__body">
        <ul>
{main_lis}        </ul>
      </div>
    </section>''')

    # 🌐 외부 자료
    if day_data["external"]:
        lis = ""
        for label, url in day_data["external"]:
            if url:
                short = re.sub(r"^https?://", "", url)
                lis += f'<li>{esc(label)}<br><span style="font-family:var(--font-mono);font-size:8pt;color:var(--ink-mute);">{esc(short)}</span></li>\n'
            else:
                lis += f"<li>{esc(label)}</li>\n"
        sections_html.append(f'''
    <section class="section">
      <div class="section__head">
        <span class="section__icon">🌐</span>
        <h2 class="section__title">외부 자료 <em style="font-weight:400;color:var(--ink-mute);font-style:normal;font-size:8.5pt;">(선택)</em></h2>
      </div>
      <div class="section__body">
        <ul>
{lis}        </ul>
      </div>
    </section>''')

    # 🛠️ 미니 챌린지 · 미니 프로젝트
    raw_md = day_data.get("challenge_raw_md", "")
    has_rich = bool(
        raw_md and (
            "\n|" in raw_md
            or raw_md.lstrip().startswith("|")
            or "```" in raw_md
            or re.search(r"^###?\s", raw_md, re.MULTILINE)
        )
    )
    if has_rich:
        # Render as full article-body markdown
        body_html = split_article_blocks(raw_md)
        # Slight title swap for project days
        title = "메인 미니 프로젝트" if "미니 프로젝트" in raw_md[:80] or day % 7 == 0 else "미니 챌린지"
        sections_html.append(f'''
    <section class="section section--rich">
      <div class="section__head">
        <span class="section__icon">🛠️</span>
        <h2 class="section__title">{title}</h2>
      </div>
      <div class="section__body section__body--rich">
{body_html}
      </div>
    </section>''')
    elif day_data["challenge"]:
        lis = "".join(f"<li>{render_inline(c)}</li>\n" for c in day_data["challenge"])
        sections_html.append(f'''
    <section class="section">
      <div class="section__head">
        <span class="section__icon">🛠️</span>
        <h2 class="section__title">미니 챌린지</h2>
      </div>
      <div class="section__body">
        <ul>
{lis}        </ul>
      </div>
    </section>''')

    # ✅ 체크포인트
    if day_data["checkpoints"]:
        items = "".join(
            f'      <div class="checkpoints__item"><span class="checkpoints__box"></span><span>{render_inline(c)}</span></div>\n'
            for c in day_data["checkpoints"]
        )
        sections_html.append(f'''
    <section class="section">
      <div class="section__head">
        <span class="section__icon">✅</span>
        <h2 class="section__title">체크포인트</h2>
      </div>
      <div class="checkpoints">
{items}    </div>
    </section>''')

    # 💭 오늘의 한 줄
    prompt = day_data["one_liner_prompt"] or "오늘 가장 의외였던 것 한 줄을 직접 작성하세요."
    sections_html.append(f'''
    <section class="section">
      <div class="section__head">
        <span class="section__icon">💭</span>
        <h2 class="section__title">오늘의 한 줄</h2>
      </div>
      <div class="oneliner">
        <p class="oneliner__prompt">{esc(prompt)}</p>
        <div class="oneliner__lines">
          <div class="oneliner__line"></div>
          <div class="oneliner__line"></div>
        </div>
      </div>
    </section>''')

    # Deeper footer
    deeper_html = ""
    if day_data["deeper"]:
        first = day_data["deeper"][0]
        label = first[0]
        ref = first[1]
        deeper_html = f'<span class="ref">{esc(ref)}</span> — {esc(label)}' if ref else esc(label)
    else:
        deeper_html = "—"

    sheet = f'''
  <article class="page">

    <header class="page-header">
      <div class="day-mark">
        <span class="day-mark__label">Day</span>
        <span class="day-mark__num">{day:02d}</span>
      </div>
      <div class="page-meta">
        <div class="page-meta__week">{esc(week_label)} / {week_len}</div>
        <div class="page-meta__theme">{esc(theme)}</div>
        <div class="page-meta__progress">
          {dots}
        </div>
      </div>
    </header>

    <section class="title-block">
      <h1 class="title-block__heading">{esc(day_data["title"])}</h1>
      <p class="title-block__lead">{esc(day_data["lead"]).replace("⏱️", "")}</p>
      {'<span class="title-block__time">⏱ ' + esc(day_data["time"]) + '</span>' if day_data["time"] else ''}
    </section>
{"".join(sections_html)}
    <footer class="deeper">
      <div class="deeper__left">
        <div class="deeper__label">더 깊이 (선택)</div>
        {deeper_html}
      </div>
      <div class="deeper__date">
        Date&nbsp;&nbsp;<span class="deeper__date-input"></span>
      </div>
    </footer>

    <div class="footer-mark">
      <span>AML NOTES · 60-DAY CHALLENGE</span>
      <span>DAY {day:02d} / 60 · TASK</span>
    </div>

  </article>'''
    return sheet


# ----- Article rendering (markdown → HTML for long-form notes) ---------------

MERMAID_BLOCK_RE = re.compile(
    r"```mermaid\s*\n(.*?)\n```",
    re.DOTALL,
)


def _extract_mermaid_blocks(md_text: str) -> tuple[str, list[str]]:
    """Pull ``` ```mermaid ... ``` ``` blocks out of markdown, replace with
    placeholders. Returns (new_md, [block_contents])."""
    blocks: list[str] = []

    def _sub(m):
        blocks.append(m.group(1))
        return f"\n\n<MERMAID_SLOT_{len(blocks)-1}>\n\n"

    new_md = MERMAID_BLOCK_RE.sub(_sub, md_text)
    return new_md, blocks


def _mermaid_to_svg(source: str) -> str | None:
    """Pre-render Mermaid source to SVG via mmdc. Returns SVG content or None.
    Results are cached in charts/mermaid-cache/<hash>.svg for stable rebuilds."""
    if not USE_MMDC:
        return None

    key = hashlib.sha1(source.encode("utf-8")).hexdigest()[:16]
    cache_file = MERMAID_CACHE / f"{key}.svg"

    if cache_file.exists():
        try:
            return cache_file.read_text(encoding="utf-8")
        except Exception:
            pass

    # Write source to temp, call mmdc, read output
    tmp_src = MERMAID_CACHE / f"{key}.mmd"
    tmp_src.write_text(source, encoding="utf-8")

    try:
        subprocess.run(
            [str(MMDC_BIN),
             "-i", str(tmp_src),
             "-o", str(cache_file),
             "-c", str(MERMAID_CONFIG),
             "-b", "transparent"],
            check=True,
            capture_output=True,
            timeout=60,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        print(f"  mmdc failed for {key}: {e}", file=sys.stderr)
        tmp_src.unlink(missing_ok=True)
        return None
    finally:
        tmp_src.unlink(missing_ok=True)

    if not cache_file.exists():
        return None

    svg = cache_file.read_text(encoding="utf-8")
    # Strip XML declaration so it inlines cleanly
    svg = re.sub(r"<\?xml[^>]*\?>\s*", "", svg)
    svg = re.sub(r"<!DOCTYPE[^>]*>\s*", "", svg)
    return svg


def _inject_mermaid_blocks(html: str, blocks: list[str]) -> str:
    for i, block in enumerate(blocks):
        svg = _mermaid_to_svg(block)
        if svg:
            wrapped = f'<div class="mermaid-wrap mermaid-wrap--svg">{svg}</div>'
        else:
            # Fallback: client-side mermaid.js rendering
            wrapped = (
                f'<div class="mermaid-wrap">'
                f'<pre class="mermaid">{html_lib_escape(block)}</pre>'
                f'</div>'
            )
        html = html.replace(
            f"<p>&lt;MERMAID_SLOT_{i}&gt;</p>", wrapped
        ).replace(
            f"<MERMAID_SLOT_{i}>", wrapped
        )
    return html


def html_lib_escape(s: str) -> str:
    """Escape for HTML text content."""
    return (
        s.replace("&", "&amp;")
         .replace("<", "&lt;")
         .replace(">", "&gt;")
    )


def split_article_blocks(md_text: str) -> str:
    """Convert a markdown note file to HTML via python-markdown.
    Pulls mermaid fences out first so they can be rendered client-side."""
    # Remove HTML comment markers that we inject (<!-- MAP-START/END -->)
    md_text = re.sub(r"<!--\s*MAP-(?:START|END)\s*-->", "", md_text)

    md_text, mermaid_blocks = _extract_mermaid_blocks(md_text)
    md = md_lib.Markdown(extensions=["extra", "sane_lists", "tables"])
    html_out = md.convert(md_text)
    html_out = _inject_mermaid_blocks(html_out, mermaid_blocks)
    return html_out


def render_article_divider(kicker: str, title: str, lead: str, path_rel: str) -> str:
    return f'''
  <div class="article-divider">
    <div class="article-divider__kicker">{esc(kicker)}</div>
    <h2 class="article-divider__title">{esc(title)}</h2>
    <p class="article-divider__lead">{esc(lead)}</p>
    <div class="article-divider__meta">{esc(path_rel)}</div>
  </div>'''


def render_article(kind: str, title: str, lead: str, path_rel: str, body_html: str,
                   day: int, total_days: int = 60) -> tuple[str, str]:
    """Return (divider_html, pages_html). The body is wrapped inside a single
    .article-page; browser will paginate via page-break."""
    divider = render_article_divider(kind, title, lead, path_rel)

    page = f'''
  <article class="article-page">
    <header class="article-head">
      <span class="article-head__kind">{esc(kind)} · Day {day:02d}</span>
      <span class="article-head__path">{esc(path_rel)}</span>
    </header>
    <div class="article-body">
{body_html}
    </div>
    <div class="article-foot">
      <span>AML NOTES · 60-DAY CHALLENGE</span>
      <span>DAY {day:02d} / {total_days} · READING</span>
    </div>
  </article>'''

    return divider, page


def extract_article_meta(md_text: str) -> tuple[str, str, str]:
    """Extract title (h1), lead (blockquote right after h1), and body (rest).
    Body = original markdown minus the h1 line and the leading blockquote."""
    lines = md_text.splitlines()
    title = ""
    lead = ""
    i = 0
    # Find h1
    while i < len(lines):
        if lines[i].startswith("# "):
            title = lines[i][2:].strip()
            i += 1
            break
        i += 1
    # Skip blank
    while i < len(lines) and not lines[i].strip():
        i += 1
    # Blockquote lead
    if i < len(lines) and lines[i].startswith("> "):
        lead_lines = []
        while i < len(lines) and lines[i].startswith("> "):
            lead_lines.append(lines[i][2:].strip())
            i += 1
        lead = " ".join(lead_lines).strip()
        # Strip "마지막 업데이트: YYYY-MM-DD"
        lead = re.sub(r"\s*마지막 업데이트:\s*\d{4}-\d{2}-\d{2}\.?\s*$", ".", lead).strip()

    body = "\n".join(lines[i:])
    return title, lead, body


# ----- Full packet for a given day ------------------------------------------

PAGE_HEAD = '''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>{title}</title>
<meta name="viewport" content="width=210mm">
<link rel="stylesheet" href="../assets/print.css">
<style>
  /* Mermaid wrapper sizing inside A4 */
  .mermaid-wrap {{ text-align: center; margin: 4mm 0 6mm 0; break-inside: avoid; }}
  .mermaid-wrap svg {{ max-width: 100%; height: auto; }}
  .article-body img,
  .section__body--rich img {{ max-width: 100%; height: auto; display: block; margin: 3mm auto 4mm; }}
  .section__body--rich img {{ max-height: 80mm; }}
  .article-body img {{ max-height: 110mm; }}
</style>
</head>
<body>

<div class="screen-bar no-print">
  <span class="screen-bar__title">{screen_title}</span>
  <div class="screen-bar__actions">
    <a class="screen-bar__btn screen-bar__btn--ghost" href="../index.html">← Index</a>
    <button class="screen-bar__btn" onclick="window.print()">🖨 Print A4</button>
  </div>
</div>
'''

PAGE_FOOT = '''
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script>
  mermaid.initialize({
    startOnLoad: true,
    theme: 'base',
    themeVariables: {
      fontFamily: '"Pretendard Variable", Pretendard, system-ui, sans-serif',
      fontSize: '13px',
      primaryColor: '#e5eaf2',
      primaryTextColor: '#111418',
      primaryBorderColor: '#1a2e4a',
      lineColor: '#3a414a',
      secondaryColor: '#fff7d6',
      tertiaryColor: '#f7f5ef'
    },
    flowchart: { htmlLabels: true, curve: 'basis', useMaxWidth: true },
    sequence: { useMaxWidth: true },
    gantt: { useMaxWidth: true }
  });
</script>
</body>
</html>
'''


def build_packet(day: int) -> str:
    day_md = ROOT / "curriculum" / f"day_{day:02d}.md"
    if not day_md.exists():
        raise FileNotFoundError(f"Missing: {day_md}")

    day_text = day_md.read_text(encoding="utf-8")
    day_data = parse_day_md(day_text)

    # Task sheet
    task_sheet_html = render_task_sheet(day, day_data)

    # Linked notes → article pages
    articles_html = []
    linked = linked_note_files(day_data, day_md)

    for kind, note_path in linked:
        note_text = note_path.read_text(encoding="utf-8")
        title, lead, body = extract_article_meta(note_text)
        body_html = split_article_blocks(body)
        path_rel = str(note_path.relative_to(ROOT)).replace(os.sep, "/")
        divider, page = render_article(
            kind=kind,
            title=title,
            lead=lead,
            path_rel=path_rel,
            body_html=body_html,
            day=day,
        )
        articles_html.append(divider)
        articles_html.append(page)

    full = (
        PAGE_HEAD.format(
            title=f"Day {day:02d} — {day_data['title']}",
            screen_title=f"AML Notes · Day {day:02d} · Study Packet",
        )
        + task_sheet_html
        + "\n".join(articles_html)
        + PAGE_FOOT
    )
    return full


# ----- CLI ------------------------------------------------------------------

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    DAYS_OUT.mkdir(parents=True, exist_ok=True)

    if args == ["all"]:
        days = list(range(1, 61))
    else:
        days = []
        for a in args:
            if "-" in a:
                s, e = a.split("-")
                days.extend(range(int(s), int(e) + 1))
            else:
                days.append(int(a))

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    for d in days:
        try:
            html_out = build_packet(d)
            out_path = DAYS_OUT / f"day_{d:02d}.html"
            out_path.write_text(html_out, encoding="utf-8")
            print(f"[OK]  day_{d:02d}.html  ({len(html_out):,} bytes)")
        except Exception as e:
            print(f"[FAIL] day_{d:02d}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
