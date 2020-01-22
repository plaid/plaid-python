from tests.integration.util import create_client


def test_all_payment_routes():
    client = create_client()

    # create recipient
    response = client.PaymentInitiation.create_recipient(
        'John Doe',
        'GB33BUKB20201555555555',
        {
            'street': ['street name 999'],
            'city': 'city',
            'postal_code': '99999',
            'country': 'GB',
        },
    )
    recipient_id = response['recipient_id']
    assert recipient_id is not None

    # get recipient
    response = client.PaymentInitiation.get_recipient(recipient_id)
    assert response['recipient_id'] is not None
    assert response['name'] is not None
    assert response['iban'] is not None
    assert response['address'] is not None

    # list recipients
    response = client.PaymentInitiation.list_recipients()
    assert response['recipients'] is not None
    assert len(response['recipients']) > 0

    # create payment
    response = client.PaymentInitiation.create_payment(
        recipient_id,
        'TestPayment',
        {
            'currency': 'GBP',
            'value': 100.00,
        },
    )
    payment_id = response['payment_id']
    assert payment_id is not None
    assert response['status'] is not None

    # create payment token
    response = client.PaymentInitiation.create_payment_token(
        payment_id,
    )
    assert response['payment_token'] is not None
    assert response['payment_token_expiration_time'] is not None

    # get payment
    response = client.PaymentInitiation.get_payment(payment_id)
    assert response['payment_id'] is not None
    assert response['payment_token'] is not None
    assert response['reference'] is not None
    assert response['amount'] is not None
    assert response['status'] is not None
    assert response['last_status_update'] is not None
    assert response['payment_token_expiration_time'] is not None
    assert response['recipient_id'] is not None

    # list payments
    response = client.PaymentInitiation.list_payments({'count': 10})
    assert response['payments'] is not None and len(response['payments']) > 0
