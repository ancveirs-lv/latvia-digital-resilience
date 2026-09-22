# Latvia Digital Resilience

[Latviski](README.lv.md) · English

A bilingual, evidence-based public reference for proposals on Latvia's digital governance, cybersecurity, coordinated vulnerability disclosure (CVD), good-faith security research, civil protection, election and critical-process resilience, and institutional accountability.

The project separates four things that are often mixed together:

1. **Source-backed baseline** — what legislation, official systems, institutional guidance, standards, or primary documentation actually establish.
2. **Project recommendation** — what this repository proposes should be changed, piloted, tested, or measured.
3. **Boundary** — what a source or concept does *not* establish.
4. **Validation** — what evidence would show whether a proposal worked.

## Documentation

The published documentation uses separate English and Latvian routes with a language switcher. The source tree mirrors that structure under `docs/en/` and `docs/lv/`.

Core areas:

- public-sector ICT governance and traceability;
- CVD and good-faith security research;
- Bug Bounty and incentive design;
- cybersecurity and digital resilience;
- civil protection and continuity;
- election and critical-process resilience;
- institutional accountability and improvement;
- evidence register and methodology.

## Evidence model

Machine-readable evidence is kept in:

- `data/sources.yaml` — authoritative or technically rigorous sources;
- `data/claims.yaml` — claim-level records with source locators, jurisdiction/context, and review dates;
- `data/proposals.yaml` — bounded project proposals with explicit normative status and non-goals;
- `data/controls.yaml` — verifiable controls linked to proposals;
- `data/pilots.yaml` — bounded pilot scope, prerequisites and predeclared acceptance evidence;
- `data/reviews.yaml` — 40 proposal-specific skeptical-review findings: four proposals × ten fixed review lenses;
- `schemas/` — JSON Schemas used by CI.

A source citation does not automatically prove every statement on a page. The evidence register records what a source **defines, supports, limits, or contextualises**.

## Quality gates

Pull requests and `main` are designed to be checked for:

- bilingual page parity;
- YAML/JSON Schema validity;
- claim/source cross-reference integrity;
- proposal/control/pilot graph integrity and complete ten-lens review coverage;
- local-link integrity;
- required page metadata;
- strict MkDocs build;
- canonical URLs and `hreflang`;
- monthly source-health checks;
- tests and least-privilege GitHub Actions.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --require-hashes -r requirements.txt
make check
mkdocs serve
```

See [INSTALL.md](INSTALL.md).

## Editorial boundary

This is not a party-political programme, campaign tool, allegation archive, legal opinion, penetration-testing mandate, or incident-response channel. Election-related material is limited to technical and organisational resilience controls and does not endorse or oppose a candidate, party, or electoral choice.

## Licensing and citation

- Code and automation: [MIT](LICENSE-CODE)
- Documentation and structured data: [CC BY 4.0](LICENSE-CONTENT)
- Citation metadata: [CITATION.cff](CITATION.cff)

Maintainer: Zigmārs Ancveirs
