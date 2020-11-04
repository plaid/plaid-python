import plaid.generated_plaid as generated_plaid
from plaid.errors import PlaidError
from plaid.version import __version__

DEFAULT_TIMEOUT = 600  # 10 minutes
API_VERSION = "2020-09-14"


class Client:
    """
    Python Plaid API client.

    See official documentation at: https://plaid.com/docs.

    """

    def __init__(self, client_id=None, secret=None, environment=None, client_app=None):
        """
        Initialize a client with credentials.

        :param  str     client_id:          Your Plaid client ID
        :arg    str     secret:             Your Plaid secret
        :arg    str     environment:        One of ``sandbox``,
                                            ``development``, or ``production``.
        :arg    str     client_app:         Internal header to include
                                                in requests
        """
        self.client_id = client_id
        self.secret = secret
        self.environment = environment
        self.client_app = client_app
        self.api_version = API_VERSION
        if self.environment == "development":
            warnings.warn(
                """
                Development is not intended for production usage.
                Swap out url for https://production.plaid.com
                via Client.config before switching to production
            """
            )

        # initializing the generated client
        configuration = generated_plaid.Configuration(
            host=f"https://{self.environment}.plaid.com",
        )
        self.generated_client = generated_plaid.ApiClient(configuration)
        self.generated_api = generated_plaid.PlaidApi(self.generated_client)

        # configuring the generated client with headers
        self.generated_client.default_headers = {
            "Plaid-Version": self.api_version,
            "User-Agent": f"Plaid Python v{__version__}",
        }
        if self.client_app:
            self.generated_client.default_headers["Plaid-Client-App"] = self.client_app

        self.Accounts = Accounts(self)
        self.AssetReport = AssetReport(self)
        self.Auth = Auth(self)
        self.BankTransfer = BankTransfer(self)
        self.Categories = Categories(self)
        self.DepositSwitch = DepositSwitch(self)
        self.Holdings = Holdings(self)
        self.Identity = Identity(self)
        self.Institutions = Institutions(self)
        self.InvestmentTransactions = InvestmentTransactions(self)
        self.Item = Item(self)
        self.Liabilities = Liabilities(self)
        self.LinkToken = LinkToken(self)
        self.PaymentInitiation = PaymentInitiation(self)
        self.Processor = Processor(self)
        self.Sandbox = Sandbox(self)
        self.Transactions = Transactions(self)
        self.Webhooks = Webhooks(self)

    def handle_request(self, method, request):
        try:
            response = method(request)
            return response.to_dict()
        except Exception as e:
            raise PlaidError.from_generated_error(e)


class API:
    """Base class for classes containing groups of API endpoints."""

    def __init__(self, client: Client):
        self.client = client
        self.client_id = self.client.client_id
        self.secret = self.client.secret
        self.gen_api = self.client.generated_api


class Accounts(API):
    """
    Accounts endpoints.

    """

    def __init__(self, client):
        super(Accounts, self).__init__(client)
        self.balance = Accounts.Balance(client)

    def get(self, access_token, _options=None, account_ids=None):
        options = _options if _options else {}
        if account_ids is not None:
            options["account_ids"] = account_ids

        options = (
            generated_plaid.AccountsGetRequestOptions(**options) if options else None
        )

        request = generated_plaid.AccountsGetRequest(
            self.client_id,
            self.secret,
            access_token,
            options,
        )
        return self.client.handle_request(self.gen_api.accounts_get, request)

    class Balance(API):
        """Accounts balance endpoint."""

        def get(self, access_token, _options=None, account_ids=None):
            options = _options if _options else {}
            if account_ids is not None:
                options["account_ids"] = account_ids

            options = (
                generated_plaid.BalanceGetRequestOptions(**options) if options else None
            )

            request = generated_plaid.BalanceGetRequest(
                access_token,
                self.secret,
                self.client_id,
                options,
            )
            return self.client.handle_request(
                self.gen_api.balance_get,
                request,
            )


