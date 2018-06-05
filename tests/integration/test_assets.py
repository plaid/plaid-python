import time
from plaid.errors import PlaidError
from tests.integration.util import (
    create_client,
    CREDENTIALS,
    SANDBOX_INSTITUTION,
)


access_token = None

def setup_module(module):
    client = create_client()
    response = client.Item.create(
        CREDENTIALS, SANDBOX_INSTITUTION, ['assets'])
    global access_token
    access_token = response['access_token']

def teardown_module(module):
    client = create_client()
    client.Item.remove(access_token)

def test_create():
    client = create_client()

    # create an asset report for one item
    options = {
        'client_report_id': '123',
        'webhook': 'https://www.example.com',
        'user': {
            'client_user_id': '789',
            'first_name': 'Jane',
            'middle_name': 'Leah',
            'last_name': 'Doe',
            'ssn': '123-45-6789',
            'phone_number': '(555) 123-4567',
            'email': 'jane.doe@example.com',
        }
    }
    response = client.AssetReport.create(
        [access_token],
        days_requested=60,
        options=options)
    assert response['asset_report_token'] is not None
    assert response['asset_report_id'] is not None

def poll_for_asset_report(client, asset_report_token, retries=20):
    try:
        return client.AssetReport.get(asset_report_token)
    except PlaidError as e:
        if e.code == 'PRODUCT_NOT_READY' and retries > 0:
            time.sleep(1)
            return poll_for_asset_report(
                client,
                asset_report_token,
                retries - 1)

        raise e

def test_get():
    client = create_client()

    # create an asset report for one item
    response = client.AssetReport.create(
        [access_token],
        days_requested=60)
    asset_report_token = response['asset_report_token']

    # retrieve the asset report
    response = poll_for_asset_report(client, asset_report_token)
    assert response['report'] is not None

def test_get_pdf():
    client = create_client()

    # create an asset report for one item
    response = client.AssetReport.create(
        [access_token],
        days_requested=60)
    asset_report_token = response['asset_report_token']

    # verify that the asset report has been generated
    get_response = poll_for_asset_report(client, asset_report_token)
    assert get_response['report'] is not None

    # retrieve the asset report as a PDF
    pdf = client.AssetReport.get_pdf(asset_report_token)
    assert pdf is not None

