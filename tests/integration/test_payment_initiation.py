import time

from tests.integration.util import create_client


def payments_after_recipient_creation(client, recipient_id):
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

    # create legacy payment token
    response = client.PaymentInitiation.create_payment_token(
        payment_id,
    )
    assert response['payment_token'] is not None
    assert response['payment_token_expiration_time'] is not None

    # create link token
    response = client.LinkToken.create({
        'user': {
            'client_user_id': str(time.time()),
        },
        'products': ["payment_initiation"],
        'client_name': "Plaid Test",
        'country_codes': ['GB'],
        'language': 'en',
        'payment_initiation': {
            'payment_id': payment_id,
        }
    })
    assert response['link_token'] is not None
    assert response['expiration'] is not None

    # get payment
    response = client.PaymentInitiation.get_payment(payment_id)
    assert response['payment_id'] is not None
    assert response['reference'] is not None
    assert response['amount'] is not None
    assert response['status'] is not None
    assert response['last_status_update'] is not None
    assert response['recipient_id'] is not None

    # list payments
    response = client.PaymentInitiation.list_payments({'count': 10})
    assert response['payments'] is not None and len(response['payments']) > 0


def test_all_payment_routes_with_bacs():
    client = create_client()
    bacs = {
        'account': '26207729',
        'sort_code': '560029',
    }

    # create recipient
    response = client.PaymentInitiation.create_recipient(
        'John Doe',
        None,
        {
            'street': ['street name 999'],
            'city': 'city',
            'postal_code': '99999',
            'country': 'GB',
        },
        bacs,
    )
    recipient_id = response['recipient_id']
    assert recipient_id is not None

    # get recipient
    response = client.PaymentInitiation.get_recipient(recipient_id)
    assert response['recipient_id'] is not None
    assert response['name'] is not None
    assert response['bacs'] is not None
    assert response['address'] is not None
    payments_after_recipient_creation(client, recipient_id)


def test_all_payment_routes_with_iban():
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
        None
    )
    recipient_id = response['recipient_id']
    assert recipient_id is not None

    # get recipient
    response = client.PaymentInitiation.get_recipient(recipient_id)
    assert response['recipient_id'] is not None
    assert response['name'] is not None
    assert response['iban'] is not None
    assert response['address'] is not None

    payments_after_recipient_creation(client, recipient_id)
