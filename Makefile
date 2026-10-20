#!make
# Requires tox to be installed and in the executable path
.PHONY: test
test:
	CLIENT_ID=$(CLIENT_ID) SECRET=$(SECRET) tox

# Setting up for local development
.PHONY: setup
setup:
	pip install -r requirements.txt

# Clean the /dist directory for a new publish
.PHONY: package-clean
package-clean:
	@rm -rf dist/*

# Build a new package into the /dist directory
.PHONY: package-build
package-build:
	pip install build
	python -m build

# Test new package before publish
.PHONY: package-check
package-check:
	twine check dist/*

# Publish the new /dist package to Pypi
.PHONY: package-publish
package-publish:
	twine upload dist/*
