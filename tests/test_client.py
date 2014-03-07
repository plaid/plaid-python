import pytest

from mock import patch, Mock

from plaid import Client, require_access_token


def test_require_access_token_decorator():
    class TestClass(object):
        access_token = 'foo'
        @require_access_token
        def some_func(self):
            return True

    obj = TestClass()
    obj.some_func()


def test_require_access_token_decorator_raises():
    class TestClass(object):
        access_token = None
        @require_access_token
        def some_func(self):
            return True

    obj = TestClass()
    with pytest.raises(Exception):
        obj.some_func()


def test_connect():
    with patch('requests.post') as mock_requests_post:
        mock_response = Mock()
        mock_response.content = '{}'
        mock_requests_post.return_value = mock_response

        client = Client('myclientid', 'mysecret')

        account_type = 'bofa'
        username = 'foo'
        password = 'bar'
        email = 'foo@bar.com'

        response = client.connect(account_type, username, password, email)

        assert mock_response == response


def test_step():
    with patch('requests.post') as mock_requests_post:
        client = Client('myclientid', 'mysecret', 'token')
        client.step('bofa', 'foo')
        assert mock_requests_post.called


def test_step_requires_access_token():
    client = Client('myclientid', 'mysecret')
    with pytest.raises(Exception):
        client.step('bofa', 'foo')


def test_delete_user():
    with patch('requests.delete') as mock_requests_delete:
        client = Client('myclientid', 'mysecret', 'token')
        client.delete_user()
        assert mock_requests_delete.called


def test_delete_user_requires_access_token():
    client = Client('myclientid', 'mysecret')
    with pytest.raises(Exception):
        client.delete_user('bofa', 'foo')


def test_transactions():
    with patch('requests.get') as mock_requests_get:
        client = Client('myclientid', 'mysecret', 'token')
        client.transactions()
        assert mock_requests_get.called


def test_transactions_requires_access_token():
    client = Client('myclientid', 'mysecret')
    with pytest.raises(Exception):
        client.transactions()


def test_entity():
    with patch('requests.get') as mock_requests_get:
        client = Client('myclientid', 'mysecret')
        client.entity(1)
        assert mock_requests_get.called


def test_categories():
    with patch('requests.get') as mock_requests_get:
        client = Client('myclientid', 'mysecret')
        client.categories()
        assert mock_requests_get.called


def test_category():
    with patch('requests.get') as mock_requests_get:
        client = Client('myclientid', 'mysecret')
        client.category(1)
        assert mock_requests_get.called


def test_categories_by_mapping():
    with patch('requests.get') as mock_requests_get:
        client = Client('myclientid', 'mysecret')
        client.categories_by_mapping('Food > Spanish Restaurant', 'plaid')
        assert mock_requests_get.called
