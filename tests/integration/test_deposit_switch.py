from tests.integration.util import (
    create_client,
)

access_token = None
target_account_id = None
deposit_switch_id = None

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

    # get account id
    account_id_response = client.Accounts.get(access_token)
    assert len(account_id_response['accounts']) != 0
    global target_account_id
    target_account_id = account_id_response['accounts'][0]['account_id']

    # create deposit switch
    deposit_switch_response = client.DepositSwitch.create(
        target_account_id,
        access_token)
    assert deposit_switch_response['deposit_switch_id'] is not None

    global deposit_switch_id
    deposit_switch_id = deposit_switch_response['deposit_switch_id']

def test_get():
    client = create_client()
    response = client.DepositSwitch.get(deposit_switch_id)
    assert response['deposit_switch_id'] is not None
    assert response['target_item_id'] is not None
    assert response['target_account_id'] is not None
    assert response['date_created'] is not None
    assert response['state'] is not None

def test_create():
    client = create_client()
    response = client.DepositSwitch.create(target_account_id, access_token)
    assert response['deposit_switch_id'] is not None

def test_create_token():
    client = create_client()
    response = client.DepositSwitch.create_token(deposit_switch_id)
    assert response['deposit_switch_token'] is not None
    assert response['deposit_switch_token_expiration_time'] is not None
