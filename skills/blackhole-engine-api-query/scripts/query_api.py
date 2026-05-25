#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Section:
    level: int
    title: str
    line_no: int
    path: tuple[str, ...]
    content: str


def clean_heading(raw: str) -> str:
    raw = re.sub(r"\s*\{#.*?\}\s*$", "", raw).strip()
    raw = raw.strip("#").strip()
    return re.sub(r"\s+", " ", raw)


def canon(value: str) -> str:
    return re.sub(r"[\s`*_#{}\[\]()/\\:：,，.;。'\"]+", "", value).lower()


def load_sections(doc_path: Path) -> list[Section]:
    text = doc_path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    heading_re = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
    headings: list[dict[str, object]] = []
    stack: list[tuple[int, str]] = []

    for idx, line in enumerate(lines):
        match = heading_re.match(line)
        if not match:
            continue
        level = len(match.group(1))
        title = clean_heading(match.group(2))
        stack = [(lvl, name) for lvl, name in stack if lvl < level]
        path = tuple(name for _, name in stack) + (title,)
        headings.append(
            {
                "level": level,
                "title": title,
                "line_no": idx + 1,
                "path": path,
            }
        )
        stack.append((level, title))

    sections: list[Section] = []
    for idx, heading in enumerate(headings):
        level = int(heading["level"])
        start = int(heading["line_no"]) - 1
        end = len(lines)
        for next_heading in headings[idx + 1 :]:
            if int(next_heading["level"]) <= level:
                end = int(next_heading["line_no"]) - 1
                break
        sections.append(
            Section(
                level=level,
                title=str(heading["title"]),
                line_no=int(heading["line_no"]),
                path=tuple(heading["path"]),  # type: ignore[arg-type]
                content="\n".join(lines[start:end]).strip(),
            )
        )
    return sections


def query_variants(query: str) -> list[str]:
    variants = {query.strip()}
    dotted_parts = re.split(r"[.\s]+", query.strip())
    if dotted_parts:
        variants.add(dotted_parts[-1])
    variants.add(query.replace("BlackHole3D.", ""))
    variants.add(query.replace("BlackHole3D", ""))
    return [variant for variant in variants if variant.strip()]


def score_section(section: Section, query: str, exact: bool) -> int:
    variants = query_variants(query)
    terms = [canon(term) for term in re.split(r"\s+", query) if canon(term)]
    full_query = canon(query)
    title = canon(section.title)
    path = canon(" ".join(section.path))
    content = canon(section.content)
    best = 0

    if full_query and full_query in path:
        best = max(best, 96)
    if terms and all(term in path for term in terms):
        best = max(best, 94)

    for variant in variants:
        q = canon(variant)
        if not q:
            continue
        if title == q:
            if q == full_query or len(terms) <= 1:
                best = max(best, 100)
            elif terms and all(term in path for term in terms):
                best = max(best, 98)
            else:
                best = max(best, 82)
        elif exact:
            continue
        elif title.endswith(q):
            best = max(best, 92)
        elif q in title:
            best = max(best, 85)
        elif q in path:
            best = max(best, 70)
        elif q in content:
            best = max(best, 45)

    if not exact:
        if terms and all(term in content for term in terms):
            best = max(best, 40)

    return best


def find_matches(
    sections: list[Section],
    query: str,
    exact: bool,
    max_matches: int,
) -> list[tuple[int, Section]]:
    scored = [
        (score_section(section, query, exact), section)
        for section in sections
        if score_section(section, query, exact) > 0
    ]
    if any(score == 100 for score, _ in scored):
        scored = [(score, section) for score, section in scored if score == 100]
    elif any(score >= 94 for score, _ in scored):
        scored = [(score, section) for score, section in scored if score >= 94]
    elif any(score >= 70 for score, _ in scored):
        scored = [(score, section) for score, section in scored if score >= 70]
    scored.sort(key=lambda item: (-item[0], item[1].line_no))
    return scored[:max_matches]


def truncate(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "\n\n[truncated]"


def print_titles(matches: list[tuple[int, Section]], doc_path: Path) -> None:
    for score, section in matches:
        path = " > ".join(section.path)
        print(f"{score:3d}  {doc_path}:{section.line_no}  {path}")


def print_sections(matches: list[tuple[int, Section]], doc_path: Path, max_chars: int) -> None:
    for index, (score, section) in enumerate(matches, start=1):
        path = " > ".join(section.path)
        if index > 1:
            print("\n" + "=" * 80 + "\n")
        print(f"# Match {index} (score {score})")
        print(f"Source: {doc_path}:{section.line_no}")
        print(f"Path: {path}\n")
        print(truncate(section.content, max_chars))


def suggest_titles(sections: list[Section], query: str) -> list[str]:
    titles = sorted({" > ".join(section.path) for section in sections})
    return difflib.get_close_matches(query, titles, n=8, cutoff=0.25)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Search BlackHole Engine API sections from the bundled Markdown reference."
    )
    parser.add_argument("query", nargs="+", help="API name, module name, event name, or keywords")
    parser.add_argument(
        "--doc",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "references" / "blackhole-engine-api.md",
        help="Path to the API Markdown document.",
    )
    parser.add_argument("--exact", action="store_true", help="Only match exact normalized titles.")
    parser.add_argument("--titles", action="store_true", help="Print matching section titles only.")
    parser.add_argument("--max-matches", type=int, default=5, help="Maximum number of matches.")
    parser.add_argument("--max-chars", type=int, default=8000, help="Maximum characters per section.")
    args = parser.parse_args()

    query = " ".join(args.query).strip()
    if not args.doc.exists():
        print(f"Document not found: {args.doc}", file=sys.stderr)
        return 2

    sections = load_sections(args.doc)
    matches = find_matches(sections, query, args.exact, args.max_matches)
    if not matches:
        print(f"No matches for: {query}")
        suggestions = suggest_titles(sections, query)
        if suggestions:
            print("\nClosest section paths:")
            for suggestion in suggestions:
                print(f"- {suggestion}")
        return 1

    if args.titles:
        print_titles(matches, args.doc)
    else:
        print_sections(matches, args.doc, args.max_chars)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
