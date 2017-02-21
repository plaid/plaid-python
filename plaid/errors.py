from plaid.utils import to_json


class PlaidError(Exception):
    retry = False
    status_code = None

    def __init__(self, message=None, code=None, http_response=None):
        data = {}
        headers = {}

        if http_response is not None:
            data = to_json(http_response)
            headers = http_response.headers

        self.http_response = http_response
        self.code = code or data.get('code')
        self.message = message or data.get('resolve')
        self.error_data = data
        self.request_id = headers.get('x-request-id')

        super(PlaidError, self).__init__(message)

    @staticmethod
    def from_http_response(response):
        exc_class = PLAID_ERROR_MAP.get(response.status_code)

        return exc_class(http_response=response) if exc_class else None


class BadRequestError(PlaidError):
    status_code = 400


class RequestFailedError(PlaidError):
    status_code = 402


class ResourceNotFoundError(PlaidError):
    status_code = 404


class ExtractorError(PlaidError):
    status_code = 501


class ExtractorRetryError(PlaidError):
    status_code = 502


class PlaidServerError(PlaidError):
    status_code = 500


class MaintainanceError(PlaidError):
    status_code = 503


class UnauthorizedError(PlaidError):
    status_code = 401


PLAID_ERROR_MAP = {
    x.status_code: x for x in PlaidError.__subclasses__() if x.status_code
}
