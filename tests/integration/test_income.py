from plaid.errors import ItemError
from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION
)

access_token = None


def setup_module(module):
    client = create_client()
    pt_response = client.Sandbox.public_token.create(
        SANDBOX_INSTITUTION, ['income'])
    exchange_response = client.Item.public_token.exchange(
        pt_response['public_token'])
    global access_token
    access_token = exchange_response['access_token']


def teardown_module(module):
    client = create_client()
    client.Item.remove(access_token)


def test_get():
    client = create_client()
    try:
        client.Income.get(access_token)
    except ItemError as ie:
        assert ie.code == u'PRODUCT_NOT_READY'
