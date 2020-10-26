# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.0.9
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class InvestmentTransaction(object):
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
        'investment_transaction_id': 'str',
        'account_id': 'str',
        'security_id': 'str',
        'date': 'str',
        'name': 'str',
        'quantity': 'float',
        'amount': 'float',
        'price': 'float',
        'fees': 'float',
        'type': 'str',
        'subtype': 'StandaloneInvestmentTransactionSubtype',
        'iso_currency_code': 'str',
        'unofficial_currency_code': 'str'
    }

    attribute_map = {
        'investment_transaction_id': 'investment_transaction_id',
        'account_id': 'account_id',
        'security_id': 'security_id',
        'date': 'date',
        'name': 'name',
        'quantity': 'quantity',
        'amount': 'amount',
        'price': 'price',
        'fees': 'fees',
        'type': 'type',
        'subtype': 'subtype',
        'iso_currency_code': 'iso_currency_code',
        'unofficial_currency_code': 'unofficial_currency_code'
    }

    def __init__(self, investment_transaction_id=None, account_id=None, security_id=None, date=None, name=None, quantity=None, amount=None, price=None, fees=None, type=None, subtype=None, iso_currency_code=None, unofficial_currency_code=None, local_vars_configuration=None):  # noqa: E501
        """InvestmentTransaction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._investment_transaction_id = None
        self._account_id = None
        self._security_id = None
        self._date = None
        self._name = None
        self._quantity = None
        self._amount = None
        self._price = None
        self._fees = None
        self._type = None
        self._subtype = None
        self._iso_currency_code = None
        self._unofficial_currency_code = None
        self.discriminator = None

        if investment_transaction_id is not None:
            self.investment_transaction_id = investment_transaction_id
        if account_id is not None:
            self.account_id = account_id
        self.security_id = security_id
        if date is not None:
            self.date = date
        if name is not None:
            self.name = name
        if quantity is not None:
            self.quantity = quantity
        if amount is not None:
            self.amount = amount
        if price is not None:
            self.price = price
        self.fees = fees
        if type is not None:
            self.type = type
        if subtype is not None:
            self.subtype = subtype
        self.iso_currency_code = iso_currency_code
        self.unofficial_currency_code = unofficial_currency_code

    @property
    def investment_transaction_id(self):
        """Gets the investment_transaction_id of this InvestmentTransaction.  # noqa: E501

        The ID of the Investment transaction, unique across all Plaid transactions. Like all Plaid identifiers, the `investment_transaction_id` is case sensitive.  # noqa: E501

        :return: The investment_transaction_id of this InvestmentTransaction.  # noqa: E501
        :rtype: str
        """
        return self._investment_transaction_id

    @investment_transaction_id.setter
    def investment_transaction_id(self, investment_transaction_id):
        """Sets the investment_transaction_id of this InvestmentTransaction.

        The ID of the Investment transaction, unique across all Plaid transactions. Like all Plaid identifiers, the `investment_transaction_id` is case sensitive.  # noqa: E501

        :param investment_transaction_id: The investment_transaction_id of this InvestmentTransaction.  # noqa: E501
        :type investment_transaction_id: str
        """

        self._investment_transaction_id = investment_transaction_id

    @property
    def account_id(self):
        """Gets the account_id of this InvestmentTransaction.  # noqa: E501

        The `account_id` of the account against which this transaction posted.  # noqa: E501

        :return: The account_id of this InvestmentTransaction.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InvestmentTransaction.

        The `account_id` of the account against which this transaction posted.  # noqa: E501

        :param account_id: The account_id of this InvestmentTransaction.  # noqa: E501
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def security_id(self):
        """Gets the security_id of this InvestmentTransaction.  # noqa: E501

        The `security_id` to which this transaction is related.  # noqa: E501

        :return: The security_id of this InvestmentTransaction.  # noqa: E501
        :rtype: str
        """
        return self._security_id

    @security_id.setter
    def security_id(self, security_id):
        """Sets the security_id of this InvestmentTransaction.

        The `security_id` to which this transaction is related.  # noqa: E501

        :param security_id: The security_id of this InvestmentTransaction.  # noqa: E501
        :type security_id: str
        """

        self._security_id = security_id

    @property
    def date(self):
        """Gets the date of this InvestmentTransaction.  # noqa: E501

        The ISO-8601 posting date for the transaction, or transacted date for pending transactions.  # noqa: E501

        :return: The date of this InvestmentTransaction.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this InvestmentTransaction.

        The ISO-8601 posting date for the transaction, or transacted date for pending transactions.  # noqa: E501

        :param date: The date of this InvestmentTransaction.  # noqa: E501
        :type date: str
        """

        self._date = date

    @property
    def name(self):
        """Gets the name of this InvestmentTransaction.  # noqa: E501

        The institution’s description of the transaction.  # noqa: E501

        :return: The name of this InvestmentTransaction.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InvestmentTransaction.

        The institution’s description of the transaction.  # noqa: E501

        :param name: The name of this InvestmentTransaction.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def quantity(self):
        """Gets the quantity of this InvestmentTransaction.  # noqa: E501

        The number of units of the security involved in this transactions  # noqa: E501

        :return: The quantity of this InvestmentTransaction.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this InvestmentTransaction.

        The number of units of the security involved in this transactions  # noqa: E501

        :param quantity: The quantity of this InvestmentTransaction.  # noqa: E501
        :type quantity: float
        """

        self._quantity = quantity

    @property
    def amount(self):
        """Gets the amount of this InvestmentTransaction.  # noqa: E501

        The complete value of the transaction. Positive values when cash is debited, e.g. purchases of stock; negative values when cash is credited, e.g. sales of stock. Treatment remains the same for cash-only movements unassociated with securities.  # noqa: E501

        :return: The amount of this InvestmentTransaction.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InvestmentTransaction.

        The complete value of the transaction. Positive values when cash is debited, e.g. purchases of stock; negative values when cash is credited, e.g. sales of stock. Treatment remains the same for cash-only movements unassociated with securities.  # noqa: E501

        :param amount: The amount of this InvestmentTransaction.  # noqa: E501
        :type amount: float
        """

        self._amount = amount

    @property
    def price(self):
        """Gets the price of this InvestmentTransaction.  # noqa: E501

        The price of the security at which this transaction occurred.  # noqa: E501

        :return: The price of this InvestmentTransaction.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this InvestmentTransaction.

        The price of the security at which this transaction occurred.  # noqa: E501

        :param price: The price of this InvestmentTransaction.  # noqa: E501
        :type price: float
        """

        self._price = price

    @property
    def fees(self):
        """Gets the fees of this InvestmentTransaction.  # noqa: E501

        The combined value of all fees applied to this transaction  # noqa: E501

        :return: The fees of this InvestmentTransaction.  # noqa: E501
        :rtype: float
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this InvestmentTransaction.

        The combined value of all fees applied to this transaction  # noqa: E501

        :param fees: The fees of this InvestmentTransaction.  # noqa: E501
        :type fees: float
        """

        self._fees = fees

    @property
    def type(self):
        """Gets the type of this InvestmentTransaction.  # noqa: E501

        Value is one of the following:   `buy`: Buying an investment `sell`: Selling an investment  `cancel`: A cancellation of a pending transaction  `cash`: Activity that modifies a cash position  `fee`: A fee on the account  `transfer`: Activity which modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer  # noqa: E501

        :return: The type of this InvestmentTransaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InvestmentTransaction.

        Value is one of the following:   `buy`: Buying an investment `sell`: Selling an investment  `cancel`: A cancellation of a pending transaction  `cash`: Activity that modifies a cash position  `fee`: A fee on the account  `transfer`: Activity which modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer  # noqa: E501

        :param type: The type of this InvestmentTransaction.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def subtype(self):
        """Gets the subtype of this InvestmentTransaction.  # noqa: E501


        :return: The subtype of this InvestmentTransaction.  # noqa: E501
        :rtype: StandaloneInvestmentTransactionSubtype
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this InvestmentTransaction.


        :param subtype: The subtype of this InvestmentTransaction.  # noqa: E501
        :type subtype: StandaloneInvestmentTransactionSubtype
        """

        self._subtype = subtype

    @property
    def iso_currency_code(self):
        """Gets the iso_currency_code of this InvestmentTransaction.  # noqa: E501

        The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-`null`.  # noqa: E501

        :return: The iso_currency_code of this InvestmentTransaction.  # noqa: E501
        :rtype: str
        """
        return self._iso_currency_code

    @iso_currency_code.setter
    def iso_currency_code(self, iso_currency_code):
        """Sets the iso_currency_code of this InvestmentTransaction.

        The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-`null`.  # noqa: E501

        :param iso_currency_code: The iso_currency_code of this InvestmentTransaction.  # noqa: E501
        :type iso_currency_code: str
        """

        self._iso_currency_code = iso_currency_code

    @property
    def unofficial_currency_code(self):
        """Gets the unofficial_currency_code of this InvestmentTransaction.  # noqa: E501

        The unofficial currency code associated with the holding. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.  # noqa: E501

        :return: The unofficial_currency_code of this InvestmentTransaction.  # noqa: E501
        :rtype: str
        """
        return self._unofficial_currency_code

    @unofficial_currency_code.setter
    def unofficial_currency_code(self, unofficial_currency_code):
        """Sets the unofficial_currency_code of this InvestmentTransaction.

        The unofficial currency code associated with the holding. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.  # noqa: E501

        :param unofficial_currency_code: The unofficial_currency_code of this InvestmentTransaction.  # noqa: E501
        :type unofficial_currency_code: str
        """

        self._unofficial_currency_code = unofficial_currency_code

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
        if not isinstance(other, InvestmentTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvestmentTransaction):
            return True

        return self.to_dict() != other.to_dict()
