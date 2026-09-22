---
title: ICT governance and traceability
description: Reuse-first evidence and lifecycle traceability for Latvian public-sector ICT without duplicating existing state registries.
---

# ICT governance and traceability

## Source-backed baseline

VIRSIS already records information about state information systems, information resources, and technology resources and services. The applicable VIRSIS rules define a formal management and registration scope. See `ict_existing_virsis_capability`.

## Project recommendation

Before creating a new central register, evidence hub, or lifecycle database:

1. map the requested fields and workflows against VIRSIS and existing shared services;
2. identify the exact gap;
3. keep sensitive evidence in its authoritative controlled system where possible;
4. index only the minimum metadata needed to prove state, ownership, integrity, and traceability.

A minimal evidence profile can look like:

`ID + type + hash + status + owner + controlled reference + mapping`

This is a **project pattern**, not a claim that current law requires this exact schema.

## Validation

A pilot should show reduced duplicate entry, demonstrable provenance, controlled access, and an auditable path from an ICT resource to the authoritative evidence supporting a decision.

Relevant evidence: `ict_existing_virsis_capability`, `ict_reuse_before_duplication`.
