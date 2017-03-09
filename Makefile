.PHONY: lint
lint:
	flake8 plaid


.PHONY: test
test: lint
	py.test --cov plaid -s -rxs ./tests/


.PHONY: setup
setup:
	pip install -r requirements.txt


.PHONY: docs
docs:
	-rm -r docs/
	sphinx-build docs_source/ docs/ -b html
