##############################################################################
# Helper module that encapsulates the HTTPS request so that it can be used
# with multiple runtimes. PK Mar. 14
##############################################################################
import os
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


# Command line
def _requests_http_request(url, method, data):
    import requests
    if method.upper() == 'GET':
        return requests.get(url, data=data)
    elif method.upper() == 'POST':
        return requests.post(url, data=data)
    elif method.upper() == 'PUT':
        return requests.put(url, data=data)
    elif method.upper() == 'DELETE':
        return requests.delete(url, data=data)
    elif method.upper() == 'PATCH':
        return requests.patch(url, data=data)

    assert False

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

    response = urlfetch.fetch(url, follow_redirects=True, method=method,
                              payload=payload)
    response.ok = response.status_code >= 200 and response.status_code < 300
    return response


def _outer_http_request():
    # We use _is_appengine to cache the one time computation of os.environ.get()
    # We do this closure so that _is_appengine is not a file scope variable
    _is_appengine = os.environ.get('SERVER_SOFTWARE', '').split('/')[0] in (
        'Development',
        'Google App Engine',
    )
    def _inner_http_request(url, method, data=None):
        if data is None:
            data = {}
        if _is_appengine:
            return _urlfetch_http_request(url, method, data)
        else:
            return _requests_http_request(url, method, data)
    return _inner_http_request
http_request = _outer_http_request()
