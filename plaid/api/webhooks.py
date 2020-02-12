from plaid.api.api import API


class Webhooks(API):
    '''
    Webhooks endpoints.
    (`HTTP docs <https://plaid.com/docs/#webhook-verification>`__)
    '''

    def get_verification_key(self,
                             key_id):
        '''
        Retrieve webhook verification key.

        :param  str     key_id: ID of key from Plaid-Verification header
        '''
        return self.client.post('/webhook_verification_key/get', {
            'key_id': key_id,
        })
