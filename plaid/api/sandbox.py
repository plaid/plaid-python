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


class PublicToken(API):
    '''Sandbox public token endpoints.'''

    def create(self,
               institution_id,
               initial_products,
               _options=None,
               webhook=None,
               transactions__start_date=None,
               transactions__end_date=None,
               ):
        '''
        Generate a public token for sandbox testing.

        :param  str     institution_id:

        :param  [str]   initial_products:

        :param  str     webhook:
        '''
        options = _options or {}
        transaction_options = {}
        transaction_options.update(options.get('transactions', {}))

        if webhook is not None:
            options['webhook'] = webhook
        if transactions__start_date is not None:
            transaction_options['start_date'] = transactions__start_date
        if transactions__end_date is not None:
            transaction_options['end_date'] = transactions__end_date
        if transaction_options:
            options['transactions'] = transaction_options

        return self.client.post_public_key('/sandbox/public_token/create', {
            'institution_id': institution_id,
            'initial_products': initial_products,
            'options': options,
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
        self.public_token = PublicToken(client)
