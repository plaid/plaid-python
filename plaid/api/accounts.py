from plaid.api.api import API


class Balance(API):
    '''Accounts balance endpoint.'''

    def get(self,
            access_token,
            _options={},
            account_ids=None):
        '''
        Retrieve real-time balance information for accounts.

        :param  str     access_token:
        :param  [str]   account_ids:    A list of account_ids to retrieve for
                                        the item. Optional.
        '''
        options = {}
        options.update(_options)
        if account_ids is not None:
            options['account_ids'] = account_ids

        return self.client.post('/accounts/balance/get', {
            'access_token': access_token,
            'options': options,
        })


class Accounts(API):
    '''
    Accounts endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#accounts>`__)

    .. autoclass:: plaid.api.accounts.Balance
        :members:
    '''

    def __init__(self, client):
        super(Accounts, self).__init__(client)
        self.balance = Balance(client)

    def get(self,
            access_token,
            _options={},
            account_ids=None):
        '''
        Retrieve high-level account information for an Item.

        :param  str     access_token:
        :param  [str]   account_ids:    A list of account_ids to retrieve for
                                        the item. Optional.
        '''
        options = {}
        options.update(_options)
        if account_ids is not None:
            options['account_ids'] = account_ids

        return self.client.post('/accounts/get', {
            'access_token': access_token,
            'options': options,
        })
