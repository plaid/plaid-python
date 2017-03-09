from plaid.errors import APIError, PlaidError


def test_from_response():
    response = {
        'display_message': None,
        'error_type': 'API_ERROR',
        'error_code': 'INTERNAL_SERVER_ERROR',
        'error_message': 'an unexpected error occurred',
        'request_id': 'abc123'
    }

    error = PlaidError.from_response(response)
    assert isinstance(error, APIError)
    assert error.code == 'INTERNAL_SERVER_ERROR'
