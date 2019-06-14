import time

from plaid.errors import ItemError
from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION,
)

access_token = None


def setup_module(module):
    client = create_client()
    pt_response = client.Sandbox.public_token.create(
        SANDBOX_INSTITUTION, ['investments'],
        transactions__start_date='2018-01-01',
        transactions__end_date='2019-01-01',
    )
    exchange_response = client.Item.public_token.exchange(
        pt_response['public_token'])
    global access_token
    access_token = exchange_response['access_token']


def get_investment_transactions_with_retries(client,
                                             access_token,
                                             start_date,
                                             end_date,
                                             account_ids=None,
                                             count=None,
                                             offset=None,
                                             num_retries=5):
    response = None
    for i in range(num_retries):
        try:
            response = \
                client.InvestmentTransactions.get(access_token,
                                                  start_date,
                                                  end_date,
                                                  account_ids=account_ids,
                                                  count=count,
                                                  offset=offset)
        except ItemError as ie:
            if ie.code == u'PRODUCT_NOT_READY':
                time.sleep(5)
                continue
            else:
                raise ie
        break
    return response


def teardown_module(module):
    client = create_client()
    client.Item.remove(access_token)


def test_get():
    client = create_client()

    response = get_investment_transactions_with_retries(client,
                                                        access_token,
                                                        '2018-01-01',
                                                        '2019-01-01',
                                                        num_retries=5)
    assert response['item'] is not None
    assert response['accounts'] is not None
    assert response['securities'] is not None
    assert response['investment_transactions'] is not None
    assert response['total_investment_transactions'] is not None

    # get transactions for selected accounts
    account_id = response['accounts'][0]['account_id']
    response = \
        get_investment_transactions_with_retries(client,
                                                 access_token,
                                                 '2018-06-01',
                                                 '2019-06-01',
                                                 account_ids=[account_id],
                                                 num_retries=5)
    assert response['investment_transactions'] is not None


def test_get_with_options():
    client = create_client()
    response = get_investment_transactions_with_retries(client,
                                                        access_token,
                                                        '2018-06-01',
                                                        '2019-06-01',
                                                        count=2,
                                                        offset=1)
    assert len(response['investment_transactions']) == 2
