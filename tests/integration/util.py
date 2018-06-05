'''Shared objects for integration testing.'''

import os

from plaid import Client


def create_client():
    '''Create a new client for testing.'''
    return Client(os.environ['CLIENT_ID'],
                  os.environ['SECRET'],
                  os.environ['PUBLIC_KEY'],
                  'sandbox',
                  api_version="2017-03-08")

CREDENTIALS = {
    'username': 'user_good',
    'password': 'pass_good',
}

MFA_DEVICE_CREDENTIALS = {
    'username': 'user_good',
    'password': 'mfa_device',
}

MFA_SELECTIONS_CREDENTIALS = {
    'username': 'user_good',
    'password': 'mfa_selections',
}

MFA_QUESTIONS_CREDENTIALS = {
    'username': 'user_good',
    'password': 'mfa_questions_1_1'
}

INVALID_CREDENTIALS = {
    'username': 'user_bad',
    'password': 'pass_bad',
}

SANDBOX_INSTITUTION = 'ins_109508'
SANDBOX_INSTITUTION_NAME = 'First Platypus Bank'

SANDBOX_INSTITUTIONS = [
    'ins_109508',
    'ins_109509',
    'ins_109510',
    'ins_109511',
    'ins_109512',
]
