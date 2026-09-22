---
title: Pierādījumu reģistrs
description: Apgalvojumu līmeņa pierādījumu robežas Latvijas digitālās noturības priekšlikumiem un avotos balstītiem faktiem.
---

# Pierādījumu reģistrs

Kanoniskais mašīnlasāmais reģistrs ir `data/claims.yaml`, bet avotu metadati — `data/sources.yaml`.

| Apgalvojuma ID | Joma | Tips | Pierādījumu robeža |
|---|---|---|---|
| `ict_existing_virsis_capability` | IKT pārvaldība | Avota fakts | Esošā VIRSIS spēja |
| `ict_reuse_before_duplication` | IKT pārvaldība | Projekta priekšlikums | Esošo spēju izmantošana pirms dublēšanas |
| `cvd_national_framework` | CVD | Avota fakts | Nacionālais ietvars un CERT.LV loma |
| `cvd_program_scope` | CVD | Avota fakts | Programmas specifiskais tvērums un nosacījumi |
| `cvd_not_pentest` | CVD | Robeža | CVD ziņošana nav pilnvērtīgs pentests |
| `security_txt_not_permission` | CVD | Robeža | Kontakta atrašana nav testēšanas atļauja |
| `bug_bounty_distinct_incentive` | Bug Bounty | Robeža | Atlīdzības slānis atšķiras no disclosure tvēruma |
| `cyber_resilience_inventory_patch_segment` | Kibernoturība | Avota fakts | Uzskaite, ielāpi, segmentācija un CVD |
| `cyber_legal_and_technical_layers` | Kibernoturība | Projekta priekšlikums | Tehniskie vērtējumi neaizstāj pienākumus |
| `vuln_signals_are_distinct` | Kibernoturība | Avota fakts | CVSS, EPSS un KEV mēra atšķirīgas lietas |
| `civil_existing_capabilities` | Civilā aizsardzība | Avota fakts | 112 Latvija un VUCAP jau eksistē |
| `civil_reuse_existing_capabilities` | Civilā aizsardzība | Projekta priekšlikums | Kartēt un izmantot esošo pirms dublēšanas |
| `election_resilience_controls` | Vēlēšanas | Avota fakts | ES vēlēšanu kiberdrošības kontroles jomas |
| `election_state_model_project_pattern` | Vēlēšanas | Projekta priekšlikums | Projekta stāvokļu modelis, ne oficiāla taksonomija |
| `accountability_whistleblowing_boundary` | Atbildība | Robeža | Sabiedrības interešu trauksme pret individuālu sūdzību |

## Atsauču semantika

`defines` nozīmē, ka avots tieši definē vai formāli nosaka punktu. `supports` nozīmē tiešu pamatojumu bez vienīgās formālās definīcijas statusa. `limits` tiek lietots, lai ierobežotu pārāk plašu interpretāciju. `context` ievieto projekta priekšlikumu kontekstā, bet nepadara to obligātu.

Pirmavots pierāda to, ko šis avots faktiski nosaka; tas automātiski nepierāda katru tālāko secinājumu.
