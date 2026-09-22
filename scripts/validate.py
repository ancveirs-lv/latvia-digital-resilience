#!/usr/bin/env python3
"""Validate bilingual documentation, structured evidence, metadata and local links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

DATASETS = (
    (ROOT / "data/sources.yaml", ROOT / "schemas/sources.schema.json"),
    (ROOT / "data/claims.yaml", ROOT / "schemas/claims.schema.json"),
)

PAGES = (
    "index.md",
    "ict-governance.md",
    "cvd-security-research.md",
    "bug-bounty.md",
    "cyber-resilience.md",
    "civil-protection.md",
    "election-resilience.md",
    "institutional-accountability.md",
    "evidence-register.md",
    "methodology.md",
    "roadmap.md",
)

REQUIRED_FILES = (
    "README.md", "README.lv.md",
    "CONTRIBUTING.md", "CONTRIBUTING.lv.md",
    "SECURITY.md", "SECURITY.lv.md",
    "GOVERNANCE.md", "GOVERNANCE.lv.md",
    "INSTALL.md", "INSTALL.lv.md",
    "LICENSE", "LICENSE-CODE", "LICENSE-CONTENT",
    "CITATION.cff", "CHANGELOG.md",
    "mkdocs.yml", "requirements.in", "requirements.txt", "Makefile",
)

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def load_yaml(path: Path) -> dict:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a mapping")
    return value


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_schema(data_path: Path, schema_path: Path) -> list[str]:
    validator = Draft202012Validator(
        load_json(schema_path), format_checker=FormatChecker()
    )
    errors = []
    for error in sorted(
        validator.iter_errors(load_yaml(data_path)),
        key=lambda value: list(value.path),
    ):
        loc = ".".join(str(p) for p in error.path) or "<root>"
        errors.append(f"{data_path.relative_to(ROOT)}:{loc}: {error.message}")
    return errors


def validate_required_files() -> list[str]:
    return [
        f"missing required file: {path}"
        for path in REQUIRED_FILES
        if not (ROOT / path).is_file()
    ]


def validate_language_pairs() -> list[str]:
    errors = []
    for page in PAGES:
        lv = DOCS / "lv" / page
        en = DOCS / "en" / page
        if not lv.is_file():
            errors.append(f"missing language page: docs/lv/{page}")
        if not en.is_file():
            errors.append(f"missing language page: docs/en/{page}")
        if lv.is_file() and en.is_file():
            def sig(path: Path) -> tuple[int, int, int]:
                lines = path.read_text(encoding="utf-8").splitlines()
                return (
                    sum(line.startswith("## ") for line in lines),
                    sum(line.startswith("|---") for line in lines),
                    sum(line.startswith("!!! ") for line in lines),
                )
            if sig(lv) != sig(en):
                errors.append(
                    f"language-pair structure differs: docs/lv/{page} {sig(lv)} "
                    f"!= docs/en/{page} {sig(en)}"
                )
    return errors


def validate_page_metadata() -> list[str]:
    errors = []
    descriptions = set()
    for locale in ("en", "lv"):
        for page in PAGES:
            path = DOCS / locale / page
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---\n") or "\n---\n" not in text[4:]:
                errors.append(f"missing YAML front matter: {path.relative_to(ROOT)}")
                continue
            _, fm, _ = text.split("---", 2)
            meta = yaml.safe_load(fm)
            if not isinstance(meta, dict):
                errors.append(f"invalid front matter: {path.relative_to(ROOT)}")
                continue
            for key in ("title", "description"):
                val = meta.get(key)
                if not isinstance(val, str) or not val.strip():
                    errors.append(f"missing {key}: {path.relative_to(ROOT)}")
            desc = meta.get("description")
            if isinstance(desc, str):
                if desc in descriptions:
                    errors.append(f"duplicate description: {path.relative_to(ROOT)}")
                descriptions.add(desc)
    return errors


def validate_evidence() -> list[str]:
    errors = []
    sources = load_yaml(ROOT / "data/sources.yaml")["sources"]
    claims = load_yaml(ROOT / "data/claims.yaml")["claims"]

    source_ids = [s["id"] for s in sources]
    claim_ids = [c["id"] for c in claims]

    if len(source_ids) != len(set(source_ids)):
        errors.append("duplicate source id")
    if len(claim_ids) != len(set(claim_ids)):
        errors.append("duplicate claim id")

    source_map = {s["id"]: s for s in sources}
    claim_map = {c["id"]: c for c in claims}

    urls = [s["url"] for s in sources]
    if len(urls) != len(set(urls)):
        errors.append("duplicate source URL")

    for claim in claims:
        cited = {c["source_id"] for c in claim["citations"]}
        missing = cited - set(source_map)
        if missing:
            errors.append(
                f"claim {claim['id']} cites unknown source(s): {', '.join(sorted(missing))}"
            )
        for sid in cited & set(source_map):
            if claim["id"] not in source_map[sid]["supports"]:
                errors.append(
                    f"one-way evidence relation: {claim['id']} -> {sid}"
                )

    for source in sources:
        for cid in source["supports"]:
            if cid not in claim_map:
                errors.append(f"source {source['id']} supports unknown claim: {cid}")
                continue
            cited = {c["source_id"] for c in claim_map[cid]["citations"]}
            if source["id"] not in cited:
                errors.append(
                    f"one-way evidence relation: {source['id']} -> {cid}"
                )
    return errors


def markdown_files() -> list[Path]:
    return sorted(list(ROOT.glob("*.md")) + list(DOCS.rglob("*.md")))


def validate_local_links() -> list[str]:
    errors = []
    for path in markdown_files():
        for raw in MARKDOWN_LINK.findall(path.read_text(encoding="utf-8")):
            target = raw.strip().split(maxsplit=1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith(("#", "mailto:")):
                continue
            rel = unquote(parsed.path)
            if not rel:
                continue
            resolved = (path.parent / rel).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"local link escapes repository in {path.relative_to(ROOT)}: {target}"
                )
                continue
            if not resolved.is_file():
                errors.append(
                    f"broken local link in {path.relative_to(ROOT)}: {target}"
                )
    return errors


def validate_repository_configuration() -> list[str]:
    errors = []
    mkdocs = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    required = (
        "site_url: https://",
        "docs_structure: folder",
        "locale: en",
        "locale: lv",
        "strict: true",
    )
    for item in required:
        if item not in mkdocs:
            errors.append(f"mkdocs.yml missing required setting: {item}")
    return errors


def run_all() -> list[str]:
    errors = []
    for data_path, schema_path in DATASETS:
        errors.extend(validate_schema(data_path, schema_path))
    errors.extend(validate_required_files())
    errors.extend(validate_language_pairs())
    errors.extend(validate_page_metadata())
    errors.extend(validate_evidence())
    errors.extend(validate_local_links())
    errors.extend(validate_repository_configuration())
    return errors


def main() -> int:
    errors = run_all()
    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    sources = len(load_yaml(ROOT / "data/sources.yaml")["sources"])
    claims = len(load_yaml(ROOT / "data/claims.yaml")["claims"])
    print(
        f"Validation passed: {sources} sources, {claims} evidence claims, "
        f"{len(PAGES)} bilingual document pairs."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
