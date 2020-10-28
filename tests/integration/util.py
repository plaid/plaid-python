'''Shared objects for integration testing.'''

import os

from plaid import Client


def create_client():
    print(os.environ['CLIENT_ID'], os.environ['SECRET'])
    '''Create a new client for testing.'''
    return Client(os.environ['CLIENT_ID'],
                  os.environ['SECRET'],
                  'sandbox',
                  client_app="plaid-python-unit-tests")


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
