from mock import patch, Mock

from plaid import Client


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
