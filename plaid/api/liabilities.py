
from plaid.api.api import API


class Liabilities(API):
    '''
    Liabilities endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#liabilities>`__)
    '''

    def get(self,
            access_token):
        '''
        Retrieve liabilities information about an item.

        :param  str     access_token:
        '''
        return self.client.post('/liabilities/get', {
            'access_token': access_token,
        })
