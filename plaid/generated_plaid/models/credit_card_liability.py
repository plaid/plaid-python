# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class CreditCardLiability(object):
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
        'aprs': 'list[APR]',
        'is_overdue': 'bool',
        'last_payment_amount': 'float',
        'last_payment_date': 'str',
        'last_statement_balance': 'float',
        'last_statement_issue_date': 'str',
        'minimum_payment_amount': 'float',
        'next_payment_due_date': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'aprs': 'aprs',
        'is_overdue': 'is_overdue',
        'last_payment_amount': 'last_payment_amount',
        'last_payment_date': 'last_payment_date',
        'last_statement_balance': 'last_statement_balance',
        'last_statement_issue_date': 'last_statement_issue_date',
        'minimum_payment_amount': 'minimum_payment_amount',
        'next_payment_due_date': 'next_payment_due_date'
    }

    def __init__(self, account_id=None, aprs=None, is_overdue=None, last_payment_amount=None, last_payment_date=None, last_statement_balance=None, last_statement_issue_date=None, minimum_payment_amount=None, next_payment_due_date=None, local_vars_configuration=None):  # noqa: E501
        """CreditCardLiability - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._aprs = None
        self._is_overdue = None
        self._last_payment_amount = None
        self._last_payment_date = None
        self._last_statement_balance = None
        self._last_statement_issue_date = None
        self._minimum_payment_amount = None
        self._next_payment_due_date = None
        self.discriminator = None

        self.account_id = account_id
        if aprs is not None:
            self.aprs = aprs
        self.is_overdue = is_overdue
        if last_payment_amount is not None:
            self.last_payment_amount = last_payment_amount
        if last_payment_date is not None:
            self.last_payment_date = last_payment_date
        if last_statement_balance is not None:
            self.last_statement_balance = last_statement_balance
        if last_statement_issue_date is not None:
            self.last_statement_issue_date = last_statement_issue_date
        if minimum_payment_amount is not None:
            self.minimum_payment_amount = minimum_payment_amount
        if next_payment_due_date is not None:
            self.next_payment_due_date = next_payment_due_date

    @property
    def account_id(self):
        """Gets the account_id of this CreditCardLiability.  # noqa: E501

        The ID of the account that this liability belongs to.  # noqa: E501

        :return: The account_id of this CreditCardLiability.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CreditCardLiability.

        The ID of the account that this liability belongs to.  # noqa: E501

        :param account_id: The account_id of this CreditCardLiability.  # noqa: E501
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def aprs(self):
        """Gets the aprs of this CreditCardLiability.  # noqa: E501

        The various interest rates that apply to the account.  # noqa: E501

        :return: The aprs of this CreditCardLiability.  # noqa: E501
        :rtype: list[APR]
        """
        return self._aprs

    @aprs.setter
    def aprs(self, aprs):
        """Sets the aprs of this CreditCardLiability.

        The various interest rates that apply to the account.  # noqa: E501

        :param aprs: The aprs of this CreditCardLiability.  # noqa: E501
        :type aprs: list[APR]
        """

        self._aprs = aprs

    @property
    def is_overdue(self):
        """Gets the is_overdue of this CreditCardLiability.  # noqa: E501

        true if a payment is currently overdue. Availability for this field is limited.  # noqa: E501

        :return: The is_overdue of this CreditCardLiability.  # noqa: E501
        :rtype: bool
        """
        return self._is_overdue

    @is_overdue.setter
    def is_overdue(self, is_overdue):
        """Sets the is_overdue of this CreditCardLiability.

        true if a payment is currently overdue. Availability for this field is limited.  # noqa: E501

        :param is_overdue: The is_overdue of this CreditCardLiability.  # noqa: E501
        :type is_overdue: bool
        """

        self._is_overdue = is_overdue

    @property
    def last_payment_amount(self):
        """Gets the last_payment_amount of this CreditCardLiability.  # noqa: E501

        The amount of the last payment.  # noqa: E501

        :return: The last_payment_amount of this CreditCardLiability.  # noqa: E501
        :rtype: float
        """
        return self._last_payment_amount

    @last_payment_amount.setter
    def last_payment_amount(self, last_payment_amount):
        """Sets the last_payment_amount of this CreditCardLiability.

        The amount of the last payment.  # noqa: E501

        :param last_payment_amount: The last_payment_amount of this CreditCardLiability.  # noqa: E501
        :type last_payment_amount: float
        """

        self._last_payment_amount = last_payment_amount

    @property
    def last_payment_date(self):
        """Gets the last_payment_date of this CreditCardLiability.  # noqa: E501

        The date of the last payment. Dates are returned in an ISO 8601 format (YYYY-MM-DD). Availability for this field is limited.  # noqa: E501

        :return: The last_payment_date of this CreditCardLiability.  # noqa: E501
        :rtype: str
        """
        return self._last_payment_date

    @last_payment_date.setter
    def last_payment_date(self, last_payment_date):
        """Sets the last_payment_date of this CreditCardLiability.

        The date of the last payment. Dates are returned in an ISO 8601 format (YYYY-MM-DD). Availability for this field is limited.  # noqa: E501

        :param last_payment_date: The last_payment_date of this CreditCardLiability.  # noqa: E501
        :type last_payment_date: str
        """

        self._last_payment_date = last_payment_date

    @property
    def last_statement_balance(self):
        """Gets the last_statement_balance of this CreditCardLiability.  # noqa: E501

        The outstanding balance on the last statement. Availability for this field is limited.  # noqa: E501

        :return: The last_statement_balance of this CreditCardLiability.  # noqa: E501
        :rtype: float
        """
        return self._last_statement_balance

    @last_statement_balance.setter
    def last_statement_balance(self, last_statement_balance):
        """Sets the last_statement_balance of this CreditCardLiability.

        The outstanding balance on the last statement. Availability for this field is limited.  # noqa: E501

        :param last_statement_balance: The last_statement_balance of this CreditCardLiability.  # noqa: E501
        :type last_statement_balance: float
        """

        self._last_statement_balance = last_statement_balance

    @property
    def last_statement_issue_date(self):
        """Gets the last_statement_issue_date of this CreditCardLiability.  # noqa: E501

        The date of the last statement. Dates are returned in an ISO 8601 format (YYYY-MM-DD).  # noqa: E501

        :return: The last_statement_issue_date of this CreditCardLiability.  # noqa: E501
        :rtype: str
        """
        return self._last_statement_issue_date

    @last_statement_issue_date.setter
    def last_statement_issue_date(self, last_statement_issue_date):
        """Sets the last_statement_issue_date of this CreditCardLiability.

        The date of the last statement. Dates are returned in an ISO 8601 format (YYYY-MM-DD).  # noqa: E501

        :param last_statement_issue_date: The last_statement_issue_date of this CreditCardLiability.  # noqa: E501
        :type last_statement_issue_date: str
        """

        self._last_statement_issue_date = last_statement_issue_date

    @property
    def minimum_payment_amount(self):
        """Gets the minimum_payment_amount of this CreditCardLiability.  # noqa: E501

        The minimum payment due for the next billing cycle.  # noqa: E501

        :return: The minimum_payment_amount of this CreditCardLiability.  # noqa: E501
        :rtype: float
        """
        return self._minimum_payment_amount

    @minimum_payment_amount.setter
    def minimum_payment_amount(self, minimum_payment_amount):
        """Sets the minimum_payment_amount of this CreditCardLiability.

        The minimum payment due for the next billing cycle.  # noqa: E501

        :param minimum_payment_amount: The minimum_payment_amount of this CreditCardLiability.  # noqa: E501
        :type minimum_payment_amount: float
        """

        self._minimum_payment_amount = minimum_payment_amount

    @property
    def next_payment_due_date(self):
        """Gets the next_payment_due_date of this CreditCardLiability.  # noqa: E501

        The due date for the next payment. The due date is `null` if a payment is not expected. Dates are returned in an ISO 8601 format (YYYY-MM-DD).  # noqa: E501

        :return: The next_payment_due_date of this CreditCardLiability.  # noqa: E501
        :rtype: str
        """
        return self._next_payment_due_date

    @next_payment_due_date.setter
    def next_payment_due_date(self, next_payment_due_date):
        """Sets the next_payment_due_date of this CreditCardLiability.

        The due date for the next payment. The due date is `null` if a payment is not expected. Dates are returned in an ISO 8601 format (YYYY-MM-DD).  # noqa: E501

        :param next_payment_due_date: The next_payment_due_date of this CreditCardLiability.  # noqa: E501
        :type next_payment_due_date: str
        """

        self._next_payment_due_date = next_payment_due_date

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
        if not isinstance(other, CreditCardLiability):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreditCardLiability):
            return True

        return self.to_dict() != other.to_dict()
