from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION,
    SANDBOX_INSTITUTION_NAME,
)


def test_get():
    client = create_client()
    response = client.Institutions.get(3, offset=1)
    assert len(response['institutions']) == 3


def test_get_by_id():
    client = create_client()
    response = client.Institutions.get_by_id(SANDBOX_INSTITUTION)
    assert response['institution']['institution_id'] == SANDBOX_INSTITUTION


def test_search():
    client = create_client()
    response = client.Institutions.search(SANDBOX_INSTITUTION_NAME)
    assert len(response['institutions']) >= 1


def test_search_with_products():
    client = create_client()
    response = client.Institutions.search(
        SANDBOX_INSTITUTION_NAME, products=['transactions'])
    assert len(response['institutions']) >= 1
