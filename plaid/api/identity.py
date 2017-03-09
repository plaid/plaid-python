from plaid.api.api import API


class Identity(API):
    '''
    Identity endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#identity>`__)
    '''

    def get(self,
            access_token):
        '''
        Retrieve information about an item.

        :param  str     access_token:
        '''
        return self.client.post('/identity/get', {
            'access_token': access_token,
        })
