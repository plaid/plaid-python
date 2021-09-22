# Publish guide

`plaid-python` is published via [Pypi][1]

1. **Prepare for release**

Follow these steps sequentially to prepare a new release to Pypi:

- Increment the library version in `plaid/setup.py` by following [semantic versioning guidelines](https://semver.org/)
- Update the `CHANGELOG.md` with the release version and relevant comments and changes
- Commit the change, create a Pull Request, and obtain approval from a Plaid team member
- Merge the commit into `master`, and pull down the latest changes locally from `master`

2. **Publish to PyPi**

Publishing to PyPi is now handled with a job. Refer to our internal OpenAPI/clib documentation on how to do this properly.

3. **Verify publish to Pypi**

Verify that the latest package version you just released matches the version
history at:

```
https://pypi.org/project/plaid-python/#history.
```

[1]: https://pypi.org/project/plaid-python/
