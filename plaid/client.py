import warnings

from plaid.api import (
    Accounts,
    AssetReport,
    Auth,
    Categories,
    CreditDetails,
    Identity,
    Income,
    Institutions,
    Item,
    Processor,
    Sandbox,
    Transactions,
)
from plaid.requester import DEFAULT_TIMEOUT, post_request
from plaid.utils import urljoin


class Client(object):
    '''
    Python Plaid API client.

    See official documentation at: https://plaid.com/docs.

    All of the endpoints documented under the ``plaid.api``
    module may be called from a ``plaid.Client`` instance.
    '''

    def __init__(self,
                 client_id,
                 secret,
                 public_key,
                 environment,
                 suppress_warnings=False,
                 timeout=DEFAULT_TIMEOUT,
                 api_version=None):
        '''
        Initialize a client with credentials.

        :param  str     client_id:          Your Plaid client ID
        :arg    str     secret:             Your Plaid secret
        :arg    str     public_key:         Your Plaid public key
        :arg    str     environment:        One of ``sandbox``,
                                            ``development``, or ``production``.
        :arg    bool    suppress_warnings:  Suppress Plaid warnings.
        :arg    int     timeout:            Timeout for API requests.

        '''
        self.client_id = client_id
        self.secret = secret
        self.public_key = public_key
        self.environment = environment
        self.suppress_warnings = suppress_warnings
        self.timeout = timeout
        self.api_version = api_version

        if self.environment == 'development' and not self.suppress_warnings:
            warnings.warn('''
                Development is not intended for production usage.
                Swap out url for https://production.plaid.com
                via Client.config before switching to production
            ''')

        # Mirror the HTTP API hierarchy
        self.Accounts = Accounts(self)
        self.AssetReport = AssetReport(self)
        self.Auth = Auth(self)
        self.Categories = Categories(self)
        self.CreditDetails = CreditDetails(self)
        self.Identity = Identity(self)
        self.Income = Income(self)
        self.Institutions = Institutions(self)
        self.Item = Item(self)
        self.Processor = Processor(self)
        self.Sandbox = Sandbox(self)
        self.Transactions = Transactions(self)

    def post(self, path, data, is_json=True):
        '''Make a post request with client_id and secret key.'''
        post_data = {
            'client_id': self.client_id,
            'secret': self.secret,
        }
        post_data.update(data)
        return self._post(path, post_data, is_json)

    def post_public(self, path, data, is_json=True):
        '''Make a post request requiring no auth.'''
        return self._post(path, data, is_json)

    def post_public_key(self, path, data, is_json=True):
        '''Make a post request using a public key.'''
        post_data = {
            'public_key': self.public_key
        }
        post_data.update(data)
        return self._post(path, post_data, is_json)

    def _post(self, path, data, is_json):
        headers = {}
        if self.api_version is not None:
            headers = {'Plaid-Version': self.api_version}
        return post_request(
            urljoin('https://' + self.environment + '.plaid.com', path),
            data=data,
            timeout=self.timeout,
            is_json=is_json,
            headers=headers,
        )
