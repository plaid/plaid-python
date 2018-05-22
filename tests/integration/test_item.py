'''
Client.Item.* tests.

Note that when using many of these methods in production, it would be necessary
to handle error cases (e.g. ``INVALID_CREDENTIAL``). However, we don't do that
here since any errors will automatically be marked as failures by the test
runner.
'''

from contextlib import contextmanager

import pytest

from plaid.errors import ItemError

from tests.integration.util import (
    create_client,
    CREDENTIALS,
    INVALID_CREDENTIALS,
    MFA_DEVICE_CREDENTIALS,
    MFA_QUESTIONS_CREDENTIALS,
    MFA_SELECTIONS_CREDENTIALS,
    SANDBOX_INSTITUTION,
)


# Ensure that any items created are also removed
@contextmanager
def ensure_item_removed(access_token):
    try:
        yield
    finally:
        create_client().Item.remove(access_token)


def test_create():
    client = create_client()
    response = client.Item.create(
        CREDENTIALS, SANDBOX_INSTITUTION, ['transactions'])

    with ensure_item_removed(response['access_token']):
        assert response['access_token'] is not None
        assert response['item']['billed_products'] == ['transactions']
        assert response['item']['institution_id'] == SANDBOX_INSTITUTION
        assert response.get('mfa_type') is None


def test_create_invalid_credentials():
    client = create_client()
    with pytest.raises(ItemError) as e:
        client.Item.create(
            INVALID_CREDENTIALS, SANDBOX_INSTITUTION, ['transactions'])
        assert e.code == 'INVALID_CREDENTIALS'


def test_create_with_options():
    client = create_client()
    response = client.Item.create(
        CREDENTIALS,
        SANDBOX_INSTITUTION,
        ['transactions'],
        transactions__start_date='2016-01-01',
        transactions__end_date='2016-02-01',
        transactions__await_results=True,
        webhook='https://plaid.com/webhook-test',
    )

    with ensure_item_removed(response['access_token']):
        assert response['access_token'] is not None
        assert response['item'] is not None
        assert response['item']['webhook'] == 'https://plaid.com/webhook-test'


def test_mfa_device():
    client = create_client()
    item_response = client.Item.create(
        MFA_DEVICE_CREDENTIALS, SANDBOX_INSTITUTION, ['transactions'])

    with ensure_item_removed(item_response['access_token']):
        assert item_response['mfa_type'] == 'device_list'

        # Send MFA indicating which device should receive the code
        device = item_response['device_list'][0]
        mfa_response = client.Item.mfa(
            item_response['access_token'],
            'device_list',
            [device['device_id']],
        )
        assert mfa_response['mfa_type'] == 'device'

        # Send MFA with the actual code
        mfa_response = client.Item.mfa(
            item_response['access_token'], 'device', ['1234'])
        assert mfa_response['item'] is not None


def test_mfa_questions():
    client = create_client()
    item_response = client.Item.create(
        MFA_QUESTIONS_CREDENTIALS, SANDBOX_INSTITUTION, ['transactions'])

    with ensure_item_removed(item_response['access_token']):
        assert item_response['mfa_type'] == 'questions'

        mfa_response = client.Item.mfa(
            item_response['access_token'], 'questions', ['answer_0_0'])
        assert mfa_response['item'] is not None


def test_mfa_selections():
    client = create_client()
    item_response = client.Item.create(
        MFA_SELECTIONS_CREDENTIALS, SANDBOX_INSTITUTION, ['transactions'])

    with ensure_item_removed(item_response['access_token']):
        assert item_response['mfa_type'] == 'selections'

        mfa_response = client.Item.mfa(
            item_response['access_token'], 'selections', ['tomato', 'ketchup'])
        assert mfa_response['item'] is not None


def test_credentials_update():
    client = create_client()
    create_response = client.Item.create(
        CREDENTIALS, SANDBOX_INSTITUTION, ['transactions'])

    with ensure_item_removed(create_response['access_token']):
        client.Sandbox.item.reset_login(create_response['access_token'])

        update_response = client.Item.credentials.update(
            create_response['access_token'], CREDENTIALS)
        assert update_response['item'] is not None


def test_get():
    client = create_client()
    create_response = client.Item.create(
        CREDENTIALS, SANDBOX_INSTITUTION, ['transactions'])

    with ensure_item_removed(create_response['access_token']):
        get_response = client.Item.get(create_response['access_token'])
        assert get_response['item'] is not None


def test_delete():
    client = create_client()
    create_response = client.Item.create(
        CREDENTIALS, SANDBOX_INSTITUTION, ['transactions'])

    delete_response = client.Item.delete(create_response['access_token'])
    assert delete_response['deleted']

def test_remove():
    client = create_client()
    create_response = client.Item.create(
        CREDENTIALS, SANDBOX_INSTITUTION, ['transactions'])

    remove_response = client.Item.remove(create_response['access_token'])
    assert remove_response['removed']

def test_public_token():
    client = create_client()
    item_response = client.Item.create(
        CREDENTIALS, SANDBOX_INSTITUTION, ['transactions'])

    with ensure_item_removed(item_response['access_token']):
        # access token -> public token
        create_response = client.Item.public_token.create(
            item_response['access_token'])
        assert create_response['public_token'] is not None

        # public token -> access token
        exchange_response = client.Item.public_token.exchange(
            create_response['public_token'])
        assert exchange_response['access_token'] is not None

def test_sandbox_public_token():
    client = create_client()
    create_response = client.Sandbox.public_token.create(
        SANDBOX_INSTITUTION, ['transactions'])
    assert create_response['public_token'] is not None

    # public token -> access token
    exchange_response = client.Item.public_token.exchange(
        create_response['public_token'])
    assert exchange_response['access_token'] is not None

def test_access_token_invalidate():
    client = create_client()
    create_response = client.Item.create(
        CREDENTIALS, SANDBOX_INSTITUTION, ['transactions'])

    try:
        invalidate_response = client.Item.access_token.invalidate(
            create_response['access_token'])
        with ensure_item_removed(invalidate_response['new_access_token']):
            assert invalidate_response['new_access_token'] is not None
    except Exception:
        with ensure_item_removed(create_response['access_token']):
            raise


def test_webhook_update():
    client = create_client()
    create_response = client.Item.create(
        CREDENTIALS, SANDBOX_INSTITUTION, ['transactions'])

    with ensure_item_removed(create_response['access_token']):
        webhook_response = client.Item.webhook.update(
            create_response['access_token'], 'https://plaid.com/webhook-test')
        assert (webhook_response['item']['webhook'] ==
                'https://plaid.com/webhook-test')
