# Python Plaid

Python bindings for the [Plaid API](https://plaid.com).

## Usage

### Connecting/Logging in with Multi Factored Authentication

```python
import json

from plaid import Client


client = Client(client_id='***', secret='***')
connect = client.connect(account_type='bofa', username='***', password='***', email='john@whatever.com')

if connect.ok:
    json_response = json.loads(connect.content)

    print json_response['mfa'][0] # Should be something like "What's your mother's maiden name?"

    step = client.step(account_type='bofa', mfa='Smith')
    if step.ok:
        transactions = json.loads(step.content)
        # ...
```

## Attribution & Maintenance

This repository was originally authored by [Chris Forrette](https://github.com/chrisforrette), and will be monitored and maintained (though not currently expanded on) by the Plaid team Please email support@plaid.com with any questions.