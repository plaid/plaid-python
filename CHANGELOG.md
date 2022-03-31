See full changelog for the OpenAPI Schema (OAS) [here](https://github.com/plaid/plaid-openapi/blob/master/CHANGELOG.md).

# 9.2.0
- Updating to OAS 2020-09-14_1.94.0

## OpenAPI Schema Changes
### 2020-09-14_1.94.0
- Add `use_case`, `company_legal_name`, `city`, `region`, `country_code`, `postal_code` as a required response field of `Application`

### 2020-09-14_1.93.2
- Remove `income_verification_id` from income webhook example
- Fix incorrect URL for `/user/create` endpoint

### 2020-09-14_1.93.1
- Remove deprecated `income_verification_id` from income webhooks
- Standardize income webhook casing

### 2020-09-14_1.93.0
- Add several new fields to `/signal/evaluate` response
- 
### 2020-09-14_1.92.4
- Add `/sandbox/transfer/fire_webhook` endpoint

### 2020-09-14_1.91.4
- Mark certain Income endpoints as deprecated in favor of the new `/credit/*` endpoints.

### 2020-09-14_1.91.3
- Add `checkout` processor to `/processor/token/create`

### 2020-09-14_1.91.2
- Add `webhook_type` parameter to `/sandbox/item/fire_webhook`
- Support for investments transactions, investments holdings and liabilities `DEFAULT_UPDATE` webhooks

### 2020-09-14_1.90.2
- Add new warning type to `/credit/bank_income/get` response

### 2020-09-14_1.90.1
- Add `marqeta` and `solid` as Auth processor partners
- Fix schema of `cause` parameter for Asset Reports
- Fix some invalid examples
 
### 2020-09-14_1.90.0
- Add `/credit/employment/get` endpoint
- Add optional `access_tokens` array to `/credit/payroll_income/precheck` request

### 2020-09-14_1.89.3
- Update description of `/sandbox/item/fire_webhook`

### 2020-09-14_1.89.2
- Update description of `accounts/get`

### 2020-09-14_1.89.1
- Added `AUTH_DATA_UPDATE` webhook code as valid input to `/sandbox/item/fire_webhook`
- Update description for `/sandbox/item/fire_webhook`

### 2020-09-14_1.89.0
- Add `/transfer/migrate_account` endpoint

### 2020-09-14_1.88.2
- Fix operationId for `/credit/payroll_income/precheck`

### 2020-09-14_1.88.1
- Remove deprecated fields from `/item/application/list`

### 2020-09-14_1.88.0
- Add `wire_routing_number` parameter to `/bank_transfer/migrate_account`

### 2020-09-14_1.87.1
- Specify minimum length of 1 for `description` on `TransferIntentCreateRequest`

### 2020-09-14_1.87.0
- Add `consent_id` support in the Institutions Search request

### 2020-09-14_1.86.1
- Add `apex_clearing` as a processor partner

### 2020-09-14_1.86.0
- Introduce Credit Payroll Income APIs
- Introduce Credit Precheck API

### 2020-09-14_1.85.1
- Add `/identity_verification/create` endpoint, kept private for now

### 2020-09-14_1.85.0
- Add `status` field to `ConnectedApplication`

# 9.1.1
- Updating to OAS 2020-09-14_1.84.5

## OpenAPI Schema Changes
### 2020-09-14_1.84.5
- Added missing `asset_report_id` field to `/asset_report/relay/refresh`

### 2020-09-14_1.84.4
- Change summary description and url for `/credit/bank_income/get`

### 2020-09-14_1.84.3
- Slight wording change for `/credit/bank_income/get` response fields

### 2020-09-14_1.84.3
- Move `user_token` to top level of `link/token/create` request 

### 2020-09-14_1.84.2
- Correct typo in enum value for Investment subtypes (`person` -> `pension`)

# 9.1.0
- Updating to OAS 2020-09-14_1.84.1

## OpenAPI Schema Changes
### 2020-09-14_1.84.1
- Fix schema to properly handle personal finance categories in `/transactions/get`

### 2020-09-14_1.84.0
- Add `user_token` parameter to `link/token/create`

### 2020-09-14_1.83.1
- Add new fields to `/credit/bank_income/get` response

### 2020-09-14_1.83.0
- Remove `permitted` decision for `/transfer/authorization/create`

### 2020-09-14_1.82.0
- Add beta field `consented_products` to `/item/get/` endpoint response

### 2020-09-14_1.82.0
- Revamp LinkTokenCreate.IncomeVerificationOptions for GA

### 2020-09-14_1.81.0
- Add `/transaction/rules/create`, `/transaction/rules/list` and `/transaction/rules/remove` endpoints

### 2020-09-14_1.80.0
- Added `/user/create` endpoint

# 9.0.0
- Updating to OAS 2020-09-14_1.79.0

## Breaking changes
- Many enum fields have been de-anonymized and renamed, new names can be found in the `2020-09-14_1.64.15` change message
- Non integer numbers are now `float64` fields

## OpenAPI Schema Changes
### 2020-09-14_1.79.0
- Update to include all changes up to `2020-09-14_1.77.4` (Undo revert from `1.78.x` updates)

### 2020-09-14_1.78.2
- Revert to `2020-09-14_1.64.13`

### 2020-09-14_1.77.4
- Remove the word "Asset" before "Relay" in every asset report relay related responses and request objects

### 2020-09-14_1.77.3
- Add "AssetReport" at the beginning of relay related responses and request objects to match the same pattern as other assets related objects

### 2020-09-14_1.77.2
- Add `ProductAccess` fields for upcoming partner

# 8.12.0
- Updating to OAS 2020-09-14_1.78.1
- Python library 8.11.0 was erroneously released as a `minor` version; 8.12.0 changes will be re-released as a `major` version shortly.

# 8.11.0
- Updating to OAS 2020-09-14_1.77.1

## OpenAPI Schema Changes
### 2020-09-14_1.77.1
- Fix extraneous field in enum that caused issue in code generation
- Added `asset_report_id` to the example for `/asset_report/relay/refresh`

### 2020-09-14_1.77.0
- Explicitly set `format: double` for non-integer numbers so generated fields prefer float64

### 2020-09-14_1.76.0
- Add three new endpoints for Assets: `/asset_report/relay/create`, `/asset_report/relay/get`, and `/asset_report/relay/rmeove`

### 2020-09-14_1.75.0
- Added `/asset_report/relay/refresh` endpoint

### 2020-09-14_1.74.0
- Add `recurring_transactions` to list of products

### 2020-09-14_1.73.0
- Add new endpoint for `/credit/bank_income/get`

### 2020-09-14_1.72.0
- Updated documentation URLs for all product endpoints. They can now be found
at `/docs/api/products/<product-name>/#endpoint` instead of `/docs/api/products/#endpoint`

### 2020-09-14_1.71.0
- internal changes

### 2020-09-14_1.70.0
- Remove deprecated `income_verification_id` from `/sandbox/income/fire_webhook`

### 2020-09-14_1.69.1
- Reorder processors enum

### 2020-09-14_1.69.0
- Added `/beta/transactions/v1/enhance` endpoint

### 2020-09-14_1.68.1
- Added `status` object to sample responses for `/institutions/get` and `institutions/search` endpoints

### 2020-09-14_1.68.0
- Mark `include_personal_finance_category_beta` property as deprecated.
- Add new argument `include_personal_finance_category` to TransactionsGetRequestOptions.
- Update docs for `/transactions/get` request and response, referencing personal_finance_category taxonomy csv file.

### 2020-09-14_1.67.1
- internal changes

### 2020-09-14_1.67.0
- Removed unused `/income/verification/summary/get` endpoint

### 2020-09-14_1.66.0
- Added Payment Consent endpoints

### 2020-09-14_1.65.0
- Removed unused `/income/verification/paystub/get` endpoint

### 2020-09-14_1.64.15
- De-anonymized enums:
  - `PaymentInitiationPaymentReverseResponse.properties.status` => `PaymentInitiationRefundStatus`
  - `PaymentInitiationPaymentCreateResponse.properties.status` => `PaymentInitiationPaymentCreateStatus`
  - `PaymentInitiationRefund.properties.status` => `PaymentInitiationRefundStatus`
  - `PaymentAmount.properties.currency` => `PaymentAmountCurrency`
  - `InvestmentTransaction.properties.type` => `InvestmentTransactionType`
  - `InvestmentTransaction.properties.subtype` => `InvestmentTransactionSubtype`
  - `TransferAuthorizationDecisionRationale.properties.code` => `TransferAuthorizationDecisionRationaleCode`
  - `TransferAuthorizationGuaranteeDecisionRationale.properties.code` => `TransferAuthorizationGuaranteeDecisionRationaleCode`
  - `TransferAuthorization.properties.decision` => `TransferAuthorizationDecision`
  - `TransferEventListRequest.properties.transfer_type` => `TransferEventListTransferType`
  - `BankTransferEventListRequest.properties.bank_transfer_type` => `BankTransferEventListBankTransferType`
  - `BankTransferEventListRequest.properties.direction` => `BankTransferEventListDirection`
  - `TransferIntentCreate.properties.status` => `TransferIntentStatus`
  - `TransferIntentGet.properties.status` => `TransferIntentStatus`
  - `TransferIntentGet.properties.authorization_decision` => `TransferIntentAuthorizationDecision`
- `IncomeVerificationPrecheckMilitaryInfo.properties.branch` is now a string field (previously enum)

### 2020-09-14_1.64.15
- Made `last_statement_balance` and `minimum_payment_amount` `nullable` for credit card liabilities schema to reflect existing API behavior.

### 2020-09-14_1.64.14
- Made `last_payment_amount` and `last_statement_issue_date` `nullable` for credit card liabilities schema to reflect existing API behavior.
- Fix transfers examples to reflect more consistent usage of `region` field.

### 2020-09-14_1.64.13
- Deprecate `idempotency_key` parameter in transfer/create

### 2020-09-14_1.64.12
- Removed the unused `required_product_access` and `optional_product_access` parameters from `RequestedScopes`

### 2020-09-14_1.64.11
- Fix some examples that were not consistent with their schemas
- Add `adjustments` as an investments transaction type to make OpenAPI file consistent with values returned by the API
- Clarify description field for `marital_status` to reflect possible values

### 2020-09-14_1.64.10
- Updated the external docs URL for Bank Transfers sandbox endpoints

### 2020-09-14_1.64.9
- De-anonymized the object filters under `LinkTokenCreateRequestAccountSubtypes`, as anonymous objects aren't compatible with the generated CLibs.
- De-anonymized some misc. objects
  - `PaymentInitiationMetadata/properties/maximum_payment_amount`
  - `PaystubOverride/properties/employer`
  - `PaystubOverride/properties/employee`
  - `PaystubOverride/properties/employee/properties/address`
  - `LiabilitiesDefaultUpdateWebhook/properties/account_ids_with_updated_liabilities`

### 2020-09-14_1.64.8
- Updated the description of the historical_balances array

### 2020-09-14_1.64.7
- Add new possible enums for income verification earnings breakdown canonical description

### 2020-09-14_1.64.6
- Hid a few product enum values that are deprecated or no longer valid for certain request fields. This affects the documentation only.

### 2020-09-14_1.64.5
- Make guarantee fields required in Transfer endpoints

### 2020-09-14_1.64.4
- Updated description for `failure_reason` field in Transfer endpoints

### 2020-09-14_1.64.3
- Make `repayment_id` required in `/transfer/repayment/return/list` endpoint

### 2020-09-14_1.64.2
- Update description for legal name field in `BankTransferUser`

### 2020-09-14_1.64.1
- Update descriptions for `/transfer/repayment/list` and `/transfer/repayment/return/list` endpoints

### 2020-09-14_1.64.0
- Remove `scheme_automatic_downgrade` from `/payment_initiation/payment/create`

### 2020-09-14_1.63.1
- Update description for `/sandbox/transfer/sweep/simulate` endpoint

### 2020-09-14_1.63.0
- Refactor account subtype enums for greater specificity. This has no changes to the API but is a major semver change for Python, Node, Go, and Java client library interfaces to the AccountSubtype object within account filtering contexts in `/link/token/create`. The `AccountSubtype` namespace in this context is now prefixed with the AccountType. (Example for Node: Old: `AccountSubtype.checking` New: `DepositoryAccountSubtype.checking`)

# 8.10.0
- Updating to OAS 2020-09-14_1.62.7

## OpenAPI Schema Changes

### 2020-09-14_1.62.7
- Update description for `datetime` and `authorized_datetime` fields in Transactions endpoints

### 2020-09-14_1.62.6
- Make `sweep_id` / `sweep_amount` fields on Transfer Event nullable

### 2020-09-14_1.62.6
- Set `institution_status` to be nullable in `InstitutionsGetResponse`

### 2020-09-14_1.62.5
- Update external docs URLs for Transfer and Bank Transfer endpoints
- Update description for `ach_return_code` field in Transfer endpoints

### 2020-09-14_1.62.4
- Add `join_date` to `/application/get` and `/item/application/list`
- Remove `created_at` from `/application/get`

### 2020-09-14_1.62.3
- Updated various description fields for Income

### 2020-09-14_1.62.2
- Add `employment` as an available product in Product array.

### 2020-09-14_1.62.1
- Add `minItems` and `minLength` validation to various fields in `/institution/*` request schemas

### 2020-09-14_1.62.0
- Add guarantee_decision and guarantee_decision rationale fields to the transfer API
- Add repayment-related resources to the transfer API

### 2020-09-14_1.61.7
- Remove `receiver_pending` and `receiver_posted` from bank transfer event types.
- Remove `BankTransferReceiverDetails` from bank transfer event types.

### 2020-09-14_1.61.6
- Update description formatting for `sweep` and `amount` fields for sweep endpoints

### 2020-09-14_1.61.5
- Added `NEW_ACCOUNTS_AVAILABLE` webhook code as valid input to `/sandbox/item/fire_webhook`
- Update description for `/sandbox/item/fire_webhook`

### 2020-09-14_1.61.4
- Set the `minimum` for the `count` and `offset` fields in `InstitutionsGetRequest`
- Set `products`, `routing_numbers`, and `oauth` fields to be nullable in `InstitutionsGetRequestOptions`
- Set `products` to be nullable in `InstitutionsSearchRequest`
- Set `oauth`, `include_auth_metadata`, and `include_payment_initiation_metadata` fields to be nullable in `InstitutionsSearchRequestOptions`
- Set `payment_id` field to be nullable in `InstitutionsSearchPaymentInitiationOptions`

### 2020-09-14_1.61.3
- Adds `DOCUMENT_TYPE_NONE` enum value for document metadata

### 2020-09-14_1.61.2
- Relax length restrictions on the `currency` field in the `Pay` schema

### 2020-09-14_1.61.1
- Use new payment statuses in `PaymentStatusUpdateWebhook`

# 8.9.0
- Updating to OAS 2020-09-14_1.61.0

# 8.8.0
- Updating to OAS 2020-09-14_1.58.1

# 8.7.0
- Updating to OAS 2020-09-14_1.54.1

# 8.6.0
- Updating to OAS 2020-09-14_1.44.0

# 8.5.0
- Updating to OAS 2020-09-14_1.40.3

# 8.4.0
- Updating to OAS 2020-09-14_1.36.1

# 8.3.0
- Updating to OAS 2020-09-14_1.34.1.
- Fixed an issue with enums in this library. The library is supposed to be able to gracefully handle
    new enum values being returned from endpoints. Previously, if there were new enum values
    endpoint calls would fail.

# 8.2.1
Updating to OAS 2020-09-14_1.31.5.

# 8.2.0
Updating to OAS 2020-09-14_1.31.1.

# 8.1.0
Updating to OAS 2020-09-14_1.26.1.

# 8.0.0
The official release of the `plaid-python` generated library. Refer to the beta migration guide for tips on migrating from older version of the libraries.

This particular version is pinned to OpenAPI version `2020-09-14_1.20.6`.

# 8.0.0b13
Updating to OAS 2020-09-14_1.19.10.

# 8.0.0b12
Updating to OAS 2020-09-14_1.16.4. See full changelog [here](https://github.com/plaid/plaid-openapi/blob/master/CHANGELOG.md).

# 8.0.0b10
Type fixes, see full changelog [here](https://github.com/plaid/plaid-openapi/blob/master/CHANGELOG.md).

# 8.0.0b9
This version represents a transition in how we maintain our external client libraries. We are now using an [API spec](https://github.com/plaid/plaid-openapi) written in `OpenAPI 3.0.0` and running our definition file through [OpenAPITool's `python` generator](https://github.com/OpenAPITools/openapi-generator).

**Python Migration Guide:**

## Client initialization
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

## Endpoints
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

## Errors

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

# 7.5.0
- Update Sphinx dependency to `1.8.5`
- Update Py dependency to `1.10.0`

# 7.4.0
- Add support for `options` to `/payment_initiation/payment/create`

# 7.3.0
- Add support for `last_updated_datetime` to `/accounts/balance/get`

# 7.2.1
- Add `account_ids` options to `/investments/holdings/get`

# 7.2.0
- The legacy `/item/public_token/create` endpoint is added back. This endpoint should only be used if you
    have your public_key enabled and are not yet migrated to link_tokens. It is marked deprecated.
- The legacy `/payment_initiation/payment/token/create` endpoint is added back. This endpoint should
    only be used if you have your public_key enabled and are not yet migrated to link_tokens. It is
    marked deprecated.

# 7.1.0

- Add options for overriding username and password to /sandbox/public_token/create

# 7.0.0

- The library has been pinned to the '2020-09-14' API release. Visit the [docs](https://plaid.com/docs/api/versioning/) to see what changed.
- the `/item/public_token/create` endpoint has been disabled in favor of the /link/token/create
    endpoint
- The `/item/add_token/create endpoint` has been disabled in favor of the /link/token/create
- The `/payment_initiation/payment/token/create` endpoint has been disabled in favor of the /link/token/create
    endpoint
- The `/item/remove` endpoint will no longer return a `removed` boolean.
- The `/institutions/get`, `/institutions/get_by_id`, and `/institutions/search` now require
    `country_codes` to be passed in.

# 6.1.0

- Add support for Link Token get endpoint ([#243](https://github.com/plaid/plaid-python/pull/243))
  - `/link/token/get`

# 6.0.0

BREAKING CHANGES:

- Add BACS as a parameter to `/recipient/create` ([#234](https://github.com/plaid/plaid-python/pull/234))

# 5.0.0

BREAKING CHANGES:

- Add support for link/token/create (#230)
- Removes the public key as input to `Client`. The public key is no longer needed by the API. (#223)

# 4.1.0

- Add classes for missing error types (`AuthError`, `AssetReportError`)

# 4.0.0

- Fix use of mutable default param in `institutions.search`
- Remove support for deprecated `/item/access_token/update_version` endpoint
- Add support for the `/sandbox/item/set_verification_status` endpoint

BREAKING CHANGES:

- Removes `client.Item.update_version`

# 3.9.0

- Add `client_user_id` field to Item add token endpoint

# 3.8.0

- Add support for Item add token endpoint (BETA)
  - `/item/add_token/create` (BETA)

# 3.7.0

- Add support for transactions refresh
  - `/transactions/refresh`

# 3.6.0

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

# 3.5.0

- Add support for new UK Payment Initiation product ([#195](https://github.com/plaid/plaid-python/pull/195))
  - `/payment_initiation/recipient/create`
  - `/payment_initiation/recipient/get`
  - `/payment_initiation/recipient/list`
  - `/payment_initiation/payment/create`
  - `/payment_initiation/payment/token/create`
  - `/payment_initiation/payment/get`
  - `/payment_initiation/payment/list`

# 3.4.0

- Add support for new Liabilities product ([#173](https://github.com/plaid/plaid-python/pull/173))
  - `/liabilities/get`

# 3.3.0

- Add support for new Investments product ([#169](https://github.com/plaid/plaid-python/pull/169))
  - `/investments/transactions/get`
  - `/investments/holdings/get`

# 3.2.0

- Add support for [version `2019-05-29`](https://plaid.com/docs/api-upgrades/) of the Plaid API

# 3.1.1

- Add [`/sandbox/item/fire_webhook`][docs-sandbox-item-fire-webhook] endpoint ([#160](https://github.com/plaid/plaid-python/pull/160))

# 3.1.0

- Fix flag name for retrieving institution display data, it is `include_optional_metadata` ([#159](https://github.com/plaid/plaid-python/pull/159))

# 3.0.0

- Remove direct integration endpoints since they are no longer supported
- `deleteItem` has been renamed `removeItem`

# 2.5.0

- Add `include_institution_data` flag to institutions endpoints
- Tests are now against Python 2 and 3 via `tox`
- Removed usage of mutable kwargs ([#139](https://github.com/plaid/plaid-python/pull/139))

# 2.4.1

- Fix error types for Asset reports ([#145](https://github.com/plaid/plaid-python/pull/145))

# 2.4.0

- Add support for Asset reports with insights ([#138](https://github.com/plaid/plaid-python/pull/138))

# 2.3.4

- Add support for Assets endpoints ([#134](https://github.com/plaid/plaid-python/pull/134))
  - `/asset_report/audit_copy/get`
  - `/asset_report/filter`
  - `/asset_report/refresh`

# 2.3.3

- Add support for Dwolla processor token ([#126](https://github.com/plaid/plaid-python/pull/126))

# 2.3.2

- Add support for new Asset endpoints ([#127](https://github.com/plaid/plaid-python/pull/127))

# 2.3.1

- Add new endpoint to create Sandbox Items ([#123](https://github.com/plaid/plaid-python/pull/123))

# 2.3.0

- Add support for [version `2018-05-22`](https://plaid.com/docs/api-upgrades/) of the Plaid API

[docs-sandbox-item-fire-webhook]: https://plaid.com/docs/#firing-webhooks
