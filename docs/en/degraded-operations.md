---
title: Degraded operations and recovery
description: Continuity proposal for critical public processes covering degraded and manual states, authoritative records, tested fallback and recovery reconciliation.
---

# Degraded operations and recovery

NIS2 includes incident handling and business continuity among cybersecurity risk-management measures. This repository uses a **project-defined**, non-normative model: `NORMAL → DEGRADED → OFFLINE/MANUAL → RECOVERY/RECONCILIATION`.

## Design rules

Public availability is not automatically the authoritative record. Fallback must be exercised. Manual operation needs explicit ownership. Recovery reconciles queued, manual and automated records. Conflict is handled explicitly. Public assurance must not expose sensitive recovery detail.

## Pilot

Run a tabletop and controlled exercise for one critical process. PASS requires the authoritative record to remain identifiable and every test record to be reconciled or explicitly marked as a conflict. Machine-readable proposal: `degraded_operations_framework`.
