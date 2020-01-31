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

        endpoint = ('/processor/stripe/bank_account_token/create'
                    if processor == 'stripe'
                    else '/processor/{}/processor_token/create'.format(
                        processor))

        return self.client.post(endpoint,
                                {
                                    'access_token': access_token,
                                    'account_id': account_id,
                                })

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
