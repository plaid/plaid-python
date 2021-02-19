from plaid.model.country_code import CountryCode
from plaid.model.products import Products
from plaid.model.institutions_get_request import InstitutionsGetRequest
from plaid.model.institutions_get_request_options import InstitutionsGetRequestOptions
from plaid.model.institutions_get_by_id_request import InstitutionsGetByIdRequest
from plaid.model.institutions_get_by_id_request_options import InstitutionsGetByIdRequestOptions
from plaid.model.institutions_search_request import InstitutionsSearchRequest
from plaid.model.institutions_search_request_options import InstitutionsSearchRequestOptions

from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION,
    SANDBOX_INSTITUTION_NAME,
)

def test_get():
    client = create_client()
    request = InstitutionsGetRequest(
        country_codes=[CountryCode('US')],
        count=3,
        offset=1
    )
    response = client.institutions_get(request)
    assert len(response['institutions']) == 3


def test_get_with_include_optional_metadata():
    client = create_client()
    request = InstitutionsGetRequest(
        country_codes=[CountryCode('US')],
        count=3,
        offset=1,
        options=InstitutionsGetRequestOptions(
            include_optional_metadata=True
        )
    )
    response = client.institutions_get(request)

    assert len(response['institutions']) == 3
    assert len(response['institutions'][0]['url']) > 0
    assert len(response['institutions'][0]['primary_color']) > 0

    assert len(response['institutions'][1]['url']) > 0
    assert len(response['institutions'][1]['primary_color']) > 0

    assert len(response['institutions'][2]['url']) > 0
    assert len(response['institutions'][2]['primary_color']) > 0


def test_get_by_id():
    client = create_client()
    request = InstitutionsGetByIdRequest(
        institution_id=SANDBOX_INSTITUTION,
        country_codes=[CountryCode('US')]
    )
    response = client.institutions_get_by_id(request)
    assert response['institution']['institution_id'] == SANDBOX_INSTITUTION


def test_get_by_id_with_include_optional_metadata():
    client = create_client()
    request = InstitutionsGetByIdRequest(
        institution_id=SANDBOX_INSTITUTION,
        country_codes=[CountryCode('US')],
        options=InstitutionsGetByIdRequestOptions(
            include_optional_metadata=True
        )
    )

    response = client.institutions_get_by_id(request)
    assert response['institution']['institution_id'] == SANDBOX_INSTITUTION
    assert response['institution']['url'] is not None

def test_search_with_products():
    client = create_client()
    request = InstitutionsSearchRequest(
        query=SANDBOX_INSTITUTION_NAME,
        products=[Products('transactions')],
        country_codes=[CountryCode('US')],
    )
    response = client.institutions_search(request)
    assert len(response['institutions']) >= 1


def test_search_with_include_optional_metadata():
    client = create_client()
    request = InstitutionsSearchRequest(
        query=SANDBOX_INSTITUTION_NAME,
        products=[Products('transactions')],
        country_codes=[CountryCode('US')],
        options=InstitutionsSearchRequestOptions(
            include_optional_metadata=True
        )
    )
    response = client.institutions_search(request)
    assert len(response['institutions']) >= 1
    assert response['institutions'][0]['url'] is not None