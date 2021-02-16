import time
import json
import os
import plaid
from plaid.model.products import Products
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.asset_report_create_request import AssetReportCreateRequest
from plaid.model.asset_report_create_request_options import AssetReportCreateRequestOptions
from plaid.model.asset_report_filter_request import AssetReportFilterRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.item_remove_request import ItemRemoveRequest
from plaid.model.asset_report_user import AssetReportUser
from plaid.model.asset_report_pdf_get_request import AssetReportPDFGetRequest
from plaid.model.asset_report_get_request import AssetReportGetRequest
from plaid.model.asset_report_refresh_request import AssetReportRefreshRequest
from plaid.model.asset_report_audit_copy_create_request import AssetReportAuditCopyCreateRequest
from plaid.model.asset_report_audit_copy_get_request import AssetReportAuditCopyGetRequest
from plaid.model.asset_report_audit_copy_remove_request import AssetReportAuditCopyRemoveRequest
from plaid.model.asset_report_remove_request import AssetReportRemoveRequest

from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION,
)

client_id = os.environ['CLIENT_ID']

access_token = None

def setup_module(module):
    client = create_client()
    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('assets')],
    )
    pt_response = client.sandbox_public_token_create(pt_request)

    exchange_request = ItemPublicTokenExchangeRequest(
        public_token=pt_response['public_token']
    )
    exchange_response = client.item_public_token_exchange(exchange_request)
    global access_token
    access_token = exchange_response['access_token']


def teardown_module(module):
    client = create_client()
    ir_request = ItemRemoveRequest(
        access_token=access_token
    )
    client.item_remove(ir_request)


def test_full_flow():
    client = create_client()

    # create an asset report for one item
    request = AssetReportCreateRequest(
        access_tokens=[access_token],
        days_requested=60,
        options=AssetReportCreateRequestOptions(
            webhook='https://www.example.com',
            client_report_id='123',
            user=AssetReportUser(
                client_user_id='789',
                first_name='Jane',
                middle_name='Leah',
                last_name='Doe',
                ssn='123-45-6789',
                phone_number='(555) 123-4567',
                email='jane.doe@example.com',
            )
        )
    )

    response = client.asset_report_create(request)
    asset_report_token = response['asset_report_token']
    asset_report_id = response['asset_report_id']
    assert asset_report_token is not None
    assert asset_report_id is not None

    # retrieve the asset report
    response = poll_for_asset_report(client, asset_report_token)
    report = response['report']
    assert report is not None

    # retrieve the asset report as an Asset Report with Insights
    request = AssetReportGetRequest(
        asset_report_token=asset_report_token,
        include_insights=True
    )
    response = client.asset_report_get(request)
    report = response['report']
    assert report is not None

    # The transactions in an Asset Report with Insights should have a non-null
    # `name` (when available).
    assert (
        name_exists_for_some_transaction(report))

    # retrieve the asset report as a PDF
    request = AssetReportPDFGetRequest(
        asset_report_token=asset_report_token,
    )
    pdf = client.asset_report_pdf_get(request)
    assert pdf is not None

    # create a filtered copy of the asset report
    account_ids_to_exclude = [report['items'][0]['accounts'][0]['account_id']]
    request = AssetReportFilterRequest(
        asset_report_token=asset_report_token,
        account_ids_to_exclude=account_ids_to_exclude
    )
    response = client.asset_report_filter(request)
    assert response['asset_report_token'] is not None

    # create a refreshed copy of the asset report
    request = AssetReportRefreshRequest(
        asset_report_token=asset_report_token,
        days_requested=10
    )
    response = client.asset_report_refresh(request)
    assert response['asset_report_token'] is not None

    # create an audit copy
    request = AssetReportAuditCopyCreateRequest(
        asset_report_token=asset_report_token,
        auditor_id=client_id
    )

    response = client.asset_report_audit_copy_create(request)
    audit_copy_token = response['audit_copy_token']
    assert audit_copy_token is not None

    # get the audit copy
    request = AssetReportAuditCopyGetRequest(
        audit_copy_token=audit_copy_token,
    )
    response = client.asset_report_audit_copy_get(request)
    audit_copy = response['report']
    assert audit_copy is not None

    # remove the audit copy token
    request = AssetReportAuditCopyRemoveRequest(
        audit_copy_token=audit_copy_token,
    )
    response = client.asset_report_audit_copy_remove(request)
    removed = response['removed']
    assert removed

    # remove the asset report
    request = AssetReportRemoveRequest(
        asset_report_token=asset_report_token
    )
    response = client.asset_report_remove(request)
    removed = response['removed']
    assert removed


def name_exists_for_some_transaction(report):
    for account in report['items'][0]['accounts']:
        if len(account['transactions']) > 0:
            return (account['transactions'][0]['name'] is not None)

    return False


def poll_for_asset_report(client, asset_report_token, retries=20):
    try:
        request = AssetReportGetRequest(
            asset_report_token=asset_report_token,
        )
        return client.asset_report_get(request)
    except plaid.ApiException as e:
        response = json.loads(e.body)
        if response['error_code'] == 'PRODUCT_NOT_READY' and retries > 0:
            time.sleep(1)
            return poll_for_asset_report(
                client,
                asset_report_token,
                retries - 1)

        raise e