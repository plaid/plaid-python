from plaid.api.api import API


class Categories(API):
    '''
    Categories endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#categories>`__)
    '''

    def get(self):
        '''Fetch all plaid categories.'''
        return self.client.post_public('/categories/get', {})
