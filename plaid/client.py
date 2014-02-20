import json
from urlparse import urljoin

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
    """
    Python Plain API client https://plaid.io/
    API version 2
    """

    url = 'https://tartan.plaid.com' # Base API URL

    TYPES = (
        ('amex', 'American Express',),
        ('bofa', 'Bank of America',),
        ('chase', 'Chase',),
        ('citi', 'Citi',),
        ('wells', 'Wells Fargo',),
    )

    endpoints = {
        'connect': '/connect',
        'step': '/connect/step'
    }

    def __init__(self, client_id, secret, access_token=None):
        """
        `client_id`     str     Your Plaid client ID
        `secret`        str     Your Plaid secret
        `access_token`  str     Access token if you already have one
        """
        self.client_id = client_id
        self.secret = secret
        self.access_token = None
        if access_token:
            self.set_access_token(access_token)

    def set_access_token(self, access_token):
        self.access_token = access_token

    def get_access_token(self):
        return self.access_token

    # Endpoints

    def connect(self, account_type, username, password, email, options={}):
        """
        Add a bank account user/login to Plaid and receive an access token
        unless a 2nd level of authentication is required, in which case 
        an MFA (Multi Factor Authentication) question(s) is returned

        `account_type`  str     The type of bank account you want to sign in to, must
                                be one of the keys in `TYPES`
        `username`      str     The username for the bank account you want to sign in to
        `password`      str     The password for the bank account you want to sign in to
        `email`         str     The email address associated with the bank account
        `options`       dict
            `pretty`    boolean     Whether to return nicely formatted JSON or not
            `webhook`   str         URL to hit once the account's transactions have been processed
            `mfa_list`  boolean     List all available MFA (Multi Factor Authentication) options
        """
        url = urljoin(self.url, self.endpoints['connect'])

        credentials = {
            'username': username,
            'password': password
        }

        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'type': account_type,
            'credentials': json.dumps(credentials),
            'email': email
        }

        if options:
            data['options'] = json.dumps(options)

        response = requests.post(url, data=data)

        if response.ok:
            json_data = json.loads(response.content)
            if json_data.has_key('access_token'):
                self.access_token = json_data['access_token']

        return response

    def step(self, account_type, mfa, options={}):
        """
        Perform a MFA (Multi Factor Authentication) step, requires `access_token`

        `account_type`  str     The type of bank account you're performing MFA on,
                                must match what you used in the `connect` call
        `mfa`           str     The MFA answer, e.g. an answer to q security question or
                                code sent to your phone, etc.
        `options`       dict
            `send_method`   dict    The send method your MFA answer is for, e.g. {'type': Phone'},
                                    should come from the list from the `mfa_list` option in the 
                                    `connect` call
        """
        url = urljoin(self.url, self.endpoints['step'])

        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'access_token': self.access_token,
            'type': account_type,
            'mfa': mfa
        }

        if options:
            data['options'] = json.dumps(options)

        return requests.post(url, data=data)

    def delete_user(self):
        """
        Delete user from Plaid, requires `access_token`
        """
        url = urljoin(self.url, self.endpoints['connect'])

        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'access_token': self.access_token
        }

        return requests.delete(url, data=data)
        

    def transactions(self, options={}):
        """
        Fetch a list of transactions, requires `access_token`

        `options`   dict
            `pretty`    boolean     Whether to return nicely formatted JSON or not
            `last`      str         Collect all transactions since this transaction ID
        """
        url = urljoin(self.url, self.endpoints['connect'])

        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'access_token': self.access_token,
            'options': json.dumps(options)
        }

        if options:
            data['options'] = json.dumps(options)

        return requests.get(url, data=data)

    def entity(self, entity_id, pretty=False):
        pass

    def categories(self):
        pass

    def category(self, category_id, pretty=False):
        pass

    def categories_by_mapping(self, mapping, type, pretty=False, full_match=True):
        pass
