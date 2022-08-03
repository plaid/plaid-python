'''
Client.Item.* tests.

Note that when using many of these methods in production, it would be necessary
to handle error cases (e.g. ``INVALID_CREDENTIAL``). However, we don't do that
here since any errors will automatically be marked as failures by the test
runner.
'''

import json
from contextlib import contextmanager

import plaid
from plaid.model.products import Products
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.item_remove_request import ItemRemoveRequest
from plaid.model.item_get_request import ItemGetRequest
from plaid.model.item_import_request import ItemImportRequest
from plaid.model.item_import_request_user_auth import ItemImportRequestUserAuth
from plaid.model.sandbox_item_fire_webhook_request import SandboxItemFireWebhookRequest
from plaid.model.item_access_token_invalidate_request import ItemAccessTokenInvalidateRequest
from plaid.model.item_webhook_update_request import ItemWebhookUpdateRequest
from plaid.model.sandbox_public_token_create_request_options import SandboxPublicTokenCreateRequestOptions


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
        request = ItemRemoveRequest(
            access_token=access_token
        )
        client = create_client()
        client.item_remove(request)


def test_get():
    client = create_client()
    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('transactions')]
    )

    pt_response = client.sandbox_public_token_create(pt_request)

    exchange_request = ItemPublicTokenExchangeRequest(
        public_token=pt_response['public_token']
    )

    exchange_response = client.item_public_token_exchange(exchange_request)

    with ensure_item_removed(exchange_response['access_token']):
        get_request = ItemGetRequest(
            access_token=exchange_response['access_token']
        )
        get_response = client.item_get(get_request)
        assert get_response['item'] is not None


def test_remove():
    client = create_client()
    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('transactions')]
    )

    pt_response = client.sandbox_public_token_create(pt_request)

    exchange_request = ItemPublicTokenExchangeRequest(
        public_token=pt_response['public_token']
    )

    exchange_response = client.item_public_token_exchange(exchange_request)
    ir_request = ItemRemoveRequest(
        access_token=exchange_response['access_token']
    )

    remove_response = client.item_remove(ir_request)
    assert remove_response['request_id']

    try:
        ir_request = ItemRemoveRequest(
            access_token=exchange_response['access_token']
        )
        client.item_remove(ir_request)
    except plaid.ApiException as e:
        response = json.loads(e.body)
        assert response['error_code'] == 'ITEM_NOT_FOUND'


def test_import():
    client = create_client()
    at_request = ItemImportRequest(
        products=[Products('identity'), Products('auth')],
        user_auth=ItemImportRequestUserAuth(
            user_id='user_good',
            auth_token='pass_good'
        )
    )
    at_response = client.item_import(at_request)
    assert at_response['access_token'] is not None


def test_public_token():
    client = create_client()
    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('transactions')]
    )

    pt_response = client.sandbox_public_token_create(pt_request)
    exchange_request = ItemPublicTokenExchangeRequest(
        public_token=pt_response['public_token']
    )

    exchange_response = client.item_public_token_exchange(exchange_request)

    with ensure_item_removed(exchange_response['access_token']):
        assert pt_response['public_token'] is not None
        assert exchange_response['access_token'] is not None


def test_sandbox_public_token():
    client = create_client()
    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('transactions')]
    )

    pt_response = client.sandbox_public_token_create(pt_request)
    assert pt_response['public_token'] is not None

    # public token -> access token
    exchange_request = ItemPublicTokenExchangeRequest(
        public_token=pt_response['public_token']
    )

    exchange_response = client.item_public_token_exchange(exchange_request)
    assert exchange_response['access_token'] is not None


def test_sandbox_fire_webhook():
    client = create_client()
    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('transactions')],
        options=SandboxPublicTokenCreateRequestOptions(
            webhook='https://plaid.com/foo/bar/hook'
        )
    )

    pt_response = client.sandbox_public_token_create(pt_request)
    assert pt_response['public_token'] is not None

    # public token -> access token
    exchange_request = ItemPublicTokenExchangeRequest(
        public_token=pt_response['public_token']
    )

    exchange_response = client.item_public_token_exchange(exchange_request)
    assert exchange_response['access_token'] is not None

    # fire webhook
    fire_request = SandboxItemFireWebhookRequest(
        access_token=exchange_response['access_token'],
        webhook_code='DEFAULT_UPDATE'
    )

    fire_webhook_response = client.sandbox_item_fire_webhook(fire_request)
    assert fire_webhook_response['webhook_fired'] is True


def test_access_token_invalidate():
    client = create_client()
    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('transactions')]
    )

    pt_response = client.sandbox_public_token_create(pt_request)
    exchange_request = ItemPublicTokenExchangeRequest(
        public_token=pt_response['public_token']
    )

    exchange_response = client.item_public_token_exchange(exchange_request)

    try:
        invalidate_request = ItemAccessTokenInvalidateRequest(
            access_token=exchange_response['access_token']
        )
        invalidate_response = client.item_access_token_invalidate(
            invalidate_request)
        with ensure_item_removed(invalidate_response['new_access_token']):
            assert invalidate_response['new_access_token'] is not None
    except Exception:
        with ensure_item_removed(exchange_response['access_token']):
            raise


def test_webhook_update():
    client = create_client()
    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('transactions')]
    )

    pt_response = client.sandbox_public_token_create(pt_request)

    exchange_request = ItemPublicTokenExchangeRequest(
        public_token=pt_response['public_token']
    )

    exchange_response = client.item_public_token_exchange(exchange_request)

    with ensure_item_removed(exchange_response['access_token']):
        webhook_request = ItemWebhookUpdateRequest(
            access_token=exchange_response['access_token'],
            webhook='https://plaid.com/webhook-test'
        )
        webhook_response = client.item_webhook_update(webhook_request)
        assert (webhook_response['item']['webhook'] ==
                'https://plaid.com/webhook-test')
