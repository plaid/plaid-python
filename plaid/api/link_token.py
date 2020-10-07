from plaid.api.api import API

link_token_field_names = [
    'user',
    'client_name',
    'products',
    'country_codes',
    'language',
    'redirect_uri',
    'android_package_name',
    'webhook',
    'link_customization_name',
    'access_token',
    'account_filters',
    'cross_app_item_add',
    'payment_initiation',
]


class LinkToken(API):
    '''Endpoints for managing link tokens.'''

    def create(self, configs):
        '''
        Create a Link token.

        :param dict configs: A required dictionary to configure the Link token.
        '''

        body = {}

        for field in link_token_field_names:
            body[field] = configs.get(field)

        return self.client.post('/link/token/create', body)

    def get(self, link_token):
        '''
        Get information about a Link token.

        :param string link_token: A valid link token created from
        link/token/create.
        '''

        return self.client.post('/link/token/get', {'link_token': link_token})
