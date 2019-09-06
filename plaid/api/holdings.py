from plaid.api.api import API


class Holdings(API):
    '''
    Holdings endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#holdings>`__)
    '''

    def get(self,
            access_token,
            session=None):
        '''
        Retrieve investment holdings information about an item.

        :param  str     access_token:
        :param  object  session:        A requests.Session instance to use for
                                        making HTTP requests. Optional.
        '''
        return self.client.post('/investments/holdings/get', {
            'access_token': access_token,
        }, session=session)
