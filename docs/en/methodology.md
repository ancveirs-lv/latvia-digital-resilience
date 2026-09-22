---
title: Methodology
description: Source hierarchy, claim types, legal and political neutrality boundaries, bilingual parity and change-control rules.
---

# Methodology

## Source hierarchy

| Level | Source type | Use |
|---|---|---|
| 1 | Latvian legislation and official institutional records | Legal duties, official capabilities and mandates |
| 2 | EUR-Lex and EU institutional material | EU legal and policy context |
| 3 | CERT.LV, ENISA, FIRST, IETF, NIST and comparable bodies | Technical definitions and operational guidance |
| 4 | Standards and peer-reviewed research | Methods, models and independent evidence |
| 5 | Secondary analysis | Context when stronger sources are unavailable |

## Claim types

- `source_fact` — a factual proposition supported by cited material;
- `boundary` — a statement constraining an over-broad interpretation;
- `project_recommendation` — this project's proposed design or policy choice;
- `editorial_policy` — rules for how the repository communicates.

A `project_recommendation` does not become law, official policy, or institutional consensus because it cites context.

## Review rules

Every evidence record carries a review date. Material changes require source review, bilingual parity, local validation, tests, and a strict site build.

Election-related content remains neutral and technical. Legal propositions are tied to jurisdiction and source text. Operational security detail is minimised.

## Ten-lens adversarial review

Material proposals are reviewed through ten fixed skeptical lenses: legal/regulatory, system owner, architecture, SOC/CSIRT, security researcher, privacy/DPO, procurement/finance, municipal/civil protection, election-process owner, and independent auditor/public.

This is a project method, not a substitute for external review. `pilot_ready` means bounded scope, machine-readable controls, acceptance criteria and explicit non-goals; it does not mean nationwide suitability or legal approval.

The canonical proposal-specific skeptical-review findings are stored in `data/reviews.yaml`; CI requires exactly one finding for each of the ten lenses for every proposal.
