from plaid.api.api import API


class Processor(API):
    '''Endpoints for creating processor tokens.'''

    def tokenCreate(self, access_token, account_id, processor, session=None):
        '''
        Create a processor token for a given processor and account ID

        :param  str     access_token:
        :param  str     account_id:
        :param  str     processor:
        :param  object  session:        A requests.Session instance to use for
                                        making HTTP requests. Optional.
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

        return self.client.post(endpoint, options, session=session)

    def stripeBankAccountTokenCreate(self, access_token, account_id, session=None):
        '''
        Create a Stripe bank_account token for a given account ID
        (`HTTP docs <https://plaid.com/docs/link/stripe>`__)

        :param  str     access_token:
        :param  str     account_id:
        :param  object  session:        A requests.Session instance to use for
                                        making HTTP requests. Optional.
        '''
        return self.client.post('/processor/stripe/bank_account_token/create', {
            'access_token': access_token,
            'account_id': account_id,
        }, session=session)

    def dwollaBankAccountTokenCreate(self, access_token, account_id, session=None):
        '''
        Create a Dwolla processor token for a given account ID
        (`HTTP docs <https://plaid.com/docs/link/dwolla>`__)

        :param  str     access_token:
        :param  str     account_id:
        :param  object  session:        A requests.Session instance to use for
                                        making HTTP requests. Optional.
        '''
        return self.client.post('/processor/dwolla/processor_token/create', {
            'access_token': access_token,
            'account_id': account_id,
        }, session=session)
