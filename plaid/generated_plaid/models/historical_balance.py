# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.1.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class HistoricalBalance(object):
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
        'date': 'str',
        'current': 'float',
        'iso_currency_code': 'str',
        'unofficial_currency_code': 'str'
    }

    attribute_map = {
        'date': 'date',
        'current': 'current',
        'iso_currency_code': 'iso_currency_code',
        'unofficial_currency_code': 'unofficial_currency_code'
    }

    def __init__(self, date=None, current=None, iso_currency_code=None, unofficial_currency_code=None, local_vars_configuration=None):  # noqa: E501
        """HistoricalBalance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date = None
        self._current = None
        self._iso_currency_code = None
        self._unofficial_currency_code = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if current is not None:
            self.current = current
        self.iso_currency_code = iso_currency_code
        self.unofficial_currency_code = unofficial_currency_code

    @property
    def date(self):
        """Gets the date of this HistoricalBalance.  # noqa: E501

        The date of the calculated historical balance, in an ISO 8601 format (YYYY-MM-DD)  # noqa: E501

        :return: The date of this HistoricalBalance.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this HistoricalBalance.

        The date of the calculated historical balance, in an ISO 8601 format (YYYY-MM-DD)  # noqa: E501

        :param date: The date of this HistoricalBalance.  # noqa: E501
        :type date: str
        """

        self._date = date

    @property
    def current(self):
        """Gets the current of this HistoricalBalance.  # noqa: E501

        The total amount of funds in the account, calculated from the `current` balance in the `balance` object by subtracting inflows and adding back outflows according to the posted date of each transaction.  If the account has any pending transactions, historical balance amounts on or after the date of the earliest pending transaction may differ if retrieved in subsequent Asset Reports as a result of those pending transactions posting.  # noqa: E501

        :return: The current of this HistoricalBalance.  # noqa: E501
        :rtype: float
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this HistoricalBalance.

        The total amount of funds in the account, calculated from the `current` balance in the `balance` object by subtracting inflows and adding back outflows according to the posted date of each transaction.  If the account has any pending transactions, historical balance amounts on or after the date of the earliest pending transaction may differ if retrieved in subsequent Asset Reports as a result of those pending transactions posting.  # noqa: E501

        :param current: The current of this HistoricalBalance.  # noqa: E501
        :type current: float
        """

        self._current = current

    @property
    def iso_currency_code(self):
        """Gets the iso_currency_code of this HistoricalBalance.  # noqa: E501

        The ISO-4217 currency code of the balance. Always `null` if `unofficial_currency_code` is non-`null`.  # noqa: E501

        :return: The iso_currency_code of this HistoricalBalance.  # noqa: E501
        :rtype: str
        """
        return self._iso_currency_code

    @iso_currency_code.setter
    def iso_currency_code(self, iso_currency_code):
        """Sets the iso_currency_code of this HistoricalBalance.

        The ISO-4217 currency code of the balance. Always `null` if `unofficial_currency_code` is non-`null`.  # noqa: E501

        :param iso_currency_code: The iso_currency_code of this HistoricalBalance.  # noqa: E501
        :type iso_currency_code: str
        """

        self._iso_currency_code = iso_currency_code

    @property
    def unofficial_currency_code(self):
        """Gets the unofficial_currency_code of this HistoricalBalance.  # noqa: E501

        The unofficial currency code associated with the balance. Always `null` if `iso_currency_code` is non-`null`.  See the [currency code schema](/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.  # noqa: E501

        :return: The unofficial_currency_code of this HistoricalBalance.  # noqa: E501
        :rtype: str
        """
        return self._unofficial_currency_code

    @unofficial_currency_code.setter
    def unofficial_currency_code(self, unofficial_currency_code):
        """Sets the unofficial_currency_code of this HistoricalBalance.

        The unofficial currency code associated with the balance. Always `null` if `iso_currency_code` is non-`null`.  See the [currency code schema](/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.  # noqa: E501

        :param unofficial_currency_code: The unofficial_currency_code of this HistoricalBalance.  # noqa: E501
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
        if not isinstance(other, HistoricalBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HistoricalBalance):
            return True

        return self.to_dict() != other.to_dict()
