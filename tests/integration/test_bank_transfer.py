import time
import plaid
from plaid.model.products import Products
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.bank_transfer_create_request import BankTransferCreateRequest
from plaid.model.bank_transfer_network import BankTransferNetwork
from plaid.model.bank_transfer_idempotency_key import BankTransferIdempotencyKey
from plaid.model.bank_transfer_type import BankTransferType
from plaid.model.bank_transfer_user import BankTransferUser
from plaid.model.bank_transfer_event_list_request import BankTransferEventListRequest
from plaid.model.bank_transfer_cancel_request import BankTransferCancelRequest
from plaid.model.bank_transfer_idempotency_key import BankTransferIdempotencyKey
from plaid.model.sandbox_bank_transfer_simulate_request import SandboxBankTransferSimulateRequest
from plaid.model.bank_transfer_list_request import BankTransferListRequest
from plaid.model.bank_transfer_event_sync_request import BankTransferEventSyncRequest
from plaid.model.bank_transfer_get_request import BankTransferGetRequest
from plaid.model.bank_transfer_balance_get_request import BankTransferBalanceGetRequest
from plaid.model.bank_transfer_migrate_account_request import BankTransferMigrateAccountRequest
from plaid.model.account_type import AccountType
from plaid.model.ach_class import ACHClass

from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION
)

from random import random
from random import seed

access_token = None
account_id = None
num_retries = 10


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

    accounts_request = AccountsGetRequest(
        access_token=access_token
    )
    accounts_response = client.accounts_get(accounts_request)
    account = next(
        acct for acct in accounts_response['accounts'] if acct['type'] == AccountType('depository'))

    global account_id
    account_id = account['account_id']
    seed()


def create_bank_transfer(client):
    bt_request = BankTransferCreateRequest(
        idempotency_key=BankTransferIdempotencyKey(str(random())),
        access_token=access_token,
        account_id=account_id,
        type=BankTransferType('credit'),
        network=BankTransferNetwork('ach'),
        amount='1.00',
        iso_currency_code='USD',
        description='test',
        user=BankTransferUser(legal_name='Firstname Lastname'),
        ach_class=ACHClass('ppd'),
        custom_tag='',
    )
    bt_response = client.bank_transfer_create(bt_request)
    assert bt_response is not None
    return bt_response['bank_transfer']


def poll_for_response(checks):
    success = False
    for i in range(num_retries):
        try:
            checks()
            success = True
            break
        except AssertionError:
            time.sleep(0.5)
            continue
    assert success


def test_create():
    client = create_client()
    bt = create_bank_transfer(client)
    assert bt is not None
    assert bt['id'] is not None


def test_cancel_success():
    client = create_client()
    bt = create_bank_transfer(client)

    def checks():
        cancel_request = BankTransferCancelRequest(
            bank_transfer_id=bt['id']
        )
        cancel_response = client.bank_transfer_cancel(cancel_request)
        assert cancel_response is not None
    poll_for_response(checks)


def test_cancel_failure():
    client = create_client()
    bt = create_bank_transfer(client)

    simulate_request = SandboxBankTransferSimulateRequest(
        bank_transfer_id=bt['id'],
        event_type='posted'
    )
    simulate_response = client.sandbox_bank_transfer_simulate(simulate_request)
    assert simulate_response is not None
    # allow event simulation to process so we don't inadvertently succeed
    time.sleep(0.1)
    # assert that a BankTransferError is thrown
    try:
        cancel_request = BankTransferCancelRequest(
            bank_transfer_id=bt['id']
        )
        client.bank_transfer_cancel(cancel_request)
        # cancel should not succeed
        assert False
    except plaid.ApiException:
        assert True
    except:
        assert False


def test_list_events():
    client = create_client()
    bt = create_bank_transfer(client)
    bt_id = bt['id']
    simulate_request = SandboxBankTransferSimulateRequest(
        bank_transfer_id=bt_id,
        event_type='posted'
    )
    simulate_response = client.sandbox_bank_transfer_simulate(simulate_request)
    assert simulate_response is not None

    def checks():
        list_events_request = BankTransferEventListRequest(
            bank_transfer_id=bt_id
        )
        list_events_response = client.bank_transfer_event_list(
            list_events_request)
        assert list_events_response is not None
        assert list_events_response['bank_transfer_events'] is not None
        assert len(list_events_response['bank_transfer_events']) >= 1
    poll_for_response(checks)


def test_sync_events():
    client = create_client()
    bt = create_bank_transfer(client)

    def checks():
        sync_request = BankTransferEventSyncRequest(
            after_id=0
        )
        sync_response = client.bank_transfer_event_sync(sync_request)
        assert sync_response is not None
        assert sync_response['bank_transfer_events'] is not None
        assert len(sync_response['bank_transfer_events']) > 0
    poll_for_response(checks)


def test_get():
    client = create_client()
    bt = create_bank_transfer(client)

    def checks():
        get_request = BankTransferGetRequest(
            bank_transfer_id=bt['id']
        )
        get_response = client.bank_transfer_get(get_request)
        assert bt == get_response['bank_transfer']
    poll_for_response(checks)


def test_list():
    client = create_client()
    bt = create_bank_transfer(client)

    def checks():
        list_request = BankTransferListRequest(
            count=1
        )
        list_response = client.bank_transfer_list(list_request)
        assert list_response is not None
        assert len(list_response['bank_transfers']) == 1
    poll_for_response(checks)


def test_balance_get():
    client = create_client()
    balance_request = BankTransferBalanceGetRequest()
    balance_response = client.bank_transfer_balance_get(balance_request)
    assert balance_response is not None
    assert balance_response['balance'] is not None
    assert balance_response['balance']['available'] is not None


def test_migrate_account():
    client = create_client()
    migrate_request = BankTransferMigrateAccountRequest(
        account_number = '100000000',
        routing_number = '121122676',
        account_type = 'checking'
    )
    migrate_response = client.bank_transfer_migrate_account(migrate_request)
    assert migrate_response is not None
    assert migrate_response['access_token'] is not None
