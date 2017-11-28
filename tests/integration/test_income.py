from plaid.errors import ItemError
from tests.integration.util import (
    create_client,
    CREDENTIALS,
    SANDBOX_INSTITUTION
)

access_token = None


def setup_module(module):
    client = create_client()
    response = client.Item.create(
        CREDENTIALS, 'ins_1', ['income'])
    global access_token
    access_token = response['access_token']


def teardown_module(module):
    client = create_client()
    client.Item.remove(access_token)


def test_get():
    client = create_client()
    try:
        client.Income.get(access_token)
    except ItemError as ie:
        assert ie.code == u'PRODUCT_NOT_READY'
