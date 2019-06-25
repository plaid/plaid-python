from plaid.api.api import API


class Auth(API):
    '''Auth endpoints.'''

    def get(self,
            access_token,
            _options=None,
            account_ids=None,
            **petal_kwargs):
        '''
        Retrieve account and routing numbers for checking and savings accounts.
        (`HTTP docs <https://plaid.com/docs/api/#auth>`__)

        :param  str     access_token:
        :param  [str]   account_ids:    A list of account_ids to retrieve for
                                        the item. Optional.
        :param dict petal_kwargs: Dict of 'proxies', 'verify', and
        'petal_headers' (used in /get/auth to attach VGS proxy, verify cert,
        and log header to the request).
        '''
        options = _options or {}
        if account_ids is not None:
            options['account_ids'] = account_ids

        return self.client.post('/auth/get', {
            'access_token': access_token,
            'options': options,
        }, **petal_kwargs)
