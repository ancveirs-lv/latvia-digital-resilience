---
title: CVD un labticīga drošības izpēte
description: Precīzas robežas starp koordinētu ievainojamību atklāšanu, programmas tvērumu, testēšanas atļauju un pentestu Latvijā.
---

# CVD un labticīga drošības izpēte

## Avotos balstīts pamats

Latvijā ir nacionāls CVD ietvars, un CERT.LV uztur valsts ievainojamību ziņošanas platformu. Resursu pārziņi var publicēt konkrētai programmai noteiktus resursus un testēšanas nosacījumus.

CVD ir **koordinācijas process**. Konkrēta programma vai politika var definēt tvērumu un nosacījumus. Šos jēdzienus nedrīkst sapludināt universālā atļaujā testēt.

CERT.LV arī skaidro, ka ievainojamību meklēšana un ziņošana platformā nav pielīdzināma pilnvērtīgam penetrācijas testam.

## Robežas

- `security.txt` palīdz atrast kontaktu un politiku; RFC 9116 pats fails nav testēšanas atļauja.
- Labs nolūks neaizstāj tvērumu.
- CVD nav universāls pentesta mandāts.
- Trešo pušu sistēmām un pakalpojumiem vajadzīga sava atļauja vai piemērojamie noteikumi.
- Datu iegūšanai jāaprobežojas ar apjomu, kas nepieciešams atļautajam pierādījumam.

## Projekta priekšlikums

Publiskā sektora CVD dizainam skaidri jānosaka tvērums, aizliegtās darbības, pierādījumu minimizācija, saņemšanas apstiprinājums, triāža, komunikācija par novēršanu, disclosure koordinācija un safe-harbour formulējums.

Saistītie pierādījumi: `cvd_national_framework`, `cvd_program_scope`, `cvd_not_pentest`, `security_txt_not_permission`.
