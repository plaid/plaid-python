from plaid.api.api import API


class Credentials(API):
    '''Item Credentials endpoints.'''

    def update(self, access_token, credentials, _options={}):
        '''
        Update the credentials associated with an item.

        Returns either a successful response or a response indicating that MFA
        (Multi Factor Authentication) is required.

        :param  dict     credentials:   See ``Item.create`` for details.
        '''
        return self.client.post('/item/credentials/update', {
            'access_token': access_token,
            'credentials': credentials,
            'options': _options,
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
    .. autoclass:: plaid.api.item.Credentials
        :members:
    .. autoclass:: plaid.api.item.Webhook
        :members:
    '''

    def __init__(self, client):
        super(Item, self).__init__(client)
        self.access_token = AccessToken(client)
        self.credentials = Credentials(client)
        self.public_token = PublicToken(client)
        self.webhook = Webhook(client)

    def create(self,
               credentials,
               institution_id,
               initial_products,
               _options={},
               transactions__start_date=None,
               transactions__end_date=None,
               transactions__await_results=None,
               webhook=None):
        '''
        Add a bank account user/login to Plaid.

        Returns either a successful response or a response indicating that MFA
        (Multi Factor Authentication) is required.

        :param  dict    credentials:                    A dictionary containing
                                                        the fields
                                                        ``username``,
                                                        ``password``, and
                                                        (optionally) ``pin``.
        :param  str     institution_id:
        :param  list    initial_products:               A list containing
                                                        product names.
        :param  str     transactions__start_date:       The date to begin the
                                                        item's initial
                                                        transaction pull.
        :param  str     transactions__end_date:         The date to end the
                                                        item's initial
                                                        transaction pull.
        :param  str     transactions__await_results:    If ``True``, wait for
                                                        the initial
                                                        transaction pull to
                                                        complete before
                                                        returning. Will
                                                        increase the user wait
                                                        time.
        :param  str     webhook:                        The URL for a webhook
                                                        associated with the
                                                        item.

        All dates should be formatted as ``YYYY-MM-DD``.
        '''
        transaction_options = {}
        transaction_options.update(_options.get('transactions', {}))
        if transactions__start_date is not None:
            transaction_options['start_date'] = transactions__start_date
        if transactions__end_date is not None:
            transaction_options['end_date'] = transactions__end_date
        if transactions__await_results is not None:
            transaction_options['await_results'] = transactions__await_results

        options = {}
        options.update(_options)
        if transaction_options:
            options['transactions'] = transaction_options
        if webhook is not None:
            options['webhook'] = webhook

        return self.client.post('/item/create', {
            'credentials': credentials,
            'institution_id': institution_id,
            'initial_products': initial_products,
            'options': options,
        })

    def mfa(self, access_token, mfa_type, responses, _options={}):
        '''
        Provide an MFA (Multi-Factor Authentication) response for an item.

        :param  str     access_token:
        :param  str     mfa_type:       The type of mfa answered (e.g. device)
        :param  [str]   responses:      The MFA response(s)
        '''
        return self.client.post('/item/mfa', {
            'access_token': access_token,
            'mfa_type': mfa_type,
            'responses': responses,
            'options': _options,
        })

    def get(self, access_token):
        '''
        Get information about the status of an item.
        (`HTTP docs <https://plaid.com/docs/api/#get-item>`__)

        :param  str     access_token:
        '''
        return self.client.post('/item/get', {
            'access_token': access_token,
        })

    def delete(self, access_token):
        '''
        Delete an item.
        (`HTTP docs <https://plaid.com/docs/api/#delete-an-item>`__)

        This also deactivates the access_token.

        :param  str     access_token:
        '''
        return self.client.post('/item/delete', {
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
