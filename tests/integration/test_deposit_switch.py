from plaid.model.products import Products
from plaid.model.item_import_request import ItemImportRequest
from plaid.model.item_import_request_user_auth import ItemImportRequestUserAuth
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.deposit_switch_create_request import DepositSwitchCreateRequest
from plaid.model.deposit_switch_get_request import DepositSwitchGetRequest
from plaid.model.deposit_switch_token_create_request import DepositSwitchTokenCreateRequest

from tests.integration.util import (
    create_client,
)

access_token = None

def setup_module(module):
    client = create_client()
    # import an item
    at_request = ItemImportRequest(
        products=[Products('identity'), Products('auth')],
        user_auth=ItemImportRequestUserAuth(
            user_id='user_good',
            auth_token='pass_good'
        )
    )
    at_response = client.item_import(at_request)
    assert at_response['access_token'] is not None
    global access_token
    access_token = at_response['access_token']


def test_full_flow():
    client = create_client()
    # get account id
    account_id_request = AccountsGetRequest(
        access_token=access_token
    )
    account_id_response = client.accounts_get(account_id_request)
    assert len(account_id_response['accounts']) != 0
    target_account_id = account_id_response['accounts'][0]['account_id']

    # create deposit switch
    create_request = DepositSwitchCreateRequest(
        target_account_id=target_account_id,
        target_access_token=access_token
    )
    create_response = client.deposit_switch_create(create_request)
    assert create_response['deposit_switch_id'] is not None

    deposit_switch_id = create_response['deposit_switch_id']

    # get deposit switch
    get_request = DepositSwitchGetRequest(
        deposit_switch_id=deposit_switch_id
    )
    get_response = client.deposit_switch_get(get_request)
    assert get_response['deposit_switch_id'] is not None
    assert get_response['target_item_id'] is not None
    assert get_response['target_account_id'] is not None
    assert get_response['date_created'] is not None
    assert get_response['state'] is not None

    # create deposit switch token
    token_request = DepositSwitchTokenCreateRequest(
        deposit_switch_id=deposit_switch_id
    )
    token_response = client.deposit_switch_token_create(token_request)
    assert token_response['deposit_switch_token'] is not None
    assert token_response['deposit_switch_token_expiration_time'] is not None
