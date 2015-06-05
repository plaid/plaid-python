.PHONY: lint
lint:
	flake8 plaid


.PHONY: test
test: lint
	py.test --cov plaid -s -rxs ./tests/


.PHONY: setup
setup:
	pip install -r requirements.txt
