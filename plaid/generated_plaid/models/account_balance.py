# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.0.11
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class AccountBalance(object):
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
        'available': 'float',
        'current': 'float',
        'limit': 'float',
        'iso_currency_code': 'str',
        'unofficial_currency_code': 'str'
    }

    attribute_map = {
        'available': 'available',
        'current': 'current',
        'limit': 'limit',
        'iso_currency_code': 'iso_currency_code',
        'unofficial_currency_code': 'unofficial_currency_code'
    }

    def __init__(self, available=None, current=None, limit=None, iso_currency_code=None, unofficial_currency_code=None, local_vars_configuration=None):  # noqa: E501
        """AccountBalance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._available = None
        self._current = None
        self._limit = None
        self._iso_currency_code = None
        self._unofficial_currency_code = None
        self.discriminator = None

        self.available = available
        if current is not None:
            self.current = current
        self.limit = limit
        self.iso_currency_code = iso_currency_code
        self.unofficial_currency_code = unofficial_currency_code

    @property
    def available(self):
        """Gets the available of this AccountBalance.  # noqa: E501

        The amount of funds available to be withdrawn from the account, as determined by the financial institution.  For `credit`-type accounts, the `available` balance typically equals the `limit` less the `current` balance, less any pending outflows plus any pending inflows.  For `depository`-type accounts, the `available` balance typically equals the `current` balance less any pending outflows plus any pending inflows. For `depository`-type accounts, the `available` balance does not include the overdraft limit.  For `investment`-type accounts, the `available` balance is the total cash available to withdraw as presented by the institution.  Note that not all institutions calculate the ` available`  balance. In the event that `available` balance is unavailable, Plaid will return an `available` balance value of `null`.  Available balance may be cached and is not guaranteed to be up-to-date in realtime unless the value was returned by `/accounts/balance/get`.  # noqa: E501

        :return: The available of this AccountBalance.  # noqa: E501
        :rtype: float
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this AccountBalance.

        The amount of funds available to be withdrawn from the account, as determined by the financial institution.  For `credit`-type accounts, the `available` balance typically equals the `limit` less the `current` balance, less any pending outflows plus any pending inflows.  For `depository`-type accounts, the `available` balance typically equals the `current` balance less any pending outflows plus any pending inflows. For `depository`-type accounts, the `available` balance does not include the overdraft limit.  For `investment`-type accounts, the `available` balance is the total cash available to withdraw as presented by the institution.  Note that not all institutions calculate the ` available`  balance. In the event that `available` balance is unavailable, Plaid will return an `available` balance value of `null`.  Available balance may be cached and is not guaranteed to be up-to-date in realtime unless the value was returned by `/accounts/balance/get`.  # noqa: E501

        :param available: The available of this AccountBalance.  # noqa: E501
        :type available: float
        """

        self._available = available

    @property
    def current(self):
        """Gets the current of this AccountBalance.  # noqa: E501

        The total amount of funds in or owed by the account.  For `credit`-type accounts, a positive balance indicates the amount owed; a negative amount indicates the lender owing the account holder.  For `loan`-type accounts, the current balance is the principal remaining on the loan.  For `investment`-type accounts, the current balance is the total value of assets as presented by the institution.  Current balance may be cached and is not guaranteed to be up-to-date in realtime unless the value was returned by `/accounts/balance/get`.  # noqa: E501

        :return: The current of this AccountBalance.  # noqa: E501
        :rtype: float
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this AccountBalance.

        The total amount of funds in or owed by the account.  For `credit`-type accounts, a positive balance indicates the amount owed; a negative amount indicates the lender owing the account holder.  For `loan`-type accounts, the current balance is the principal remaining on the loan.  For `investment`-type accounts, the current balance is the total value of assets as presented by the institution.  Current balance may be cached and is not guaranteed to be up-to-date in realtime unless the value was returned by `/accounts/balance/get`.  # noqa: E501

        :param current: The current of this AccountBalance.  # noqa: E501
        :type current: float
        """

        self._current = current

    @property
    def limit(self):
        """Gets the limit of this AccountBalance.  # noqa: E501

        For `credit`-type accounts, this represents the credit limit.   For `depository`-type accounts, this represents the pre-arranged overdraft limit, which is common for current (checking) accounts in Europe.   In North America, this field is typically only available for `credit`-type accounts.  # noqa: E501

        :return: The limit of this AccountBalance.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this AccountBalance.

        For `credit`-type accounts, this represents the credit limit.   For `depository`-type accounts, this represents the pre-arranged overdraft limit, which is common for current (checking) accounts in Europe.   In North America, this field is typically only available for `credit`-type accounts.  # noqa: E501

        :param limit: The limit of this AccountBalance.  # noqa: E501
        :type limit: float
        """

        self._limit = limit

    @property
    def iso_currency_code(self):
        """Gets the iso_currency_code of this AccountBalance.  # noqa: E501

        The ISO-4217 currency code of the balance. Always null if `unofficial_currency_code` is non-null.  # noqa: E501

        :return: The iso_currency_code of this AccountBalance.  # noqa: E501
        :rtype: str
        """
        return self._iso_currency_code

    @iso_currency_code.setter
    def iso_currency_code(self, iso_currency_code):
        """Sets the iso_currency_code of this AccountBalance.

        The ISO-4217 currency code of the balance. Always null if `unofficial_currency_code` is non-null.  # noqa: E501

        :param iso_currency_code: The iso_currency_code of this AccountBalance.  # noqa: E501
        :type iso_currency_code: str
        """

        self._iso_currency_code = iso_currency_code

    @property
    def unofficial_currency_code(self):
        """Gets the unofficial_currency_code of this AccountBalance.  # noqa: E501

        The unofficial currency code associated with the balance. Always null if `iso_currency_code` is non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](/docs/api/accounts#currency-code-schema) for a full listing of supported `unofficial_currency_code`s.  # noqa: E501

        :return: The unofficial_currency_code of this AccountBalance.  # noqa: E501
        :rtype: str
        """
        return self._unofficial_currency_code

    @unofficial_currency_code.setter
    def unofficial_currency_code(self, unofficial_currency_code):
        """Sets the unofficial_currency_code of this AccountBalance.

        The unofficial currency code associated with the balance. Always null if `iso_currency_code` is non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](/docs/api/accounts#currency-code-schema) for a full listing of supported `unofficial_currency_code`s.  # noqa: E501

        :param unofficial_currency_code: The unofficial_currency_code of this AccountBalance.  # noqa: E501
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
        if not isinstance(other, AccountBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountBalance):
            return True

        return self.to_dict() != other.to_dict()
