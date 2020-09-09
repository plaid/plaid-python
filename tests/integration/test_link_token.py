import time

from tests.integration.util import create_client


def test_link_token_create_required():
    client = create_client()

    # build the configs
    configs = {
        'user': {
            'client_user_id': str(time.time()),
        },
        'products': ["auth", "transactions"],
        'client_name': "Plaid Test",
        'country_codes': ['GB'],
        'language': 'en',
    }

    # create link token
    response = client.LinkToken.create(configs)

    # assert on response
    assert response['link_token'] is not None
    assert response['expiration'] is not None


def test_link_token_create_optional():
    client = create_client()

    # build the configs
    configs = {
        'user': {
            'client_user_id': str(time.time()),
        },
        'products': ["auth", "transactions"],
        'client_name': "Plaid Test",
        'country_codes': ['GB'],
        'language': 'en',
        'webhook': 'https://sample-webhook-uri.com',
        'link_customization_name': 'default',
        'account_filters': {
            'depository': {
                'account_subtypes': ['checking', 'savings'],
            },
        },
    }

    # create link token
    response = client.LinkToken.create(configs)

    # assert on response
    assert response['link_token'] is not None
    assert response['expiration'] is not None


def test_link_token_create_and_get():
    client = create_client()

    # build the configs
    configs = {
        'user': {
            'client_user_id': str(time.time()),
        },
        'products': ["auth", "transactions"],
        'client_name': "Plaid Test",
        'country_codes': ['GB'],
        'language': 'en',
        'webhook': 'https://sample-webhook-uri.com',
        'link_customization_name': 'default',
        'account_filters': {
            'depository': {
                'account_subtypes': ['checking', 'savings'],
            },
        },
    }

    # create link token
    createResponse = client.LinkToken.create(configs)

    # assert on response
    assert createResponse['link_token'] is not None
    assert createResponse['expiration'] is not None

    getResponse = client.LinkToken.get(createResponse['link_token'])
    assert getResponse['link_token'] == createResponse['link_token']
    assert getResponse['created_at'] is not None
    assert getResponse['expiration'] is not None

    assert getResponse['metadata'] is not None
    assert (getResponse['metadata']['initial_products'] ==
            ['auth', 'transactions'])
    assert (getResponse['metadata']['webhook'] ==
            'https://sample-webhook-uri.com')
    assert getResponse['metadata']['country_codes'] == ['GB']
    assert getResponse['metadata']['language'] == 'en'
    assert (getResponse['metadata']['account_filters'] ==
            {'depository': {'account_subtypes': ['checking', 'savings']}})
    assert getResponse['metadata']['client_name'] == 'Plaid Test'
