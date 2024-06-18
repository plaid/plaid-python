import time

from plaid.model.identity_verification_status import IdentityVerificationStatus
from plaid.model.identity_verification_create_request_user import IdentityVerificationCreateRequestUser
from plaid.model.identity_verification_request_user import IdentityVerificationRequestUser
from plaid.model.strategy import Strategy

from plaid.model.identity_verification_create_request import IdentityVerificationCreateRequest
from plaid.model.identity_verification_get_request import IdentityVerificationGetRequest
from plaid.model.identity_verification_list_request import IdentityVerificationListRequest
from plaid.model.identity_verification_retry_request import IdentityVerificationRetryRequest

from tests.integration.util import create_client

TEMPLATE_ID = "flwtmp_aWogUuKsL6NEHU"
CLIENT_USER_ID = "idv-user-" + str(time.time())
EMAIL = "idv-user-" + str(time.time()) + "@example.com"

def test_identity_verification_create_and_retry():
    client = create_client()

    create_request = IdentityVerificationCreateRequest(
        client_user_id=CLIENT_USER_ID,
        is_shareable=True,
        template_id=TEMPLATE_ID,
        gave_consent=True,
        user=IdentityVerificationCreateRequestUser(
            email_address=EMAIL,
        )
    )
    # create IDV request
    create_response = client.identity_verification_create(create_request)

    # assert on response
    assert create_response["shareable_url"] is not None
    assert create_response["status"] == IdentityVerificationStatus("active")

    retry_request = IdentityVerificationRetryRequest(
        template_id=TEMPLATE_ID,
        client_user_id=CLIENT_USER_ID,
        strategy=Strategy('reset'),
        user=IdentityVerificationRequestUser(
            email_address=EMAIL,
        )
    )
    # retry IDV request
    retry_response = client.identity_verification_retry(retry_request)

    assert retry_response["shareable_url"] is not None
    assert retry_response["status"] == IdentityVerificationStatus("active")

    list_request = IdentityVerificationListRequest(
        template_id=TEMPLATE_ID,
        client_user_id=CLIENT_USER_ID
    )
    # list IDV request
    list_response = client.identity_verification_list(list_request)

    assert list_response["identity_verifications"][0]["client_user_id"] == CLIENT_USER_ID

    identity_verification_id = list_response["identity_verifications"][0]["id"]

    get_request = IdentityVerificationGetRequest(
        identity_verification_id=identity_verification_id
    )
    # get IDV request
    get_response = client.identity_verification_get(get_request)

    assert get_response["id"] == identity_verification_id
