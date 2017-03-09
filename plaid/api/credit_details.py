from plaid.api.api import API


class CreditDetails(API):
    '''
    Credit details endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#credit-details>`__)
    '''

    def get(self,
            access_token):
        '''
        Retrieve credit details associated with an item.

        :param  str     access_token:
        '''
        return self.client.post('/credit_details/get', {
            'access_token': access_token,
        })
