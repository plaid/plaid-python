import pytest

from plaid import Client
from plaid.utils import to_json
from plaid.errors import (
    ResourceNotFoundError,
    UnauthorizedError
)

no_mfa_credentials = {
    'username': 'plaid_test',
    'password': 'plaid_good',
}


def test_auth_no_mfa():
    client = Client('test_id', 'test_secret')
    response = client.auth('wells', no_mfa_credentials)
    assert to_json(response)['access_token'] == 'test_wells'


def test_auth_mfa():
    client = Client('test_id', 'test_secret')
    response = client.auth('pnc', no_mfa_credentials)
    assert response.status_code == 201
    assert to_json(response)['type'] == 'questions'


def test_auth_step():
    client = Client('test_id', 'test_secret', access_token='test_pnc')
    response = client.auth_step('pnc', 'tomato')
    assert response.status_code == 200
    assert to_json(response)['access_token'] == 'test_pnc'


def test_auth_delete():
    client = Client('test_id', 'test_secret', access_token='test_chase')
    response = client.auth_delete()
    assert response.status_code == 200
    assert to_json(response)['message'] == 'Successfully removed from your account'


def test_auth_update():
    client = Client('test_id', 'test_secret', access_token='test_amex')
    response = client.auth_update(no_mfa_credentials)
    assert response.status_code == 200


def test_connect_no_mfa():
    client = Client('test_id', 'test_secret')
    response = client.connect('amex', no_mfa_credentials)
    assert response.status_code == 200
    assert to_json(response)['access_token'] == 'test_amex'


def test_connect_mfa_question():
    client = Client('test_id', 'test_secret')
    response = client.connect('bofa', no_mfa_credentials)
    assert response.status_code == 201
    assert to_json(response)['type'] == 'questions'


def test_connect_mfa_list():
    client = Client('test_id', 'test_secret')
    # These credentials erroneously still force mfa in the sandbox
    # Should disambiguate by disallowing institution on API level
    # for this particular calling
    response = client.connect('chase', no_mfa_credentials)
    assert response.status_code == 201
    assert to_json(response)['type'] == 'list'


def test_connect_step_question():
    client = Client('test_id', 'test_secret', access_token='test_bofa')
    response = client.connect_step('bofa', 'tomato')
    assert response.status_code == 200
    assert to_json(response)['access_token'] == 'test_bofa'


def test_connect_step_question_loop():
    client = Client('test_id', 'test_secret', access_token='test_bofa')
    response = client.connect_step('bofa', 'again')
    assert response.status_code == 201
    assert to_json(response)['type'] == 'questions'


def test_connect_step_device_email():
    client = Client('test_id', 'test_secret', access_token='test_chase')
    response = client.connect_step('chase', None, options={
        'send_method': {'type': 'email'}
    })
    assert response.status_code == 201
    assert to_json(response)['type'] == 'device'
    assert to_json(response)['mfa']['message'] == 'Code sent to t..t@plaid.com'


def test_connect_step_device_phone():
    client = Client('test_id', 'test_secret', access_token='test_chase')
    response = client.connect_step('chase', None, options={
        'send_method': {'type': 'phone'}
    })
    assert response.status_code == 201
    assert to_json(response)['type'] == 'device'
    assert to_json(response)['mfa']['message'] == 'Code sent to xxx-xxx-5309'


def test_connect_delete():
    client = Client('test_id', 'test_secret', access_token='test_chase')
    response = client.connect_delete()
    assert response.status_code == 200
    assert to_json(response)['message'] == 'Successfully removed from your account'


def test_connect_update():
    client = Client('test_id', 'test_secret', access_token='test_amex')
    response = client.connect_update(no_mfa_credentials)
    assert response.status_code == 200


def test_connect_step_update():
    client = Client('test_id', 'test_secret', access_token='test_bofa')
    response = client.connect_update_step('bofa', 'tomato')
    assert response.status_code == 200


def test_info_no_mfa():
    client = Client('test_id', 'test_secret')
    response = client.info('wells', no_mfa_credentials)
    assert to_json(response)['access_token'] == 'test_wells'


def test_info_mfa():
    client = Client('test_id', 'test_secret')
    response = client.info('pnc', no_mfa_credentials)
    assert response.status_code == 201
    assert to_json(response)['type'] == 'questions'


def test_info_step():
    client = Client('test_id', 'test_secret', access_token='test_pnc')
    response = client.info_step('pnc', 'tomato')
    assert response.status_code == 200
    assert to_json(response)['access_token'] == 'test_pnc'


def test_income_no_mfa():
    client = Client('test_id', 'test_secret')
    response = client.income('wells', no_mfa_credentials)
    assert to_json(response)['access_token'] == 'test_wells'


def test_income_mfa():
    client = Client('test_id', 'test_secret')
    response = client.income('bofa', no_mfa_credentials)
    assert response.status_code == 201
    assert to_json(response)['type'] == 'questions'


