class PlaidError(Exception):
    retry = False
    status_code = None

    def __init__(self, message=None, code=None, error_data=None):
        self.code = code
        self.message = message
        self.error_data = error_data
        super(PlaidError, self).__init__(message)


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
