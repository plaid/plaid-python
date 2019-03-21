from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION,
    SANDBOX_INSTITUTION_NAME,
)


def test_get():
    client = create_client()
    response = client.Institutions.get(3, offset=1)
    assert len(response['institutions']) == 3


def test_get_with_include_optional_metadata():
    client = create_client()
    response = client.Institutions.get(3, offset=1, _options={
        'include_optional_metadata': True,
    })
    assert len(response['institutions']) == 3
    assert len(response['institutions'][0]['url']) > 0
    assert len(response['institutions'][0]['logo']) > 0
    assert len(response['institutions'][0]['primary_color']) > 0

    assert len(response['institutions'][1]['url']) > 0
    assert len(response['institutions'][1]['logo']) > 0
    assert len(response['institutions'][1]['primary_color']) > 0

    assert len(response['institutions'][2]['url']) > 0
    assert len(response['institutions'][2]['logo']) > 0
    assert len(response['institutions'][2]['primary_color']) > 0


def test_get_by_id():
    client = create_client()
    response = client.Institutions.get_by_id(SANDBOX_INSTITUTION)
    assert response['institution']['institution_id'] == SANDBOX_INSTITUTION


def test_get_by_id_with_include_optional_metadata():
    client = create_client()
    response = client.Institutions.get_by_id(SANDBOX_INSTITUTION, _options={
        'include_optional_metadata': True,
    })
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


def test_search_with_include_optional_metadata():
    client = create_client()
    response = client.Institutions.search(
        SANDBOX_INSTITUTION_NAME, _options={
            'include_optional_metadata': True,
        })
    assert len(response['institutions']) >= 1
