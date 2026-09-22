---
title: IKT pārvaldība un izsekojamība
description: Esošo valsts reģistru nedublējoša pierādījumu un dzīves cikla izsekojamības pieeja Latvijas publiskā sektora IKT.
---

# IKT pārvaldība un izsekojamība

## Avotos balstīts pamats

VIRSIS jau uzkrāj informāciju par valsts informācijas sistēmām, informācijas resursiem un tehnoloģiskajiem resursiem un pakalpojumiem. Piemērojamie VIRSIS noteikumi nosaka formālu pārvaldības un reģistrācijas tvērumu. Skatīt `ict_existing_virsis_capability`.

## Projekta priekšlikums

Pirms jauna centrāla reģistra, pierādījumu mezgla vai dzīves cikla datubāzes izveides:

1. jāsalīdzina vajadzīgie lauki un procesi ar VIRSIS un esošajiem koplietošanas pakalpojumiem;
2. jānosauc precīzs trūkums;
3. sensitīvi pierādījumi pēc iespējas jāatstāj to autoritatīvajā kontrolētajā sistēmā;
4. centrāli jāindeksē tikai minimāli metadati, kas vajadzīgi stāvokļa, īpašnieka, integritātes un izsekojamības pierādīšanai.

Minimāls pierādījumu profils var būt:

`ID + type + hash + status + owner + controlled reference + mapping`

Tas ir **projekta modelis**, ne apgalvojums, ka spēkā esošais regulējums prasa tieši šādu shēmu.

## Validācija

Pilotam jāparāda mazāka datu dublēšana, pārbaudāma provenance, kontrolēta piekļuve un auditējams ceļš no IKT resursa līdz autoritatīvajam pierādījumam, kas pamato lēmumu.

Saistītie pierādījumi: `ict_existing_virsis_capability`, `ict_reuse_before_duplication`.
