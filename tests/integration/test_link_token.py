import time
from plaid.model.country_code import CountryCode
from plaid.model.products import Products
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_get_request import LinkTokenGetRequest
from plaid.model.link_token_account_filters import LinkTokenAccountFilters
from plaid.model.account_subtypes import AccountSubtypes
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.depository_filter import DepositoryFilter
from tests.integration.util import create_client


def test_link_token_create_required():
    client = create_client()

    request = LinkTokenCreateRequest(
        products=['auth', 'transactions'],
        client_name='Plaid Test',
        country_codes=['GB'],
        language='en',
        user=LinkTokenCreateRequestUser(
            client_user_id=str(time.time())
        )
    )
    # create link token
    response = client.link_token_create(request)

    # assert on response
    assert response['link_token'] is not None
    assert response['expiration'] is not None


def test_link_token_create_optional():
    client = create_client()

    # build the configs
    request = LinkTokenCreateRequest(
        products=['auth', 'transactions'],
        client_name='Plaid Test',
        country_codes=['GB'],
        language='en',
        webhook='https://sample-webhook-uri.com',
        link_customization_name='default',
        account_filters=LinkTokenAccountFilters(
            depository=DepositoryFilter(
                account_subtypes=AccountSubtypes(
                    ['checking', 'savings'])
            )
        ),
        user=LinkTokenCreateRequestUser(
            client_user_id=str(time.time())
        )
    )

    # create link token
    response = client.link_token_create(request)

    # assert on response
    assert response['link_token'] is not None
    assert response['expiration'] is not None


def test_link_token_create_and_get():
    client = create_client()

    # build the configs
    request = LinkTokenCreateRequest(
        products=['auth', 'transactions'],
        client_name='Plaid Test',
        country_codes=['GB'],
        language='en',
        webhook='https://sample-webhook-uri.com',
        link_customization_name='default',
        account_filters=LinkTokenAccountFilters(
            depository=DepositoryFilter(
                account_subtypes=AccountSubtypes(
                    ['checking', 'savings'])
            )
        ),
        user=LinkTokenCreateRequestUser(
            client_user_id=str(time.time())
        )
    )
    # create link token
    createResponse = client.link_token_create(request)

    # assert on response
    assert createResponse['link_token'] is not None
    assert createResponse['expiration'] is not None

    getRequest = LinkTokenGetRequest(
        link_token=createResponse['link_token']
    )
    getResponse = client.link_token_get(getRequest)
    assert getResponse['link_token'] == createResponse['link_token']
    assert getResponse['created_at'] is not None
    assert getResponse['expiration'] is not None

    assert getResponse['metadata'] is not None
    assert (getResponse['metadata']['initial_products'] ==
            [Products('auth'), Products('transactions')])
    assert (getResponse['metadata']['webhook'] ==
            'https://sample-webhook-uri.com')
    assert getResponse['metadata']['country_codes'] == [CountryCode('GB')]
    assert getResponse['metadata']['language'] == 'en'
    assert getResponse['metadata']['account_filters']['depository']['account_subtypes'] == \
        AccountSubtypes(['checking', 'savings'])
    assert getResponse['metadata']['client_name'] == 'Plaid Test'