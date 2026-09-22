# Installation and publication

## Local environment

Requirements: Git, Python 3.11+, and internet access for the first dependency installation.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --require-hashes -r requirements.txt
make check
mkdocs serve
```

Production build:

```bash
make build
```

The generated `site/` directory is ignored by Git.

## GitHub Pages

The repository includes `.github/workflows/pages.yml`. In **Settings → Pages**, select **GitHub Actions** as the build source. The expected URL is:

`https://ancveirs-lv.github.io/latvia-digital-resilience/`

## Main-branch protection

After the `validate-and-build` check exists, protect `main` with a ruleset or branch protection that requires the check, blocks force-pushes and deletion, and routes normal changes through pull requests.
