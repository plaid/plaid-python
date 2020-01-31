## 3.5.0

- Add support for new UK Payment Initiation product ([#195](https://github.com/plaid/plaid-python/pull/195))
  - `/payment_initiation/recipient/create`
  - `/payment_initiation/recipient/get`
  - `/payment_initiation/recipient/list`
  - `/payment_initiation/payment/create`
  - `/payment_initiation/payment/token/create`
  - `/payment_initiation/payment/get`
  - `/payment_initiation/payment/list`

## 3.4.0

- Add support for new Liabilities product ([#173](https://github.com/plaid/plaid-python/pull/173))
  - `/liabilities/get`

## 3.3.0

- Add support for new Investments product ([#169](https://github.com/plaid/plaid-python/pull/169))
  - `/investments/transactions/get`
  - `/investments/holdings/get`

## 3.2.0

- Add support for [version `2019-05-29`](https://plaid.com/docs/api-upgrades/) of the Plaid API

## 3.1.1

- Add [`/sandbox/item/fire_webhook`][docs-sandbox-item-fire-webhook] endpoint ([#160](https://github.com/plaid/plaid-python/pull/160))

## 3.1.0

- Fix flag name for retrieving institution display data, it is `include_optional_metadata` ([#159](https://github.com/plaid/plaid-python/pull/159))

## 3.0.0

- Remove direct integration endpoints since they are no longer supported
- `deleteItem` has been renamed `removeItem`

## 2.5.0

- Add `include_institution_data` flag to institutions endpoints
- Tests are now against Python 2 and 3 via `tox`
- Removed usage of mutable kwargs ([#139](https://github.com/plaid/plaid-python/pull/139))

## 2.4.1

- Fix error types for Asset reports ([#145](https://github.com/plaid/plaid-python/pull/145))

## 2.4.0

- Add support for Asset reports with insights ([#138](https://github.com/plaid/plaid-python/pull/138))

## 2.3.4

- Add support for Assets endpoints ([#134](https://github.com/plaid/plaid-python/pull/134))
  - `/asset_report/audit_copy/get`
  - `/asset_report/filter`
  - `/asset_report/refresh`

## 2.3.3

- Add support for Dwolla processor token ([#126](https://github.com/plaid/plaid-python/pull/126))

## 2.3.2

- Add support for new Asset endpoints ([#127](https://github.com/plaid/plaid-python/pull/127))

## 2.3.1

- Add new endpoint to create Sandbox Items ([#123](https://github.com/plaid/plaid-python/pull/123))

## 2.3.0

- Add support for [version `2018-05-22`](https://plaid.com/docs/api-upgrades/) of the Plaid API


[docs-sandbox-item-fire-webhook]: https://plaid.com/docs/#firing-webhooks
