class PlaidError(Exception):
    '''
    A Plaid API error.

    :ivar   str     type:               A broad categorization of the error,
                                        corresponding to the error class.
    :ivar   str     code:               An error code for programmatic use.
    :ivar   str     message:            A developer-friendly error message. Not
                                        safe for programmatic use.
    :ivar   str     display_message:    A user-friendly error message. Not safe
                                        for programmatic use. May be None.
    :ivar   str     request_id:         A unique id returned for all server
                                        responses.
    '''

    def __init__(self, message, type, code, display_message, request_id=""):
        super(PlaidError, self).__init__(message)
        self.type = type
        self.code = code
        self.display_message = display_message
        self.request_id = request_id

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
                   response['request_id'])


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


PLAID_ERROR_TYPE_MAP = {
    'INSTITUTION_ERROR': InstitutionError,
    'INVALID_REQUEST': InvalidRequestError,
    'INVALID_INPUT': InvalidInputError,
    'RATE_LIMIT_EXCEEDED': RateLimitExceededError,
    'API_ERROR': APIError,
    'ITEM_ERROR': ItemError,
}