def test_income_step():
    client = Client('test_id', 'test_secret', access_token='test_chase')
    response = client.income_step('chase', '1234')
    assert response.status_code == 200
    assert to_json(response)['access_token'] == 'test_chase'


def test_risk_no_mfa():
    client = Client('test_id', 'test_secret')
    response = client.risk('wells', no_mfa_credentials)
    assert to_json(response)['access_token'] == 'test_wells'


def test_risk_mfa():
    client = Client('test_id', 'test_secret')
    response = client.risk('bofa', no_mfa_credentials)
    assert response.status_code == 201
    assert to_json(response)['type'] == 'questions'


def test_risk_step():
    client = Client('test_id', 'test_secret', access_token='test_chase')
    response = client.risk_step('chase', '1234')
    assert response.status_code == 200
    assert to_json(response)['access_token'] == 'test_chase'


def test_upgrade():
    client = Client('test_id', 'test_secret', access_token='test_bofa')
    response = client.upgrade('info')
    assert response.status_code == 200
    assert 'info' in to_json(response).keys()


def test_exchange():
    client = Client('test_id', 'test_secret')
    response = client.exchange_token('test,chase,connected')
    assert response.status_code == 200
    assert to_json(response)['access_token'] == 'test_chase'
    assert client.access_token == 'test_chase'


def test_balance():
    client = Client('test_id', 'test_secret', access_token='test_bofa')
    response = client.balance()
    assert response.status_code == 200


def test_get_auth():
    client = Client('test_id', 'test_secret', access_token='test_bofa')
    response = client.auth_get()
    assert response.status_code == 200


def test_get_connect():
    client = Client('test_id', 'test_secret', access_token='test_bofa')
    response = client.connect_get()
    assert response.status_code == 200


def test_get_info():
    client = Client('test_id', 'test_secret', access_token='test_bofa')
    response = client.info_get()
    assert response.status_code == 200
    assert 'info' in to_json(response)
    assert 'names' in to_json(response)['info']


def test_categories():
    client = Client('test_idzz', 'test_secret')
    response = client.categories()
    assert response.status_code == 200


def test_category():
    client = Client('test_id', 'test_secret')
    response = client.category(client.categories().json()[0]['id'])
    assert response.status_code == 200


def test_institutions():
    client = Client('test_id', 'test_secret')
    response = client.institutions()
    assert response.status_code == 200


def test_institution():
    client = Client('test_id', 'test_secret')
    response = client.institution(
        to_json(client.institutions())[0]['id']
    )

    assert response.status_code == 200


def test_institution_search():
    client = Client('test_id', 'test_secret')
    response = client.institution_search('wells', 'auth')
    assert response.status_code == 200


def test_institution_search_with_multi_tokens():
    client = Client('test_id', 'test_secret')
    response = client.institution_search('wells fargo', 'auth')
    assert response.status_code == 200
    assert to_json(response)[0]['name'] == 'Wells Fargo'


def test_institution_search_with_bad_product():
    client = Client('test_id', 'test_secret')
    response = client.institution_search('wells fargo', 'bad')
    assert response.status_code == 200
    assert len(to_json(response)) == 0


def test_institution_search_without_product():
    client = Client('test_id', 'test_secret')
    response = client.institution_search('wells')
    assert response.status_code == 200


def test_institution_search_with_bad_id():
    client = Client('test_id', 'test_secret')
    response = client.institution_search(institution_id='bad')
    assert response.status_code == 200
    assert len(to_json(response)) == 0


def test_institution_search_requires_q_or_id():
    client = Client('test_id', 'test_secret')
    with pytest.raises(AssertionError):
        client.institution_search(p='auth')


def test_UnauthorizedError_bad_token():
    client = Client('test_id', 'test_secret', 'test_zoba')
    with pytest.raises(UnauthorizedError):
        client.balance()


def test_unauthorizedError_bad_username():
    client = Client('test_idz', 'test_secret')
    with pytest.raises(UnauthorizedError):
        client.balance()


def test_unauthorizedError_bad_password():
    client = Client('test_id', 'test_secretz')
    with pytest.raises(UnauthorizedError):
        client.balance()


def test_ResourceNotFound_connect():
    client = Client('test_id', 'test_secret')
    with pytest.raises(ResourceNotFoundError):
        client.connect('pnc', no_mfa_credentials)


def test_ResourceNotFound_categories():
    client = Client('test_id', 'test_secret')
    with pytest.raises(ResourceNotFoundError):
        client.category('pnc')


def test_ResourceNotFound_categories_with_suppressed_error():
    Client.config({'suppress_http_errors': True})
    client = Client('test_id', 'test_secret')
    response = client.category('pnc')
    assert response.status_code == 404
    assert (
        to_json(response)['message'] == 'unable to find category'
    )
