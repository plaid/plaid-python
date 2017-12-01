from tests.integration.util import (
    create_client,
    CREDENTIALS,
    SANDBOX_INSTITUTION,
)

access_token = None


def setup_module(module):
    client = create_client()
    response = client.Item.create(
        CREDENTIALS, SANDBOX_INSTITUTION, ['auth'])
    global access_token
    access_token = response['access_token']


def teardown_module(module):
    client = create_client()
    client.Item.remove(access_token)


def test_get():
    client = create_client()

    # get auth for all accounts
    response = client.Auth.get(access_token)
    assert response['accounts'] is not None
    assert response['numbers'] is not None

    # get auth for selected accounts
    account_id = response['accounts'][0]['account_id']
    response = client.Auth.get(access_token, account_ids=[account_id])
    assert len(response['numbers']) == 1
