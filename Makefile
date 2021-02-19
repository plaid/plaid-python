#!make
CURRENT_DIR:=$(shell pwd)
OPENAPI_VERSION:=1.5.4-beta
OPENAPI_FILE:=2020-09-14.yml
PYTHON_PACKAGE_VERSION=$(shell cat setup.py | grep VERSION | head -1 | sed -e "s/^VERSION=//" -e "s/'//"  -e "s/'//")
OPENAPI_GENERATOR:=docker run --rm -v $(CURRENT_DIR):/local openapitools/openapi-generator-cli:v5.0.1 generate

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
	python setup.py sdist

# Test new package before publish
.PHONY: package-check
package-check:
	twine check dist/*

# Publish the new /dist package to Pypi
.PHONY: package-publish
package-publish:
	twine upload dist/*

.PHONY: pull-openapi
pull-openapi:
	curl https://raw.githubusercontent.com/plaid/plaid-openapi/$(OPENAPI_VERSION)/$(OPENAPI_FILE) --output $(CURRENT_DIR)/$(OPENAPI_FILE)

.PHONY: build-openapi
build-openapi:
	$(OPENAPI_GENERATOR) -g python \
			-i local/$(OPENAPI_FILE) \
			-o local/ \
			-p packageName=plaid,packageVersion='$(PYTHON_PACKAGE_VERSION)' \
			--global-property apiTests=false,modelTests=false \
			-t local/templates/python