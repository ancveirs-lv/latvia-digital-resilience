---
title: Ten-lens skeptical review
description: Adversarial review of four resilience proposals from ten fixed stakeholder perspectives.
---

# Ten-lens skeptical review

This is a **structured adversarial review method**, not a claim that ten independent external reviewers endorsed the proposals.

| Lens | Strongest objection | Required response |
|---|---|---|
| Legal / regulatory | Are recommendations being presented as law or authorisation? | Mark normative status and cite exact jurisdiction/source. |
| System owner | Does this duplicate authoritative data or reporting? | Reuse-first design and measure duplication. |
| Architecture | Is this a centralised shadow system? | Minimal pointers and explicit source systems. |
| SOC / CSIRT | Does paperwork slow response? | Generate evidence from workflow, not after the event. |
| Security researcher | Is scope or safe-harbour ambiguous? | Publish assets, conduct, stop conditions and third-party boundary. |
| Privacy / DPO | Is sensitive data copied unnecessarily? | Minimise data and use controlled references. |
| Procurement / finance | Is a new platform proposed before a measurable gap? | Pilot existing tools first and quantify cost. |
| Municipal / civil protection | Can it work under dependency or staffing loss? | Provide degraded/manual modes and exercises. |
| Election process owner | Could publication or testing create process risk? | Separate public assurance from sensitive detail and constrain testing. |
| Independent auditor / public | Is success self-declared? | Predeclare acceptance criteria and evidence artefacts. |

## Findings

**ICT traceability:** risk of a duplicate warehouse; require capability mapping against VIRSIS first.

**CVD:** risk of false confidence about permission; require explicit scope, authority, stop conditions and third-party boundaries.

**Vulnerability prioritisation:** risk of false precision; preserve signal provenance and explainable decisions.

**Degraded operations:** risk of paper-only continuity; exercise transitions and reconciliation.

## Disposition

All four proposals are suitable for **bounded pilots**, not automatic nationwide mandates. Promotion beyond `pilot_ready` requires documented outcomes and applicable legal, privacy, security and operational review.

The canonical proposal-specific 4 × 10 review matrix is stored in `data/reviews.yaml` and is completeness-checked by CI.
