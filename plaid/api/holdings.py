from plaid.api.api import API


class Holdings(API):
    '''
    Holdings endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#holdings>`__)
    '''

    def get(self,
            access_token,
            _options=None,
            account_ids=None):
        '''
        Retrieve investment holdings information about an item.

        :param  str     access_token:
        :param  [str]   account_ids:    A list of account_ids to retrieve for
                                the item. Optional.
        '''

        options = _options or {}
        if account_ids is not None:
            options['account_ids'] = account_ids

        return self.client.post('/investments/holdings/get', {
            'access_token': access_token,
            'options': options,
        })