class AssetReport(API):
    """Assets endpoints."""

    def __init__(self, client: Client):
        super(AssetReport, self).__init__(client)
        self.audit_copy = AssetReport.AuditCopy(client)

    def create(self, access_tokens, days_requested, options=None):
        request = generated_plaid.AssetReportCreateRequest(
            self.client_id,
            self.secret,
            access_tokens,
            days_requested,
            options,
        )
        return self.client.handle_request(
            self.gen_api.asset_report_create,
            request,
        )

    def filter(self, asset_report_token, account_ids_to_exclude):
        request = generated_plaid.AssetReportFilterRequest(
            self.client_id,
            self.secret,
            asset_report_token,
            account_ids_to_exclude,
        )
        return self.client.handle_request(
            self.gen_api.asset_report_filter,
            request,
        )

    def refresh(self, asset_report_token, days_requested, options=None):
        request = generated_plaid.AssetReportRefreshRequest(
            self.client_id,
            self.secret,
            asset_report_token,
            days_requested,
            options,
        )
        return self.client.handle_request(
            self.gen_api.asset_report_refresh,
            request,
        )

    def get(self, asset_report_token, include_insights=False):
        request = generated_plaid.AssetReportGetRequest(
            self.client_id,
            self.secret,
            asset_report_token,
            include_insights,
        )
        return self.client.handle_request(
            self.gen_api.asset_report_get,
            request,
        )

    def get_pdf(self, asset_report_token):
        request = generated_plaid.AssetReportPDFGetRequest(
            self.client_id, self.secret, asset_report_token
        )
        temp_pdf_path = self.gen_api.asset_report_pdf_get(request)
        temp_pdf_fd = open(temp_pdf_path, "rb")
        contents = temp_pdf_fd.read()
        temp_pdf_fd.close()
        return contents

    def remove(self, asset_report_token):
        request = generated_plaid.AssetReportRemoveRequest(
            self.client_id,
            self.secret,
            asset_report_token,
        )
        return self.client.handle_request(
            self.gen_api.asset_report_remove,
            request,
        )

    class AuditCopy(API):
        """Audit copy endpoints. Use this class via the `audit_copy` member on
        the `AssetReport` class."""

        def create(self, asset_report_token, auditor_id):
            request = generated_plaid.AssetReportAuditCopyCreateRequest(
                self.client_id,
                self.secret,
                asset_report_token,
                auditor_id,
            )
            return self.client.handle_request(
                self.gen_api.asset_report_audit_copy_create,
                request,
            )

        def get(self, audit_copy_token):
            request = generated_plaid.AssetReportAuditCopyGetRequest(
                self.client_id,
                self.secret,
                audit_copy_token,
            )

            return self.client.handle_request(
                self.gen_api.asset_report_audit_copy_get,
                request,
            )

        def remove(self, audit_copy_token):
            request = generated_plaid.AssetReportAuditCopyRemoveRequest(
                self.client_id,
                self.secret,
                audit_copy_token,
            )
            return self.client.handle_request(
                self.gen_api.asset_report_audit_copy_remove,
                request,
            )


class Auth(API):
    """Auth endpoints."""

    def get(self, access_token, _options=None, account_ids=None):
        options = _options if _options else {}
        if account_ids is not None:
            options["account_ids"] = account_ids

        options = generated_plaid.AuthGetRequestOptions(**options) if options else None

        request = generated_plaid.AuthGetRequest(
            self.client_id,
            self.secret,
            access_token,
            options,
        )
        return self.client.handle_request(
            self.gen_api.auth_get,
            request,
        )


