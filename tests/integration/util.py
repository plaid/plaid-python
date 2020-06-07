'''Shared objects for integration testing.'''

import os

from plaid import Client


def create_client():
    '''Create a new client for testing.'''
    return Client(
        client_id=os.environ['CLIENT_ID'],
        secret=os.environ['SECRET'],
        environment='sandbox',
        api_version="2019-05-29",
        client_app="plaid-python-unit-tests"
    )


SANDBOX_INSTITUTION = 'ins_109508'
SANDBOX_INSTITUTION_NAME = 'First Platypus Bank'

SANDBOX_INSTITUTIONS = [
    'ins_109508',
    'ins_109509',
    'ins_109510',
    'ins_109511',
    'ins_109512',
]

WEBHOOK_VERIFICATION_KEY_ID = '6c5516e1-92dc-479e-a8ff-5a51992e0001'
