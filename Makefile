#!make

DOCKER = docker run --env-file .env plaid-python

.PHONY: build
build:
	docker build -t plaid-python .

.PHONY: lint
lint: build
	$(DOCKER) flake8 plaid

.PHONY: test
test: lint
	$(DOCKER) tox

.PHONY: docs
docs:
	-rm -r docs/
	sphinx-build docs_source/ docs/ -b html
	touch docs/.nojekyll
	cp docs_source/index.html docs/

# Clean the /dist directory for a new publish
.PHONY: package-clean
package-clean:
	@rm -rf dist/*

# Build a new package into the /dist directory
.PHONY: package-build
package-build:
	python setup.py sdist

# Test new package before publish
.PHONY: package-check
package-check:
	twine check dist/*

# Publish the new /dist package to Pypi
.PHONY: package-publish
package-publish:
	twine upload dist/*
