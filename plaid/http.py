##############################################################################
# Helper module that encapsulates the HTTPS request so that it can be used
# with multiple runtimes. PK Mar. 14
##############################################################################
import os
import urllib

# Command line
def _requests_http_request(url, method, data):
    import requests
    if method.upper() == 'GET':
        return requests.get(url, data = data)
    elif method.upper() == 'POST':
        return requests.post(url, data = data)
    elif method.upper() == 'PUT':
        return requests.put(url, data = data)
    elif method.upper() == 'DELETE':
        return requests.delete(url, data = data)
    elif method.upper() == 'PATCH':
        return requests.patch(url, data = data)

    assert False

# Google App Engine
def _urlfetch_http_request(url, method, data):
    from google.appengine.api import urlfetch

    method = method.upper()
    qs = urllib.urlencode(data)
    if method == 'POST':
        payload = qs
    else:
        payload = None
        url += '?' + qs

    response = urlfetch.fetch(url,
        follow_redirects = True,
        method = method,
        payload = payload
    )

    response.ok = response.status_code >= 200 and response.status_code < 300
    return response

_is_appengine = None
def http_request(url, method, data = {}):
    global _is_appengine
    if _is_appengine is None:
        ss = os.environ.get('SERVER_SOFTWARE')
        _is_appengine = (ss and (ss.startswith('Development/') or ss.startswith('Google App Engine/')))

    if _is_appengine:
        return _urlfetch_http_request(url, method, data)
    else:
        return _requests_http_request(url, method, data)

        

