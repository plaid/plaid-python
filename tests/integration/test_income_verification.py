from plaid.model.products import Products

from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.sandbox_public_token_create_request_options import SandboxPublicTokenCreateRequestOptions
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest

from plaid.model.income_verification_documents_download_request import IncomeVerificationDocumentsDownloadRequest
from plaid.model.income_verification_paystubs_get_request import IncomeVerificationPaystubsGetRequest
from plaid.model.income_verification_taxforms_get_request import IncomeVerificationTaxformsGetRequest
from plaid.model.income_verification_precheck_request import IncomeVerificationPrecheckRequest
from plaid.model.income_verification_precheck_employer import IncomeVerificationPrecheckEmployer
from plaid.model.income_verification_precheck_user import IncomeVerificationPrecheckUser
from plaid.model.income_verification_precheck_employer_address import IncomeVerificationPrecheckEmployerAddress
from plaid.model.signal_address_data import SignalAddressData


from tests.integration.util import (
    create_client,
)

# Test constants
INCOME_INSTITUTION = 'ins_135842'
INCOME_PRODUCTS = [Products('income_verification')]
WEBHOOK_URL = 'examplewebhook.com'

access_token = None

def setup_module():
    client = create_client()

    sandbox_public_token_create_request = SandboxPublicTokenCreateRequest(
        institution_id=INCOME_INSTITUTION,
        initial_products=INCOME_PRODUCTS,
        options=SandboxPublicTokenCreateRequestOptions(
            webhook=WEBHOOK_URL
        )
    )
    sandbox_public_token_create_response = client.sandbox_public_token_create(sandbox_public_token_create_request)
    sandbox_public_token = sandbox_public_token_create_response['public_token']
    assert(sandbox_public_token is not None)

    item_public_token_exchange_request = ItemPublicTokenExchangeRequest(
        public_token=sandbox_public_token
    )
    item_public_token_exchange_response = client.item_public_token_exchange(item_public_token_exchange_request)
    global access_token
    access_token = item_public_token_exchange_response['access_token']
    assert(access_token is not None)

def test_paystubs_get():
    client = create_client()
    income_verification_paystubs_get_request = IncomeVerificationPaystubsGetRequest(
        access_token=access_token
    )
    income_verification_paystubs_get_response = client.income_verification_paystubs_get(income_verification_paystubs_get_request)
    assert(income_verification_paystubs_get_response is not None)
    assert(income_verification_paystubs_get_response['paystubs'] is not None)
    assert(income_verification_paystubs_get_response['document_metadata'] is not None)

def test_precheck():
    client = create_client()
    precheck_employer = IncomeVerificationPrecheckEmployer(
        name='Plaid Inc.',
        tax_id='123-45-6709',
        address=IncomeVerificationPrecheckEmployerAddress(
            street='234 Work St.',
            city='Anytown',
            region='CA',
            postal_code='12345',
            country='US',
        ),
        url='http://www.employer.com'
    )
    precheck_user = IncomeVerificationPrecheckUser(
        first_name='Jane',
        last_name='Doe',
        email_address='janedoe@gmail.com',
        home_address=SignalAddressData(
            street='234 First St.',
            city='Anytown',
            region='CA',
            postal_code='12345',
            country='US',
        ),
    )
    income_verification_precheck_request = IncomeVerificationPrecheckRequest(
        employer=precheck_employer,
        user=precheck_user
    )

    income_verification_precheck_response = client.income_verification_precheck(income_verification_precheck_request)
    assert(income_verification_precheck_response is not None)
    assert(income_verification_precheck_response['precheck_id'] is not None)
    assert(income_verification_precheck_response['confidence'] is not None)

def test_taxforms_get():
    client = create_client()
    income_verification_taxforms_get_request = IncomeVerificationTaxformsGetRequest(
        access_token=access_token
    )
    income_verification_taxforms_get_response = client.income_verification_taxforms_get(income_verification_taxforms_get_request)
    assert(income_verification_taxforms_get_response is not None)
    assert(income_verification_taxforms_get_response['taxforms'] is not None)
    assert(income_verification_taxforms_get_response['document_metadata'] is not None)
