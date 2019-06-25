import json
from functools import partial

import requests

from plaid.errors import PlaidError
from plaid.version import __version__


ALLOWED_METHODS = {'post'}
DEFAULT_TIMEOUT = 600  # 10 minutes

try:
    from json.decoder import JSONDecodeError
except ImportError:
    # json parsing throws a ValueError in python2
    JSONDecodeError = ValueError


def _requests_http_request(
        url,
        method,
        data,
        headers,
        timeout=DEFAULT_TIMEOUT,
        **petal_kwargs):
    """Petal kwargs can include 'proxies', 'verify', and 'petal_headers'
    (used in /get/auth to attach VGS proxy, verify cert, and log header
    to the request).
    """
    normalized_method = method.lower()
    petal_headers = petal_kwargs.get('petal_headers', None)
    if petal_headers:
        headers.update(petal_headers)
    headers.update({'User-Agent': 'Plaid Python v{}'.format(__version__)})
    if normalized_method in ALLOWED_METHODS:
        return getattr(requests, normalized_method)(
            url,
            json=data,
            headers=headers,
            timeout=timeout,
            proxies=petal_kwargs.get('proxies'),
            verify=petal_kwargs.get('verify')
        )
    else:
        raise Exception(
            'Invalid request method {}'.format(method)
        )


def http_request(
        url,
        method=None,
        data=None,
        headers=None,
        timeout=DEFAULT_TIMEOUT,
        is_json=True,
        **petal_kwargs):
    response = _requests_http_request(
        url,
        method,
        data or {},
        headers or {},
        timeout,
        **petal_kwargs)

    if is_json or response.headers['Content-Type'] == 'application/json':
        try:
            response_body = json.loads(response.text)
        except JSONDecodeError:
            raise PlaidError.from_response({
                'error_message': response.text,
                'error_type': 'API_ERROR',
                'error_code': 'INTERNAL_SERVER_ERROR',
                'display_message': None,
                'request_id': '',
                'causes': [],
            })
        if response_body.get('error_type'):
            raise PlaidError.from_response(response_body)
        else:
            return response_body
    else:
        return response.content


# helpers to simplify partial function application
post_request = partial(http_request, method='POST')