class BankTransfer(API):
    def __init__(self, client: Client):
        super(BankTransfer, self).__init__(client)
        self.balance = BankTransfer.Balance(client)

    def cancel(self, bank_transfer_id):
        request = generated_plaid.BankTransferCancelRequest(
            self.client_id,
            self.secret,
            bank_transfer_id,
        )

        return self.client.handle_request(
            self.gen_api.bank_transfer_cancel,
            request,
        )

    def create(
        self,
        idempotency_key,
        access_token,
        account_id,
        type,
        network,
        amount,
        iso_currency_code,
        description,
        user,
        metadata,
        ach_class=None,
        custom_tag=None,
        origination_account_id=None,
    ):
        request = generated_plaid.BankTransferCreateRequest(
            self.client_id,
            self.secret,
            idempotency_key,
            access_token,
            account_id,
            type,
            network,
            amount,
            iso_currency_code,
            description,
            ach_class,
            user,
            custom_tag,
            metadata,
            origination_account_id,
        )

        return self.client.handle_request(
            self.gen_api.bank_transfer_create,
            request,
        )

    def list_events(
        self,
        start_date=None,
        end_date=None,
        bank_transfer_id=None,
        account_id=None,
        bank_transfer_type=None,
        event_types=None,
        count=None,
        offset=None,
        origination_account_id=None,
        direction=None,
    ):

        request = generated_plaid.BankTransferEventListRequest(
            self.client_id,
            self.secret,
            start_date,
            end_date,
            bank_transfer_id,
            account_id,
            bank_transfer_type,
            event_types,
            count,
            offset,
            origination_account_id,
            direction,
        )

        return self.client.handle_request(
            self.gen_api.bank_transfer_event_list,
            request,
        )

    def sync_events(self, after_id, count=None):

        request = generated_plaid.BankTransferEventSyncRequest(
            self.client_id,
            self.secret,
            after_id,
            count,
        )

        return self.client.handle_request(
            self.gen_api.bank_transfer_event_sync,
            request,
        )

    def get(self, bank_transfer_id):
        request = generated_plaid.BankTransferGetRequest(
            self.client_id,
            self.secret,
            bank_transfer_id,
        )

        return self.client.handle_request(
            self.gen_api.bank_transfer_get,
            request,
        )

    def list(
        self,
        start_date=None,
        end_date=None,
        count=None,
        offset=None,
        origination_account_id=None,
        direction=None,
    ):

        request = generated_plaid.BankTransferListRequest(
            self.client_id,
            self.secret,
            start_date,
            end_date,
            count,
            offset,
            origination_account_id,
            direction,
        )

        return self.client.handle_request(
            self.gen_api.bank_transfer_list,
            request,
        )

    def migrate_account(
        self,
        account_number,
        routing_number,
        account_type,
    ):

        request = generated_plaid.BankTransferMigrateAccountRequest(
            self.client_id,
            self.secret,
            account_number,
            routing_number,
            account_type,
        )

        return self.client.handle_request(
            self.gen_api.bank_transfer_migrate_account,
            request,
        )

    class Balance(API):
        def get(self, origination_account_id=None):
            request = generated_plaid.BankTransferBalanceGetRequest(
                self.client_id, self.secret, origination_account_id
            )

            return self.client.handle_request(
                self.gen_api.bank_transfer_balance_get,
                request,
            )


class Categories(API):
    """
    Categories endpoints.
    """

    def get(self):
        request = {}
        return self.client.handle_request(self.gen_api.categories_get, request)


class DepositSwitch(API):
    """
    Deposit Switch endpoints.
    """

    def get(self, deposit_switch_id):
        request = generated_plaid.DepositSwitchGetRequest(
            self.client_id,
            self.secret,
            deposit_switch_id,
        )

        return self.client.handle_request(
            self.gen_api.deposit_switch_get,
            request,
        )

    def create(self, target_account_id, target_access_token):
        request = generated_plaid.DepositSwitchCreateRequest(
            self.client_id,
            self.secret,
            target_access_token,
            target_account_id,
        )

        return self.client.handle_request(
            self.gen_api.deposit_switch_create,
            request,
        )

    def create_token(self, deposit_switch_id):
        request = generated_plaid.DepositSwitchTokenCreateRequest(
            self.client_id,
            self.secret,
            deposit_switch_id,
        )

        return self.client.handle_request(
            self.gen_api.deposit_switch_token_create,
            request,
        )


