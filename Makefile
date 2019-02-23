#!make

.PHONY: lint
lint:
	flake8 plaid

# Requires tox to be installed and in the executable path
.PHONY: test
test: lint
	./.env tox

# Setting up for local development
.PHONY: setup
setup:
	pip install -r requirements.txt

.PHONY: docs
docs:
	-rm -r docs/
	sphinx-build docs_source/ docs/ -b html
	touch docs/.nojekyll
