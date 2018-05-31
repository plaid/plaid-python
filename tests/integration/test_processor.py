'''
Client.Processor.* tests.
'''

from contextlib import contextmanager

import pytest

from plaid.errors import InvalidRequestError

from tests.integration.util import (
    create_client
)


def test_stripe_processor_token():
    client = create_client()
    # Just test the failure case - behavior here depends on the API keys used
    with pytest.raises(InvalidRequestError) as e:
        client.Processor.stripeBankAccountTokenCreate(
            'fakeAccessToken', 'fakeAccountId')
        assert e.code == 'INVALID_INPUT'


def test_dwolla_processor_token():
    client = create_client()
    # Just test the failure case - behavior here depends on the API keys used
    with pytest.raises(InvalidRequestError) as e:
        client.Processor.dwollaBankAccountTokenCreate(
            'fakeAccessToken', 'fakeAccountId')
        assert e.code == 'INVALID_INPUT'
