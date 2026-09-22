---
title: Degradēta darbība un atjaunošana
description: Kritisku publisku procesu nepārtrauktības priekšlikums ar degradētu un manuālu darbību, autoritatīvu ierakstu, pārbaudītu fallback un atjaunošanas saskaņošanu.
---

# Degradēta darbība un atjaunošana

NIS2 ietver incidentu pārvaldību un darbības nepārtrauktību kiberdrošības risku pārvaldības pasākumos. Repozitorijs izmanto **projekta veidotu**, nenormatīvu modeli: `NORMAL → DEGRADED → OFFLINE/MANUAL → RECOVERY/RECONCILIATION`.

## Dizaina noteikumi

Publiskā pieejamība automātiski nenozīmē autoritatīvu ierakstu. Fallback ir jāvingrina. Manuālai darbībai vajadzīga skaidra atbildība. Atjaunošanā saskaņo rindā esošos, manuālos un automatizētos ierakstus. Konflikti tiek apstrādāti skaidri. Publisks gatavības apliecinājums neatklāj sensitīvas atjaunošanas detaļas.

## Pilots

Veic galda un kontrolētu praktisku vingrinājumu vienam kritiskam procesam. PASS prasa, lai autoritatīvais ieraksts paliek identificējams un katrs testa ieraksts tiek saskaņots vai skaidri marķēts kā konflikts. Mašīnlasāmais priekšlikums: `degraded_operations_framework`.
