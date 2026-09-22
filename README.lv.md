# Latvijas digitālā noturība

Latviski · [English](README.md)

Divvalodu, pierādījumos balstīta publiska atsauce priekšlikumiem par Latvijas digitālo pārvaldību, kiberdrošību, koordinētu ievainojamību atklāšanu (CVD), labticīgu drošības izpēti, civilo aizsardzību, vēlēšanu un citu kritisku procesu noturību, kā arī institucionālo atbildību.

Projekts nošķir četras lietas, kuras publiskā diskusijā bieži tiek sajauktas:

1. **Avotos balstīts pamats** — ko faktiski nosaka normatīvie akti, esošās valsts spējas, institucionālās vadlīnijas, standarti vai pirmavoti.
2. **Projekta priekšlikums** — ko šis repozitorijs iesaka mainīt, pilotēt, pārbaudīt vai mērīt.
3. **Robeža** — ko konkrētais avots vai jēdziens *nepierāda* un nenosaka.
4. **Validācija** — kādi pierādījumi ļautu novērtēt, vai priekšlikums ir strādājis.

## Dokumentācija

Publicētajai vietnei ir atsevišķi angļu un latviešu maršruti ar valodas pārslēdzēju. Avota struktūra to atkārto `docs/en/` un `docs/lv/`.

Galvenie virzieni:

- valsts IKT pārvaldība un izsekojamība;
- CVD un labticīga drošības izpēte;
- Bug Bounty un atlīdzības mehānismi;
- kiberdrošība un digitālā noturība;
- civilā aizsardzība un darbības nepārtrauktība;
- vēlēšanu un citu kritisku procesu noturība;
- institucionālā atbildība un uzlabojumu procesi;
- pierādījumu reģistrs un metodoloģija.

## Pierādījumu modelis

Mašīnlasāmie pierādījumi glabājas:

- `data/sources.yaml` — autoritatīvi vai tehniski rigorozie avoti;
- `data/claims.yaml` — apgalvojumu līmeņa ieraksti ar avotu vietām, jurisdikciju/kontekstu un pārskatīšanas datumiem;
- `schemas/` — JSON shēmas, kuras pārbauda CI.

Atsauce uz avotu automātiski nenozīmē, ka tas pamato visu lapā rakstīto. Pierādījumu reģistrs norāda, ko avots **definē, pamato, ierobežo vai tikai ievieto kontekstā**.

## Kvalitātes vārti

Pull request un `main` ir paredzēti automātiskai pārbaudei:

- LV/EN lapu strukturālā paritāte;
- YAML/JSON Schema validācija;
- apgalvojumu un avotu savstarpējo saišu integritāte;
- lokālo saišu pārbaude;
- obligātie lapu metadati;
- stingrs MkDocs build;
- canonical URL un `hreflang`;
- ikmēneša avotu pieejamības pārbaude;
- testi un minimālas GitHub Actions atļaujas.

## Ātrais sākums

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --require-hashes -r requirements.txt
make check
mkdocs serve
```

Skatīt [INSTALL.lv.md](INSTALL.lv.md).

## Redakcionālā robeža

Šis nav partiju politikas manifests, priekšvēlēšanu instruments, apsūdzību arhīvs, juridisks atzinums, pentesta pilnvarojums vai incidentu ziņošanas kanāls. Vēlēšanu sadaļa ir ierobežota ar tehnisku un organizatorisku procesu noturību un neatbalsta vai nenoraida nevienu kandidātu, partiju vai vēlēšanu izvēli.

## Licence un citēšana

- kods un automatizācija: [MIT](LICENSE-CODE);
- dokumentācija un strukturētie dati: [CC BY 4.0](LICENSE-CONTENT);
- citēšanas metadati: [CITATION.cff](CITATION.cff).

Uzturētājs: Zigmārs Ancveirs
