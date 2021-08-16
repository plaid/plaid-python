from plaid.model.products import Products
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.item_remove_request import ItemRemoveRequest
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.accounts_get_request_options import AccountsGetRequestOptions
from plaid.model.accounts_balance_get_request import AccountsBalanceGetRequest
from plaid.model.accounts_balance_get_request_options import AccountsBalanceGetRequestOptions


from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION,
)

access_token = None

def setup_module(module):
    client = create_client()

    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('transactions')]
    )

    pt_response = client.sandbox_public_token_create(pt_request)

    exchange_request = ItemPublicTokenExchangeRequest(
        public_token=pt_response['public_token']
    )
    exchange_response = client.item_public_token_exchange(exchange_request)
    global access_token
    access_token = exchange_response['access_token']


def teardown_module(module):
    client = create_client()
    ir_request = ItemRemoveRequest(
        access_token=access_token
    )
    client.item_remove(ir_request)


def test_get():
    client = create_client()

    # get all accounts
    ag_request = AccountsGetRequest(
        access_token=access_token
    )

    response = client.accounts_get(ag_request)
    assert response['accounts'] is not None

    # get selected accounts
    account_id = response['accounts'][0]['account_id']
    ag_request = AccountsGetRequest(
        access_token=access_token,
        options=AccountsGetRequestOptions(
            account_ids=[account_id]
        )
    )

    response = client.accounts_get(ag_request)
    assert len(response['accounts']) == 1
    assert response['accounts'][0]['account_id'] == account_id


def test_balances_get():
    client = create_client()

    # get all accounts
    abg_request = AccountsBalanceGetRequest(
        access_token=access_token
    )
    response = client.accounts_balance_get(abg_request)
    assert response['accounts'] is not None

    # get selected accounts
    account_id = response['accounts'][0]['account_id']
    abg_request = AccountsBalanceGetRequest(
        access_token=access_token,
        options=AccountsBalanceGetRequestOptions(
            account_ids=[account_id]
        )
    )
    response = client.accounts_balance_get(abg_request)

    assert len(response['accounts']) == 1
    assert response['accounts'][0]['account_id'] == account_id