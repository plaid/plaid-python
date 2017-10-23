# Publish guide

`plaid-python` is published via [pypi](https://pypi.python.org/pypi/plaid-python).

1. Increment `plaid/version.py`, commit the change, and push to `master`. This version is pulled in when publishing to Pypi.

2. Publish to the test Pypi repository:

```bash
python setup.py sdist upload -r pypitest
```

3. Publish to the production Pypi repository:

```bash
python setup.py sdist upload -r pypi
```
