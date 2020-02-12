plaid-python  [![Circle CI](https://circleci.com/gh/plaid/plaid-python.svg?style=svg&circle-token=02afb22cf19d78230650df63f9b62c1ba3aa0d93)](https://circleci.com/gh/plaid/plaid-python) [![PyPI version](https://badge.fury.io/py/plaid-python.svg)](https://badge.fury.io/py/plaid-python)
============

The official python client library for the [Plaid API][1].

## Table of Contents

- [plaid-python](#plaid-python)
  * [Install](#install)
  * [Documentation](#documentation)
  * [Getting Started](#getting-started)
    + [Calling Endpoints](#calling-endpoints)
    + [Errors](#errors)
  * [Examples](#examples)
  * [Known Issues](#known-issues)
  * [Contributing](#contributing)
  * [Legacy API](#legacy-api)
  * [License](#license)

## Install

```console
$ pip install plaid-python
```

## Documentation

The module supports all Plaid API endpoints.  For complete information about
the API, head to the [docs][2].

For a full list of endpoints and arguments, see the [python docs][7].

## Getting Started

### Calling Endpoints

To call an endpoint you must create a `Client` object.

```python
from plaid import Client

# Available environments are 'sandbox', 'development', and 'production'.
client = Client(client_id='***', secret='***', public_key='***', environment='sandbox')
```

Each endpoint returns a dictionary which contains the parsed JSON from the
HTTP response.

### Versioning

You can specify the Plaid API version you wish to use when initializing `plaid`.

```python
from plaid import Client

client = Client(
  client_id='***',
  secret='***',
  public_key='***',
  environment='sandbox',
  api_version='2019-05-29'  # Specify API version
)
```

For information about what has changed between versions and how to update your integration, head to the [API upgrade guide][api-upgrades].

### Errors

All non-200 responses will throw a `plaid.errors.PlaidError`.

```python
import requests
from plaid import Client
from plaid.errors import APIError, ItemError

client = Client(client_id='***', secret='***', public_key='***', environment='sandbox')

try:
    client.Auth.get(access_token)
except ItemError as e:
    # check the code attribute of the error to determine the specific error
    if e.code == 'ITEM_LOGIN_REQUIRED':
        # the users' login information has changed, generate a public_token
        # for the user and initialize Link in update mode to
        # restore access to this user's data
        # see https://plaid.com/docs/api/#updating-items-via-link
    else:
        ...
except APIError as e:
    if e.code == 'PLANNED_MAINTENANCE':
        # inform user
    else:
        ...
except requests.Timeout:
    # retry request
```

For more information on Plaid response codes, head to the [docs][3].


## Examples

### Create an Item using Link
Exchange a `public_token` from [Plaid Link][4] for a Plaid access token:
```python
from plaid import Client


client = Client(client_id='***', secret='***', public_key='***', environment='sandbox')

# the public token is received from Plaid Link
response = client.Item.public_token.exchange(public_token)
access_token = response['access_token']
```

### Create a Stripe bank account token

Exchange a Plaid Link `public_token` for an API `access_token`.  Then exchange
that `access_token` and the Plaid Link `account_id` (received along with the
`public_token`) for a Stripe `bank_account_token`:

```python
from plaid import Client


client = Client(client_id='***', secret='***', public_key='***', environment='sandbox')

exchange_token_response = client.Item.public_token.exchange('[Plaid Link public_token]')
access_token = exchange_token_response['access_token']

stripe_response = client.Processor.stripeBankAccountTokenCreate(access_token, '[Account ID]')
bank_account_token = stripe_response['stripe_bank_account_token']
```

### Remove Item

```python
from plaid import Client

client = Client(client_id='***', secret='***', public_key='***', environment='sandbox')

# Provide the access token for the Item you want to remove
client.Item.remove(access_token)
```

### Retrieve Transactions
```python
from plaid import Client

client = Client(client_id='***', secret='***', public_key='***', environment='sandbox')

response = client.Transactions.get(access_token, start_date='2016-07-12', end_date='2017-01-09')
transactions = response['transactions']

# the transactions in the response are paginated, so make multiple calls while increasing the offset to
# retrieve all transactions
while len(transactions) < response['total_transactions']:
    response = client.Transactions.get(access_token, start_date='2016-07-12', end_date='2017-01-09',
                                       offset=len(transactions)
                                      )
    transactions.extend(response['transactions'])
```

### Retrieve Other Data
Most other item data can be retrieved by following this pattern:
```python
from plaid import Client

client = Client(client_id='***', secret='***', public_key='***', environment='sandbox')

response = client.Auth.get(access_token)
numbers = response['numbers']
```

### Authentication

Public endpoints (category information) require no authentication and can be
accessed as follows:

```python
import plaid

client = plaid.Client(None, None, None)

categories = client.Categories.get()
```

Authenticated endpoints require either a `(client_id, secret)` pair or
a `public_key` to access. You do not need to pass in authentication to
individual endpoints once you have set it on the `plaid.Client` object.

## Known Issues

Please open an [issue][5] for anything not on this list!

1. `SSLError: EOF occurred in violation of protocol (_ssl.c:581)`
(https://github.com/plaid/plaid-python/issues/62) -
Work around is installing `pyopenssl ndg-httpsclient pyasn1` from pip.

2. Requests are no longer made using `urlfetch.fetch` on Google App Engine. You will need to use the appengine requests
adapter to monkeypatch requests. See the [app engine documentation][8] for details.
## Contributing

Please see [Contributing](CONTRIBUTING.md) for guidelines and instructions
for local development.

### Attribution & Maintenance

This repository was originally authored by [Chris Forrette](https://github.com/chrisforrette).
Version 1.0.0 was authored by [Ben Plesser](https://github.com/Bpless).
Version 2.0.0 was authored by [Joy Zheng](https://github.com/joyzheng) and
[Rohan Shah](https://github.com/r-ohan).

### Contributors
- [@chrisforrette](https://github.com/chrisforrette) (Chris Forrette)
- [@gae123](https://github.com/gae123)

## Legacy API

If you're looking for a Python client that works with the legacy Plaid API, use [`plaid-python-legacy`][10], available via pypi.

## License
[MIT][6]

[1]: https://plaid.com
[2]: https://plaid.com/docs/api
[3]: https://plaid.com/docs/api#errors
[4]: https://github.com/plaid/link
[5]: https://github.com/plaid/plaid-python/issues/new
[6]: https://github.com/plaid/plaid-python/blob/master/LICENSE
[7]: https://plaid.github.io/plaid-python/index.html
[8]: https://cloud.google.com/appengine/docs/python/issue-requests
[9]: https://blog.plaid.com/improving-our-api/
[10]: https://github.com/plaid/plaid-python-legacy
[api-upgrades]: https://plaid.com/docs/api-upgrades/
