import json
from functools import partial

import requests

from plaid.errors import PlaidError
from plaid.version import __version__


ALLOWED_METHODS = {'post'}
TIMEOUT = 600  # 10 minutes


def _requests_http_request(url, method, data):
    normalized_method = method.lower()
    if normalized_method in ALLOWED_METHODS:
        return getattr(requests, normalized_method)(
            url,
            json=data,
            headers={
                'User-Agent': 'Plaid Python v{}'.format(__version__),
            },
            timeout=TIMEOUT,
        )
    else:
        raise Exception(
            'Invalid request method {}'.format(method)
        )


def http_request(url, method=None, data=None):
    response = _requests_http_request(url, method, data or {})
    response_body = json.loads(response.text)
    if response_body.get('error_type'):
        raise PlaidError.from_response(response_body)
    else:
        return response_body


# helpers to simplify partial function application
post_request = partial(http_request, method='POST')
