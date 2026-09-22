---
title: ICT lifecycle traceability
description: Evidence-bounded project module with controls and pilot acceptance criteria.
---

# ICT lifecycle traceability

Public-sector ICT assurance can contain many artefacts without a reliable chain connecting a service, approved change, deployed release, accountable owner and supporting evidence. VIRSIS already covers state ICT resources and VARAM says ICT development activity descriptions have been moving gradually into VIRSIS since Q3 2025. The project therefore proposes a minimal evidence pointer, not another central evidence warehouse.

## Project proposal

`service → change → approval → build/release → deployment → verification → incident/exception → retirement`

The authoritative artefact stays in its source system. Controls require authoritative-system ownership, minimal pointers, change-to-release linkage and emergency-change reconciliation.

## Pilot

Use one non-classified public-sector service and one bounded release cycle. PASS means an auditor can reconstruct the lifecycle without undocumented human memory and without copying source code, secrets or restricted evidence into a new repository.

## Boundary

This is a project architecture pattern, not a statutory requirement. Machine-readable proposal: `ict_lifecycle_traceability`.
