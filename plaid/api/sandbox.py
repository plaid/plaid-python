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

    def fire_webhook(self, access_token, webhook_code):
        '''
        Fire a webhook for an item

        :param  str     access_token:
        :param  str     webhook_code:
        '''
        return self.client.post('/sandbox/item/fire_webhook', {
            'access_token': access_token,
            'webhook_code': webhook_code,
        })

    def set_verification_status(self, access_token, account_id,
                                verification_status):
        '''
        Set verification status for an item created via the
        automated microdeposits flow

        :param  str     access_token:
        :param  str     account_id:
        :param  str     verification_status:
        '''
        return self.client.post('/sandbox/item/set_verification_status', {
            'access_token': access_token,
            'account_id': account_id,
            'verification_status': verification_status,
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
               override_username=None,
               override_password=None
               ):
        '''
        Generate a public token for sandbox testing.

        :param  str     institution_id:

        :param  [str]   initial_products:

        :param  str     webhook:
        '''
        options = _options or {}

        if webhook is not None:
            options['webhook'] = webhook
        if override_username is not None:
            options['override_username'] = override_username
        if override_password is not None:
            options['override_password'] = override_password

        transaction_options = {}
        transaction_options.update(options.get('transactions', {}))
        if transactions__start_date is not None:
            transaction_options['start_date'] = transactions__start_date
        if transactions__end_date is not None:
            transaction_options['end_date'] = transactions__end_date
        if transaction_options:
            options['transactions'] = transaction_options

        return self.client.post('/sandbox/public_token/create', {
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
