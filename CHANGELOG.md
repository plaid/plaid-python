## 3.1.1

- Add [`/sandbox/item/fire_webhook`][docs-sandbox-item-fire-webhook] endpoint ([#160](https://github.com/plaid/plaid-python/pull/160))

## 3.1.0

- Fix flag name for retrieving institution display data, it is `include_optional_metadata`

## 3.0.0

- Remove direct integration endpoints since they are no longer supported
- `deleteItem` has been renamed `removeItem`

## 2.5.0

- Add `include_institution_data` flag to institutions endpoints
- Tests are now against Python 2 and 3 via `tox`
- Removed usage of mutable kwargs ([#139](https://github.com/plaid/plaid-python/pull/139))

## 2.4.1

- Fix error types for asset reports ([#145](https://github.com/plaid/plaid-python/pull/145))

## 2.4.0

- Add support for asset reports with insights ([#138](https://github.com/plaid/plaid-python/pull/138))

[docs-sandbox-item-fire-webhook]: https://plaid.com/docs/#firing-webhooks