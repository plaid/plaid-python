from plaid.errors import APIError, PlaidError


def test_from_response():
    response = {
        'display_message': None,
        'error_type': 'API_ERROR',
        'error_code': 'INTERNAL_SERVER_ERROR',
        'error_message': 'an unexpected error occurred',
        'request_id': 'abc123',
        'causes': [
            {
                'error_type': 'API_ERROR',
                'error_code': 'INTERNAL_SERVER_ERROR',
                'error_message': 'an unexpected error occurred',
                'item_id': '456',
            },
        ],
    }

    error = PlaidError.from_response(response)
    assert isinstance(error, APIError)
    assert error.code == 'INTERNAL_SERVER_ERROR'
    assert error.message == 'an unexpected error occurred'

    assert len(error.causes) == 1
    cause = error.causes[0]
    assert cause.type == 'API_ERROR'
    assert cause.code == 'INTERNAL_SERVER_ERROR'
    assert cause.message == 'an unexpected error occurred'
    assert cause.item_id == '456'
