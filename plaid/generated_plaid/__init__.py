# coding: utf-8

# flake8: noqa

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from plaid.generated_plaid.api.plaid_api import PlaidApi

# import ApiClient
from plaid.generated_plaid.api_client import ApiClient
from plaid.generated_plaid.configuration import Configuration
from plaid.generated_plaid.exceptions import OpenApiException
from plaid.generated_plaid.exceptions import ApiTypeError
from plaid.generated_plaid.exceptions import ApiValueError
from plaid.generated_plaid.exceptions import ApiKeyError
from plaid.generated_plaid.exceptions import ApiAttributeError
from plaid.generated_plaid.exceptions import ApiException
# import models into sdk package
from plaid.generated_plaid.models.ach_class import ACHClass
from plaid.generated_plaid.models.apr import APR
from plaid.generated_plaid.models.account_assets import AccountAssets
from plaid.generated_plaid.models.account_assets_all_of import AccountAssetsAllOf
from plaid.generated_plaid.models.account_balance import AccountBalance
from plaid.generated_plaid.models.account_base import AccountBase
from plaid.generated_plaid.models.account_identity import AccountIdentity
from plaid.generated_plaid.models.account_identity_all_of import AccountIdentityAllOf
from plaid.generated_plaid.models.account_subtype import AccountSubtype
from plaid.generated_plaid.models.account_type import AccountType
from plaid.generated_plaid.models.accounts_get_request import AccountsGetRequest
from plaid.generated_plaid.models.accounts_get_request_options import AccountsGetRequestOptions
from plaid.generated_plaid.models.accounts_get_response import AccountsGetResponse
from plaid.generated_plaid.models.address import Address
from plaid.generated_plaid.models.address_data import AddressData
from plaid.generated_plaid.models.amount import Amount
from plaid.generated_plaid.models.asset_report import AssetReport
from plaid.generated_plaid.models.asset_report_audit_copy_create_request import AssetReportAuditCopyCreateRequest
from plaid.generated_plaid.models.asset_report_audit_copy_create_response import AssetReportAuditCopyCreateResponse
from plaid.generated_plaid.models.asset_report_audit_copy_get_request import AssetReportAuditCopyGetRequest
from plaid.generated_plaid.models.asset_report_audit_copy_remove_request import AssetReportAuditCopyRemoveRequest
from plaid.generated_plaid.models.asset_report_audit_copy_remove_response import AssetReportAuditCopyRemoveResponse
from plaid.generated_plaid.models.asset_report_create_request import AssetReportCreateRequest
from plaid.generated_plaid.models.asset_report_create_request_options import AssetReportCreateRequestOptions
from plaid.generated_plaid.models.asset_report_create_response import AssetReportCreateResponse
from plaid.generated_plaid.models.asset_report_filter_request import AssetReportFilterRequest
from plaid.generated_plaid.models.asset_report_filter_response import AssetReportFilterResponse
from plaid.generated_plaid.models.asset_report_get_request import AssetReportGetRequest
from plaid.generated_plaid.models.asset_report_get_response import AssetReportGetResponse
from plaid.generated_plaid.models.asset_report_item import AssetReportItem
from plaid.generated_plaid.models.asset_report_pdf_get_request import AssetReportPDFGetRequest
from plaid.generated_plaid.models.asset_report_refresh_request import AssetReportRefreshRequest
from plaid.generated_plaid.models.asset_report_refresh_request_options import AssetReportRefreshRequestOptions
from plaid.generated_plaid.models.asset_report_refresh_response import AssetReportRefreshResponse
from plaid.generated_plaid.models.asset_report_remove_request import AssetReportRemoveRequest
from plaid.generated_plaid.models.asset_report_remove_response import AssetReportRemoveResponse
from plaid.generated_plaid.models.asset_report_user import AssetReportUser
from plaid.generated_plaid.models.assets_error_webhook import AssetsErrorWebhook
from plaid.generated_plaid.models.assets_product_ready_webhook import AssetsProductReadyWebhook
from plaid.generated_plaid.models.auth_get_numbers import AuthGetNumbers
from plaid.generated_plaid.models.auth_get_request import AuthGetRequest
from plaid.generated_plaid.models.auth_get_request_options import AuthGetRequestOptions
from plaid.generated_plaid.models.auth_get_response import AuthGetResponse
from plaid.generated_plaid.models.automatically_verified_webhook import AutomaticallyVerifiedWebhook
from plaid.generated_plaid.models.balance_get_request import BalanceGetRequest
from plaid.generated_plaid.models.balance_get_request_options import BalanceGetRequestOptions
from plaid.generated_plaid.models.balance_get_response import BalanceGetResponse
from plaid.generated_plaid.models.bank_transfer import BankTransfer
from plaid.generated_plaid.models.bank_transfer_balance import BankTransferBalance
from plaid.generated_plaid.models.bank_transfer_balance_get_request import BankTransferBalanceGetRequest
from plaid.generated_plaid.models.bank_transfer_balance_get_response import BankTransferBalanceGetResponse
from plaid.generated_plaid.models.bank_transfer_cancel_request import BankTransferCancelRequest
from plaid.generated_plaid.models.bank_transfer_cancel_response import BankTransferCancelResponse
from plaid.generated_plaid.models.bank_transfer_create_request import BankTransferCreateRequest
from plaid.generated_plaid.models.bank_transfer_create_response import BankTransferCreateResponse
from plaid.generated_plaid.models.bank_transfer_direction import BankTransferDirection
from plaid.generated_plaid.models.bank_transfer_event import BankTransferEvent
from plaid.generated_plaid.models.bank_transfer_event_list_request import BankTransferEventListRequest
from plaid.generated_plaid.models.bank_transfer_event_list_response import BankTransferEventListResponse
from plaid.generated_plaid.models.bank_transfer_event_sync_request import BankTransferEventSyncRequest
from plaid.generated_plaid.models.bank_transfer_event_sync_response import BankTransferEventSyncResponse
from plaid.generated_plaid.models.bank_transfer_event_type import BankTransferEventType
from plaid.generated_plaid.models.bank_transfer_failure import BankTransferFailure
from plaid.generated_plaid.models.bank_transfer_get_request import BankTransferGetRequest
from plaid.generated_plaid.models.bank_transfer_get_response import BankTransferGetResponse
from plaid.generated_plaid.models.bank_transfer_list_request import BankTransferListRequest
from plaid.generated_plaid.models.bank_transfer_list_response import BankTransferListResponse
from plaid.generated_plaid.models.bank_transfer_migrate_account_request import BankTransferMigrateAccountRequest
from plaid.generated_plaid.models.bank_transfer_migrate_account_response import BankTransferMigrateAccountResponse
from plaid.generated_plaid.models.bank_transfer_network import BankTransferNetwork
from plaid.generated_plaid.models.bank_transfer_receiver_details import BankTransferReceiverDetails
from plaid.generated_plaid.models.bank_transfer_status import BankTransferStatus
from plaid.generated_plaid.models.bank_transfer_type import BankTransferType
from plaid.generated_plaid.models.bank_transfer_user import BankTransferUser
from plaid.generated_plaid.models.categories_get_response import CategoriesGetResponse
from plaid.generated_plaid.models.category import Category
from plaid.generated_plaid.models.cause import Cause
from plaid.generated_plaid.models.country_code import CountryCode
from plaid.generated_plaid.models.credit_card_liability import CreditCardLiability
from plaid.generated_plaid.models.default_update_webhook import DefaultUpdateWebhook
from plaid.generated_plaid.models.deposit_switch_create_request import DepositSwitchCreateRequest
from plaid.generated_plaid.models.deposit_switch_create_response import DepositSwitchCreateResponse
from plaid.generated_plaid.models.deposit_switch_get_request import DepositSwitchGetRequest
from plaid.generated_plaid.models.deposit_switch_get_response import DepositSwitchGetResponse
from plaid.generated_plaid.models.deposit_switch_token_create_request import DepositSwitchTokenCreateRequest
from plaid.generated_plaid.models.deposit_switch_token_create_response import DepositSwitchTokenCreateResponse
from plaid.generated_plaid.models.email import Email
from plaid.generated_plaid.models.error import Error
from plaid.generated_plaid.models.external_payment_schedule import ExternalPaymentSchedule
from plaid.generated_plaid.models.historical_balance import HistoricalBalance
from plaid.generated_plaid.models.historical_update_webhook import HistoricalUpdateWebhook
from plaid.generated_plaid.models.holding import Holding
from plaid.generated_plaid.models.holdings_default_update_webhook import HoldingsDefaultUpdateWebhook
from plaid.generated_plaid.models.identity_get_request import IdentityGetRequest
from plaid.generated_plaid.models.identity_get_request_options import IdentityGetRequestOptions
from plaid.generated_plaid.models.identity_get_response import IdentityGetResponse
from plaid.generated_plaid.models.inflow_model import InflowModel
from plaid.generated_plaid.models.initial_update_webhook import InitialUpdateWebhook
from plaid.generated_plaid.models.institution import Institution
from plaid.generated_plaid.models.institution_status import InstitutionStatus
from plaid.generated_plaid.models.institutions_get_by_id_request import InstitutionsGetByIdRequest
from plaid.generated_plaid.models.institutions_get_by_id_request_options import InstitutionsGetByIdRequestOptions
from plaid.generated_plaid.models.institutions_get_by_id_response import InstitutionsGetByIdResponse
from plaid.generated_plaid.models.institutions_get_request import InstitutionsGetRequest
from plaid.generated_plaid.models.institutions_get_request_options import InstitutionsGetRequestOptions
from plaid.generated_plaid.models.institutions_get_response import InstitutionsGetResponse
from plaid.generated_plaid.models.institutions_search_request import InstitutionsSearchRequest
from plaid.generated_plaid.models.institutions_search_request_options import InstitutionsSearchRequestOptions
from plaid.generated_plaid.models.institutions_search_response import InstitutionsSearchResponse
from plaid.generated_plaid.models.investment_holdings_get_request_options import InvestmentHoldingsGetRequestOptions
from plaid.generated_plaid.models.investment_transaction import InvestmentTransaction
from plaid.generated_plaid.models.investments_default_update_webhook import InvestmentsDefaultUpdateWebhook
from plaid.generated_plaid.models.investments_holdings_get_request import InvestmentsHoldingsGetRequest
from plaid.generated_plaid.models.investments_holdings_get_response import InvestmentsHoldingsGetResponse
from plaid.generated_plaid.models.investments_transactions_get_request import InvestmentsTransactionsGetRequest
from plaid.generated_plaid.models.investments_transactions_get_request_options import InvestmentsTransactionsGetRequestOptions
from plaid.generated_plaid.models.investments_transactions_get_response import InvestmentsTransactionsGetResponse
from plaid.generated_plaid.models.item import Item
from plaid.generated_plaid.models.item_access_token_invalidate_request import ItemAccessTokenInvalidateRequest
from plaid.generated_plaid.models.item_access_token_invalidate_response import ItemAccessTokenInvalidateResponse
from plaid.generated_plaid.models.item_error_webhook import ItemErrorWebhook
from plaid.generated_plaid.models.item_get_request import ItemGetRequest
from plaid.generated_plaid.models.item_get_response import ItemGetResponse
from plaid.generated_plaid.models.item_import_request import ItemImportRequest
from plaid.generated_plaid.models.item_import_request_options import ItemImportRequestOptions
from plaid.generated_plaid.models.item_import_request_user_auth import ItemImportRequestUserAuth
from plaid.generated_plaid.models.item_import_response import ItemImportResponse
from plaid.generated_plaid.models.item_product_ready_webhook import ItemProductReadyWebhook
from plaid.generated_plaid.models.item_public_token_create_request import ItemPublicTokenCreateRequest
from plaid.generated_plaid.models.item_public_token_create_response import ItemPublicTokenCreateResponse
from plaid.generated_plaid.models.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.generated_plaid.models.item_public_token_exchange_response import ItemPublicTokenExchangeResponse
from plaid.generated_plaid.models.item_remove_request import ItemRemoveRequest
from plaid.generated_plaid.models.item_remove_response import ItemRemoveResponse
from plaid.generated_plaid.models.item_status import ItemStatus
from plaid.generated_plaid.models.item_status_investments import ItemStatusInvestments
from plaid.generated_plaid.models.item_status_last_webhook import ItemStatusLastWebhook
from plaid.generated_plaid.models.item_status_transactions import ItemStatusTransactions
from plaid.generated_plaid.models.item_webhook_update_request import ItemWebhookUpdateRequest
from plaid.generated_plaid.models.item_webhook_update_response import ItemWebhookUpdateResponse
from plaid.generated_plaid.models.jwk_public_key import JWKPublicKey
from plaid.generated_plaid.models.jwt_header import JWTHeader
from plaid.generated_plaid.models.liabilities_get_request import LiabilitiesGetRequest
from plaid.generated_plaid.models.liabilities_get_request_options import LiabilitiesGetRequestOptions
from plaid.generated_plaid.models.liabilities_get_response import LiabilitiesGetResponse
from plaid.generated_plaid.models.liabilities_object import LiabilitiesObject
from plaid.generated_plaid.models.liability_override import LiabilityOverride
from plaid.generated_plaid.models.link_token_create_request import LinkTokenCreateRequest
from plaid.generated_plaid.models.link_token_create_request_account_subtypes import LinkTokenCreateRequestAccountSubtypes
from plaid.generated_plaid.models.link_token_create_request_account_subtypes_credit import LinkTokenCreateRequestAccountSubtypesCredit
from plaid.generated_plaid.models.link_token_create_request_account_subtypes_depository import LinkTokenCreateRequestAccountSubtypesDepository
from plaid.generated_plaid.models.link_token_create_request_account_subtypes_investment import LinkTokenCreateRequestAccountSubtypesInvestment
from plaid.generated_plaid.models.link_token_create_request_account_subtypes_loan import LinkTokenCreateRequestAccountSubtypesLoan
from plaid.generated_plaid.models.link_token_create_request_payment_initiation import LinkTokenCreateRequestPaymentInitiation
from plaid.generated_plaid.models.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.generated_plaid.models.link_token_create_response import LinkTokenCreateResponse
from plaid.generated_plaid.models.link_token_get_metadata_response import LinkTokenGetMetadataResponse
from plaid.generated_plaid.models.link_token_get_request import LinkTokenGetRequest
from plaid.generated_plaid.models.link_token_get_response import LinkTokenGetResponse
from plaid.generated_plaid.models.location import Location
from plaid.generated_plaid.models.mfa import MFA
from plaid.generated_plaid.models.meta import Meta
from plaid.generated_plaid.models.mortgage_interest_rate import MortgageInterestRate
from plaid.generated_plaid.models.mortgage_liability import MortgageLiability
from plaid.generated_plaid.models.mortgage_property_address import MortgagePropertyAddress
from plaid.generated_plaid.models.numbers import Numbers
from plaid.generated_plaid.models.numbers_ach import NumbersACH
from plaid.generated_plaid.models.numbers_bacs import NumbersBACS
from plaid.generated_plaid.models.numbers_eft import NumbersEFT
from plaid.generated_plaid.models.numbers_international import NumbersInternational
from plaid.generated_plaid.models.override_accounts import OverrideAccounts
from plaid.generated_plaid.models.owner import Owner
from plaid.generated_plaid.models.owner_override import OwnerOverride
from plaid.generated_plaid.models.pslf_status import PSLFStatus
from plaid.generated_plaid.models.payment_amount import PaymentAmount
from plaid.generated_plaid.models.payment_initiation_address import PaymentInitiationAddress
from plaid.generated_plaid.models.payment_initiation_payment_create_request import PaymentInitiationPaymentCreateRequest
from plaid.generated_plaid.models.payment_initiation_payment_create_response import PaymentInitiationPaymentCreateResponse
from plaid.generated_plaid.models.payment_initiation_payment_get_request import PaymentInitiationPaymentGetRequest
from plaid.generated_plaid.models.payment_initiation_payment_get_response import PaymentInitiationPaymentGetResponse
from plaid.generated_plaid.models.payment_initiation_payment_list_request import PaymentInitiationPaymentListRequest
from plaid.generated_plaid.models.payment_initiation_payment_list_response import PaymentInitiationPaymentListResponse
from plaid.generated_plaid.models.payment_initiation_recipient import PaymentInitiationRecipient
from plaid.generated_plaid.models.payment_initiation_recipient_create_request import PaymentInitiationRecipientCreateRequest
from plaid.generated_plaid.models.payment_initiation_recipient_create_response import PaymentInitiationRecipientCreateResponse
from plaid.generated_plaid.models.payment_initiation_recipient_get_request import PaymentInitiationRecipientGetRequest
from plaid.generated_plaid.models.payment_initiation_recipient_get_response import PaymentInitiationRecipientGetResponse
from plaid.generated_plaid.models.payment_initiation_recipient_list_request import PaymentInitiationRecipientListRequest
from plaid.generated_plaid.models.payment_initiation_recipient_list_response import PaymentInitiationRecipientListResponse
from plaid.generated_plaid.models.payment_meta import PaymentMeta
from plaid.generated_plaid.models.payment_status_update_webhook import PaymentStatusUpdateWebhook
from plaid.generated_plaid.models.pending_expiration_webhook import PendingExpirationWebhook
from plaid.generated_plaid.models.phone_number import PhoneNumber
from plaid.generated_plaid.models.processor_apex_processor_token_create_request import ProcessorApexProcessorTokenCreateRequest
from plaid.generated_plaid.models.processor_auth_get_request import ProcessorAuthGetRequest
from plaid.generated_plaid.models.processor_auth_get_response import ProcessorAuthGetResponse
from plaid.generated_plaid.models.processor_balance_get_request import ProcessorBalanceGetRequest
from plaid.generated_plaid.models.processor_balance_get_response import ProcessorBalanceGetResponse
from plaid.generated_plaid.models.processor_identity_get_request import ProcessorIdentityGetRequest
from plaid.generated_plaid.models.processor_identity_get_response import ProcessorIdentityGetResponse
from plaid.generated_plaid.models.processor_number import ProcessorNumber
from plaid.generated_plaid.models.processor_stripe_bank_account_token_create_request import ProcessorStripeBankAccountTokenCreateRequest
from plaid.generated_plaid.models.processor_stripe_bank_account_token_create_response import ProcessorStripeBankAccountTokenCreateResponse
from plaid.generated_plaid.models.processor_token_create_request import ProcessorTokenCreateRequest
from plaid.generated_plaid.models.processor_token_create_response import ProcessorTokenCreateResponse
from plaid.generated_plaid.models.product_status import ProductStatus
from plaid.generated_plaid.models.product_status_breakdown import ProductStatusBreakdown
from plaid.generated_plaid.models.products import Products
from plaid.generated_plaid.models.recaptcha_required_error import RecaptchaRequiredError
from plaid.generated_plaid.models.recipient_bacs import RecipientBACS
from plaid.generated_plaid.models.sandbox_bank_transfer_simulate_request import SandboxBankTransferSimulateRequest
from plaid.generated_plaid.models.sandbox_bank_transfer_simulate_response import SandboxBankTransferSimulateResponse
from plaid.generated_plaid.models.sandbox_item_fire_webhook_request import SandboxItemFireWebhookRequest
from plaid.generated_plaid.models.sandbox_item_fire_webhook_response import SandboxItemFireWebhookResponse
from plaid.generated_plaid.models.sandbox_item_reset_login_request import SandboxItemResetLoginRequest
from plaid.generated_plaid.models.sandbox_item_reset_login_response import SandboxItemResetLoginResponse
from plaid.generated_plaid.models.sandbox_item_set_verification_status_request import SandboxItemSetVerificationStatusRequest
from plaid.generated_plaid.models.sandbox_item_set_verification_status_response import SandboxItemSetVerificationStatusResponse
from plaid.generated_plaid.models.sandbox_processor_token_create_request import SandboxProcessorTokenCreateRequest
from plaid.generated_plaid.models.sandbox_processor_token_create_request_options import SandboxProcessorTokenCreateRequestOptions
from plaid.generated_plaid.models.sandbox_processor_token_create_response import SandboxProcessorTokenCreateResponse
from plaid.generated_plaid.models.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.generated_plaid.models.sandbox_public_token_create_request_options import SandboxPublicTokenCreateRequestOptions
from plaid.generated_plaid.models.sandbox_public_token_create_request_options_transactions import SandboxPublicTokenCreateRequestOptionsTransactions
from plaid.generated_plaid.models.sandbox_public_token_create_response import SandboxPublicTokenCreateResponse
from plaid.generated_plaid.models.security import Security
from plaid.generated_plaid.models.servicer_address_data import ServicerAddressData
from plaid.generated_plaid.models.standalone_account_type import StandaloneAccountType
from plaid.generated_plaid.models.standalone_currency_code_list import StandaloneCurrencyCodeList
from plaid.generated_plaid.models.standalone_investment_transaction_subtype import StandaloneInvestmentTransactionSubtype
from plaid.generated_plaid.models.standalone_investment_transaction_type import StandaloneInvestmentTransactionType
from plaid.generated_plaid.models.student_loan import StudentLoan
from plaid.generated_plaid.models.student_loan_repayment_model import StudentLoanRepaymentModel
from plaid.generated_plaid.models.student_loan_status import StudentLoanStatus
from plaid.generated_plaid.models.student_repayment_plan import StudentRepaymentPlan
from plaid.generated_plaid.models.transaction import Transaction
from plaid.generated_plaid.models.transaction_code import TransactionCode
from plaid.generated_plaid.models.transaction_override import TransactionOverride
from plaid.generated_plaid.models.transactions_get_request import TransactionsGetRequest
from plaid.generated_plaid.models.transactions_get_request_options import TransactionsGetRequestOptions
from plaid.generated_plaid.models.transactions_get_response import TransactionsGetResponse
from plaid.generated_plaid.models.transactions_refresh_request import TransactionsRefreshRequest
from plaid.generated_plaid.models.transactions_refresh_response import TransactionsRefreshResponse
from plaid.generated_plaid.models.transactions_removed_webhook import TransactionsRemovedWebhook
from plaid.generated_plaid.models.user_custom_password import UserCustomPassword
from plaid.generated_plaid.models.user_permission_revoked_webhook import UserPermissionRevokedWebhook
from plaid.generated_plaid.models.verification_expired_webhook import VerificationExpiredWebhook
from plaid.generated_plaid.models.warning import Warning
from plaid.generated_plaid.models.webhook_update_acknowledged_webhook import WebhookUpdateAcknowledgedWebhook
from plaid.generated_plaid.models.webhook_verification_key_get_request import WebhookVerificationKeyGetRequest
from plaid.generated_plaid.models.webhook_verification_key_get_response import WebhookVerificationKeyGetResponse

