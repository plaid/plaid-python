# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    <!--
    Prevent massive diffs on generated code.

    The version of the OpenAPI document: 2020-09-14_1.1.1
     -->
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class StudentLoan(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'account_id': 'str',
        'account_number': 'str',
        'disbursement_dates': 'list[str]',
        'expected_payoff_date': 'str',
        'guarantor': 'str',
        'interest_rate_percentage': 'float',
        'is_overdue': 'bool',
        'last_payment_amount': 'float',
        'last_payment_date': 'str',
        'last_statement_balance': 'float',
        'last_statement_issue_date': 'str',
        'loan_name': 'str',
        'loan_status': 'StudentLoanStatus',
        'minimum_payment_amount': 'float',
        'next_payment_due_date': 'str',
        'origination_date': 'str',
        'origination_principal_amount': 'float',
        'outstanding_interest_amount': 'float',
        'payment_reference_number': 'str',
        'pslf_status': 'PSLFStatus',
        'repayment_plan': 'StudentRepaymentPlan',
        'sequence_number': 'str',
        'servicer_address': 'ServicerAddressData',
        'ytd_interest_paid': 'float',
        'ytd_principal_paid': 'float'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account_number': 'account_number',
        'disbursement_dates': 'disbursement_dates',
        'expected_payoff_date': 'expected_payoff_date',
        'guarantor': 'guarantor',
        'interest_rate_percentage': 'interest_rate_percentage',
        'is_overdue': 'is_overdue',
        'last_payment_amount': 'last_payment_amount',
        'last_payment_date': 'last_payment_date',
        'last_statement_balance': 'last_statement_balance',
        'last_statement_issue_date': 'last_statement_issue_date',
        'loan_name': 'loan_name',
        'loan_status': 'loan_status',
        'minimum_payment_amount': 'minimum_payment_amount',
        'next_payment_due_date': 'next_payment_due_date',
        'origination_date': 'origination_date',
        'origination_principal_amount': 'origination_principal_amount',
        'outstanding_interest_amount': 'outstanding_interest_amount',
        'payment_reference_number': 'payment_reference_number',
        'pslf_status': 'pslf_status',
        'repayment_plan': 'repayment_plan',
        'sequence_number': 'sequence_number',
        'servicer_address': 'servicer_address',
        'ytd_interest_paid': 'ytd_interest_paid',
        'ytd_principal_paid': 'ytd_principal_paid'
    }

    def __init__(self, account_id=None, account_number=None, disbursement_dates=None, expected_payoff_date=None, guarantor=None, interest_rate_percentage=None, is_overdue=None, last_payment_amount=None, last_payment_date=None, last_statement_balance=None, last_statement_issue_date=None, loan_name=None, loan_status=None, minimum_payment_amount=None, next_payment_due_date=None, origination_date=None, origination_principal_amount=None, outstanding_interest_amount=None, payment_reference_number=None, pslf_status=None, repayment_plan=None, sequence_number=None, servicer_address=None, ytd_interest_paid=None, ytd_principal_paid=None, local_vars_configuration=None):  # noqa: E501
        """StudentLoan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._account_number = None
        self._disbursement_dates = None
        self._expected_payoff_date = None
        self._guarantor = None
        self._interest_rate_percentage = None
        self._is_overdue = None
        self._last_payment_amount = None
        self._last_payment_date = None
        self._last_statement_balance = None
        self._last_statement_issue_date = None
        self._loan_name = None
        self._loan_status = None
        self._minimum_payment_amount = None
        self._next_payment_due_date = None
        self._origination_date = None
        self._origination_principal_amount = None
        self._outstanding_interest_amount = None
        self._payment_reference_number = None
        self._pslf_status = None
        self._repayment_plan = None
        self._sequence_number = None
        self._servicer_address = None
        self._ytd_interest_paid = None
        self._ytd_principal_paid = None
        self.discriminator = None

        self.account_id = account_id
        self.account_number = account_number
        self.disbursement_dates = disbursement_dates
        self.expected_payoff_date = expected_payoff_date
        self.guarantor = guarantor
        if interest_rate_percentage is not None:
            self.interest_rate_percentage = interest_rate_percentage
        self.is_overdue = is_overdue
        self.last_payment_amount = last_payment_amount
        self.last_payment_date = last_payment_date
        self.last_statement_balance = last_statement_balance
        self.last_statement_issue_date = last_statement_issue_date
        self.loan_name = loan_name
        if loan_status is not None:
            self.loan_status = loan_status
        self.minimum_payment_amount = minimum_payment_amount
        self.next_payment_due_date = next_payment_due_date
        self.origination_date = origination_date
        self.origination_principal_amount = origination_principal_amount
        self.outstanding_interest_amount = outstanding_interest_amount
        self.payment_reference_number = payment_reference_number
        if pslf_status is not None:
            self.pslf_status = pslf_status
        if repayment_plan is not None:
            self.repayment_plan = repayment_plan
        self.sequence_number = sequence_number
        if servicer_address is not None:
            self.servicer_address = servicer_address
        self.ytd_interest_paid = ytd_interest_paid
        self.ytd_principal_paid = ytd_principal_paid

    @property
    def account_id(self):
        """Gets the account_id of this StudentLoan.  # noqa: E501

        The ID of the account that this liability belongs to.  # noqa: E501

        :return: The account_id of this StudentLoan.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this StudentLoan.

        The ID of the account that this liability belongs to.  # noqa: E501

        :param account_id: The account_id of this StudentLoan.  # noqa: E501
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def account_number(self):
        """Gets the account_number of this StudentLoan.  # noqa: E501

        The account number of the loan.  # noqa: E501

        :return: The account_number of this StudentLoan.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this StudentLoan.

        The account number of the loan.  # noqa: E501

        :param account_number: The account_number of this StudentLoan.  # noqa: E501
        :type account_number: str
        """

        self._account_number = account_number

    @property
    def disbursement_dates(self):
        """Gets the disbursement_dates of this StudentLoan.  # noqa: E501

        The dates on which loaned funds were disbursed or will be disbursed. These are often in the past. Dates are returned in an ISO 8601 format (YYYY-MM-DD).  # noqa: E501

        :return: The disbursement_dates of this StudentLoan.  # noqa: E501
        :rtype: list[str]
        """
        return self._disbursement_dates

    @disbursement_dates.setter
    def disbursement_dates(self, disbursement_dates):
        """Sets the disbursement_dates of this StudentLoan.

        The dates on which loaned funds were disbursed or will be disbursed. These are often in the past. Dates are returned in an ISO 8601 format (YYYY-MM-DD).  # noqa: E501

        :param disbursement_dates: The disbursement_dates of this StudentLoan.  # noqa: E501
        :type disbursement_dates: list[str]
        """

        self._disbursement_dates = disbursement_dates

    @property
    def expected_payoff_date(self):
        """Gets the expected_payoff_date of this StudentLoan.  # noqa: E501

        The date when the student loan is expected to be paid off. Availability for this field is limited. Dates are returned in an ISO 8601 format (YYYY-MM-DD).  # noqa: E501

        :return: The expected_payoff_date of this StudentLoan.  # noqa: E501
        :rtype: str
        """
        return self._expected_payoff_date

    @expected_payoff_date.setter
    def expected_payoff_date(self, expected_payoff_date):
        """Sets the expected_payoff_date of this StudentLoan.

        The date when the student loan is expected to be paid off. Availability for this field is limited. Dates are returned in an ISO 8601 format (YYYY-MM-DD).  # noqa: E501

        :param expected_payoff_date: The expected_payoff_date of this StudentLoan.  # noqa: E501
        :type expected_payoff_date: str
        """

        self._expected_payoff_date = expected_payoff_date

    @property
    def guarantor(self):
        """Gets the guarantor of this StudentLoan.  # noqa: E501

        The guarantor of the student loan.  # noqa: E501

        :return: The guarantor of this StudentLoan.  # noqa: E501
        :rtype: str
        """
        return self._guarantor

    @guarantor.setter
    def guarantor(self, guarantor):
        """Sets the guarantor of this StudentLoan.

        The guarantor of the student loan.  # noqa: E501

        :param guarantor: The guarantor of this StudentLoan.  # noqa: E501
        :type guarantor: str
        """

        self._guarantor = guarantor

    @property
    def interest_rate_percentage(self):
        """Gets the interest_rate_percentage of this StudentLoan.  # noqa: E501

        The interest rate on the loan as a percentage.  # noqa: E501

        :return: The interest_rate_percentage of this StudentLoan.  # noqa: E501
        :rtype: float
        """
        return self._interest_rate_percentage

    @interest_rate_percentage.setter
    def interest_rate_percentage(self, interest_rate_percentage):
        """Sets the interest_rate_percentage of this StudentLoan.

        The interest rate on the loan as a percentage.  # noqa: E501

        :param interest_rate_percentage: The interest_rate_percentage of this StudentLoan.  # noqa: E501
        :type interest_rate_percentage: float
        """

        self._interest_rate_percentage = interest_rate_percentage

    @property
    def is_overdue(self):
        """Gets the is_overdue of this StudentLoan.  # noqa: E501

        `true` if a payment is currently overdue. Availability for this field is limited.  # noqa: E501

        :return: The is_overdue of this StudentLoan.  # noqa: E501
        :rtype: bool
        """
        return self._is_overdue

    @is_overdue.setter
    def is_overdue(self, is_overdue):
        """Sets the is_overdue of this StudentLoan.

        `true` if a payment is currently overdue. Availability for this field is limited.  # noqa: E501

        :param is_overdue: The is_overdue of this StudentLoan.  # noqa: E501
        :type is_overdue: bool
        """

        self._is_overdue = is_overdue

    @property
    def last_payment_amount(self):
        """Gets the last_payment_amount of this StudentLoan.  # noqa: E501

        The amount of the last payment.  # noqa: E501

        :return: The last_payment_amount of this StudentLoan.  # noqa: E501
        :rtype: float
        """
        return self._last_payment_amount

    @last_payment_amount.setter
    def last_payment_amount(self, last_payment_amount):
        """Sets the last_payment_amount of this StudentLoan.

        The amount of the last payment.  # noqa: E501

        :param last_payment_amount: The last_payment_amount of this StudentLoan.  # noqa: E501
        :type last_payment_amount: float
        """

        self._last_payment_amount = last_payment_amount

    @property
    def last_payment_date(self):
        """Gets the last_payment_date of this StudentLoan.  # noqa: E501

        The date of the last payment. Dates are returned in an ISO 8601 format (YYYY-MM-DD).  # noqa: E501

        :return: The last_payment_date of this StudentLoan.  # noqa: E501
        :rtype: str
        """
        return self._last_payment_date

    @last_payment_date.setter
    def last_payment_date(self, last_payment_date):
        """Sets the last_payment_date of this StudentLoan.

        The date of the last payment. Dates are returned in an ISO 8601 format (YYYY-MM-DD).  # noqa: E501

        :param last_payment_date: The last_payment_date of this StudentLoan.  # noqa: E501
        :type last_payment_date: str
        """

        self._last_payment_date = last_payment_date

    @property
    def last_statement_balance(self):
        """Gets the last_statement_balance of this StudentLoan.  # noqa: E501

        The outstanding balance on the last statement. This field could also be interpreted as the next payment due. Availability for this field is limited.   # noqa: E501

        :return: The last_statement_balance of this StudentLoan.  # noqa: E501
        :rtype: float
        """
        return self._last_statement_balance

    @last_statement_balance.setter
    def last_statement_balance(self, last_statement_balance):
        """Sets the last_statement_balance of this StudentLoan.

        The outstanding balance on the last statement. This field could also be interpreted as the next payment due. Availability for this field is limited.   # noqa: E501

        :param last_statement_balance: The last_statement_balance of this StudentLoan.  # noqa: E501
        :type last_statement_balance: float
        """

        self._last_statement_balance = last_statement_balance

    @property
    def last_statement_issue_date(self):
        """Gets the last_statement_issue_date of this StudentLoan.  # noqa: E501

        The date of the last statement. Dates are returned in an ISO 8601 format (YYYY-MM-DD).  # noqa: E501

        :return: The last_statement_issue_date of this StudentLoan.  # noqa: E501
        :rtype: str
        """
        return self._last_statement_issue_date

    @last_statement_issue_date.setter
    def last_statement_issue_date(self, last_statement_issue_date):
        """Sets the last_statement_issue_date of this StudentLoan.

        The date of the last statement. Dates are returned in an ISO 8601 format (YYYY-MM-DD).  # noqa: E501

        :param last_statement_issue_date: The last_statement_issue_date of this StudentLoan.  # noqa: E501
        :type last_statement_issue_date: str
        """

        self._last_statement_issue_date = last_statement_issue_date

    @property
    def loan_name(self):
        """Gets the loan_name of this StudentLoan.  # noqa: E501

        The type of loan, e.g., \"Consolidation Loans\".  # noqa: E501

        :return: The loan_name of this StudentLoan.  # noqa: E501
        :rtype: str
        """
        return self._loan_name

    @loan_name.setter
    def loan_name(self, loan_name):
        """Sets the loan_name of this StudentLoan.

        The type of loan, e.g., \"Consolidation Loans\".  # noqa: E501

        :param loan_name: The loan_name of this StudentLoan.  # noqa: E501
        :type loan_name: str
        """

        self._loan_name = loan_name

    @property
    def loan_status(self):
        """Gets the loan_status of this StudentLoan.  # noqa: E501


        :return: The loan_status of this StudentLoan.  # noqa: E501
        :rtype: StudentLoanStatus
        """
        return self._loan_status

    @loan_status.setter
    def loan_status(self, loan_status):
        """Sets the loan_status of this StudentLoan.


        :param loan_status: The loan_status of this StudentLoan.  # noqa: E501
        :type loan_status: StudentLoanStatus
        """

        self._loan_status = loan_status

    @property
    def minimum_payment_amount(self):
        """Gets the minimum_payment_amount of this StudentLoan.  # noqa: E501

        The minimum payment due for the next billing cycle. There are some exceptions: Some institutions require a minimum payment across all loans associated with an account number. Our API presents that same minimum payment amount on each loan. The institutions that do this are: Great Lakes ( `ins_116861`), Firstmark (`ins_116295`), Commonbond Firstmark Services (`ins_116950`), Nelnet (`ins_116528`), EdFinancial Services (`ins_116304`), Granite State (`ins_116308`), and Oklahoma Student Loan Authority (`ins_116945`). Firstmark (`ins_116295` ) will display as $0 if there is an autopay program in effect.  # noqa: E501

        :return: The minimum_payment_amount of this StudentLoan.  # noqa: E501
        :rtype: float
        """
        return self._minimum_payment_amount

    @minimum_payment_amount.setter
    def minimum_payment_amount(self, minimum_payment_amount):
        """Sets the minimum_payment_amount of this StudentLoan.

        The minimum payment due for the next billing cycle. There are some exceptions: Some institutions require a minimum payment across all loans associated with an account number. Our API presents that same minimum payment amount on each loan. The institutions that do this are: Great Lakes ( `ins_116861`), Firstmark (`ins_116295`), Commonbond Firstmark Services (`ins_116950`), Nelnet (`ins_116528`), EdFinancial Services (`ins_116304`), Granite State (`ins_116308`), and Oklahoma Student Loan Authority (`ins_116945`). Firstmark (`ins_116295` ) will display as $0 if there is an autopay program in effect.  # noqa: E501

        :param minimum_payment_amount: The minimum_payment_amount of this StudentLoan.  # noqa: E501
        :type minimum_payment_amount: float
        """

        self._minimum_payment_amount = minimum_payment_amount

    @property
    def next_payment_due_date(self):
        """Gets the next_payment_due_date of this StudentLoan.  # noqa: E501

        The due date for the next payment. The due date is `null` if a payment is not expected. A payment is not expected if `loan_status.type` is `deferment`, `in_school`, `consolidated`, `paid in full`, or `transferred`. Dates are returned in an ISO 8601 format (YYYY-MM-DD).  # noqa: E501

        :return: The next_payment_due_date of this StudentLoan.  # noqa: E501
        :rtype: str
        """
        return self._next_payment_due_date

    @next_payment_due_date.setter
    def next_payment_due_date(self, next_payment_due_date):
        """Sets the next_payment_due_date of this StudentLoan.

        The due date for the next payment. The due date is `null` if a payment is not expected. A payment is not expected if `loan_status.type` is `deferment`, `in_school`, `consolidated`, `paid in full`, or `transferred`. Dates are returned in an ISO 8601 format (YYYY-MM-DD).  # noqa: E501

        :param next_payment_due_date: The next_payment_due_date of this StudentLoan.  # noqa: E501
        :type next_payment_due_date: str
        """

        self._next_payment_due_date = next_payment_due_date

    @property
    def origination_date(self):
        """Gets the origination_date of this StudentLoan.  # noqa: E501

        The date on which the loan was initially lent. Dates are returned in an ISO 8601 format (YYYY-MM-DD).   # noqa: E501

        :return: The origination_date of this StudentLoan.  # noqa: E501
        :rtype: str
        """
        return self._origination_date

    @origination_date.setter
    def origination_date(self, origination_date):
        """Sets the origination_date of this StudentLoan.

        The date on which the loan was initially lent. Dates are returned in an ISO 8601 format (YYYY-MM-DD).   # noqa: E501

        :param origination_date: The origination_date of this StudentLoan.  # noqa: E501
        :type origination_date: str
        """

        self._origination_date = origination_date

    @property
    def origination_principal_amount(self):
        """Gets the origination_principal_amount of this StudentLoan.  # noqa: E501

        The original principal balance of the loan.  # noqa: E501

        :return: The origination_principal_amount of this StudentLoan.  # noqa: E501
        :rtype: float
        """
        return self._origination_principal_amount

    @origination_principal_amount.setter
    def origination_principal_amount(self, origination_principal_amount):
        """Sets the origination_principal_amount of this StudentLoan.

        The original principal balance of the loan.  # noqa: E501

        :param origination_principal_amount: The origination_principal_amount of this StudentLoan.  # noqa: E501
        :type origination_principal_amount: float
        """

        self._origination_principal_amount = origination_principal_amount

    @property
    def outstanding_interest_amount(self):
        """Gets the outstanding_interest_amount of this StudentLoan.  # noqa: E501

        The total dollar amount of the accrued interest balance. For Sallie Mae ( `ins_116944`), this amount is included in the current balance of the loan, so this field will return as `null`.  # noqa: E501

        :return: The outstanding_interest_amount of this StudentLoan.  # noqa: E501
        :rtype: float
        """
        return self._outstanding_interest_amount

    @outstanding_interest_amount.setter
    def outstanding_interest_amount(self, outstanding_interest_amount):
        """Sets the outstanding_interest_amount of this StudentLoan.

        The total dollar amount of the accrued interest balance. For Sallie Mae ( `ins_116944`), this amount is included in the current balance of the loan, so this field will return as `null`.  # noqa: E501

        :param outstanding_interest_amount: The outstanding_interest_amount of this StudentLoan.  # noqa: E501
        :type outstanding_interest_amount: float
        """

        self._outstanding_interest_amount = outstanding_interest_amount

    @property
    def payment_reference_number(self):
        """Gets the payment_reference_number of this StudentLoan.  # noqa: E501

        The relevant account number that should be used to reference this loan for payments. In the majority of cases, `payment_reference_number` will match a`ccount_number,` but in some institutions, such as Great Lakes (`ins_116861`), it will be different.  # noqa: E501

        :return: The payment_reference_number of this StudentLoan.  # noqa: E501
        :rtype: str
        """
        return self._payment_reference_number

    @payment_reference_number.setter
    def payment_reference_number(self, payment_reference_number):
        """Sets the payment_reference_number of this StudentLoan.

        The relevant account number that should be used to reference this loan for payments. In the majority of cases, `payment_reference_number` will match a`ccount_number,` but in some institutions, such as Great Lakes (`ins_116861`), it will be different.  # noqa: E501

        :param payment_reference_number: The payment_reference_number of this StudentLoan.  # noqa: E501
        :type payment_reference_number: str
        """

        self._payment_reference_number = payment_reference_number

    @property
    def pslf_status(self):
        """Gets the pslf_status of this StudentLoan.  # noqa: E501


        :return: The pslf_status of this StudentLoan.  # noqa: E501
        :rtype: PSLFStatus
        """
        return self._pslf_status

    @pslf_status.setter
    def pslf_status(self, pslf_status):
        """Sets the pslf_status of this StudentLoan.


        :param pslf_status: The pslf_status of this StudentLoan.  # noqa: E501
        :type pslf_status: PSLFStatus
        """

        self._pslf_status = pslf_status

    @property
    def repayment_plan(self):
        """Gets the repayment_plan of this StudentLoan.  # noqa: E501


        :return: The repayment_plan of this StudentLoan.  # noqa: E501
        :rtype: StudentRepaymentPlan
        """
        return self._repayment_plan

    @repayment_plan.setter
    def repayment_plan(self, repayment_plan):
        """Sets the repayment_plan of this StudentLoan.


        :param repayment_plan: The repayment_plan of this StudentLoan.  # noqa: E501
        :type repayment_plan: StudentRepaymentPlan
        """

        self._repayment_plan = repayment_plan

    @property
    def sequence_number(self):
        """Gets the sequence_number of this StudentLoan.  # noqa: E501

        The sequence number of the student loan. Heartland ECSI (`ins_116948`) does not make this field available.  # noqa: E501

        :return: The sequence_number of this StudentLoan.  # noqa: E501
        :rtype: str
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this StudentLoan.

        The sequence number of the student loan. Heartland ECSI (`ins_116948`) does not make this field available.  # noqa: E501

        :param sequence_number: The sequence_number of this StudentLoan.  # noqa: E501
        :type sequence_number: str
        """

        self._sequence_number = sequence_number

    @property
    def servicer_address(self):
        """Gets the servicer_address of this StudentLoan.  # noqa: E501


        :return: The servicer_address of this StudentLoan.  # noqa: E501
        :rtype: ServicerAddressData
        """
        return self._servicer_address

    @servicer_address.setter
    def servicer_address(self, servicer_address):
        """Sets the servicer_address of this StudentLoan.


        :param servicer_address: The servicer_address of this StudentLoan.  # noqa: E501
        :type servicer_address: ServicerAddressData
        """

        self._servicer_address = servicer_address

    @property
    def ytd_interest_paid(self):
        """Gets the ytd_interest_paid of this StudentLoan.  # noqa: E501

        The year to date (YTD) interest paid. Availability for this field is limited.  # noqa: E501

        :return: The ytd_interest_paid of this StudentLoan.  # noqa: E501
        :rtype: float
        """
        return self._ytd_interest_paid

    @ytd_interest_paid.setter
    def ytd_interest_paid(self, ytd_interest_paid):
        """Sets the ytd_interest_paid of this StudentLoan.

        The year to date (YTD) interest paid. Availability for this field is limited.  # noqa: E501

        :param ytd_interest_paid: The ytd_interest_paid of this StudentLoan.  # noqa: E501
        :type ytd_interest_paid: float
        """

        self._ytd_interest_paid = ytd_interest_paid

    @property
    def ytd_principal_paid(self):
        """Gets the ytd_principal_paid of this StudentLoan.  # noqa: E501

        The year to date (YTD) principal paid. Availability for this field is limited.  # noqa: E501

        :return: The ytd_principal_paid of this StudentLoan.  # noqa: E501
        :rtype: float
        """
        return self._ytd_principal_paid

    @ytd_principal_paid.setter
    def ytd_principal_paid(self, ytd_principal_paid):
        """Sets the ytd_principal_paid of this StudentLoan.

        The year to date (YTD) principal paid. Availability for this field is limited.  # noqa: E501

        :param ytd_principal_paid: The ytd_principal_paid of this StudentLoan.  # noqa: E501
        :type ytd_principal_paid: float
        """

        self._ytd_principal_paid = ytd_principal_paid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StudentLoan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StudentLoan):
            return True

        return self.to_dict() != other.to_dict()
