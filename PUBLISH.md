# Publish guide

`plaid-python` is published via [pypi](https://pypi.python.org/pypi/plaid-python).

1. Increment `plaid/version.py` and `CHANGELOG.md`, commit the change, and push to `master`. The version specified in `plaid/version.py` is pulled in when publishing to Pypi.

2. Publish to the test Pypi repository:

```bash
python setup.py sdist upload -r https://test.pypi.org/legacy/
```

3. Publish to the production Pypi repository:

```bash
python setup.py sdist upload -r https://upload.pypi.org/legacy/
```
