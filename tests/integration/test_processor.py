'''
Client.Processor.* tests.
'''
import pytest

from plaid.errors import InvalidRequestError

from tests.integration.util import (
    create_client
)


def test_create_token():
    client = create_client()
    # Just test the failure case - behavior here depends on the API keys used
    with pytest.raises(InvalidRequestError) as e:
        client.Processor.token_create(
            'fakeAccessToken', 'fakeAccountId', 'fakeProcessor')
        assert e.code == 'INVALID_INPUT'


def test_stripe_processor_token():
    client = create_client()
    # Just test the failure case - behavior here depends on the API keys used
    with pytest.raises(InvalidRequestError) as e:
        client.Processor.stripe_bank_account_token_create(
            'fakeAccessToken', 'fakeAccountId')
        assert e.code == 'INVALID_INPUT'


def test_dwolla_processor_token():
    client = create_client()
    # Just test the failure case - behavior here depends on the API keys used
    with pytest.raises(InvalidRequestError) as e:
        client.Processor.dwolla_bank_account_token_create(
            'fakeAccessToken', 'fakeAccountId')
        assert e.code == 'INVALID_INPUT'
