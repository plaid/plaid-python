from plaid.api.api import API


class LinkToken(API):
    '''Endpoints for managing link tokens.'''
    def create(self, configs):
        '''
        Create a Link token.

        :param dict configs: A required dictionary to configure the Link token.
        '''
        return self.client.post('/link/token/create', configs)
        # return self.client.post('/link/token/create', {
        #     'user': configs.get('user'),
        #     'client_name': configs.get('client_name'),
        #     'products': configs.get('products'),
        #     'country_codes': configs.get('country_codes'),
        #     'language': configs.get('language'),
        #     'locale': configs.get('locale'),
        #     'redirect_uri': configs.get('redirect_uri'),
        #     'android_package_name': configs.get('android_package_name'),
        #     'webhook': configs.get('webhook'),
        #     'institution_id': configs.get('institution_id'),
        #     'link_customization_name': configs.get('link_customization_name'),
        #     'access_token': configs.get('access_token'),
        #     'account_filters': configs.get('account_filters'),
        #     'cross_app_item_add': configs.get('cross_app_item_add'),
        #     'payment_initiation': configs.get('payment_initiation'),
        # })
