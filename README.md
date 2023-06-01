plaid-python  [![Circle CI](https://circleci.com/gh/plaid/plaid-python.svg?style=svg&circle-token=02afb22cf19d78230650df63f9b62c1ba3aa0d93)](https://circleci.com/gh/plaid/plaid-python) [![PyPI version](https://badge.fury.io/py/plaid-python.svg)](https://badge.fury.io/py/plaid-python)
============

The official python client library for the [Plaid API][1], which is generated from our [OpenAPI spec](https://github.com/plaid/plaid-openapi). For the last non-generated version of our library, go [here](https://github.com/plaid/plaid-python/commit/26ca2baccc382209557ac87f034e747bc802c9aa).

## Table of Contents

- [plaid-python](#plaid-python)
  * [Install](#install)
  * [Documentation](#documentation)
  * [Getting Started](#getting-started)
    + [Calling Endpoints](#calling-endpoints)
    + [Errors](#errors)
  * [Examples](#examples)
  * [Contributing](#contributing)
  * [Legacy API](#legacy-api)
  * [License](#license)

## Install

This library only supports `python3`!

```console
$ pip3 install plaid-python
```

## Documentation

The module supports all Plaid API endpoints.  For complete information about
the API, head to the [docs][2].

## Getting Started

### Calling Endpoints

To call an endpoint you must create a `PlaidApi` object.

```python
import plaid
from plaid.api import plaid_api

# Available environments are
# 'Production'
# 'Development'
# 'Sandbox'
configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': client_id,
        'secret': secret,
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)
```

Each endpoint returns a dictionary which contains the parsed JSON from the
HTTP response.

### Versioning

This release only supports the latest Plaid API version, `2020-09-14`.

For information about what has changed between versions and how to update your integration, head to the [API upgrade guide][api-upgrades].

The plaid-python client library is typically updated on a monthly basis. The canonical source for the latest version number is the [client library changelog](https://github.com/plaid/plaid-python/blob/master/CHANGELOG.md).

### Errors

All non-200 responses will throw a `plaid.ApiException`.

```python
import plaid
from plaid.model.asset_report_get_request import AssetReportGetRequest

try:
    request = AssetReportGetRequest(
        asset_report_token=asset_report_token,
    )
    return client.asset_report_get(request)
except plaid.ApiException as e:
    response = json.loads(e.body)
    # check the code attribute of the error to determine the specific error
    if response['error_code'] == 'ITEM_LOGIN_REQUIRED':
        # the users' login information has changed, generate a public_token
        # for the user and initialize Link in update mode to
        # restore access to this user's data
        # see https://plaid.com/docs/api/#updating-items-via-link
    else:
        ...
```

For more information on Plaid response codes, head to the [docs][3].

## Data type differences from API and from previous versions

### Converting the response to a JSON

As this is a common question, we've included this in the README. `plaid-python` uses models like `TransactionsSyncResponse` to encapsulate API responses. If you want to convert this to a JSON, do something like this:

```python
import json
...
response = ... # type TransactionsSyncResponse
# to_dict makes it first a python dictionary, and then we turn it into a string JSON.
json_string = json.dumps(response.to_dict(), default=str)
```
### Dates

Dates and datetimes in requests, which are represented as strings in the API and in previous client library versions, are represented in this version of the Python client library as Python `datetime.date` or `datetime.datetime` objects. If you need to convert between dates and strings, you can use the `datetime.strptime` method. For an example, see the Retrieve Transactions sample code later in this Readme. For more information on the Python's `datetime` module, see [Python's official documentation](https://docs.python.org/3/library/datetime.html).

Note that the `datetime.strptime` method [will silently remove time zone information](https://www.enricozini.org/blog/2009/debian/using-python-datetime/). Time zone information is required for request fields that accept datetimes. Failing to include time zone information (or passing in a string, instead of a `datetime.datetime` object) will result in an error. See the following examples for guidance on `datetime.date` and `datetime.datetime` usage.

If the API reference documentation for a field specifies `format: date`, either of following are acceptable:

```py
from datetime import date

a = date(2022, 5, 5)
b = date.fromisoformat('2022-05-05')
```

If the API reference documentation for a field specifies `format: date-time`, the following is acceptable:


```py
from datetime import datetime

a = datetime(2022, 5, 5, 22, 35, 49, tzinfo=datetime.timezone.utc)
```

### Enums

While the API and previous library versions represent enums using strings, this current library uses Python classes with restricted values.

Old:
```
'products': ['auth', 'transactions'],
'country_codes': ['US'],
```

Current:
```
products=[Products('auth'), Products('transactions')],
country_codes=[CountryCode('US')],
```

## Examples

### Create an Item using Link
Exchange a `public_token` from [Plaid Link][4] for a Plaid access token:
```python
import plaid
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest

# the public token is received from Plaid Link
exchange_request = ItemPublicTokenExchangeRequest(
    public_token=pt_response['public_token']
)
exchange_response = client.item_public_token_exchange(exchange_request)
access_token = exchange_response['access_token']
```

### Create a Stripe bank account token
Exchange a Plaid Link `public_token` for an API `access_token`.  Then exchange
that `access_token` and the Plaid Link `account_id` (received along with the
`public_token`) for a Stripe `bank_account_token`:

```python
import plaid
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.processor_stripe_bank_account_token_create_request import ProcessorStripeBankAccountTokenCreateRequest

exchange_request = ItemPublicTokenExchangeRequest(
    public_token=pt_response['public_token']
)
exchange_response = client.item_public_token_exchange(exchange_request)
access_token = exchange_response['access_token']

request = ProcessorStripeBankAccountTokenCreateRequest(
    access_token=access_token,
    account_id='[Account ID]',
)
stripe_response = client.processor_stripe_bank_account_token_create(request)
bank_account_token = stripe_response['stripe_bank_account_token']
```

### Remove Item
```python
import plaid
from plaid.model.item_remove_request import ItemRemoveRequest

# Provide the access token for the Item you want to remove
request = ItemRemoveRequest(
    access_token=accessToken
)
response = client.item_remove(request)
```

### Retrieve Transactions (preferred method)
```python
import plaid
from plaid.model.transactions_sync_request import TransactionsSyncRequest

request = TransactionsSyncRequest(
    access_token=access_token,
)
response = client.transactions_sync(request)
transactions = response['added']

# the transactions in the response are paginated, so make multiple calls while incrementing the cursor to
# retrieve all transactions
while (response['has_more']):
    request = TransactionsSyncRequest(
        access_token=access_token,
        cursor=response['next_cursor']
    )
    response = client.transactions_sync(request)
    transactions += response['added']
```


### Retrieve Transactions (older method)
```python
import plaid
from plaid.model.transactions_get_request_options import TransactionsGetRequestOptions
from plaid.model.transactions_get_request import TransactionsGetRequest

request = TransactionsGetRequest(
    access_token=access_token,
    start_date=datetime.strptime('2020-01-01', '%Y-%m-%d').date(),
    end_date=datetime.strptime('2021-01-01', '%Y-%m-%d').date(),
)
response = client.transactions_get(request)
transactions = response['transactions']

# the transactions in the response are paginated, so make multiple calls while increasing the offset to
# retrieve all transactions
while len(transactions) < response['total_transactions']:
    options = TransactionsGetRequestOptions()
    options.offset = len(transactions)

    request = TransactionsGetRequest(
        access_token=access_token,
        start_date=datetime.strptime('2020-01-01', '%Y-%m-%d').date(),
        end_date=datetime.strptime('2021-01-01', '%Y-%m-%d').date(),
        options=options
    )
    response = client.transactions_get(request)
```

### Retrieve Asset Report PDF

```python
from plaid.model.asset_report_pdf_get_request import AssetReportPDFGetRequest

pdf_request = AssetReportPDFGetRequest(asset_report_token=PDF_TOKEN)
pdf = client.asset_report_pdf_get(pdf_request)
FILE = open('asset_report.pdf', 'wb')
FILE.write(pdf.read())
FILE.close()
```

### Authentication

Public endpoints (category information) require no authentication and can be
accessed as follows:

```python
categories = client.categories_get({})
```

Authenticated endpoints require a `(client_id, secret)` pair. You do not need to pass in authentication to individual endpoints once you have set it on the `plaid.Configuration` object.


## Contributing

Please see [Contributing](CONTRIBUTING.md) for guidelines and instructions for local development.

## License
[MIT][6]

[1]: https://plaid.com
[2]: https://plaid.com/docs/api
[3]: https://plaid.com/docs/api#errors
[4]: https://plaid.com/docs/link/
[5]: https://github.com/plaid/plaid-python/issues/new
[6]: https://github.com/plaid/plaid-python/blob/master/LICENSE
[7]: https://plaid.github.io/plaid-python/contents.html
[8]: https://cloud.google.com/appengine/docs/python/issue-requests
[9]: https://blog.plaid.com/improving-our-api/
[10]: https://github.com/plaid/plaid-python-legacy
[api-upgrades]: https://plaid.com/docs/api-upgrades/
