import json

import requests

# @todo Sandboxing?
# @todo "Single Request Call"

"""
HTTP response codes
200: Success
400: Bad Request
401: Unauthorized
402: Request Failed
404: Cannot be found 
50X: Server error

Maybe User/Transaction class?
"""

class Client(object):

    url = 'https://tartan.plaid.com'

    TYPES = (
        ('amex', 'American Express',),
        ('bofa', 'Bank of America',),
        ('chase', 'Chase',),
        ('citi', 'Citi',),
        ('wells', 'Wells Fargo',),
    )

    def __init__(self, client_id, secret, access_token=None):
        self.client_id = client_id
        self.secret = secret
        if access_token:
            self.set_access_token(access_token)

    def set_access_token(self, access_token):
        self.access_token = access_token

    # Endpoints

    def add_user(self, username, password, email, type, pretty=False, webhook=None, list=False):
        pass

    def step(self, client_id, secret, access_token, type, mfa, send_method=False):
        pass

    def delete_user(self, client_id, secret, access_token):
        pass

    def transactions(self, client_id, secret, access_token, last=None, pretty=False):
        pass

    def entity(self, entity_id, pretty=False):
        pass

    def categories(self):
        pass

    def category(self, category_id, pretty=False):
        pass

    def categories_by_mapping(self, mapping, type, pretty=False, full_match=True):
        pass
