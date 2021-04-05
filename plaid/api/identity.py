from plaid.api.api import API


class Identity(API):
    '''
    Identity endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#identity>`__)
    '''

    def get(self,
            access_token,
            _options=None,
            account_ids=None):
        '''
        Retrieve information about an item.

        :param  str     access_token:
        :param  [str]   account_ids:    A list of account_ids to retrieve for
                                the item. Optional.
        '''

        options = _options or {}
        if account_ids is not None:
            options['account_ids'] = account_ids
        return self.client.post('/identity/get', {
            'access_token': access_token,
            'options': options,
        })
