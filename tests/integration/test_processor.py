'''
Client.Processor.* tests.
'''
from tests.integration.util import (
    create_client
)
import pytest
import plaid
import json
from plaid.model.processor_token_create_request import ProcessorTokenCreateRequest
from plaid.model.processor_stripe_bank_account_token_create_request import ProcessorStripeBankAccountTokenCreateRequest


def test_create_token():
    client = create_client()
    # Just test the failure case - behavior here depends on the API keys used
    with pytest.raises(plaid.ApiException) as e:
        request = ProcessorTokenCreateRequest(
            access_token='fakeAccessToken',
            account_id='fakeAccountId',
            processor='fakeProcessor'
        )
        client.processor_token_create(request)
        response = json.loads(e.body)
        assert response['error_code'] == 'INVALID_INPUT'


def test_stripe_processor_token():
    client = create_client()
    # Just test the failure case - behavior here depends on the API keys used
    with pytest.raises(plaid.ApiException) as e:
        request = ProcessorStripeBankAccountTokenCreateRequest(
            access_token='fakeAccessToken',
            account_id='fakeAccountId',
        )
        client.processor_stripe_bank_account_token_create(request)
        response = json.loads(e.body)
        assert response['error_code'] == 'INVALID_INPUT'


def test_dwolla_processor_token():
    client = create_client()
    # Just test the failure case - behavior here depends on the API keys used
    with pytest.raises(plaid.ApiException) as e:
        request = ProcessorTokenCreateRequest(
            access_token='fakeAccessToken',
            account_id='fakeAccountId',
            processor='dwolla'
        )
        client.processor_token_create(request)
        response = json.loads(e.body)
        assert response['error_code'] == 'INVALID_INPUT'