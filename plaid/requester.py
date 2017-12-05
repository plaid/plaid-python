import json
from functools import partial

import requests

from plaid.errors import PlaidError
from plaid.version import __version__


ALLOWED_METHODS = {'post'}
DEFAULT_TIMEOUT = 600  # 10 minutes


def _requests_http_request(url, method, data, timeout=DEFAULT_TIMEOUT):
    normalized_method = method.lower()
    if normalized_method in ALLOWED_METHODS:
        return getattr(requests, normalized_method)(
            url,
            json=data,
            headers={
                'User-Agent': 'Plaid Python v{}'.format(__version__),
            },
            timeout=timeout,
        )
    else:
        raise Exception(
            'Invalid request method {}'.format(method)
        )


def http_request(url, method=None, data=None, timeout=DEFAULT_TIMEOUT):
    response = _requests_http_request(url, method, data or {}, timeout)
    try:
        response_body = json.loads(response.text)
    except json.JSONDecodeError:
        raise PlaidError.from_response({
            'error_message': response.text,
            'error_type': 'API_ERROR',
            'error_code': 'INTERNAL_SERVER_ERROR',
            'display_message': None,
        })
    if response_body.get('error_type'):
        raise PlaidError.from_response(response_body)
    else:
        return response_body


# helpers to simplify partial function application
post_request = partial(http_request, method='POST')
