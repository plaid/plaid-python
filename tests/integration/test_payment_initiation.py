import time
from plaid.model.country_code import CountryCode
from plaid.model.payment_initiation_payment_list_request import PaymentInitiationPaymentListRequest
from plaid.model.payment_initiation_payment_create_request import PaymentInitiationPaymentCreateRequest
from plaid.model.link_token_create_request_payment_initiation import LinkTokenCreateRequestPaymentInitiation
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.payment_initiation_payment_get_request import PaymentInitiationPaymentGetRequest
from plaid.model.payment_initiation_payment_list_request import PaymentInitiationPaymentListRequest
from plaid.model.payment_initiation_recipient_list_request import PaymentInitiationRecipientListRequest
from plaid.model.payment_initiation_address import PaymentInitiationAddress
from plaid.model.payment_initiation_recipient_create_request import PaymentInitiationRecipientCreateRequest
from plaid.model.payment_initiation_recipient_get_request import PaymentInitiationRecipientGetRequest
from plaid.model.products import Products
from plaid.model.nullable_recipient_bacs import NullableRecipientBACS
from plaid.model.amount import Amount

from tests.integration.util import create_client


def payments_after_recipient_creation(client, recipient_id):
    # list recipients
    request = PaymentInitiationRecipientListRequest()

    response = client.payment_initiation_recipient_list(request)
    assert response['recipients'] is not None
    assert len(response['recipients']) > 0

    # create payment
    request = PaymentInitiationPaymentCreateRequest(
        recipient_id=recipient_id,
        reference='TestPayment',
        amount=Amount(
            currency='GBP',
            value=100.00
        )
    )
    response = client.payment_initiation_payment_create(request)
    payment_id = response['payment_id']
    assert payment_id is not None
    assert response['status'] is not None

    # create link token
    request = LinkTokenCreateRequest(
        products=[Products('payment_initiation')],
        client_name='Plaid Test',
        country_codes=[CountryCode('GB')],
        language='en',
        user=LinkTokenCreateRequestUser(
            client_user_id=str(time.time())
        ),
        payment_initiation=LinkTokenCreateRequestPaymentInitiation(
            payment_id=payment_id
        )
    )
    response = client.link_token_create(request)
    assert response['link_token'] is not None
    assert response['expiration'] is not None

    # get payment
    request = PaymentInitiationPaymentGetRequest(
        payment_id=payment_id
    )
    response = client.payment_initiation_payment_get(request)
    assert response['payment_id'] is not None
    assert response['reference'] is not None
    assert response['amount'] is not None
    assert response['status'] is not None
    assert response['last_status_update'] is not None
    assert response['recipient_id'] is not None

    # list payments
    request = PaymentInitiationPaymentListRequest(
        count=10
    )
    response = client.payment_initiation_payment_list(request)
    assert response['payments'] is not None and len(response['payments']) > 0


def test_all_payment_routes_with_bacs():
    client = create_client()

    # create recipient
    request = PaymentInitiationRecipientCreateRequest(
        name='John Doe',
        bacs=NullableRecipientBACS(account='26207729', sort_code='560029'),
        address=PaymentInitiationAddress(
            street=['street name 999'],
            city='city',
            postal_code='99999',
            country='GB'
        )
    )
    response = client.payment_initiation_recipient_create(request)
    recipient_id = response['recipient_id']
    assert recipient_id is not None

    # get recipient
    request = PaymentInitiationRecipientGetRequest(
        recipient_id=recipient_id
    )
    response = client.payment_initiation_recipient_get(request)
    assert response['recipient_id'] is not None
    assert response['name'] is not None
    assert response['bacs'] is not None
    assert response['address'] is not None
    payments_after_recipient_creation(client, recipient_id)


def test_all_payment_routes_with_iban():
    client = create_client()

    # create recipient
    request = PaymentInitiationRecipientCreateRequest(
        name='John Doe',
        iban='GB33BUKB20201555555555',
        address=PaymentInitiationAddress(
            street=['street name 999'],
            city='city',
            postal_code='99999',
            country='GB'
        )
    )
    response = client.payment_initiation_recipient_create(request)
    recipient_id = response['recipient_id']
    assert recipient_id is not None

    # get recipient
    request = PaymentInitiationRecipientGetRequest(
        recipient_id=recipient_id
    )
    response = client.payment_initiation_recipient_get(request)
    assert response['recipient_id'] is not None
    assert response['name'] is not None
    assert response['iban'] is not None
    assert response['address'] is not None

    payments_after_recipient_creation(client, recipient_id)