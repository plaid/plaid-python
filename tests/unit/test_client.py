from plaid import Client
from plaid.environments import environments

def test_client_invalid_environment():
    try:
        client = Client("client_id", "secret", "invalid-env")
    except Exception as error:
        assert error is not None
    else:
        # should not have reached this code
        assert false


def test_client_success():
    client = Client(
        'client_id',
        'secret',
        environments['SANDBOX']
    )
    assert client is not None
    
