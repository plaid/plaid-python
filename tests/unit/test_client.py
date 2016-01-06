from plaid.client import (
    inject_credentials,
    inject_url,
    store_access_token
)
from plaid.errors import UnauthorizedError


def test_inject_credentials_decorator():
    class TestClass(object):
        def __init__(self):
            self.client_id = 'bob'
            self.secret = 'my_secret'
            self.access_token = 'access_me'

        @inject_credentials
        def some_func(self, credentials, url):
            return [credentials, url]

    plaid_url = 'http://plaid.com'

    obj = TestClass()
    creds, url = obj.some_func(plaid_url)
    assert url == plaid_url
    assert creds == {
        'client_id': 'bob',
        'secret': 'my_secret',
        'access_token': 'access_me'
    }


def test_failed_inject_credentials_decorator():
    class TestClass(object):
        def __init__(self):
            self.client_id = 'bob'
            self.secret = 'my_secret'

        @inject_credentials
        def some_func(self, credentials, url):
            return [credentials, url]

    plaid_url = 'http://plaid.com'

    obj = TestClass()
    try:
        creds, url = obj.some_func(plaid_url)
    except UnauthorizedError as e:
        assert(e.code == 1000)
        assert(e.message == 'some_func requires `access_token`')
    else:
        assert False


def test_inject_url():
    class TestClass(object):
        base_url = 'http://plaid.com'
        ENDPOINTS = {
            'auth': '/auth',
        }

        @inject_url('auth')
        def some_func(self, url, extra):
            return [url, extra]

    obj = TestClass()
    url, extra = obj.some_func(5)
    assert extra == 5
    assert url == 'http://plaid.com/auth'


def test_store_access_token():
    class Response(object):
        status_code = 200
        text = '{"access_token": 5}'
        ok = True

    class TestClass(object):
        def __init__(self):
            self.access_token = None

        @store_access_token
        def some_func(self):
            return Response()

    obj = TestClass()
    response = obj.some_func()
    assert response.text == '{"access_token": 5}'
    assert obj.access_token == 5


def test_store_access_token_sans_token():
    class Response(object):
        status_code = 200
        text = '{"no_access_token": 5}'
        ok = True

    class TestClass(object):
        def __init__(self):
            self.access_token = None

        @store_access_token
        def some_func(self):
            return Response()

    obj = TestClass()
    obj.some_func()
    assert obj.access_token is None


def test_store_access_token_on_non_200():
    class Response(object):
        status_code = 201
        text = '{"access_token": 5}'
        ok = True

    class TestClass(object):
        def __init__(self):
            self.access_token = 5

        @store_access_token
        def some_func(self):
            return Response()

    obj = TestClass()
    obj.some_func()
    assert obj.access_token == 5
