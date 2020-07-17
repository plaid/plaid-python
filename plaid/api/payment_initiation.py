from plaid.api.api import API


class PaymentInitiation(API):
    '''Payment Initiation endpoints.'''

    def create_recipient(self, name, iban, address, bacs):
        '''
        Creates a payment recipient.

        :param  str     name:
        :param  str     iban:
        :param  dict    address: A dictionary containing street, city,
                                 postal_code, and country fields.
        :param  dict    bacs: A dictionary containing account and sort_code
        '''

        return self.client.post('/payment_initiation/recipient/create', {
            'name': name,
            'iban': iban,
            'address': address,
            'bacs': bacs,
        })

    def get_recipient(self, recipient_id):
        '''
        Retrieves a payment recipient.

        :param  str     recipient_id:
        '''

        return self.client.post('/payment_initiation/recipient/get', {
            'recipient_id': recipient_id,
        })

    def list_recipients(self):
        '''
        Lists all the payment recipients.
        '''

        return self.client.post('/payment_initiation/recipient/list', {})

    def create_payment(self, recipient_id, reference, amount):
        '''
        Creates a payment.

        :param  str     recipient_id:
        :param  str     reference:
        :param  dict    amount:       A dictionary containing currency and
                                      value fields.
        '''

        return self.client.post('/payment_initiation/payment/create', {
            'recipient_id': recipient_id,
            'reference': reference,
            'amount': amount,
        })

    def create_payment_token(self, payment_id):
        '''
        Creates a payment.

        :param  str     payment_id:
        '''

        return self.client.post('/payment_initiation/payment/token/create', {
            'payment_id': payment_id,
        })

    def get_payment(self, payment_id):
        '''
        Retrieves a payment.

        :param  str     payment_id:
        '''

        return self.client.post('/payment_initiation/payment/get', {
            'payment_id': payment_id,
        })

    def list_payments(self, options):
        '''
        Lists all the payments.

        :param dict    options:       A dictionary containing count, and
                                      cursor fields.
        '''

        return self.client.post('/payment_initiation/payment/list', options)
