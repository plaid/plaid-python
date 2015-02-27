import json
from urlparse import urljoin
from PlaidError import PlaidError
from PlaidMfaResetError import PlaidMfaResetError
from datetime import datetime
from http import http_request

# @todo Sandboxing?
# @todo "Single Request Call"

def require_access_token(func):
    def inner_func(self, *args, **kwargs):
        if not self.access_token:
            raise Exception('`%s` method requires `access_token`' %
                            func.__name__)
        return func(self, *args, **kwargs)
    return inner_func

def as_dictionary(func):
    def wrapper_func(*args, **kwargs):
        retval = func(*args, **kwargs)
        if retval.ok:
            return json.loads(retval.content)
        else:
            # TODO handle these plaid errors better
            if retval.json()['code'] == 1215:
                raise PlaidMfaResetError(retval.json()['resolve'])
            else:
                raise PlaidError(retval.json()['resolve'])
        return retval
    return wrapper_func

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError, e:
        return False
    return True

class Client(object):
    """
    Python Plain API v2 client https://plaid.io/

    See official documentation at: https://plaid.io/v2/docs
    """

    url = 'https://tartan.plaid.com'  # Base API URL

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
        'connect_step': '/connect/step',
        'entity': '/entity',
        'categories': '/category',
        'category': '/category/id/%s',
        'categories_by_mapping': '/category/map',
        'balance': '/balance',
        'auth': '/auth',
        'auth_step': '/auth/step',
        'numbers': '/auth/get',
        'institutions': '/institutions',
        'upgrade': '/upgrade',
        'transactions': '/connect/get'
    }

    def __init__(self, client_id, secret, url, access_token=None):
        """
        `client_id`     str     Your Plaid client ID
        `secret`        str     Your Plaid secret
        `access_token`  str     Access token if you already have one
        `url`           str     Url of the plaid endpoint to hit
        """
        self.client_id = client_id
        self.secret = secret
        self.access_token = None
        self.url = url

        if access_token:
            self.set_access_token(access_token)

    def set_access_token(self, access_token):
        self.access_token = access_token

    def get_access_token(self):
        return self.access_token

    def get_account_types(self):
        return self.ACCOUNT_TYPES

    @require_access_token
    def sandboxed(self):
        return self.access_token == 'test'

    # Endpoints
    @as_dictionary
    def connect(self, account_type, username, password, email, options=None):
        """
        Add a bank account user/login to Plaid and receive an access token
        unless a 2nd level of authentication is required, in which case
        an MFA (Multi Factor Authentication) question(s) is returned

        `account_type`  str     The type of bank account you want to sign in
                                to, must be one of the keys in `ACCOUNT_TYPES`
        `username`      str     The username for the bank account you want to
                                sign in to
        `password`      str     The password for the bank account you want to
                                sign in to
        `email`         str     The email address associated with the bank
                                account
        `options`       dict
            `webhook`   str         URL to hit once the account's transactions
                                    have been processed
            `mfa_list`  boolean     List all available MFA (Multi Factor
                                    Authentication) options
        """
        if options is None:
            options = {}
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

        response = http_request(url, 'POST', data)

        if response.ok:
            json_data = json.loads(response.content)
            if json_data.has_key('access_token'):
                self.access_token = json_data['access_token']

        return response

    @as_dictionary
    def auth(self, account_type, username, password, options=None):
        """
        Add a bank account user/login to Plaid and receive an access token
        unless a 2nd level of authentication is required, in which case
        an MFA (Multi Factor Authentication) question(s) is returned

        `account_type`  str     The type of bank account you want to sign in
                                to, must be one of the keys in `ACCOUNT_TYPES`
        `username`      str     The username for the bank account you want to
                                sign in to
        `password`      str     The password for the bank account you want to
                                sign in to
        `options`       dict
            `webhook`   str         URL to hit once the account's transactions
                                    have been processed
            `mfa_list`  boolean     List all available MFA (Multi Factor
                                    Authentication) options
        """
        if options is None:
            options = {}
        url = urljoin(self.url, self.endpoints['auth'])

        credentials = {
            'username': username,
            'password': password
        }

        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'type': account_type,
            'credentials': json.dumps(credentials)
        }

        if options:
            data['options'] = json.dumps(options)

        response = http_request(url, 'POST', data)

        if response.ok:
            json_data = json.loads(response.content)
            if json_data.has_key('access_token'):
                self.access_token = json_data['access_token']

        return response

    @require_access_token
    @as_dictionary
    def connect_step(self, mfa, account_type=None, options=None):
        """
        Perform a MFA (Multi Factor Authentication) step, requires
        `access_token`

        `account_type`  str     The type of bank account you're performing MFA
                                on, must match what you used in the `connect`
                                call
        `mfa`           str     The MFA answer, e.g. an answer to q security
                                question or code sent to your phone, etc.
        `options`       dict
            `send_method`   dict    The send method your MFA answer is for,
                                    e.g. {'type': Phone'}, should come from
                                    the list from the `mfa_list` option in
                                    the `connect` call
        """
        if options is None:
            options = {}
        url = urljoin(self.url, self.endpoints['connect_step'])

        # Handle dictionary MFAs
        if isinstance(mfa, dict):
            mfa = json.dumps(mfa)

        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'access_token': self.access_token,
            'type': account_type,
            'mfa': mfa
        }

        if options:
            data['options'] = json.dumps(options)

        return http_request(url, 'POST', data)

    @require_access_token
    @as_dictionary
    def auth_step(self, mfa, account_type=None, options=None):
        """
        Perform a MFA (Multi Factor Authentication) step, requires
        `access_token`

        `account_type`  str     The type of bank account you're performing MFA
                                on, must match what you used in the `connect`
                                call
        `mfa`           str     The MFA answer, e.g. an answer to q security
                                question or code sent to your phone, etc.
        `options`       dict
            `send_method`   dict    The send method your MFA answer is for,
                                    e.g. {'type': Phone'}, should come from
                                    the list from the `mfa_list` option in
                                    the `connect` call
        """
        if options is None:
            options = {}
        url = urljoin(self.url, self.endpoints['auth_step'])

        # Handle dictionary MFAs
        if isinstance(mfa, dict):
            mfa = json.dumps(mfa)

        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'access_token': self.access_token,
            'type': account_type,
            'mfa': mfa
        }

        if options:
            data['options'] = json.dumps(options)

        return http_request(url, 'POST', data)

    @require_access_token
    @as_dictionary
    def upgrade(self, upgrade_to):
        """
        Upgrade account to another plaid type

        """
        url = urljoin(self.url, self.endpoints['upgrade'])

        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'access_token': self.access_token,
            'upgrade_to': upgrade_to
        }

        return http_request(url, 'POST', data)


    @require_access_token
    @as_dictionary
    def delete_connect_user(self):
        """
        Delete user from Plaid connect, requires `access_token`
        """
        url = urljoin(self.url, self.endpoints['connect'])

        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'access_token': self.access_token
        }

        return http_request(url, 'DELETE', data)


    @require_access_token
    @as_dictionary
    def delete_auth_user(self):
        """
        Delete user from Plaid auth, requires `access_token`
        """
        url = urljoin(self.url, self.endpoints['auth'])

        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'access_token': self.access_token
        }

        return http_request(url, 'DELETE', data)


    @require_access_token
    def transactions(self, options=None):
        """
        Fetch a list of transactions, requires `access_token`
        !!! DOES NOT USE as_dictionary decorator due to sketchy sandbox handling code

        `options`   dict
        """
        url = urljoin(self.url, self.endpoints['transactions'])

        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'access_token': self.access_token,
        }

        if options and not self.sandboxed():
            # Options not supported in sandbox mode - handle manually below
            data['options'] = json.dumps(options)

        # Make the request and raise exception if it's fucked up
        transactions_request = http_request(url, 'POST', data)
        if transactions_request.ok:
            json_response = json.loads(transactions_request.content)
        else:
            raise PlaidError(transactions_request.json()['resolve'])

        if self.sandboxed():
            # We have to manually apply the specified options
            filtered_transactions = []
            transactions = json_response['transactions']

            # Possible options:
            # 1) filter by account_id ('account')
            check_account = 'account' in options

            # 2) filter by date greater than or equal to a given date ('gte')
            check_date = 'gte' in options

            correct_account = True
            correct_date = True
            for transaction in transactions:
                if check_account:
                    correct_account = transaction['_account'] == options['account']
                if check_date:
                    transaction_date = datetime.strptime(transaction['date'], "%Y-%m-%d").date()
                    threshold_date = datetime.strptime(options['gte'], "%Y-%m-%d").date()
                    correct_date = transaction_date >= threshold_date

                if correct_date and correct_account:
                    filtered_transactions.append(transaction)

            json_response['transactions'] = filtered_transactions

        return json_response

    @as_dictionary
    def entity(self, entity_id, options=None):
        """
        Fetch a specific entity's data

        `entity_id`     str     Entity id to fetch
        """
        url = urljoin(self.url, self.endpoints['entity'])
        return http_request(url, 'GET', {'entity_id': entity_id})

    @as_dictionary
    def categories(self):
        """
        Fetch all categories
        """
        url = urljoin(self.url, self.endpoints['categories'])
        return http_request(url, 'GET')

    @as_dictionary
    def category(self, category_id, options=None):
        """
        Fetch a specific category

        `category_id`   str     Category id to fetch
        """
        url = urljoin(self.url, self.endpoints['category']) % category_id
        return http_request(url, 'GET')

    @as_dictionary
    def categories_by_mapping(self, mapping, category_type, options=None):
        """
        Fetch category data by category mapping and data source

        `mapping`       str     The category mapping to explore,
                                e.g. "Food > Spanish Restaurant",
                                see all categories here:
                                https://github.com/plaid/Support/blob/master/categories.md
        `category_type` str     The category data source, must be a value from
                                `CATEGORY_TYPES`
        `options`       dict
            `full_match`    boolean     Whether to try an exact match for
                                        `mapping`. Setting to `False` will
                                        return best match.
        """
        if options is None:
            options = {}
        url = urljoin(self.url, self.endpoints['categories_by_mapping'])
        data = {
            'mapping': mapping,
            'type': category_type
        }
        if options:
            data['options'] = json.dumps(options)
        return http_request(url, 'GET', data)

    @require_access_token
    @as_dictionary
    def balance(self, options=None):
        """
        Fetch the real-time balance of the user's accounts

        """
        if options is None:
            options = {}
        url = urljoin(self.url, self.endpoints['balance'])
        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'access_token': self.access_token
        }
        if options:
            data['options'] = json.dumps(options)

        return http_request(url, 'GET', data)

    @require_access_token
    @as_dictionary
    def numbers(self):
        """
        Fetch the account/routing numbers for this user

        """
        url = urljoin(self.url, self.endpoints['numbers'])
        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'access_token': self.access_token
        }

        return http_request(url, 'POST', data)

    @as_dictionary
    def institutions(self):
        """
        Fetch the available institutions
        """
        url = urljoin(self.url, self.endpoints['institutions'])
        return http_request(url, 'GET')

    @as_dictionary
    def institution(self, institution_id):
        """
        Get institution by id
        """
        url = urljoin(self.url, self.endpoints['institutions'] + '/' + institution_id)
        return http_request(url, 'GET')
