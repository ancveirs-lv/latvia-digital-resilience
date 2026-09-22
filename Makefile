.PHONY: install validate test serve build verify-site check sources

install:
	python -m pip install --require-hashes -r requirements.txt

validate:
	python scripts/validate.py

test:
	python -m pytest -q

serve:
	mkdocs serve

build:
	mkdocs build --strict
	python scripts/postprocess_site.py
	python scripts/verify_site.py

verify-site: build

sources:
	python scripts/check_external_links.py

check: validate test build
