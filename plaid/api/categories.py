from plaid.api.api import API


class Categories(API):
    '''
    Categories endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#categories>`__)
    '''

    def get(self, session=None):
        '''
        Fetch all plaid categories.

        :param  object  session:        A requests.Session instance to use for
                                        making HTTP requests. Optional.
        '''
        return self.client.post_public('/categories/get', {}, session=session)
