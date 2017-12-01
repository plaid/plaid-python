from tests.integration.util import (
    create_client,
    CREDENTIALS,
    SANDBOX_INSTITUTION,
)

access_token = None


def setup_module(module):
    client = create_client()
    response = client.Item.create(
        CREDENTIALS,
        SANDBOX_INSTITUTION,
        ['transactions'],
        transactions__start_date='2016-01-01',
        transactions__end_date='2017-01-01',
        transactions__await_results=True,
    )
    global access_token
    access_token = response['access_token']


def teardown_module(module):
    client = create_client()
    client.Item.remove(access_token)


def test_get():
    client = create_client()

    # get transactions for all accounts
    response = client.Transactions.get(
        access_token, '2016-01-01', '2017-01-01')
    assert response['accounts'] is not None
    assert response['transactions'] is not None

    # get transactions for selected accounts
    account_id = response['accounts'][0]['account_id']
    response = client.Transactions.get(
        access_token, '2016-01-01', '2017-01-01', account_ids=[account_id])
    assert response['transactions'] is not None


def test_get_with_options():
    client = create_client()
    response = client.Transactions.get(
        access_token, '2016-01-01', '2017-01-01', count=2, offset=1)
    assert len(response['transactions']) == 2
