from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION
)
from random import random
from random import seed
from plaid.errors import BankTransferError

access_token = None
account_id = None

def setup_module(module):
    client = create_client()
    pt_response = client.Sandbox.public_token.create(
        SANDBOX_INSTITUTION, ['auth'])
    exchange_response = client.Item.public_token.exchange(
        pt_response['public_token'])
    global access_token
    access_token = exchange_response['access_token']
    accounts_response = client.Accounts.get(access_token)
    account = next(acct for acct in accounts_response['accounts'] if acct['type'] == 'depository')
    global account_id
    account_id = account['account_id']
    seed()

def create_bank_transfer(client):
    bt_response = client.BankTransfer.create(
        str(random()),
        access_token,
        account_id,
        'credit',
        'ach',
        '1.00',
        'USD',
        'test',
        {'legal_name': 'Firstname Lastname'},
        metadata=None,
        ach_class='ppd',
        custom_tag=None,
    )
    assert bt_response is not None
    return bt_response['bank_transfer']

def test_create():
    client = create_client()
    bt = create_bank_transfer(client)
    assert bt is not None
    assert bt['id'] is not None

def test_cancel_success():
    client = create_client()
    bt = create_bank_transfer(client)
    cancel_response = client.BankTransfer.cancel(bt['id'])
    assert cancel_response is not None

def test_cancel_failure():
    client = create_client()
    bt = create_bank_transfer(client)
    simulate_response = client.Sandbox.bank_transfer.simulate(bt['id'], 'posted')
    assert simulate_response is not None
    # assert that a BankTransferError is thrown
    try:
        client.BankTransfer.cancel(bt['id'])
    except BankTransferError:
        assert True
    except:
        assert False

def test_list_events():
    client = create_client()
    bt = create_bank_transfer(client)
    bt_id = bt['id']
    simulate_response = client.Sandbox.bank_transfer.simulate(bt['id'], 'posted')
    assert simulate_response is not None
    list_events_response = client.BankTransfer.list_events(bank_transfer_id=bt_id)
    assert list_events_response is not None
    assert list_events_response['bank_transfer_events'] is not None
    assert len(list_events_response['bank_transfer_events']) == 2

def test_sync_events():
    client = create_client()
    bt = create_bank_transfer(client)
    sync_response = client.BankTransfer.sync_events(0)
    assert sync_response is not None
    assert sync_response['bank_transfer_events'] is not None
    assert len(sync_response['bank_transfer_events']) > 0

def test_get():
    client = create_client()
    bt = create_bank_transfer(client)
    get_response = client.BankTransfer.get(bt['id'])
    assert bt == get_response['bank_transfer']

def test_list():
    client = create_client()
    bt = create_bank_transfer(client)
    list_response = client.BankTransfer.list(count=1)
    assert list_response is not None
    assert len(list_response['bank_transfers']) == 1
    assert list_response['bank_transfers'][0] == bt

def test_balance_get():
    client = create_client()
    balance_response = client.BankTransfer.balance.get()
    assert balance_response is not None
    assert balance_response['balance'] is not None
    assert balance_response['balance']['available'] is not None

def test_migrate_account():
    client = create_client()
    migrate_response = client.BankTransfer.migrate_account('100000000', '121122676', 'checking')
    assert migrate_response is not None
    assert migrate_response['access_token'] is not None
