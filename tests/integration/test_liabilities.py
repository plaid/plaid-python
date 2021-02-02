from plaid.model.products import Products
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.item_remove_request import ItemRemoveRequest
from plaid.model.liabilities_get_request import LiabilitiesGetRequest
from plaid.model.liabilities_get_request_options import LiabilitiesGetRequestOptions

from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION
)

access_token = None

def setup_module(module):
    client = create_client()
    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('liabilities')]
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
    # get liabilities for all accounts
    request = LiabilitiesGetRequest(
        access_token=access_token
    )
    response = client.liabilities_get(request)
    assert response['item'] is not None
    assert response['accounts'] is not None
    assert response['liabilities'] is not None

    # get liabiliteis for specified account
    account_id = response['accounts'][0]['account_id']
    request = LiabilitiesGetRequest(
        access_token=access_token,
        options=LiabilitiesGetRequestOptions(
            account_ids=[account_id]
        )
    )
    response = client.liabilities_get(request)
    assert response['liabilities'] is not None
    assert len(response['accounts']) == 1