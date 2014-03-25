import json
from urlparse import urljoin

import requests

# @todo Sandboxing?
# @todo "Single Request Call"

def require_access_token(func):
    def inner_func(self, *args, **kwargs):
        if not self.access_token:
            raise Exception('`%s` method requires `access_token`' % func.__name__)
        return func(self, *args, **kwargs)
    return inner_func


class Client(object):
    """
    Python Plain API v2 client https://plaid.io/

    See official documentation at: https://plaid.io/v2/docs
    """

    url = 'https://tartan.plaid.com' # Base API URL

    ACCOUNT_TYPES = (
        ('amex', 'American Express',),
        ('bofa', 'Bank of America',),
        ('chase', 'Chase',),
        ('citi', 'Citi',),
        ('wells', 'Wells Fargo',),
    )

    CATEGORY_TYPES = [
        'plaid',
        'foursquare',
        'factual',
        'amex'
    ]

    endpoints = {
        'connect': '/connect',
        'step': '/connect/step',
        'entity': '/entity',
        'categories': '/category',
        'category': '/category/id/%s',
        'categories_by_mapping': '/category/map',
        'balance': '/balance'
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

    def get_account_types(self):
        return self.ACCOUNT_TYPES

    # Endpoints

    def connect(self, account_type, username, password, email, options={}):
        """
        Add a bank account user/login to Plaid and receive an access token
        unless a 2nd level of authentication is required, in which case 
        an MFA (Multi Factor Authentication) question(s) is returned

        `account_type`  str     The type of bank account you want to sign in to, must
                                be one of the keys in `ACCOUNT_TYPES`
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

    @require_access_token
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

    @require_access_token
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
        

    @require_access_token
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

    def entity(self, entity_id, options={}):
        """
        Fetch a specific entity's data

        `entity_id`     str     Entity id to fetch
        `options`       dict
            `pretty`    boolean Whether to return nicely formatted JSON or not
        """
        url = urljoin(self.url, self.endpoints['entity'])
        data = {
            'entity_id': entity_id
        }

        if options:
            data['options'] = json.dumps(options)

        return requests.get(url, data=data)

    def categories(self):
        """
        Fetch all categories
        """
        url = urljoin(self.url, self.endpoints['categories'])
        return requests.get(url)

    def category(self, category_id, options={}):
        """
        Fetch a specific category

        `category_id`   str     Category id to fetch
        `options`       dict
            `pretty`    boolean Whether to return nicely formatted JSON or not
        """
        url = urljoin(self.url, self.endpoints['category']) % category_id
        data = {}
        if options:
            data['options'] = json.dumps(options)
        return requests.get(url, data=data)

    def categories_by_mapping(self, mapping, category_type, options={}):
        """
        Fetch category data by category mapping and data source

        `mapping`       str     The category mapping to explore, e.g. "Food > Spanish Restaurant",
                                see all categories here: 
                                https://github.com/plaid/Support/blob/master/categories.md
        `category_type` str     The category data source, must be a value from `CATEGORY_TYPES`
        `options`       dict
            `pretty`        boolean     Whether to return nicely formatted JSON or not
            `full_match`    boolean     Whether to try an exact match for `mapping`. Setting
                                        to `False` will return best match.
        """
        url = urljoin(self.url, self.endpoints['categories_by_mapping'])
        data = {
            'mapping': mapping,
            'type': category_type
        }
        if options:
            data['options'] = json.dumps(options)
        return requests.get(url, data=data)

    @require_access_token
    def balance(self, options = {}):
        """
        Fetch the real-time balance of the user's accounts

        `options`       dict
            `pretty`        boolean     Whether to return nicely formatted JSON or not
        """
        url = urljoin(self.url, self.endpoints['balance'])
        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'access_token': self.access_token
        }
        if options:
            data['options'] = json.dumps(options)

        return requests.get(url, data=data)

