---
title: Vēlēšanu un kritisku procesu noturība
description: Neitrālas tehniskas darbības nepārtrauktības kontroles vēlēšanām un citiem kritiskiem publiskiem procesiem bez politiskas aģitācijas.
---

# Vēlēšanu un kritisku procesu noturība

## Tvērums

Šī lapa attiecas uz tehnisku un organizatorisku noturību. Tā nevērtē partijas, kandidātus, balsojuma izvēli, kampaņu saturu vai vēlēšanu rezultātu.

## Avotos balstīts pamats

ES vēlēšanu kiberdrošības vadlīnijas aptver risku pārvaldību, informācijas apmaiņu, informētību un mācības, incidentu pārvaldību un kontroles visā vēlēšanu ciklā.

## Projekta nepārtrauktības modelis

Repozitorijā izmantots šāds **projekta veidots** stāvokļu modelis:

`NORMAL → DEGRADED → OFFLINE/MANUAL → RECOVERY/RECONCILIATION`

Tas netiek pasniegts kā oficiāla Latvijas vēlēšanu stāvokļu taksonomija.

Noderīgi kontroles jautājumi:

- Kurš ieraksts ir autoritatīvs?
- Kura publiskā sistēma drīkst būt nepieejama, nemainot autoritatīvo rezultātu?
- Kādi ir Go/No-Go vārti?
- Kuri fallback ceļi ir praktiski notestēti?
- Kas tiek iesaldēts pirms kritiskā notikuma?
- Kā emergency izmaiņas tiek apstiprinātas, reģistrētas un rollbackotas?
- Kā pēc atjaunošanas tiek saskaņoti manuālie un automatizētie ieraksti?
- Kas koordinē starpinstitūciju incidentu un publisko komunikāciju?

Saistītie pierādījumi: `election_resilience_controls`, `election_state_model_project_pattern`.
