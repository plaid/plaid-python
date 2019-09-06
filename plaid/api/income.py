from plaid.api.api import API


class Income(API):
    '''
    Income endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#income>`__)
    '''

    def get(self, access_token, session=None):
        '''
        Retrieve income data associated with an item.
        Adds the income product to the item if it does not already have it.

        :param str access_token:
        :param  object  session:        A requests.Session instance to use for
                                        making HTTP requests. Optional.
        '''
        return self.client.post('/income/get', {
            'access_token': access_token,
        }, session=session)
