from plaid.api.api import API


class Item(API):
    '''Sandbox item endpoints.'''

    def reset_login(self, access_token):
        '''
        Put an item into an ITEM_LOGIN_REQUIRED error state.

        :param  str     access_token:
        '''
        return self.client.post('/sandbox/item/reset_login', {
            'access_token': access_token,
        })


class Sandbox(API):
    '''
    Sandbox-only endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#sandbox>`__)

    These endpoints may not be used in other environments.

    .. autoclass:: plaid.api.sandbox.Item
        :members:
    '''

    def __init__(self, client):
        super(Sandbox, self).__init__(client)
        self.item = Item(client)