class Holdings(API):
    """
    Holdings endpoints.
    """

    def get(self, access_token, _options=None, account_ids=None):
        options = _options if _options else {}
        if account_ids is not None:
            options["account_ids"] = account_ids

        options = (
            generated_plaid.InvestmentsHoldingsGetRequestOptions(**options)
            if options
            else None
        )

        request = generated_plaid.InvestmentsHoldingsGetRequest(
            self.client_id,
            self.secret,
            access_token,
            options,
        )
        return self.client.handle_request(
            self.gen_api.investments_holdings_get,
            request,
        )


class Identity(API):
    """
    Identity endpoints.
    """

    def get(self, access_token):
        request = generated_plaid.IdentityGetRequest(
            self.client_id,
            self.secret,
            access_token,
        )
        return self.client.handle_request(
            self.gen_api.identity_get,
            request,
        )


class Institutions(API):
    """
    Institutions endpoints.
    """

    def get(
        self,
        country_codes,
        count,
        offset=0,
        _options=None,
        products=None,
        routing_numbers=None,
        oauth=None,
        include_optional_metadata=None,
    ):
        options = _options if _options else {}
        if products is not None:
            options["products"] = products
        if routing_numbers is not None:
            options["routing_numbers"] = routing_numbers
        if oauth is not None:
            options["oauth"] = oauth
        if include_optional_metadata is not None:
            options["include_optional_metadata"] = include_optional_metadata

        options = (
            generated_plaid.InstitutionsGetRequestOptions(**options)
            if options
            else None
        )

        request = generated_plaid.InstitutionsGetRequest(
            self.client_id,
            self.secret,
            count,
            offset,
            country_codes,
            options,
        )

        return self.client.handle_request(
            self.gen_api.institutions_get,
            request,
        )

    def get_by_id(
        self,
        institution_id,
        country_codes,
        _options=None,
        include_optional_metadata=None,
        include_status=None,
    ):
        options = _options or {}
        if include_optional_metadata is not None:
            options["include_optional_metadata"] = include_optional_metadata
        if include_status is not None:
            options["include_status"] = include_status

        options = (
            generated_plaid.InstitutionsGetByIdRequestOptions(**options)
            if options
            else None
        )

        request = generated_plaid.InstitutionsGetByIdRequest(
            self.client_id,
            self.secret,
            institution_id,
            country_codes,
            options,
        )

        return self.client.handle_request(
            self.gen_api.institutions_get_by_id,
            request,
        )

    def search(
        self,
        query,
        products,
        country_codes,
        _options=None,
        oauth=None,
        include_optional_metadata=None,
    ):
        options = _options if _options else {}
        if oauth is not None:
            options["oauth"] = oauth
        if include_optional_metadata is not None:
            options["include_optional_metadata"] = include_optional_metadata

        options = (
            generated_plaid.InstitutionsSearchRequestOptions(**options)
            if options
            else None
        )

        request = generated_plaid.InstitutionSearchRequest(
            self.client_id,
            self.secret,
            query,
            products,
            country_codes,
            options,
        )

        return self.client.handle_request(
            self.gen_api.institutions_search,
            request,
        )


