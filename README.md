plaid-python  [![Build Status](https://travis-ci.org/plaid/plaid-python.svg)](https://travis-ci.org/plaid/plaid-python)
============

The official python client library for the [Plaid API][1].

This module was recently refactored and released with breaking changes as version `1.0.x`.

## Table of Contents

- [plaid-python](#plaid-python)
  * [Install](#install)
  * [Documentation](#documentation)
  * [Getting Started](#getting-started)
    + [Public Endpoints](#public-endpoints)
    + [Authenticated Endpoints](#authenticated-endpoints)
  * [Support](#support)
  * [Contribute](#contribute)
  * [Contributers](#contributers)
  * [License](#license)


## Install

Via pip:

```console
pip install plaid-python
```

Via source:

```console
git clone git@github.com:plaid/plaid-python.git
python setup.py install
```

## Documentation

The module supports all Plaid API endpoints.  For complete information about the API, head to the [docs][2].


## Getting Started

### Configuration

```python
from plaid import Client

Client.config({
    'url': 'https://tartan.plaid.com'
})
```

By default, all non-200 responses will throw an error.

For more information on Plaid response codes, head to [codes][3].

```python
from plaid import Client
from plaid import errors as plaid_errors


client = Client(client_id='***', secret='***')
try:
    response = client.connect('bofa', {
        'username': '[something_invalid]',
        'password': '***'
    })
except plaid_errors.UnauthorizedError:
     # handle this
```

If you would prefer to handle non-20x status codes yourself,
you can configure the client to suppress these exceptions

```python
import json

from plaid import Client

Client.config({
    'url': 'https://tartan.plaid.com',
    'suppress_http_errors': True,
})

response = client.connect('bofa', {
    'username': '[something_invalid]',
    'password': '***'
})

if response.ok:
    content = json.loads(response.content)
else:
    # handle non-20x status codes
```

### Public Endpoints

Public endpoints (category and institution information) require no authentication and can be accessed as follows:

```python
from plaid import Client
from plaid import errors as plaid_errors
from plaid.utils import json


client = Client()
institutions = json.loads(client.institutions().content)
categories = json.loads(client.categories().content)
```

### Authenticated Endpoints
Authenticated endpoints require a valid `client_id` and `secret` to access.  You can use the sandbox client_id and secret for testing (`test_id` and `test_secret`) during development mode.


### Add Connect user

```python
from plaid import Client
from plaid import errors as plaid_errors
from plaid.utils import json


client = Client(client_id='***', secret='***')
account_type = 'bofa'

try:
    response = client.connect(account_type, {
     'username': '***',
     'password': '***'
    })
except plaid_errors.PlaidError:
     pass
else:
    connect_data = json.loads(response.content)
```

### MFA add Connect User

```python
from plaid import Client
from plaid import errors as plaid_errors
from plaid.utils import json


client = Client(client_id='***', secret='***')
account_type = 'bofa'

try:
    response = client.connect(account_type, {
     'username': '***',
     'password': '***'
    })
except plaid_errors.PlaidError, e:
     pass
else:
    if response.status_code == 200:
        # User connected
        data = json.loads(response.content)
    elif response.stat_code == 201:
        # MFA required
        try:
            mfa_response = answer_mfa(json.loads(response.content))
        except plaid_errors.PlaidError, e:
            pass
        else:
            # check for 200 vs 201 responses
            # 201 indicates that additional MFA steps required


def answer_mfa(data):
    if data['type'] == 'questions':
        # Ask your user for the answer to the question[s].
        # Although questions is a list, there is only ever a
        # single element in this list, at present
        return answer_question([q['question'] for q in data['mfa']])
    elif data['type'] == 'list':
        return answer_list(data['mfa'])
    elif data['type'] == 'selection':
        return answer_selections(data['mfa'])
    else:
        raise Exception('Unknown mfa type from Plaid')


def answer_question(questions):
    # We have magically inferred the answer
    # so we respond immediately
    # In the real world, we would present questions[0]
    # to our user and submit their response
    answer = 'dogs'
    return client.connect_step(account_type, answer)


def answer_list(devices):
    # You should specify the device to which the passcode is sent.
    # The available devices are present in the devices list
    return client.connect_step('bofa', None, options={
        'send_method': {'type': 'phone'}
    })


def answer_selections(selections):
    # We have magically inferred the answers
    # so we respond immediately
    # In the real world, we would present the selection
    # questions and choices to our user and submit their responses
    # in a JSON-encoded array with answers provided
    # in the same order as the given questions
    answer = json.dumps(['Yes', 'No'])
    return client.connect_step(account_type, answer)
```

### Add Auth User

Effectively the same as Connect.

```python
client = Client(client_id='***', secret='***')
response = client.auth('bofa', {
    'username': '***',
    'password': '***'
})
```

### MFA add Auth User

Effectively the same as Connect.

```python
client = Client(client_id='***', secret='***')
response = client.auth('bofa', {
    'username': '***',
    'password': '***'
})

mfa_response = client.auth_step('bofa', 'my_answer')
```

### Upgrade Account

Add a product (auth or connect to the user)

```python
client = Client(client_id='***', secret='***', access_token='usertoken')
response = client.upgrade('connect')
```

### Delete User

```python
client = Client(client_id='***', secret='***', access_token='usertoken')

client.connect_delete()  ## deletes Connect user

# OR

client.auth_delete()  ## deletes Auth user
```

### Exchange

Exchange a `public_token` from [Plaid Link][4] for a Plaid access token and then
retrieve account data:

```python
client = Client(client_id='***', secret='***')
response = client.exchange_token('test,chase,connected')
# client.access_token should now be populated with a
# valid access_token;  we can make authenticated requests
client.auth('chase', {
    'username': '***',
    'password': '***'
})
```

### Get Accounts

User previously Auth-ed

```python
client = Client(client_id='***', secret='***', access_token='usertoken')
accounts = json.loads(client.auth_get().content)
```

### Get Account Balances

User previously added

```python
client = Client(client_id='***', secret='***', access_token='usertoken')
response = client.balance()
```

### Get Transactions

User previously Connected-ed

```python
client = Client(client_id='***', secret='***', access_token='usertoken')
response = client.connect_get()
json.loads(response.content)
```

## Attribution & Maintenance

This repository was originally authored by [Chris Forrette](https://github.com/chrisforrette).
Version 1.0.0 was authored by [Ben Plesser](https://github.com/Bpless).

## Support

Open an [issue][5]!

## Contribute

All pull requests should be linted with flakes8 and tested by running:

```console
$ make test
```

## Contributors
- [PK](https://github.com/gae123) - fixes and Google App Engine Support

## License
[MIT][6]

[1]: https://plaid.com
[2]: https://plaid.com/docs
[3]: https://plaid.com/docs/#response-codes
[4]: https://github.com/plaid/link
[5]: https://github.com/plaid/plaid-python/issues/new
[6]: https://github.com/plaid/plaid-python/blob/master/LICENSE
