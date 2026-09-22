# Uzstādīšana un publicēšana

## Lokālā vide

Nepieciešams Git, Python 3.11+ un interneta pieslēgums pirmajai atkarību instalēšanai.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --require-hashes -r requirements.txt
make check
mkdocs serve
```

Produkcijas build:

```bash
make build
```

Ģenerētā `site/` direktorija Git vēsturē netiek iekļauta.

## GitHub Pages

Repozitorijā ir `.github/workflows/pages.yml`. **Settings → Pages** sadaļā par build avotu izvēlies **GitHub Actions**. Paredzētā adrese:

`https://ancveirs-lv.github.io/latvia-digital-resilience/`

## `main` aizsardzība

Kad eksistē `validate-and-build` pārbaude, aizsargā `main` ar ruleset vai branch protection: pieprasi šo pārbaudi, bloķē force-push un zara dzēšanu, un parastās izmaiņas virzi caur Pull Request.
