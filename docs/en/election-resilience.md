---
title: Election and critical-process resilience
description: Neutral technical continuity controls for elections and other critical public processes without political advocacy.
---

# Election and critical-process resilience

## Scope

This page concerns technical and organisational resilience. It does not evaluate parties, candidates, voting choices, campaign messages, or electoral outcomes.

## Source-backed baseline

EU election-cybersecurity guidance addresses risk management, information sharing, awareness and training, incident management, and controls across the election cycle.

## Project continuity pattern

The repository uses the following **project-defined** state model:

`NORMAL → DEGRADED → OFFLINE/MANUAL → RECOVERY/RECONCILIATION`

It is not presented as an official Latvian election-state taxonomy.

Useful control questions include:

- What is the authoritative record?
- Which public-facing system can fail without changing the authoritative result?
- What are the Go/No-Go gates?
- Which fallback paths have been tested?
- What is frozen before the critical event?
- How are emergency changes approved, logged and rolled back?
- How are manual and automated records reconciled after recovery?
- Who coordinates cross-institution incidents and public communication?

Relevant evidence: `election_resilience_controls`, `election_state_model_project_pattern`.
