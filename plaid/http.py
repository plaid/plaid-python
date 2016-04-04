##############################################################################
# Helper module that encapsulates the HTTPS request so that it can be used
# with multiple runtimes. PK Mar. 14
##############################################################################
import os

from plaid.version import __version__
from plaid.utils import urlencode
from plaid.errors import BadRequestError


ALLOWED_METHODS = {'delete', 'get', 'patch', 'post'}


def _requests_http_request(url, method, data):
    import requests

    normalized_method = method.lower()
    if normalized_method in ALLOWED_METHODS:
        return getattr(requests, normalized_method)(url, data=data, headers={
            'User-Agent': 'Plaid Python v{}'.format(__version__)
        })
    else:
        raise BadRequestError(
            'Invalid request method {}'.format(method)
        )


# Google App Engine
def _urlfetch_http_request(url, method, data):
    from google.appengine.api import urlfetch

    method = method.upper()
    qs = urlencode(data)
    if method == 'POST':
        payload = qs
    else:
        payload = None
        url += '?' + qs

    headers = {
        'User-Agent': 'Plaid Python v{}'.format(__version__)
    }

    res = urlfetch.fetch(
        url,
        follow_redirects=True,
        method=method,
        payload=payload,
        headers=headers,
        deadline=60  # seconds
    )

    # Add consistent interface across requests library and urlfetch
    res.ok = res.status_code >= 200 and res.status_code < 300
    res.text = res.content
    return res


def _outer_http_request():
    # _is_appengine caches one time computation of os.environ.get().
    # Closure means that _is_appengine is not a file scope variable
    _is_appengine = os.environ.get('SERVER_SOFTWARE', '').split('/')[0] in (
        'Development',
        'Google App Engine',
    )

    req = _urlfetch_http_request if _is_appengine else _requests_http_request

    def _inner_http_request(url, method, data):
        return req(url, method, data)
    return _inner_http_request
