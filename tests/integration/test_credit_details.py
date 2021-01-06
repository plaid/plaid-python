from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION,
)

access_token = None


def setup_module(module):
    client = create_client()
    pt_response = client.Sandbox.public_token.create(
        SANDBOX_INSTITUTION, ['credit_details'])
    exchange_response = client.Item.public_token.exchange(
        pt_response['public_token'])
    global access_token
    access_token = exchange_response['access_token']


def teardown_module(module):
    client = create_client()
    client.Item.remove(access_token)


def test_get():
    client = create_client()
    response = client.CreditDetails.get(access_token)
    assert response['accounts'] is not None
    assert response['credit_details'] is not None
