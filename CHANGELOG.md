See full changelog for the OpenAPI Schema (OAS) [here](https://github.com/plaid/plaid-openapi/blob/master/CHANGELOG.md).

## 8.8.0
- Updating to OAS 2020-09-14_1.58.1

## 8.7.0
- Updating to OAS 2020-09-14_1.54.1

## 8.6.0
- Updating to OAS 2020-09-14_1.44.0

## 8.5.0
- Updating to OAS 2020-09-14_1.40.3

## 8.4.0
- Updating to OAS 2020-09-14_1.36.1

## 8.3.0
- Updating to OAS 2020-09-14_1.34.1.
- Fixed an issue with enums in this library. The library is supposed to be able to gracefully handle
    new enum values being returned from endpoints. Previously, if there were new enum values
    endpoint calls would fail.

## 8.2.1
Updating to OAS 2020-09-14_1.31.5.

## 8.2.0
Updating to OAS 2020-09-14_1.31.1.

## 8.1.0
Updating to OAS 2020-09-14_1.26.1.

## 8.0.0
The official release of the `plaid-python` generated library. Refer to the beta migration guide for tips on migrating from older version of the libraries.

This particular version is pinned to OpenAPI version `2020-09-14_1.20.6`.

## 8.0.0b13
Updating to OAS 2020-09-14_1.19.10.

## 8.0.0b12
Updating to OAS 2020-09-14_1.16.4. See full changelog [here](https://github.com/plaid/plaid-openapi/blob/master/CHANGELOG.md).

## 8.0.0b10
Type fixes, see full changelog [here](https://github.com/plaid/plaid-openapi/blob/master/CHANGELOG.md).

## 8.0.0b9
This version represents a transition in how we maintain our external client libraries. We are now using an [API spec](https://github.com/plaid/plaid-openapi) written in `OpenAPI 3.0.0` and running our definition file through [OpenAPITool's `python` generator](https://github.com/OpenAPITools/openapi-generator).

**Python Migration Guide:**

### Client initialization
From:
```python
from plaid import Client
Client(
    client_id=os.environ['CLIENT_ID'],
    secret=os.environ['SECRET'],
    environment='sandbox',
    api_version="2020-09-14",
    client_app="plaid-python-unit-tests"
)
```

To:
```python
import plaid
from plaid.api import plaid_api
configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': client_id,
        'secret': secret,
        'plaidVersion': '2020-09-14'
    }
)
api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)
```

### Endpoints
All endpoint requests now take a request model and the functions have been renamed to include `_`.

From:
```python
response = client.Auth.get(access_token)
```

To:
```python
import plaid
from plaid.model.auth_get_request import AuthGetRequest
from plaid.model.auth_get_request_options import AuthGetRequestOptions

ag_request = AuthGetRequest(
    access_token=access_token
)

response = client.auth_get(ag_request)
```

### Errors

From:
```python
try:
    client.Auth.get(access_token)
except ItemError as e:
    if e.code == 'ITEM_LOGIN_REQUIRED':
    else:
        ...
except APIError as e:
    if e.code == 'PLANNED_MAINTENANCE':
        # inform user
    else:
        ...
```

To:
```python
try:
    request = AssetReportGetRequest(
        asset_report_token=asset_report_token,
    )
    return client.asset_report_get(request)
except plaid.ApiException as e:
    response = json.loads(e.body)
    if response['error_code'] == 'ITEM_LOGIN_REQUIRED':
    else:
```

## 7.5.0
- Update Sphinx dependency to `1.8.5`
- Update Py dependency to `1.10.0`

## 7.4.0
- Add support for `options` to `/payment_initiation/payment/create`

## 7.3.0
- Add support for `last_updated_datetime` to `/accounts/balance/get`

## 7.2.1
- Add `account_ids` options to `/investments/holdings/get`

## 7.2.0
- The legacy `/item/public_token/create` endpoint is added back. This endpoint should only be used if you
    have your public_key enabled and are not yet migrated to link_tokens. It is marked deprecated.
- The legacy `/payment_initiation/payment/token/create` endpoint is added back. This endpoint should
    only be used if you have your public_key enabled and are not yet migrated to link_tokens. It is
    marked deprecated.

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
