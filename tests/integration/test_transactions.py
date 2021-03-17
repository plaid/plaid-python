import time

from plaid.errors import ItemError
from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION,
)

access_token = None
START_DATE = '2020-01-01'
END_DATE = '2021-03-15'

# NOTE: Data is only generated over the past 2 years.  Ensure that the date
# range used for transactions/get is within 2 years old


def setup_module(module):
    client = create_client()
    pt_response = client.Sandbox.public_token.create(
        SANDBOX_INSTITUTION, ['transactions'],
        transactions__start_date=START_DATE,
        transactions__end_date=END_DATE,
    )
    exchange_response = client.Item.public_token.exchange(
        pt_response['public_token'])
    global access_token
    access_token = exchange_response['access_token']


def get_transactions_with_retries(client,
                                  access_token,
                                  start_date,
                                  end_date,
                                  account_ids=None,
                                  count=None,
                                  offset=None,
                                  num_retries=50):
    response = None
    for i in range(num_retries):
        try:
            response = client.Transactions.get(access_token,
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


def refresh_transactions(client,
                         access_token):
    return client.Transactions.refresh(access_token)


def teardown_module(module):
    client = create_client()
    client.Item.remove(access_token)


def test_get():
    client = create_client()

    response = get_transactions_with_retries(client,
                                             access_token,
                                             START_DATE,
                                             END_DATE,
                                             num_retries=5)
    assert response['accounts'] is not None
    assert response['transactions'] is not None

    # get transactions for selected accounts
    account_id = response['accounts'][0]['account_id']
    response = get_transactions_with_retries(client,
                                             access_token,
                                             START_DATE,
                                             END_DATE,
                                             account_ids=[account_id],
                                             num_retries=50)
    assert response['transactions'] is not None


def test_get_with_options():
    client = create_client()
    response = get_transactions_with_retries(client,
                                             access_token,
                                             START_DATE,
                                             END_DATE,
                                             count=2,
                                             offset=1)
    assert len(response['transactions']) == 2


def test_refresh():
    client = create_client()

    response = refresh_transactions(client,
                                    access_token)
    # response should be empty (aside from request_id)
    assert response is not None
