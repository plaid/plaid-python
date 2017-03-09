from plaid.api.api import API


class Income(API):
    '''
    Income endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#income>`__)
    '''
    def get(self, access_token):
        '''
        Retrieve income data associated with an item.
        Adds the income product to the item if it does not already have it.

        :param str access_token:
        '''
        return self.client.post('/income/get', {
            'access_token': access_token,
        })
