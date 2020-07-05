import warnings

from plaid.api import (
    Accounts,
    AssetReport,
    Auth,
    Categories,
    CreditDetails,
    DepositSwitch,
    Holdings,
    Identity,
    Income,
    Institutions,
    InvestmentTransactions,
    Item,
    Liabilities,
    LinkToken,
    PaymentInitiation,
    Processor,
    Sandbox,
    Transactions,
    Webhooks,
)

from plaid.internal.requester import DEFAULT_TIMEOUT, post_request
from plaid.internal.utils import urljoin


class Client(object):
    '''
    Python Plaid API client.

    See official documentation at: https://plaid.com/docs.

    All of the endpoints documented under the ``plaid.api``
    module may be called from a ``plaid.Client`` instance.
    '''

    def __init__(self,
                 client_id=None,
                 secret=None,
                 environment=None,
                 suppress_warnings=False,
                 timeout=DEFAULT_TIMEOUT,
                 api_version=None,
                 client_app=None):
        '''
        Initialize a client with credentials.

        :param  str     client_id:          Your Plaid client ID
        :arg    str     secret:             Your Plaid secret
        :arg    str     environment:        One of ``sandbox``,
                                            ``development``, or ``production``.
        :arg    bool    suppress_warnings:  Suppress Plaid warnings.
        :arg    int     timeout:            Timeout for API requests.
        :arg    str     api_version:        API version to use for requests
        :arg    str     client_app:         Internal header to include
                                                in requests
        '''
        self.client_id = client_id
        self.secret = secret
        self.environment = environment
        self.suppress_warnings = suppress_warnings
        self.timeout = timeout
        self.api_version = api_version
        self.client_app = client_app

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
        self.DepositSwitch = DepositSwitch(self)
        self.Holdings = Holdings(self)
        self.Identity = Identity(self)
        self.Income = Income(self)
        self.Institutions = Institutions(self)
        self.InvestmentTransactions = InvestmentTransactions(self)
        self.Item = Item(self)
        self.Liabilities = Liabilities(self)
        self.LinkToken = LinkToken(self)
        self.PaymentInitiation = PaymentInitiation(self)
        self.Processor = Processor(self)
        self.Sandbox = Sandbox(self)
        self.Transactions = Transactions(self)
        self.Webhooks = Webhooks(self)

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

    def _post(self, path, data, is_json):
        headers = {}
        if self.api_version is not None:
            headers['Plaid-Version'] = self.api_version
        if self.client_app is not None:
            headers['Plaid-Client-App'] = self.client_app
        return post_request(
            urljoin('https://' + self.environment + '.plaid.com', path),
            data=data,
            timeout=self.timeout,
            is_json=is_json,
            headers=headers,
        )
