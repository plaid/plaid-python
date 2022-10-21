import pytest

from plaid.model.products import Products
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.sandbox_public_token_create_request_options import SandboxPublicTokenCreateRequestOptions
from plaid.model.sandbox_public_token_create_request_options_income_verification import SandboxPublicTokenCreateRequestOptionsIncomeVerification
from plaid.model.income_verification_source_type import IncomeVerificationSourceType
from plaid.model.sandbox_public_token_create_request_income_verification_bank_income import SandboxPublicTokenCreateRequestIncomeVerificationBankIncome


from tests.integration.util import (
    create_client,
    SANDBOX_INSTITUTION
)

@pytest.mark.skip(reason="TODO (czhou): unskip when tests are fixed")
def test_sandbox_income_verification():
    client = create_client()

    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=SANDBOX_INSTITUTION,
        initial_products=[Products('income_verification')],
        options=SandboxPublicTokenCreateRequestOptions(
            income_verification=SandboxPublicTokenCreateRequestOptionsIncomeVerification(
                income_source_types=[IncomeVerificationSourceType('bank')],
                bank_income=SandboxPublicTokenCreateRequestIncomeVerificationBankIncome(
                    days_requested=180,
                ),
            ),
        ),
    )
    pt_response = client.sandbox_public_token_create(pt_request)
    assert pt_response is not None
    assert pt_response['public_token'] is not None
