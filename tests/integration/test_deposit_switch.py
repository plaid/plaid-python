from tests.integration.util import (
    create_client,
)

access_token = None


def setup_module(module):
    client = create_client()
    # import an item
    at_response = client.Item.import_item(
        ['identity', 'auth'],
        {'user_id': 'user_good', 'auth_token': 'pass_good'},
        None)
    assert at_response['access_token'] is not None
    global access_token
    access_token = at_response['access_token']


def test_full_flow():
    client = create_client()
    # get account id
    account_id_response = client.Accounts.get(access_token)
    assert len(account_id_response['accounts']) != 0
    target_account_id = account_id_response['accounts'][0]['account_id']

    # create deposit switch
    create_response = client.DepositSwitch.create(
        target_account_id,
        access_token)
    assert create_response['deposit_switch_id'] is not None

    deposit_switch_id = create_response['deposit_switch_id']

    # get deposit switch
    get_response = client.DepositSwitch.get(deposit_switch_id)
    assert get_response['deposit_switch_id'] is not None
    assert get_response['target_item_id'] is not None
    assert get_response['target_account_id'] is not None
    assert get_response['date_created'] is not None
    assert get_response['state'] is not None

    # create deposit switch token
    token_response = client.DepositSwitch.create_token(deposit_switch_id)
    assert token_response['deposit_switch_token'] is not None
    assert token_response['deposit_switch_token_expiration_time'] is not None
