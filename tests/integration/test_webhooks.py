'''
Webhook tests
'''

from tests.integration.util import (
    create_client,
    WEBHOOK_VERIFICATION_KEY_ID
)


def test_get_webhook_verification_key():
    client = create_client()
    pt_response = client.Webhooks.get_verification_key(
        WEBHOOK_VERIFICATION_KEY_ID
    )
    assert pt_response['key'] is not None
    assert pt_response['key']['alg'] is not None
    assert pt_response['key']['created_at'] is not None
    assert pt_response['key']['crv'] is not None
    assert pt_response['key']['kid'] is not None
    assert pt_response['key']['kty'] is not None
    assert pt_response['key']['use'] is not None
    assert pt_response['key']['x'] is not None
    assert pt_response['key']['y'] is not None
