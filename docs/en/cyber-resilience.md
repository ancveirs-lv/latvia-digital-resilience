---
title: Cybersecurity and digital resilience
description: Asset awareness, vulnerability prioritisation, lifecycle security and incident readiness without collapsing technical signals into legal obligations.
---

# Cybersecurity and digital resilience

## Source-backed baseline

CERT.LV's 2026 guidance emphasises knowing externally and internally exposed assets, patching, segmentation, and organised vulnerability handling.

The EU legal layer includes risk-management duties and product-lifecycle cybersecurity requirements. Technical prioritisation remains a separate analytical layer.

## Vulnerability signals

| Signal | Primary question |
|---|---|
| CVSS | How severe are the vulnerability characteristics and impact under the scoring model? |
| EPSS | How likely is exploitation in the wild within the model's prediction horizon? |
| KEV | Is the vulnerability in CISA's catalogue of known exploited vulnerabilities? |

These signals are not interchangeable.

## Project recommendation

Use an auditable decision record combining asset criticality, exposure, technical severity, exploitation evidence or probability, compensating controls, remediation feasibility, and applicable legal/contractual deadlines.

Relevant evidence: `cyber_resilience_inventory_patch_segment`, `cyber_legal_and_technical_layers`, `vuln_signals_are_distinct`.
