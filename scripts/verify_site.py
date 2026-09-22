#!/usr/bin/env python3
"""Verify localization, canonical URLs, metadata and sitemap."""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
PAGES = (
    "index", "ict-governance", "cvd-security-research", "bug-bounty",
    "cyber-resilience", "civil-protection", "election-resilience",
    "institutional-accountability", "evidence-register", "methodology", "roadmap",
    "ict-lifecycle-traceability", "cvd-authorization-framework",
    "vulnerability-prioritisation", "degraded-operations",
    "skeptical-review", "compliance-boundaries",
)

def base_url() -> str:
    cfg = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    value = cfg.get("site_url")
    if not isinstance(value, str) or not value.startswith("https://"):
        raise ValueError("mkdocs.yml must define an HTTPS site_url")
    return value.rstrip("/") + "/"

BASE = base_url()

class HeadParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.language = None
        self.canonical = None
        self.alternates = {}
        self.description = None
        self.properties = {}

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "html":
            self.language = values.get("lang")
        elif tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href")
        elif tag == "link" and values.get("rel") == "alternate":
            lang, href = values.get("hreflang"), values.get("href")
            if lang and href:
                self.alternates[lang] = href
        elif tag == "meta" and values.get("name") == "description":
            self.description = values.get("content")
        elif tag == "meta" and values.get("property") and values.get("content"):
            self.properties[values["property"]] = values["content"]

def page_path(locale: str, page: str) -> Path:
    prefix = Path() if locale == "en" else Path("lv")
    leaf = "index.html" if page == "index" else f"{page}/index.html"
    return SITE / prefix / leaf

def page_url(locale: str, page: str) -> str:
    lp = "" if locale == "en" else "lv/"
    pp = "" if page == "index" else f"{page}/"
    return BASE + lp + pp

def verify() -> list[str]:
    errors = []
    descriptions = set()
    expected_urls = set()

    for locale in ("en", "lv"):
        for page in PAGES:
            path = page_path(locale, page)
            expected = page_url(locale, page)
            expected_urls.add(expected)
            if not path.is_file():
                errors.append(f"missing built page: {path.relative_to(ROOT)}")
                continue

            parser = HeadParser()
            parser.feed(path.read_text(encoding="utf-8"))

            if parser.language != locale:
                errors.append(f"wrong html lang: {path.relative_to(ROOT)}")
            if parser.canonical != expected:
                errors.append(f"wrong canonical: {path.relative_to(ROOT)}")

            for lang in ("en", "lv"):
                if parser.alternates.get(lang) != page_url(lang, page):
                    errors.append(
                        f"missing/wrong {lang} alternate: {path.relative_to(ROOT)}"
                    )
            if parser.alternates.get("x-default") != page_url("en", page):
                errors.append(f"missing/wrong x-default: {path.relative_to(ROOT)}")

            if not parser.description:
                errors.append(f"missing meta description: {path.relative_to(ROOT)}")
            elif parser.description in descriptions:
                errors.append(f"duplicate meta description: {path.relative_to(ROOT)}")
            else:
                descriptions.add(parser.description)

            expected_og = {"og:type": "website", "og:url": expected}
            for key, value in expected_og.items():
                if parser.properties.get(key) != value:
                    errors.append(f"missing/wrong {key}: {path.relative_to(ROOT)}")
            for key in ("og:title", "og:description"):
                if not parser.properties.get(key):
                    errors.append(f"missing {key}: {path.relative_to(ROOT)}")

    sitemap = SITE / "sitemap.xml"
    if not sitemap.is_file():
        errors.append("missing sitemap.xml")
    else:
        root = ET.parse(sitemap).getroot()
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        actual = {
            node.text
            for node in root.findall("sm:url/sm:loc", ns)
            if node.text
        }
        missing = expected_urls - actual
        if missing:
            errors.append("sitemap missing: " + ", ".join(sorted(missing)))

    return errors

def main() -> int:
    errors = verify()
    if errors:
        print(f"Built-site verification failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Built-site verification passed: {len(PAGES) * 2} localized pages.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
