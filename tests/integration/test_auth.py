import json
import plaid
from plaid.model.products import Products
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.item_remove_request import ItemRemoveRequest
from plaid.model.auth_get_request import AuthGetRequest
from plaid.model.auth_get_request_options import AuthGetRequestOptions

from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION,
)

access_token = None

def setup_module(module):
    client = create_client()
    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('auth')]
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

    ag_request = AuthGetRequest(
        access_token=access_token
    )
    # get auth for all accounts
    response = client.auth_get(ag_request)
    assert response['accounts'] is not None
    assert response['numbers'] is not None

    # get auth for selected accounts
    account_id = response['accounts'][0]['account_id']
    ag_request = AuthGetRequest(
        access_token=access_token,
        options=AuthGetRequestOptions(account_ids=[account_id])
    )
    response = client.auth_get(ag_request)
    for key in [
        'eft',
        'ach',
        'international',
        'bacs',
    ]:
        assert key in response['numbers']


def test_auth_error():
    client = create_client()

    corrupted_access_token = access_token[:-1] + chr(ord(access_token[-1]) + 1)

    try:
        ag_request = AuthGetRequest(
            access_token=corrupted_access_token,
        )
        response = client.auth_get(ag_request)
    except plaid.ApiException as e:
        response = json.loads(e.body)
        assert response['error_code'] == 'INVALID_ACCESS_TOKEN'