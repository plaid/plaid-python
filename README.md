# plaid-python [![PyPI version](https://badge.fury.io/py/plaid-python.svg)](https://badge.fury.io/py/plaid-python)

The official python client library for the [Plaid API][1], which is generated from our [OpenAPI spec](https://github.com/plaid/plaid-openapi).

## Table of Contents

- [Installation](#installation)
- [Versioning](#versioning)
- [Getting Started](#getting-started)
  - [Calling Endpoints](#calling-endpoints)
  - [Errors](#errors)
  - [Converting the response to a JSON](#converting-the-response-to-a-json)
  - [Dates](#dates)
- [Examples](#examples)
- [Migration Guide](#migration-guide)
- [Contributing](#contributing)
- [License](#license)

## Installation

This library only supports `python3`!

```console
$ pip3 install plaid-python
```

## Versioning

This release only supports the latest Plaid API version, `2020-09-14`.

For information about what has changed between versions and how to update your integration, head to the [API upgrade guide][api-upgrades].

The plaid-python client library is typically updated on a monthly basis. The canonical source for the latest version number is the [client library changelog](https://github.com/plaid/plaid-python/blob/master/CHANGELOG.md). New versions are published as [GitHub tags](https://github.com/plaid/plaid-python/tags), not as Releases. New versions are also published on [PyPi](https://pypi.org/project/plaid-python/). Plaid uses semantic versioning to version the client libraries, with potentially breaking changes being indicated by a major version bump.

All users are strongly recommended to use a recent version of the library, as older versions do not contain support for new endpoints and fields. For more details, see the [Migration Guide](#migration-guide).

## Getting Started

### Calling Endpoints

To call an endpoint you must create a `PlaidApi` object.

```python
import plaid
from plaid.api import plaid_api

# Available environments are
# 'Production'
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

## Examples

For more examples, see the [test suites](https://github.com/plaid/plaid-python/tree/master/tests), [Quickstart](https://github.com/plaid/quickstart/tree/master/python), or [API Reference documentation](https://plaid.com/docs/api/).

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

## Migration guide

### 8.0.0 or later to latest

Migrating from version 8.0.0 or later of the library to a recent version should involve very minor integration changes. Many customers will not need to make changes to their integrations at all. To see a list of all potentially-breaking changes since your current version, see the [client library changelog](https://github.com/plaid/plaid-python/blob/master/CHANGELOG.md) and search for "Breaking changes in this version". Breaking changes are annotated at the top of each major version header.

### Pre-8.0.0 to latest

Version 8.0.0 of the client library was released in August 2021 and contains multiple interface changes, as described below.

#### Client initialization

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

#### Endpoints

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

#### Errors

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

#### Data type changes

See the sections above on [Dates](#dates) and [Converting the response to a JSON](#converting-the-response-to-a-json).

##### Enums

While the API and previous library versions prior to 8.0.0 represent enums using strings, this current library uses Python classes with restricted values.

From:

```
'products': ['auth', 'transactions'],
'country_codes': ['US'],
```

To:

```
products=[Products('auth'), Products('transactions')],
country_codes=[CountryCode('US')],
```

#### Configuration options

Some configuration options, including request timeouts, have moved from global (client-level) to being specified a per-request level, and additional configuration options have been added.

Global configuration options: [configuration.py](https://github.com/plaid/plaid-python/blob/master/plaid/configuration.py)
Per-request configuration options: [api_client.py](https://github.com/plaid/plaid-python/blob/master/plaid/api_client.py#L117)

From:

```
class PlaidClient(plaid.Client):
   def __init__(
       self,
      ...
       timeout=60
   ):
   ...
```

To:

```
response = client.accounts_balance_get(request, _request_timeout=60)
```

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
