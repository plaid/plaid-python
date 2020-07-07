from plaid.api.api import API


class LinkToken(API):
    '''Endpoints for managing link tokens.'''
    def create(self, configs):
        '''
        Create a Link token.

        :param dict configs: A required dictionary to configure the Link token.
        '''
        return self.client.post('/link/token/create', {
            'user': configs['user'],
            'client_name': configs['client_name'],
            'products': configs['products'],
            'country_codes': configs['country_codes'],
            'language': configs['language'],
            'locale': configs['language'],
            'redirect_uri': configs['redirect_uri'],
            'android_package_name': configs['android_package_name'],
            'webhook': configs['webhook'],
            'institution_id': configs['institution_id'],
            'link_customization_name': configs['link_customization_name'],
            'access_token': configs['access_token'],
            'account_filters': configs['account_filters'],
            'cross_app_item_add': configs['cross_app_item_add'],
            'payment_initiation': configs['payment_initiation'],
        })
