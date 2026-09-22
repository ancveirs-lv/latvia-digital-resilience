---
title: Metodoloģija
description: Avotu hierarhija, apgalvojumu tipi, juridiskās un politiskās neitralitātes robežas, divvalodu paritāte un izmaiņu kontrole.
---

# Metodoloģija

## Avotu hierarhija

| Līmenis | Avota veids | Izmantojums |
|---|---|---|
| 1 | Latvijas normatīvie akti un oficiāli institūciju materiāli | Juridiskie pienākumi, oficiālās spējas un mandāti |
| 2 | EUR-Lex un ES institūciju materiāli | ES juridiskais un politikas konteksts |
| 3 | CERT.LV, ENISA, FIRST, IETF, NIST un salīdzināmas institūcijas | Tehniskās definīcijas un operacionālās vadlīnijas |
| 4 | Standarti un recenzēti pētījumi | Metodes, modeļi un neatkarīgi pierādījumi |
| 5 | Sekundārā analīze | Konteksts, ja nav stiprāka pirmavota |

## Apgalvojumu tipi

- `source_fact` — fakts, ko pamato citētais materiāls;
- `boundary` — apgalvojums, kas ierobežo pārāk plašu interpretāciju;
- `project_recommendation` — šī projekta piedāvāts dizains vai politikas izvēle;
- `editorial_policy` — noteikumi, kā repozitorijs komunicē.

`project_recommendation` nekļūst par likumu, oficiālu politiku vai institucionālu vienošanos tikai tādēļ, ka tam pievienots konteksta avots.

## Pārskatīšanas noteikumi

Katram pierādījumu ierakstam ir pārskatīšanas datums. Būtiskām izmaiņām vajadzīga avotu pārbaude, LV/EN paritāte, lokālā validācija, testi un stingrs vietnes build.

Vēlēšanu saturs paliek neitrāls un tehnisks. Juridiskie apgalvojumi tiek piesaistīti jurisdikcijai un avota tekstam. Operacionāli sensitīvas detaļas tiek minimizētas.

## Desmit skatpunktu adversariālais audits

Būtiski priekšlikumi tiek pārbaudīti caur desmit fiksētiem skeptiskiem skatpunktiem: juridiskais/regulatīvais, sistēmas īpašnieks, arhitektūra, SOC/CSIRT, drošības pētnieks, privātums/DPO, iepirkumi/finanses, pašvaldība/civilā aizsardzība, vēlēšanu procesa īpašnieks un neatkarīgs auditors/sabiedrība.

Šī ir projekta metode, ne ārēja audita aizstājējs. `pilot_ready` nozīmē ierobežotu tvērumu, mašīnlasāmas kontroles, acceptance criteria un skaidrus ne-mērķus; tas nenozīmē valsts mēroga piemērotību vai juridisku apstiprinājumu.

Kanoniskie priekšlikumiem specifiskie skeptiskā audita atradumi glabājas `data/reviews.yaml`; CI katram priekšlikumam prasa tieši vienu atradumu katrā no desmit skatpunktiem.
