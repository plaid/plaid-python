from plaid.api.api import API


class Identity(API):
    '''
    Identity endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#identity>`__)
    '''

    def get(self,
            access_token,
            session=None):
        '''
        Retrieve information about an item.

        :param  str     access_token:
        :param  object  session:        A requests.Session instance to use for
                                        making HTTP requests. Optional.
        '''
        return self.client.post('/identity/get', {
            'access_token': access_token,
        }, session=session)
