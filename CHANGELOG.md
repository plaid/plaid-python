## 8.0.0b4
Fix a regression with `warnings` not being imported, which is required for `Client` initialization in the development environment.

## 8.0.0b3
`request_id` added back to link token.
`bank_transfers` fixes.
`/processor/auth/get` fix nested type return object.
`/link/token/create` fix nested type return object.

## 8.0.0b2
Fix a regression in sending the `User-Agent` header.

## 8.0.0b1
This version represents a transition in how we maintain our external client libraries. We are now using an API spec written in `OpenAPI 3.0.0` and are running our definition file through [OpenAPITool's `python` generator](https://github.com/OpenAPITools/openapi-generator).

As part of this transition, we have created a wrapper around existing APIs to ease the burden of migrating to the new API client. The completely unwrapped version will be available next year as we have a few internal changes left to fully support it.

The `OpenAPI` file will be actively maintained and published (coming soon) whenever changes are made to any of our external HTTP API surfaces.  This client library is now pinned to Python `3.7.x` with tests running on Python `3.7.8`.

- Added the `BankTransfer` product.
  - This also adds the endpoint `Sandbox.bank_transfer.simulate`.
- Exposed optional parameters for multiple endpoints:
  - `Holdings.get`
  - `Institutions.get`
  - `Institutions.get_by_id`
  - `Institutions.search`
  - `Item.import_item`
  - `PaymentInitiation.list_payments`
- Added new optional parameter `schedule` to `PaymentInitiation.create_payment`
- Added new `Processor` endpoints:
  - `auth_get`, `balance_get`, `identity_get`

BREAKING CHANGES:

- Removed the `CreditDetails` and `Income` products.
- Removed ability to specify `api_version`, `timeout`, and `suppress_warnings`.
  - The API Version is pinned as of `7.0.0`, so `api_version` shouldn't be here anymore
  - `timeout` and `suppress_warnings` aren't parameters that are configurable in the output generated code.  For things that could be configured once the generated code is unwrapped, check out `generated_plaid.Configuration`.
- Made `products` non-optional for `Institutions.search`.
- Renamed all `Processor` endpoints from `camelCase` to `snake_case`.

Other Deprecations:

- Removed all in-code documentation.  Refer to our new [docs](https://plaid.com/docs), which are generated from the same OpenAPI schema!

## 7.1.0

- Add options for overriding username and password to /sandbox/public_token/create

## 7.0.0

- The library has been pinned to the '2020-09-14' API release. Visit the [docs](https://plaid.com/docs/api/versioning/) to see what changed.
- the `/item/public_token/create` endpoint has been disabled in favor of the /link/token/create
    endpoint
- The `/item/add_token/create endpoint` has been disabled in favor of the /link/token/create
- The `/payment_initiation/payment/token/create` endpoint has been disabled in favor of the /link/token/create
    endpoint
- The `/item/remove` endpoint will no longer return a `removed` boolean.
- The `/institutions/get`, `/institutions/get_by_id`, and `/institutions/search` now require
    `country_codes` to be passed in.

## 6.1.0

- Add support for Link Token get endpoint ([#243](https://github.com/plaid/plaid-python/pull/243))
  - `/link/token/get`

## 6.0.0

BREAKING CHANGES:

- Add BACS as a parameter to `/recipient/create` ([#234](https://github.com/plaid/plaid-python/pull/234))

## 5.0.0

BREAKING CHANGES:

- Add support for link/token/create (#230)
- Removes the public key as input to `Client`. The public key is no longer needed by the API. (#223)

## 4.1.0

- Add classes for missing error types (`AuthError`, `AssetReportError`)

## 4.0.0

- Fix use of mutable default param in `institutions.search`
- Remove support for deprecated `/item/access_token/update_version` endpoint
- Add support for the `/sandbox/item/set_verification_status` endpoint

BREAKING CHANGES:

- Removes `client.Item.update_version`

## 3.9.0

- Add `client_user_id` field to Item add token endpoint

## 3.8.0

- Add support for Item add token endpoint (BETA)
  - `/item/add_token/create` (BETA)

## 3.7.0

- Add support for transactions refresh
  - `/transactions/refresh`

## 3.6.0

- Add support for webhook verification
  - `/webhook_verification/get`
- Add support for generic processor token
  - `/processor/token/create`
- Add support for deposit switch
  - `/deposit_switch/token/create`
  - `/deposit_switch/create`
  - `/deposit_switch/get`
- Add support for item import
  - `/item/import`

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