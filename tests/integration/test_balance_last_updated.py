from datetime import (
  datetime,
  timedelta,
)

from plaid.errors import PlaidError

from tests.integration.util import (
    create_client,
    BALANCE_INSTITUTION,
)

access_token = None


def setup_module(module):
    client = create_client()
    pt_response = client.Sandbox.public_token.create(
        BALANCE_INSTITUTION, ['transactions'])
    exchange_response = client.Item.public_token.exchange(
        pt_response['public_token'])
    global access_token
    access_token = exchange_response['access_token']


def teardown_module(module):
    client = create_client()
    client.Item.remove(access_token)


def test_balance_get_with_last_updated():
    client = create_client()

    # verify last_updated_datetime
    min_last_updated = (datetime.utcnow() - timedelta(2)).replace(
        microsecond=0).isoformat() + '+00:00'
    response = client.Accounts.balance.get(
        access_token, min_last_updated_datetime=min_last_updated)
    assert response['accounts'] is not None
    last_updated = response['accounts'][0]['balances']['last_updated_datetime']
    assert last_updated is not None

    # error if last_updated_datetime is earlier than the min requested
    min_last_updated = datetime.utcnow().replace(
        microsecond=0).isoformat() + '+00:00'
    try:
        response = client.Accounts.balance.get(
            access_token, min_last_updated_datetime=min_last_updated)
    except PlaidError as e:
        assert e.code == 'LAST_UPDATED_DATETIME_OUT_OF_RANGE'