class Item(API):
    """
    Item endpoints.

    """

    def __init__(self, client):
        super(Item, self).__init__(client)
        self.access_token = Item.AccessToken(client)
        self.public_token = Item.PublicToken(client)
        self.webhook = Item.Webhook(client)

    def get(self, access_token):
        request = generated_plaid.ItemGetRequest(
            self.client_id,
            self.secret,
            access_token,
        )
        return self.client.handle_request(
            self.gen_api.item_get,
            request,
        )

    def remove(self, access_token):
        request = generated_plaid.ItemRemoveRequest(
            self.client_id,
            self.secret,
            access_token,
        )
        return self.client.handle_request(
            self.gen_api.item_remove,
            request,
        )

    def import_item(self, products, user_auth, _options=None, webhook=None):
        options = _options if _options else {}
        if webhook is not None:
            options["webhook"] = webhook

        options = (
            generated_plaid.ItemImportRequestOptions(**options) if options else None
        )

        request = generated_plaid.ItemImportRequest(
            self.client_id,
            self.secret,
            products,
            user_auth,
            options,
        )
        return self.client.handle_request(
            self.gen_api.item_import,
            request,
        )

    class PublicToken(API):
        def exchange(self, public_token):
            request = generated_plaid.ItemPublicTokenExchangeRequest(
                self.client_id,
                self.secret,
                public_token,
            )
            return self.client.handle_request(
                self.gen_api.item_public_token_exchange,
                request,
            )

    class AccessToken(API):
        def invalidate(self, access_token):
            request = generated_plaid.ItemAccessTokenInvalidateRequest(
                self.client_id,
                self.secret,
                access_token,
            )
            return self.client.handle_request(
                self.gen_api.item_access_token_invalidate,
                request,
            )

    class Webhook(API):
        def update(self, access_token, webhook):
            request = generated_plaid.ItemWebhookUpdateRequest(
                self.client_id,
                self.secret,
                access_token,
                webhook,
            )
            return self.client.handle_request(
                self.gen_api.item_webhook_update,
                request,
            )


class InvestmentTransactions(API):
    """InvestmentTransactions endpoints."""

    def get(
        self,
        access_token,
        start_date,
        end_date,
        _options=None,
        account_ids=None,
        count=None,
        offset=None,
    ):
        options = _options if _options else {}
        if account_ids is not None:
            options["account_ids"] = account_ids
        if count is not None:
            options["count"] = count
        if offset is not None:
            options["offset"] = offset

        options = (
            generated_plaid.InvestmentsTransactionsGetRequestOptions(**options)
            if options
            else None
        )

        request = generated_plaid.InvestmentsTransactionsGetRequest(
            self.client_id,
            self.secret,
            access_token,
            start_date,
            end_date,
            options,
        )

        return self.client.handle_request(
            self.gen_api.investments_transactions_get,
            request,
        )


class Liabilities(API):
    """
    Liabilities endpoints.
    """

    def get(self, access_token, _options=None, account_ids=None):
        options = _options if _options else {}
        if account_ids is not None:
            options["account_ids"] = account_ids

        options = (
            generated_plaid.LiabilitiesGetRequestOptions(**options) if options else None
        )

        request = generated_plaid.LiabilitiesGetRequest(
            self.client_id, self.secret, access_token, options
        )

        return self.client.handle_request(
            self.gen_api.liabilities_get,
            request,
        )


class LinkToken(API):
    """Endpoints for managing link tokens."""

    def create(self, configs):
        configs["client_id"] = self.client_id
        configs["secret"] = self.secret
        request = generated_plaid.LinkTokenCreateRequest(**configs)

        return self.client.handle_request(
            self.gen_api.link_token_create,
            request,
        )

    def get(self, link_token):
        request = generated_plaid.LinkTokenGetRequest(
            self.client_id,
            self.secret,
            link_token,
        )

        return self.client.handle_request(
            self.gen_api.link_token_get,
            request,
        )


