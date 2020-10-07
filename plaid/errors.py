class BaseError(Exception):
    '''
    A base error class.

    :ivar   str     message:            A developer-friendly error message. Not
                                        safe for programmatic use.
    :ivar   str     type:               A broad categorization of the error,
                                        corresponding to the error class.
    :ivar   str     code:               An error code for programmatic use.
    :ivar   str     display_message:    A user-friendly error message. Not safe
                                        for programmatic use. May be None.
    '''
    def __init__(
        self,
        message,
        type,
        code,
        display_message,
    ):
        super(BaseError, self).__init__(message)

        # In Python 3, the Exception class does not expose a `message`
        # attribute so we need to set it explicitly. See
        # https://www.python.org/dev/peps/pep-0352/#retracted-ideas.
        self.message = message

        self.type = type
        self.code = code
        self.display_message = display_message


class PlaidError(BaseError):
    '''
    A Plaid API error.

    :ivar   str     message:            A developer-friendly error message. Not
                                        safe for programmatic use.
    :ivar   str     type:               A broad categorization of the error,
                                        corresponding to the error class.
    :ivar   str     code:               An error code for programmatic use.
    :ivar   str     display_message:    A user-friendly error message. Not safe
                                        for programmatic use. May be None.
    :ivar   str     request_id:         A unique id returned for all server
                                        responses.
    :ivar   list    causes:             A list of reasons explaining why the
                                        error happened.
    '''

    def __init__(
        self,
        message,
        type,
        code,
        display_message,
        request_id="",
        causes=None,
    ):
        super(PlaidError, self).__init__(
            message,
            type,
            code,
            display_message,
        )
        self.request_id = request_id
        self.causes = [
            PlaidCause(
                cause['error_message'],
                cause['error_type'],
                cause['error_code'],
                cause.get('display_message', ''),
                cause['item_id'],
            ) for cause in causes or []
        ]

    @staticmethod
    def from_response(response):
        '''
        Create an error of the right class from an API response.

        :param   response    dict        Response JSON
        '''
        cls = PLAID_ERROR_TYPE_MAP.get(response['error_type'], PlaidError)
        return cls(response['error_message'],
                   response['error_type'],
                   response['error_code'],
                   response['display_message'],
                   response['request_id'],
                   response.get('causes'))


class PlaidCause(BaseError):
    '''
    A cause of a Plaid error.

    :ivar   str     message:            A developer-friendly error message. Not
                                        safe for programmatic use.
    :ivar   str     type:               A broad categorization of the error,
                                        corresponding to the error class.
    :ivar   str     code:               An error code for programmatic use.
    :ivar   str     display_message:    A user-friendly error message. Not safe
                                        for programmatic use. May be None.
    :ivar   str     item_id:            The item ID.
    '''

    def __init__(
        self,
        message,
        type,
        code,
        display_message,
        item_id,
    ):
        super(PlaidCause, self).__init__(
            message,
            type,
            code,
            display_message,
        )
        self.item_id = item_id


class InvalidRequestError(PlaidError):
    '''The request is malformed and cannot be processed.'''

    pass


class InvalidInputError(PlaidError):
    '''The request is correctly formatted, but the values are incorrect.'''

    pass


class RateLimitExceededError(PlaidError):
    '''The request is valid but has exceeded established rate limits.'''

    pass


class APIError(PlaidError):
    '''Planned maintenance or an API internal server error.'''

    pass


class ItemError(PlaidError):
    '''There is invalid information about an item or it is not supported.'''

    pass


class InstitutionError(PlaidError):
    '''There are errors for the requested financial institution.'''

    pass


class AuthError(PlaidError):
    '''There are errors with verifying or pulling auth numbers data.'''

    pass


class AssetReportError(PlaidError):
    '''There are errors with creating the asset report.'''

    pass


PLAID_ERROR_TYPE_MAP = {
    'INSTITUTION_ERROR': InstitutionError,
    'INVALID_REQUEST': InvalidRequestError,
    'INVALID_INPUT': InvalidInputError,
    'RATE_LIMIT_EXCEEDED': RateLimitExceededError,
    'API_ERROR': APIError,
    'ITEM_ERROR': ItemError,
    'AUTH_ERROR': AuthError,
    'ASSET_REPORT_ERROR': AssetReportError,
}
