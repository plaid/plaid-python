'''
Webhook tests
'''

from tests.integration.util import (
    create_client,
    WEBHOOK_VERIFICATION_KEY_ID
)

from plaid.model.webhook_verification_key_get_request import WebhookVerificationKeyGetRequest

def test_get_webhook_verification_key():
    client = create_client()

    request = WebhookVerificationKeyGetRequest(
        key_id=WEBHOOK_VERIFICATION_KEY_ID
    )
    response = client.webhook_verification_key_get(request)
    assert response['key'] is not None
    assert response['key']['alg'] is not None
    assert response['key']['crv'] is not None
    assert response['key']['kid'] is not None
    assert response['key']['kty'] is not None
    assert response['key']['use'] is not None
    assert response['key']['x'] is not None
    assert response['key']['y'] is not None