class PaymentInitiation(API):
    """Payment Initiation endpoints."""

    def create_recipient(self, name, iban, address, bacs):
        address = (
            generated_plaid.PaymentInitiationAddress(**address) if address else None
        )
        if bacs:
            bacs = generated_plaid.PaymentInitiationRecipientGetResponseBacs(
                bacs.get("account"),
                bacs.get("sort_code"),
            )
        request = generated_plaid.PaymentInitiationRecipientCreateRequest(
            self.client_id,
            self.secret,
            name,
            iban,
            bacs,
            address,
        )

        return self.client.handle_request(
            self.gen_api.payment_initiation_recipient_create,
            request,
        )

    def get_recipient(self, recipient_id):
        request = generated_plaid.PaymentInitiationRecipientGetRequest(
            self.client_id,
            self.secret,
            recipient_id,
        )

        return self.client.handle_request(
            self.gen_api.payment_initiation_recipient_get,
            request,
        )

    def list_recipients(self):
        request = generated_plaid.PaymentInitiationRecipientListRequest(
            self.client_id,
            self.secret,
        )

        return self.client.handle_request(
            self.gen_api.payment_initiation_recipient_list,
            request,
        )

    def create_payment(self, recipient_id, reference, amount, schedule=None):
        request = generated_plaid.PaymentInitiationPaymentCreateRequest(
            self.client_id,
            self.secret,
            recipient_id,
            reference,
            amount,
            schedule,
        )

        return self.client.handle_request(
            self.gen_api.payment_initiation_payment_create,
            request,
        )

    def get_payment(self, payment_id):
        request = generated_plaid.PaymentIntiationPaymentGetRequest(
            self.client_id,
            self.secret,
            payment_id,
        )

        return self.client.handle_request(
            self.gen_api.payment_intiation_payment_get,
            request,
        )

    def list_payments(self, count=None, cursor=None):
        request = generated_plaid.PaymentInitiationPaymentListRequest(
            self.client_id,
            self.secret,
            count,
            cursor,
        )

        return self.client.handle_request(
            self.gen_api.payment_initiation_payment_list, request
        )


class Processor(API):
    """Endpoints for creating processor tokens."""

    def token_create(self, access_token, account_id, processor):
        if processor == "stripe":
            return self.stripe_bank_account_token_create(access_token, account_id)
        elif processor == "apex":
            return self.apex_bank_account_token_create(access_token, account_id)
        else:
            request = generated_plaid.ProcessorTokenCreateRequest(
                self.client_id,
                self.secret,
                access_token,
                account_id,
                processor,
            )

            return self.client.handle_request(
                self.gen_api.processor_token_create, request
            )

    def stripe_bank_account_token_create(self, access_token, account_id):
        request = generated_plaid.ProcessorStripeBankAccountTokenCreateRequest(
            self.client_id,
            self.secret,
            access_token,
            account_id,
        )

        return self.client.handle_request(
            self.gen_api.processor_stripe_bank_account_token_create,
            request,
        )

    def dwolla_bank_account_token_create(self, access_token, account_id):
        return self.token_create(access_token, account_id, "dwolla")

    def apex_bank_account_token_create(self, access_token, account_id):
        request = generated_plaid.ProcessorApexProcessorTokenCreateRequest(
            self.client_id,
            self.secret,
            access_token,
            account_id,
        )

        return self.client.handle_request(
            self.gen_api.processor_apex_processor_token_create,
            request,
        )

    def auth_get(self, processor_token):
        request = generated_plaid.ProcessorAuthGetRequest(
            self.client_id,
            self.secret,
            processor_token,
        )

        return self.client.handle_request(
            self.gen_api.processor_auth_get,
            request,
        )

    def balance_get(self, processor_token):
        request = generated_plaid.ProcessorBalanceGetRequest(
            self.client_id,
            self.secret,
            processor_token,
        )

        return self.client.handle_request(
            self.gen_api.processor_balance_get,
            request,
        )

    def identity_get(self, processor_token):
        request = generated_plaid.ProcessorIdentityGetRequest(
            self.client_id,
            self.secret,
            processor_token,
        )

        return self.client.handle_request(
            self.gen_api.processor_identity_get,
            request,
        )


