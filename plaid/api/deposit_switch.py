from plaid.api.api import API


class DepositSwitch(API):
    '''
    Deposit Switch endpoints.
    (`HTTP docs <coming soon>`__)
    '''

    def get(self, deposit_switch_id):
        '''
        Gets deposit switch information given a deposit switch id.

        :param  str deposit_switch_id:  ID of deposit switch to get.
        '''

        return self.client.post('/deposit_switch/get', {
            'deposit_switch_id': deposit_switch_id,
        })

    def create(self, target_account_id, target_access_token):
        '''
        Creates a deposit switch given target account id and target access
        token.
        (`HTTP docs <coming soon>`__)

        :param  str target_account_id:      The id of the bank account that
                                            the deposit switch will go to.
        :param  str target_access_token:    The access token to create the
                                            the deposit switch.
        '''
        return self.client.post('/deposit_switch/create', {
            'target_account_id': target_account_id,
            'target_access_token': target_access_token,
        })

    def create_token(self, deposit_switch_id):
        '''
        Creates a deposit switch token, which is used to initialize a deposit
        switch.
        (`HTTP docs <coming soon>`__)

        :param  str deposit_switch_id:  ID of deposit switch
        '''
        return self.client.post('/deposit_switch/token/create', {
            'deposit_switch_id': deposit_switch_id,
        })
