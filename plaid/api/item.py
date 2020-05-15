from plaid.api.api import API


class AddToken(API):
    '''Endpoints for managing item add tokens.'''
    def create(self, user):
        '''
        Create a Link item add token.

        :param  dict user:  An optional dictionary with additional user data.
        '''
        return self.client.post('/item/add_token/create', {
            'user': user,
        })


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

    .. autoclass:: plaid.api.item.AddToken
        :members:
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
        self.add_token = AddToken(client)
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

    def import_item(self, products, user_auth, _options):
        '''
        Imports an item.
        (`HTTP docs coming soon`__)

        :param  [str]   initial_products:   List of products that the item
                                            will be enabled for.
        :param  dict    user_auth:          User authentication fields for the
                                            item.
        :param  dict    options:            Additional options.
        '''
        options = _options or {}

        return self.client.post('/item/import', {
            'products': products,
            'user_auth': user_auth,
            'options': options,
        })
