#!/usr/bin/env python3
"""Check registered evidence URLs; fail only on permanent 404/410."""

from __future__ import annotations

import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import yaml

ROOT = Path(__file__).resolve().parents[1]
PERMANENT = {404, 410}
INCONCLUSIVE = {401, 403, 405, 408, 425, 429}

def check(url: str, attempts: int = 2) -> tuple[str, str]:
    request = Request(
        url,
        headers={"User-Agent": "latvia-digital-resilience-source-health/0.1"},
        method="GET",
    )
    result = ("warning", "unknown")
    for attempt in range(attempts):
        try:
            with urlopen(request, timeout=12) as response:
                code = response.status
                if 200 <= code < 400:
                    return "ok", str(code)
                if code in PERMANENT:
                    return "failed", str(code)
                result = ("warning", str(code))
        except HTTPError as error:
            if error.code in PERMANENT:
                return "failed", str(error.code)
            result = (
                "warning" if error.code in INCONCLUSIVE or error.code >= 500 else "failed",
                str(error.code),
            )
        except (URLError, TimeoutError) as error:
            result = ("warning", error.__class__.__name__)
        if attempt + 1 < attempts:
            time.sleep(1)
    return result

def main() -> int:
    sources = yaml.safe_load(
        (ROOT / "data/sources.yaml").read_text(encoding="utf-8")
    )["sources"]
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(lambda s: check(s["url"]), sources))

    failures = 0
    for source, (state, detail) in zip(sources, results, strict=True):
        print(f"{state.upper():7} {detail:12} {source['id']}: {source['url']}")
        failures += state == "failed"
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
