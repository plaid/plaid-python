import time
import json
import plaid
from plaid.model.products import Products
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.sandbox_public_token_create_request_options import SandboxPublicTokenCreateRequestOptions
from plaid.model.sandbox_public_token_create_request_options_statements import SandboxPublicTokenCreateRequestOptionsStatements
from plaid.model.statements_list_request import StatementsListRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.item_remove_request import ItemRemoveRequest
from plaid.model.statements_download_request import StatementsDownloadRequest
from plaid.model.statements_refresh_request import StatementsRefreshRequest
from datetime import datetime as dt
import hashlib

from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION,
)

access_token = None

START_DATE = dt.strptime("2023-12-01", "%Y-%m-%d").date()
END_DATE = dt.strptime("2024-02-01", "%Y-%m-%d").date()
REFRESH_START_DATE = dt.strptime("2023-12-01", "%Y-%m-%d").date()
REFRESH_END_DATE = dt.strptime("2024-02-01", "%Y-%m-%d").date()
MAX_RETRIES = 5
RETRY_INTERVAL_SECONDS = 5


def setup_module(module):
    client = create_client()
    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('statements')],
        options=SandboxPublicTokenCreateRequestOptions(
            statements=SandboxPublicTokenCreateRequestOptionsStatements(
                start_date=START_DATE,
                end_date=END_DATE,
            )
        )
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


def list_statements_with_retries(client, access_token, num_retries=MAX_RETRIES):
    response = None
    for i in range(num_retries):
        try:
            request = StatementsListRequest(access_token=access_token)
            response = client.statements_list(request)
        except plaid.ApiException as e:
            response = json.loads(e.body)
            if response['error_code'] == 'PRODUCT_NOT_READY':
                time.sleep(RETRY_INTERVAL_SECONDS)
                continue
            else:
                raise e
        break
    return response


def download_statement(client, statement_id):
    try:
        request = StatementsDownloadRequest(
            access_token=access_token,
            statement_id=statement_id,
        )
        return client.statements_download(request, _return_http_data_only=False)
    except plaid.ApiException as e:
        raise e


def refresh_statements(client, start_date, end_date):
    try:
        request = StatementsRefreshRequest(
            access_token=access_token,
            start_date=start_date,
            end_date=end_date,
        )
        return client.statements_refresh(request)
    except plaid.ApiException as e:
        raise e


def get_sha_256(buffered_reader):
    sha256_hash = hashlib.sha256()
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: buffered_reader.read(4096), b""):
        sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def test_full_flow():
    client = create_client()

    list_statements_response = list_statements_with_retries(client, access_token, num_retries=MAX_RETRIES)
    assert len(list_statements_response['accounts']) > 0
    assert len(list_statements_response['accounts'][0]['statements']) > 0

    for account in list_statements_response['accounts']:
        for statement in account['statements']:
            data, status_code, headers = download_statement(client, statement_id=statement['statement_id'])
            assert data is not None
            assert status_code == 200
            assert get_sha_256(data) == headers.get('plaid-content-hash')

    refresh_request_id = refresh_statements(client, start_date=REFRESH_START_DATE, end_date=REFRESH_END_DATE)
    assert refresh_request_id is not None

    # when setting up your integration, it is better to use webhooks rather than poll Plaid's API
    refreshed_list_statements_response = list_statements_with_retries(client, access_token, num_retries=10)
    assert len(refreshed_list_statements_response['accounts']) > 0
    assert len(refreshed_list_statements_response['accounts'][0]['statements']) > 0
