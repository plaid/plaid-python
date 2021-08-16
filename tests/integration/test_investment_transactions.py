import time
import datetime as dt
import plaid
import json
from plaid.model.products import Products
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.sandbox_public_token_create_request_options import SandboxPublicTokenCreateRequestOptions
from plaid.model.sandbox_public_token_create_request_options_transactions import SandboxPublicTokenCreateRequestOptionsTransactions
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.investments_transactions_get_request import InvestmentsTransactionsGetRequest
from plaid.model.investments_transactions_get_request_options import InvestmentsTransactionsGetRequestOptions
from plaid.model.item_remove_request import ItemRemoveRequest


from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION,
)

access_token = None

START_DATE = dt.date(2020, 1, 1)
END_DATE = dt.date(2021, 1, 1)


def setup_module(module):
    client = create_client()
    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('investments')],
        options=SandboxPublicTokenCreateRequestOptions(
            transactions=SandboxPublicTokenCreateRequestOptionsTransactions(
                start_date=START_DATE,
                end_date=END_DATE
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
            options = InvestmentsTransactionsGetRequestOptions()

            if count is not None:
                options.count = count
            if offset is not None:
                options.offset = offset
            if account_ids is not None:
                options.account_ids = account_ids

            request = InvestmentsTransactionsGetRequest(
                access_token=access_token,
                start_date=start_date,
                end_date=end_date,
                options=options
            )
            response = \
                client.investments_transactions_get(request)
        except plaid.ApiException as e:
            response = json.loads(e.body)
            if response.code == 'PRODUCT_NOT_READY':
                time.sleep(5)
                continue
            else:
                raise e
        break
    return response


def teardown_module(module):
    client = create_client()
    ir_request = ItemRemoveRequest(
        access_token=access_token
    )
    client.item_remove(ir_request)


def test_get():
    client = create_client()

    response = get_investment_transactions_with_retries(client,
                                                        access_token,
                                                        START_DATE,
                                                        END_DATE,
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
                                                 START_DATE,
                                                 END_DATE,
                                                 account_ids=[account_id],
                                                 num_retries=5)
    assert response['investment_transactions'] is not None


def test_get_with_options():
    client = create_client()
    response = get_investment_transactions_with_retries(client,
                                                        access_token,
                                                        START_DATE,
                                                        END_DATE,
                                                        count=2,
                                                        offset=1)
    assert len(response['investment_transactions']) == 2
