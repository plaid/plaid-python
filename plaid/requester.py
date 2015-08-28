from functools import partial

from plaid.errors import PLAID_ERROR_MAP

from plaid.http import _outer_http_request
from plaid.utils import to_json


_base_http_request = _outer_http_request()


# method keyword arg to simplify partial function application
def http_request(url, method=None, data=None, suppress_errors=False):
    response = _base_http_request(url, method, data or {})
    ERROR = PLAID_ERROR_MAP.get(response.status_code)
    if not suppress_errors and ERROR is not None:
        json_data = to_json(response)
        raise ERROR(json_data['resolve'], json_data['code'])
    else:
        return response


delete_request = partial(http_request, method='DELETE')
get_request = partial(http_request, method='GET')
post_request = partial(http_request, method='POST')
patch_request = partial(http_request, method='PATCH')
