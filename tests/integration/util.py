'''Shared objects for integration testing.'''

import os
import plaid
from plaid.api import plaid_api

client_id = os.environ['CLIENT_ID']
secret = os.environ['SECRET']

def create_client():
    '''Create a new client for testing.'''
    configuration = plaid.Configuration(
        host=plaid.Environment.Sandbox,
        api_key={
            'clientId': client_id,
            'secret': secret,
            'plaidVersion': '2020-09-14'
        }
    )


    api_client = plaid.ApiClient(configuration)
    return plaid_api.PlaidApi(api_client)

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
