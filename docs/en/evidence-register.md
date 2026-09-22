---
title: Evidence register
description: Claim-level evidence boundaries for Latvia Digital Resilience proposals and source-backed factual statements.
---

# Evidence register

The canonical machine-readable register is `data/claims.yaml`; source metadata is in `data/sources.yaml`.

| Claim ID | Area | Type | Evidence boundary |
|---|---|---|---|
| `ict_existing_virsis_capability` | ICT governance | Source fact | Existing VIRSIS capability |
| `ict_reuse_before_duplication` | ICT governance | Project recommendation | Reuse-first design principle |
| `cvd_national_framework` | CVD | Source fact | National framework and CERT.LV role |
| `cvd_program_scope` | CVD | Source fact | Programme-specific scope and conditions |
| `cvd_not_pentest` | CVD | Boundary | CVD reporting is not a full pentest |
| `security_txt_not_permission` | CVD | Boundary | Contact discovery is not testing permission |
| `bug_bounty_distinct_incentive` | Bug Bounty | Boundary | Reward layer is distinct from disclosure scope |
| `cyber_resilience_inventory_patch_segment` | Cyber resilience | Source fact | Inventory, patching, segmentation and CVD |
| `cyber_legal_and_technical_layers` | Cyber resilience | Project recommendation | Technical scoring does not replace duties |
| `vuln_signals_are_distinct` | Cyber resilience | Source fact | CVSS, EPSS and KEV measure different things |
| `civil_existing_capabilities` | Civil protection | Source fact | 112 Latvija and VUCAP already exist |
| `civil_reuse_existing_capabilities` | Civil protection | Project recommendation | Map and reuse before duplication |
| `election_resilience_controls` | Elections | Source fact | EU election-cybersecurity control areas |
| `election_state_model_project_pattern` | Elections | Project recommendation | Project state model, not official taxonomy |
| `accountability_whistleblowing_boundary` | Accountability | Boundary | Public-interest whistleblowing vs personal grievance |

## Citation semantics

`defines` means the source directly defines or formally establishes the point. `supports` means it provides direct support without being the sole formal definition. `limits` means it is used specifically to constrain an over-broad interpretation. `context` means it informs a project recommendation but does not make the recommendation mandatory.

A primary source proves what that source establishes; it does not automatically prove every downstream inference.
