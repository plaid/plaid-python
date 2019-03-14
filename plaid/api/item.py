from plaid.api.api import API


class PublicToken(API):
    '''Endpoints for translating between public tokens and access tokens.'''

    def exchange(self, public_token):
        '''
        Exchange a Link public_token for an API access_token.
        (`HTTP docs <https://plaid.com/docs/api/#exchange-token-flow>`__)

        :param  str     public_token:
        '''
        return self.client.post('/item/public_token/exchange', {
            'public_token': public_token,
        })

    def create(self, access_token):
        '''
        Create a Link public_token for an API access_token.
        (`HTTP docs <https://plaid.com/docs/api/#create-public-token>`__)

        :param  str     access_token:
        '''
        return self.client.post('/item/public_token/create', {
            'access_token': access_token,
        })


class AccessToken(API):
    '''Access token endpoints.'''

    def invalidate(self, access_token):
        '''
        Rotate the access token for an item.
        (`HTTP docs <https://plaid.com/docs/api/#rotate-access-token>`__)

        :param  str     access_token:
        '''
        return self.client.post('/item/access_token/invalidate', {
            'access_token': access_token,
        })

    def update_version(self, access_token):
        '''
        Transition an access token to work with the current version of
        the Plaid API
        (`HTTP docs <https://plaid.com/docs/api/#update-access-token-
        version>`__)

        :param  str      access_token:
        '''
        return self.client.post('/item/access_token/update_version', {
            'access_token_v1': access_token,
        })


class Webhook(API):
    '''Webhook endpoints.'''

    def update(self, access_token, webhook):
        '''
        Update the webhook for an Item.
        (`HTTP docs <https://plaid.com/docs/api/#update-webhook>`__)

        :param  str     access_token:
        :param  str     webhook: The URL of the webhook to associate.
        '''
        return self.client.post('./item/webhook/update', {
            'access_token': access_token,
            'webhook': webhook,
        })


class Item(API):
    '''
    Item endpoints.
    (`HTTP docs <https://plaid.com/docs/api/#item-management>`__)

    .. autoclass:: plaid.api.item.AccessToken
        :members:
    .. autoclass:: plaid.api.item.PublicToken
        :members:
    .. autoclass:: plaid.api.item.Webhook
        :members:
    '''

    def __init__(self, client):
        super(Item, self).__init__(client)
        self.access_token = AccessToken(client)
        self.public_token = PublicToken(client)
        self.webhook = Webhook(client)

    def get(self, access_token):
        '''
        Get information about the status of an item.
        (`HTTP docs <https://plaid.com/docs/api/#get-item>`__)

        :param  str     access_token:
        '''
        return self.client.post('/item/get', {
            'access_token': access_token,
        })

    def remove(self, access_token):
        '''
        Remove an item.
        (`HTTP docs <https://plaid.com/docs/api/#remove-an-item>`__)

        This also deactivates the access_token.

        :param  str     access_token:
        '''
        return self.client.post('/item/remove', {
            'access_token': access_token,
        })
