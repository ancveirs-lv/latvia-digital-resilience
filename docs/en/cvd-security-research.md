---
title: CVD and good-faith security research
description: Precise boundaries between coordinated vulnerability disclosure, programme scope, testing permission and penetration testing in Latvia.
---

# CVD and good-faith security research

## Source-backed baseline

Latvia has a national CVD framework and CERT.LV operates the national vulnerability-reporting platform. Resource owners can publish programme-specific resources and testing conditions.

CVD is a **coordination process**. A programme or policy can define scope and conditions. Those concepts should not be collapsed into a universal permission to test.

CERT.LV also states that vulnerability discovery and reporting through the platform is not equivalent to a full penetration test.

## Boundaries

- `security.txt` helps discover contacts and policy information; RFC 9116 does not make the file itself testing permission.
- Good intent is not a substitute for scope.
- CVD is not a blanket pentest mandate.
- Third-party systems and services require their own authority or applicable terms.
- Data collection should be limited to what is necessary for the permitted proof.

## Project recommendation

A public-sector CVD design should make scope, prohibited actions, evidence minimisation, acknowledgement, triage, remediation communication, disclosure coordination, and safe-harbour language explicit.

Relevant evidence: `cvd_national_framework`, `cvd_program_scope`, `cvd_not_pentest`, `security_txt_not_permission`.
