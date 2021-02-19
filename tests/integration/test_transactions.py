import time
import json
import plaid
from datetime import datetime
from datetime import timedelta
from plaid.model.products import Products
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.sandbox_public_token_create_request_options import SandboxPublicTokenCreateRequestOptions
from plaid.model.sandbox_public_token_create_request_options_transactions import SandboxPublicTokenCreateRequestOptionsTransactions
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.transactions_get_request_options import TransactionsGetRequestOptions
from plaid.model.item_remove_request import ItemRemoveRequest
from plaid.model.transactions_refresh_request import TransactionsRefreshRequest
from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION,
)

access_token = None

# NOTE: Data is only generated over the past 2 years.  Ensure that the date
# range used for transactions/get is within 2 years old

START_DATE = (datetime.now() - timedelta(days=(365*2)))
END_DATE = datetime.now()
DATE_FORMAT = '%Y-%m-%d'

def setup_module(module):
    client = create_client()
    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('transactions')],
        options=SandboxPublicTokenCreateRequestOptions(
            transactions=SandboxPublicTokenCreateRequestOptionsTransactions(
                start_date=START_DATE.strftime(DATE_FORMAT),
                end_date=END_DATE.strftime(DATE_FORMAT)
            )
        )
    )
    pt_response = client.sandbox_public_token_create(pt_request)
    exchange_request = ItemPublicTokenExchangeRequest(
        public_token=pt_response['public_token']
    )
    exchange_response = client.item_public_token_exchange(exchange_request)
    global access_token
    access_token = exchange_response['access_token']


def get_transactions_with_retries(client,
                                  access_token,
                                  account_ids=None,
                                  count=None,
                                  offset=None,
                                  num_retries=20):
    response = None
    for i in range(num_retries):
        try:
            options = TransactionsGetRequestOptions()

            if count is not None:
                options.count = count
            if offset is not None:
                options.offset = offset
            if account_ids is not None:
                options.account_ids = account_ids

            request = TransactionsGetRequest(
                access_token=access_token,
                start_date=START_DATE.date(),
                end_date=END_DATE.date(),
                options=options
            )
            response = client.transactions_get(request)

        except plaid.ApiException as e:
            response = json.loads(e.body)
            if response['error_code'] == 'PRODUCT_NOT_READY':
                time.sleep(5)
                continue
            else:
                raise e
        break
    return response


def refresh_transactions(client,
                         access_token):
    request = TransactionsRefreshRequest(
        access_token=access_token
    )
    return client.transactions_refresh(request)


def teardown_module(module):
    client = create_client()
    ir_request = ItemRemoveRequest(
        access_token=access_token
    )
    client.item_remove(ir_request)


def test_get():
    client = create_client()

    response = get_transactions_with_retries(client,
                                             access_token,
                                             num_retries=10)
    assert response['accounts'] is not None
    assert response['transactions'] is not None

    # get transactions for selected accounts
    account_id = response['accounts'][0]['account_id']
    response = get_transactions_with_retries(client,
                                             access_token,
                                             account_ids=[account_id],
                                             num_retries=10)
    assert response['transactions'] is not None


def test_get_with_options():
    client = create_client()
    response = get_transactions_with_retries(client,
                                             access_token,
                                             count=2,
                                             offset=1)
    assert len(response['transactions']) == 2


def test_refresh():
    client = create_client()

    response = refresh_transactions(client,
                                    access_token)
    # response should be empty (aside from request_id)
    assert response is not None