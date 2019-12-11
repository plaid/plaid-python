from plaid.api.api import API


class Processor(API):
    '''Endpoints for creating processor tokens.'''

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

    def dwollaProcessorTokenCreate(self, access_token, account_id):
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

    def modernTreasuryProcessorTokenCreate(self, access_token, account_id):
        '''
        Create a Modern Treasury processor token for a given account ID
        (`HTTP docs <https://plaid.com/docs/modern-treasury/>`__)

        :param  str     access_token:
        :param  str     account_id:
        '''
        return self.client.post('/processor/modern_treasury/processor_token/create',
                                {
                                    'access_token': access_token,
                                    'account_id': account_id,
                                })
