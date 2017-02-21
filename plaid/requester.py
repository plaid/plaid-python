from functools import partial

from plaid.errors import PlaidError

from plaid.http import _outer_http_request


_base_http_request = _outer_http_request()


# method keyword arg to simplify partial function application
def http_request(url, method=None, data=None, suppress_errors=False):
    response = _base_http_request(url, method, data or {})
    ERROR = PlaidError.from_http_response(response)

    if not suppress_errors and ERROR:
        raise ERROR

    return response


delete_request = partial(http_request, method='DELETE')
get_request = partial(http_request, method='GET')
post_request = partial(http_request, method='POST')
patch_request = partial(http_request, method='PATCH')
