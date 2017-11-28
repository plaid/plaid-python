from tests.integration.util import (
    create_client,
    CREDENTIALS,
    SANDBOX_INSTITUTION,
)

access_token = None


def setup_module(module):
    client = create_client()
    response = client.Item.create(
        CREDENTIALS, SANDBOX_INSTITUTION, ['transactions'])
    global access_token
    access_token = response['access_token']


def teardown_module(module):
    client = create_client()
    client.Item.remove(access_token)


def test_get():
    client = create_client()

    # get all accounts
    response = client.Accounts.get(access_token)
    assert response['accounts'] is not None

    # get selected accounts
    account_id = response['accounts'][0]['account_id']
    response = client.Accounts.get(access_token, account_ids=[account_id])
    assert len(response['accounts']) == 1


def test_balances_get():
    client = create_client()

    # get all accounts
    response = client.Accounts.balance.get(access_token)
    assert response['accounts'] is not None

    # get selected accounts
    account_id = response['accounts'][0]['account_id']
    response = client.Accounts.balance.get(
        access_token, account_ids=[account_id])
    assert len(response['accounts']) == 1
