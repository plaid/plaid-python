from plaid.api.api import API


class Processor(API):
    '''Endpoints for creating processor tokens.'''

    def stripeBankAccountTokenCreate(self, access_token, account_id):
        '''
        Create a Stripe bank_account token for a given account ID
        (`HTTP docs <https://plaid.com/docs/link/stripe>`__)

        :param  str     public_token:
        :param  str     account_id:
        '''
        return self.client.post('/processor/stripe/bank_account_token/create',
                                {
                                    'access_token': access_token,
                                    'account_id': account_id,
                                })
