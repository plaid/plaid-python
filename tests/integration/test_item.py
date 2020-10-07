'''
Client.Item.* tests.

Note that when using many of these methods in production, it would be necessary
to handle error cases (e.g. ``INVALID_CREDENTIAL``). However, we don't do that
here since any errors will automatically be marked as failures by the test
runner.
'''

from contextlib import contextmanager

from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION,
)


# Ensure that any items created are also removed
@contextmanager
def ensure_item_removed(access_token):
    try:
        yield
    finally:
        create_client().Item.remove(access_token)


def test_get():
    client = create_client()
    pt_response = client.Sandbox.public_token.create(
        SANDBOX_INSTITUTION, ['transactions'])
    exchange_response = client.Item.public_token.exchange(
        pt_response['public_token'])

    with ensure_item_removed(exchange_response['access_token']):
        get_response = client.Item.get(exchange_response['access_token'])
        assert get_response['item'] is not None


def test_remove():
    client = create_client()
    pt_response = client.Sandbox.public_token.create(
        SANDBOX_INSTITUTION, ['transactions'])
    exchange_response = client.Item.public_token.exchange(
        pt_response['public_token'])

    client.Item.remove(exchange_response['access_token'])


def test_import():
    client = create_client()
    at_response = client.Item.import_item(
        ['identity', 'auth'],
        {'user_id': 'user_good', 'auth_token': 'pass_good'},
        None)
    assert at_response['access_token'] is not None


def test_public_token():
    client = create_client()
    pt_response = client.Sandbox.public_token.create(
        SANDBOX_INSTITUTION, ['transactions'])
    exchange_response = client.Item.public_token.exchange(
        pt_response['public_token'])
    with ensure_item_removed(exchange_response['access_token']):
        assert pt_response['public_token'] is not None
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


def test_sandbox_fire_webhook():
    client = create_client()
    create_response = client.Sandbox.public_token.create(
        SANDBOX_INSTITUTION, ['transactions'],
        webhook='https://plaid.com/foo/bar/hook')
    assert create_response['public_token'] is not None

    # public token -> access token
    exchange_response = client.Item.public_token.exchange(
        create_response['public_token'])
    assert exchange_response['access_token'] is not None

    # fire webhook
    fire_webhook_response = client.Sandbox.item.fire_webhook(
        exchange_response['access_token'],
        'DEFAULT_UPDATE'
    )
    assert fire_webhook_response['webhook_fired'] is True


def test_access_token_invalidate():
    client = create_client()
    pt_response = client.Sandbox.public_token.create(
        SANDBOX_INSTITUTION, ['transactions'])
    exchange_response = client.Item.public_token.exchange(
        pt_response['public_token'])

    try:
        invalidate_response = client.Item.access_token.invalidate(
            exchange_response['access_token'])
        with ensure_item_removed(invalidate_response['new_access_token']):
            assert invalidate_response['new_access_token'] is not None
    except Exception:
        with ensure_item_removed(exchange_response['access_token']):
            raise


def test_webhook_update():
    client = create_client()
    pt_response = client.Sandbox.public_token.create(
        SANDBOX_INSTITUTION, ['transactions'])
    exchange_response = client.Item.public_token.exchange(
        pt_response['public_token'])

    with ensure_item_removed(exchange_response['access_token']):
        webhook_response = client.Item.webhook.update(
            exchange_response['access_token'],
            'https://plaid.com/webhook-test')
        assert (webhook_response['item']['webhook'] ==
                'https://plaid.com/webhook-test')
