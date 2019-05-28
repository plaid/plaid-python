from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION,
)

access_token = None


def setup_module(module):
    client = create_client()
    pt_response = client.Sandbox.public_token.create(
        SANDBOX_INSTITUTION, ['identity'])
    exchange_response = client.Item.public_token.exchange(
        pt_response['public_token'])
    global access_token
    access_token = exchange_response['access_token']


def teardown_module(module):
    client = create_client()
    client.Item.remove(access_token)


def test_get():
    client = create_client()
    response = client.Identity.get(access_token)
    assert response['accounts'] is not None
    for account in response['accounts']:
        assert account['owners'] is not None
        assert len(account['owners']) > 0
