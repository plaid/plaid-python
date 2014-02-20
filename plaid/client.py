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

    url = 'https://tartan.plaid.com'

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
        self.client_id = client_id
        self.secret = secret
        if access_token:
            self.set_access_token(access_token)

    def set_access_token(self, access_token):
        self.access_token = access_token

    # Endpoints

    def connect(self, account_type, username, password, email, \
            pretty=False, webhook=None, mfa_list=False):
        """
        Add a bank account user/login to Plaid and receive an access token
        unless a 2nd level of authentication is required, in which case 
        an MFA (Multi Factor Authentication) question(s) is returned
        """
        url = urljoin(self.url, self.endpoints['connect'])

        credentials = {
            'username': username,
            'password': password
        }

        options = {
            'pretty': pretty,
            'list': mfa_list
        }

        if webhook:
            options['webhook'] = webhook

        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'type': account_type,
            'credentials': json.dumps(credentials),
            'email': email,
            'options': json.dumps(options)
        }

        response = requests.post(url, data=data)

        if response.ok:
            json_data = json.loads(response.content)
            if json_data.has_key('access_token'):
                self.access_token = json_data['access_token']

        return response

    def step(self, account_type, mfa, pretty=False, send_method_type=None):
        """
        """
        url = urljoin(self.url, '/connect/step')

        options = {
            'pretty': pretty
        }

        if send_method_type:
            options['send_method'] = {'type': send_method_type}

        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'access_token': self.access_token,
            'type': account_type,
            'mfa': mfa,
            'options': json.dumps(options)
        }

        return requests.post(url, data=data)

    def delete_user(self):
        pass

    def transactions(self, last=None, pretty=False):
        """
        Fetch a list of transactions
        """
        url = urljoin(self.url, '/connect')

        options = {
            'pretty': pretty
        }

        if last:
            options['last'] = last

        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'access_token': self.access_token,
            'options': json.dumps(options)
        }

        return requests.get(url, data=data)

    def entity(self, entity_id, pretty=False):
        pass

    def categories(self):
        pass

    def category(self, category_id, pretty=False):
        pass

    def categories_by_mapping(self, mapping, type, pretty=False, full_match=True):
        pass
