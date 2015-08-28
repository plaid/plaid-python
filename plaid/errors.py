class PlaidError(Exception):
    retry = False

    def __init__(self, message=None, code=None):
        self.code = code
        self.message = message
        super(PlaidError, self).__init__(message)


class BadRequestError(PlaidError):
    pass


class RequestFailedError(PlaidError):
    pass


class ResourceNotFoundError(PlaidError):
    pass


class ExtractorError(PlaidError):
    pass


class ExtractorRetryError(PlaidError):
    retry = True


class PlaidServerError(PlaidError):
    pass


class MaintainanceError(PlaidError):
    pass


class UnauthorizedError(PlaidError):
    pass


PLAID_ERROR_MAP = {
    400: BadRequestError,
    401: UnauthorizedError,
    402: RequestFailedError,
    404: ResourceNotFoundError,
    500: PlaidServerError,
    501: ExtractorError,
    502: ExtractorRetryError,
    503: MaintainanceError,
}
