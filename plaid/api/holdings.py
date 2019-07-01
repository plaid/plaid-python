from plaid.api.api import API


class Holdings(API):
    '''
    Holdings endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#holdings>`__)
    '''

    def get(self,
            access_token):
        '''
        Retrieve investment holdings information about an item.

        :param  str     access_token:
        '''
        return self.client.post('/investments/holdings/get', {
            'access_token': access_token,
        })
