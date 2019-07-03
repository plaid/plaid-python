'''Shared objects for integration testing.'''

import os

from plaid import Client


def create_client():
    '''Create a new client for testing.'''
    return Client(os.environ['CLIENT_ID'],
                  os.environ['SECRET'],
                  os.environ['PUBLIC_KEY'],
                  'sandbox',
                  api_version="2019-05-29",
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
