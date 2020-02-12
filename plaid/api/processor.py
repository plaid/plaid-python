from plaid.api.api import API


class Processor(API):
    '''Endpoints for creating processor tokens.'''

    def tokenCreate(self, access_token, account_id, processor):
        '''
        Create a processor token for a given processor and account ID

        :param  str     access_token:
        :param  str     account_id:
        :param  str     processor:
        '''
        endpoint = 'processor/token/create'
        options = {
            'access_token': access_token,
            'account_id': account_id,
            'processor': processor
        }

        if processor == 'stripe':
            endpoint = '/processor/stripe/bank_account_token/create'
            del options['processor']
        elif processor == 'apex':
            endpoint = '/processor/apex/processor_token/create'
            del options['processor']

        return self.client.post(endpoint, options)

    def stripeBankAccountTokenCreate(self, access_token, account_id):
        '''
        Create a Stripe bank_account token for a given account ID
        (`HTTP docs <https://plaid.com/docs/link/stripe>`__)

        :param  str     access_token:
        :param  str     account_id:
        '''
        return self.client.post('/processor/stripe/bank_account_token/create',
                                {
                                    'access_token': access_token,
                                    'account_id': account_id,
                                })

    def dwollaBankAccountTokenCreate(self, access_token, account_id):
        '''
        Create a Dwolla processor token for a given account ID
        (`HTTP docs <https://plaid.com/docs/link/dwolla>`__)

        :param  str     access_token:
        :param  str     account_id:
        '''
        return self.client.post('/processor/dwolla/processor_token/create',
                                {
                                    'access_token': access_token,
                                    'account_id': account_id,
                                })
