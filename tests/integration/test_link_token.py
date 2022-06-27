import time
from plaid.model.depository_account_subtypes import DepositoryAccountSubtypes
from plaid.model.depository_account_subtype import DepositoryAccountSubtype
from plaid.model.country_code import CountryCode
from plaid.model.depository_filter import DepositoryFilter
from plaid.model.link_token_account_filters import LinkTokenAccountFilters
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_auth import LinkTokenCreateRequestAuth
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.link_token_get_request import LinkTokenGetRequest
from plaid.model.products import Products
from tests.integration.util import create_client

CLIENT_NAME = "Plaid Test"


def test_link_token_create_required():
    client = create_client()

    request = LinkTokenCreateRequest(
        products=[Products("auth"), Products("transactions")],
        client_name=CLIENT_NAME,
        country_codes=[CountryCode("GB")],
        language="en",
        user=LinkTokenCreateRequestUser(client_user_id=str(time.time())),
    )
    # create link token
    response = client.link_token_create(request)

    # assert on response
    assert response["link_token"] is not None
    assert response["expiration"] is not None


def test_link_token_create_optional():
    client = create_client()

    # build the configs
    request = LinkTokenCreateRequest(
        products=[Products("auth"), Products("transactions")],
        client_name=CLIENT_NAME,
        country_codes=[CountryCode("GB")],
        language="en",
        webhook="https://sample-webhook-uri.com",
        link_customization_name="default",
        account_filters=LinkTokenAccountFilters(
            depository=DepositoryFilter(
                account_subtypes=DepositoryAccountSubtypes(
                    [DepositoryAccountSubtype("checking"), DepositoryAccountSubtype("savings")]
                )
            )
        ),
        user=LinkTokenCreateRequestUser(client_user_id=str(time.time())),
    )

    # create link token
    response = client.link_token_create(request)

    # assert on response
    assert response["link_token"] is not None
    assert response["expiration"] is not None


def test_link_token_create_and_get():
    client = create_client()

    # build the configs
    request = LinkTokenCreateRequest(
        products=[Products("auth"), Products("transactions")],
        client_name=CLIENT_NAME,
        country_codes=[CountryCode("GB")],
        language="en",
        webhook="https://sample-webhook-uri.com",
        link_customization_name="default",
        account_filters=LinkTokenAccountFilters(
            depository=DepositoryFilter(
                account_subtypes=DepositoryAccountSubtypes(
                    [DepositoryAccountSubtype("checking"), DepositoryAccountSubtype("savings")]
                )
            )
        ),
        user=LinkTokenCreateRequestUser(client_user_id=str(time.time())),
    )
    # create link token
    createResponse = client.link_token_create(request)

    # assert on response
    assert createResponse["link_token"] is not None
    assert createResponse["expiration"] is not None

    getRequest = LinkTokenGetRequest(link_token=createResponse["link_token"])
    getResponse = client.link_token_get(getRequest)
    assert getResponse["link_token"] == createResponse["link_token"]
    assert getResponse["created_at"] is not None
    assert getResponse["expiration"] is not None

    assert getResponse["metadata"] is not None
    assert getResponse["metadata"]["initial_products"] == [
        Products("auth"),
        Products("transactions"),
    ]
    assert getResponse["metadata"]["webhook"] == "https://sample-webhook-uri.com"
    assert getResponse["metadata"]["country_codes"] == [CountryCode("GB")]
    assert getResponse["metadata"]["language"] == "en"
    assert getResponse["metadata"]["account_filters"]["depository"][
        "account_subtypes"
    ] == DepositoryAccountSubtypes(
        [DepositoryAccountSubtype("checking"), DepositoryAccountSubtype("savings")]
    )
    assert getResponse["metadata"]["client_name"] == CLIENT_NAME


def test_link_token_create_extended_auth():
    client = create_client()

    request = LinkTokenCreateRequest(
        products=[Products("auth")],
        client_name=CLIENT_NAME,
        country_codes=[CountryCode("US")],
        language="en",
        user=LinkTokenCreateRequestUser(client_user_id=str(time.time())),
        auth=LinkTokenCreateRequestAuth(
            auth_type_select_enabled=True,
            automated_microdeposits_enabled=True,
            instant_match_enabled=True,
            same_day_microdeposits_enabled=True,
        ),
    )

    # create link token
    createResponse = client.link_token_create(request)

    # assert on createResponse
    assert createResponse["link_token"] is not None
    assert createResponse["expiration"] is not None
