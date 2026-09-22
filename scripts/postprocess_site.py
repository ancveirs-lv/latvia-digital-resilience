#!/usr/bin/env python3
"""Make hreflang URLs absolute and add x-default."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
CANONICAL = re.compile(r'<link\s+rel="canonical"\s+href="([^"]+)"\s*>')
ALTERNATE = re.compile(
    r'<link\s+rel="alternate"\s+href="([^"]+)"\s+hreflang="([^"]+)"\s*>'
)

def process(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    match = CANONICAL.search(text)
    if not match:
        return
    canonical = match.group(1)
    alternates: dict[str, str] = {}

    def repl(match: re.Match[str]) -> str:
        href, locale = match.groups()
        absolute = urljoin(canonical, href)
        alternates[locale] = absolute
        return f'<link rel="alternate" hreflang="{locale}" href="{absolute}">'

    text = ALTERNATE.sub(repl, text)
    if "en" not in alternates:
        raise ValueError(f"missing English alternate: {path.relative_to(ROOT)}")
    if 'hreflang="x-default"' not in text:
        tag = (
            f'<link rel="alternate" hreflang="x-default" '
            f'href="{alternates["en"]}">'
        )
        text = text.replace("</head>", f"  {tag}\n</head>", 1)
    path.write_text(text, encoding="utf-8")

def main() -> int:
    for path in sorted(SITE.rglob("*.html")):
        process(path)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
