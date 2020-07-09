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
