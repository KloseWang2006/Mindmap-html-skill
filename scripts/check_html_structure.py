#!/usr/bin/env python3
"""Read-only structural checks for generated lecture mind-map HTML files."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path


class BasicHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.start_tags: list[str] = []
        self.end_tags: list[str] = []
        self.titles: list[str] = []
        self._in_title = False

    def handle_starttag(self, tag: str, attrs) -> None:  # type: ignore[no-untyped-def]
        self.start_tags.append(tag.lower())
        if tag.lower() == "title":
            self._in_title = True

    def handle_endtag(self, tag: str) -> None:
        self.end_tags.append(tag.lower())
        if tag.lower() == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title and data.strip():
            self.titles.append(data.strip())


def check_file(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    parser = BasicHTMLParser()
    parser.feed(text)
    lower = text.lower()
    return {
        "file": str(path),
        "doctype": "<!doctype html" in lower,
        "html": "html" in parser.start_tags and "html" in parser.end_tags,
        "head": "head" in parser.start_tags and "head" in parser.end_tags,
        "body": "body" in parser.start_tags and "body" in parser.end_tags,
        "title": parser.titles[0] if parser.titles else "",
        "container_refs": text.count('class="container"') + text.count("class='container'"),
        "section_cards": text.count('class="section '),
        "section_headers": text.count("section-header"),
        "tree_nodes": text.count("tree-level-1"),
        "tables": text.count("<table"),
        "lines": text.count("\n") + 1,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Check lecture mind-map HTML structure without modifying files.")
    parser.add_argument("html", nargs="+", help="HTML file(s) to inspect")
    args = parser.parse_args()

    failed = False
    for raw in args.html:
        path = Path(raw)
        if not path.exists():
            print(f"[MISSING] {path}")
            failed = True
            continue
        result = check_file(path)
        required = ["doctype", "html", "head", "body"]
        ok = all(bool(result[key]) for key in required) and bool(result["title"])
        status = "OK" if ok else "CHECK"
        if not ok:
            failed = True
        print(f"[{status}] {result['file']}")
        print(
            "  title={title!r} lines={lines} container_refs={container_refs} "
            "section_cards={section_cards} section_headers={section_headers} "
            "tree_nodes={tree_nodes} tables={tables}".format(**result)
        )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