class Sandbox(API):
    """
    Sandbox-only endpoints.

    These endpoints may not be used in other environments.

    """

    def __init__(self, client: Client):
        super(Sandbox, self).__init__(client)
        self.bank_transfer = Sandbox.BankTransfer(client)
        self.item = Sandbox.Item(client)
        self.public_token = Sandbox.PublicToken(client)

    class BankTransfer(API):
        def simulate(self, bank_transfer_id, event_type, failure_reason=None):
            request = generated_plaid.SandboxBankTransferSimulateRequest(
                self.client_id,
                self.secret,
                bank_transfer_id,
                event_type,
                failure_reason,
            )

            return self.client.handle_request(
                self.gen_api.sandbox_bank_transfer_simulate,
                request,
            )

    class Item(API):
        """Sandbox item endpoints."""

        def reset_login(self, access_token):
            request = generated_plaid.SandboxItemResetLoginRequest(
                self.client_id,
                self.secret,
                access_token,
            )
            return self.client.handle_request(
                self.gen_api.sandbox_item_reset_login,
                request,
            )

        def fire_webhook(self, access_token, webhook_code):
            request = generated_plaid.SandboxItemFireWebhookRequest(
                self.client_id,
                self.secret,
                access_token,
                webhook_code,
            )
            return self.client.handle_request(
                self.gen_api.sandbox_item_fire_webhook,
                request,
            )

        def set_verification_status(
            self, access_token, account_id, verification_status
        ):
            request = generated_plaid.SandboxItemSetVerificationStatusRequest(
                self.client_id,
                self.secret,
                access_token,
                account_id,
                verification_status,
            )
            return self.client.handle_request(
                self.gen_api.sandbox_item_set_verification_status,
                request,
            )

    class PublicToken(API):
        """Sandbox public token endpoints."""

        def create(
            self,
            institution_id,
            initial_products,
            _options=None,
            webhook=None,
            override_username="user_good",
            override_password="pass_good",
            transactions__start_date=None,
            transactions__end_date=None,
        ):
            options = _options if _options else {}
            if webhook is not None:
                options["webhook"] = webhook
            if override_username is not None:
                options["override_username"] = override_username
            if override_password is not None:
                options["override_password"] = override_password
            if (
                transactions__start_date is not None
                or transactions__end_date is not None
            ):
                transactions = (
                    generated_plaid.SandboxPublicTokenCreateRequestOptionsTransactions(
                        transactions__start_date,
                        transactions__end_date,
                    )
                )
                options["transactions"] = transactions

            options = (
                generated_plaid.SandboxPublicTokenCreateRequestOptions(**options)
                if options
                else None
            )

            request = generated_plaid.SandboxPublicTokenCreateRequest(
                self.client_id,
                self.secret,
                institution_id,
                initial_products,
                options,
            )
            return self.client.handle_request(
                self.gen_api.sandbox_public_token_create,
                request,
            )


class Transactions(API):
    """Transactions endpoints."""

    def get(
        self,
        access_token,
        start_date,
        end_date,
        _options=None,
        account_ids=None,
        count=None,
        offset=None,
    ):
        options = _options if _options else {}
        if account_ids is not None:
            options["account_ids"] = account_ids if account_ids else None
        if count is not None:
            options["count"] = count
        if offset is not None:
            options["offset"] = offset

        options = (
            generated_plaid.TransactionsGetRequestOptions(**options)
            if options
            else None
        )

        request = generated_plaid.TransactionsGetRequest(
            self.client_id,
            options,
            access_token,
            self.secret,
            start_date,
            end_date,
        )

        return self.client.handle_request(
            self.gen_api.transactions_get,
            request,
        )

    def refresh(self, access_token):
        request = generated_plaid.TransactionsRefreshRequest(
            self.client_id,
            access_token,
            self.secret,
        )

        return self.client.handle_request(
            self.gen_api.transactions_refresh,
            request,
        )


class Webhooks(API):
    """
    Webhooks endpoints.
    """

    def get_verification_key(self, key_id):
        request = generated_plaid.WebhookVerificationKeyGetRequest(
            self.client_id,
            self.secret,
            key_id,
        )

        return self.client.handle_request(
            self.gen_api.webhook_verification_key_get,
            request,
        )
