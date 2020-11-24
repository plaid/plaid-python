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


class Holding(object):
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
        'security_id': 'str',
        'institution_price': 'float',
        'institution_price_as_of': 'str',
        'institution_value': 'float',
        'cost_basis': 'float',
        'quantity': 'float',
        'iso_currency_code': 'str',
        'unofficial_currency_code': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'security_id': 'security_id',
        'institution_price': 'institution_price',
        'institution_price_as_of': 'institution_price_as_of',
        'institution_value': 'institution_value',
        'cost_basis': 'cost_basis',
        'quantity': 'quantity',
        'iso_currency_code': 'iso_currency_code',
        'unofficial_currency_code': 'unofficial_currency_code'
    }

    def __init__(self, account_id=None, security_id=None, institution_price=None, institution_price_as_of=None, institution_value=None, cost_basis=None, quantity=None, iso_currency_code=None, unofficial_currency_code=None, local_vars_configuration=None):  # noqa: E501
        """Holding - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._security_id = None
        self._institution_price = None
        self._institution_price_as_of = None
        self._institution_value = None
        self._cost_basis = None
        self._quantity = None
        self._iso_currency_code = None
        self._unofficial_currency_code = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if security_id is not None:
            self.security_id = security_id
        if institution_price is not None:
            self.institution_price = institution_price
        self.institution_price_as_of = institution_price_as_of
        if institution_value is not None:
            self.institution_value = institution_value
        self.cost_basis = cost_basis
        if quantity is not None:
            self.quantity = quantity
        self.iso_currency_code = iso_currency_code
        self.unofficial_currency_code = unofficial_currency_code

    @property
    def account_id(self):
        """Gets the account_id of this Holding.  # noqa: E501

        The Plaid `account_id` associated with the holding.  # noqa: E501

        :return: The account_id of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Holding.

        The Plaid `account_id` associated with the holding.  # noqa: E501

        :param account_id: The account_id of this Holding.  # noqa: E501
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def security_id(self):
        """Gets the security_id of this Holding.  # noqa: E501

        The Plaid `security_id` associated with the holding.  # noqa: E501

        :return: The security_id of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._security_id

    @security_id.setter
    def security_id(self, security_id):
        """Sets the security_id of this Holding.

        The Plaid `security_id` associated with the holding.  # noqa: E501

        :param security_id: The security_id of this Holding.  # noqa: E501
        :type security_id: str
        """

        self._security_id = security_id

    @property
    def institution_price(self):
        """Gets the institution_price of this Holding.  # noqa: E501

        The last price given by the institution for this security.  # noqa: E501

        :return: The institution_price of this Holding.  # noqa: E501
        :rtype: float
        """
        return self._institution_price

    @institution_price.setter
    def institution_price(self, institution_price):
        """Sets the institution_price of this Holding.

        The last price given by the institution for this security.  # noqa: E501

        :param institution_price: The institution_price of this Holding.  # noqa: E501
        :type institution_price: float
        """

        self._institution_price = institution_price

    @property
    def institution_price_as_of(self):
        """Gets the institution_price_as_of of this Holding.  # noqa: E501

        The date at which `institution_price` was current.  # noqa: E501

        :return: The institution_price_as_of of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._institution_price_as_of

    @institution_price_as_of.setter
    def institution_price_as_of(self, institution_price_as_of):
        """Sets the institution_price_as_of of this Holding.

        The date at which `institution_price` was current.  # noqa: E501

        :param institution_price_as_of: The institution_price_as_of of this Holding.  # noqa: E501
        :type institution_price_as_of: str
        """

        self._institution_price_as_of = institution_price_as_of

    @property
    def institution_value(self):
        """Gets the institution_value of this Holding.  # noqa: E501

        The value of the holding, as reported by the institution.  # noqa: E501

        :return: The institution_value of this Holding.  # noqa: E501
        :rtype: float
        """
        return self._institution_value

    @institution_value.setter
    def institution_value(self, institution_value):
        """Sets the institution_value of this Holding.

        The value of the holding, as reported by the institution.  # noqa: E501

        :param institution_value: The institution_value of this Holding.  # noqa: E501
        :type institution_value: float
        """

        self._institution_value = institution_value

    @property
    def cost_basis(self):
        """Gets the cost_basis of this Holding.  # noqa: E501

        The cost basis of the holding.  # noqa: E501

        :return: The cost_basis of this Holding.  # noqa: E501
        :rtype: float
        """
        return self._cost_basis

    @cost_basis.setter
    def cost_basis(self, cost_basis):
        """Sets the cost_basis of this Holding.

        The cost basis of the holding.  # noqa: E501

        :param cost_basis: The cost_basis of this Holding.  # noqa: E501
        :type cost_basis: float
        """

        self._cost_basis = cost_basis

    @property
    def quantity(self):
        """Gets the quantity of this Holding.  # noqa: E501

        The total quantity of the asset held, as reported by the financial institution.  # noqa: E501

        :return: The quantity of this Holding.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Holding.

        The total quantity of the asset held, as reported by the financial institution.  # noqa: E501

        :param quantity: The quantity of this Holding.  # noqa: E501
        :type quantity: float
        """

        self._quantity = quantity

    @property
    def iso_currency_code(self):
        """Gets the iso_currency_code of this Holding.  # noqa: E501

        The ISO-4217 currency code of the holding. Always `null` if `unofficial_currency_code` is non-`null`.  # noqa: E501

        :return: The iso_currency_code of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._iso_currency_code

    @iso_currency_code.setter
    def iso_currency_code(self, iso_currency_code):
        """Sets the iso_currency_code of this Holding.

        The ISO-4217 currency code of the holding. Always `null` if `unofficial_currency_code` is non-`null`.  # noqa: E501

        :param iso_currency_code: The iso_currency_code of this Holding.  # noqa: E501
        :type iso_currency_code: str
        """

        self._iso_currency_code = iso_currency_code

    @property
    def unofficial_currency_code(self):
        """Gets the unofficial_currency_code of this Holding.  # noqa: E501

        The unofficial currency code associated with the holding. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.   # noqa: E501

        :return: The unofficial_currency_code of this Holding.  # noqa: E501
        :rtype: str
        """
        return self._unofficial_currency_code

    @unofficial_currency_code.setter
    def unofficial_currency_code(self, unofficial_currency_code):
        """Sets the unofficial_currency_code of this Holding.

        The unofficial currency code associated with the holding. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.   # noqa: E501

        :param unofficial_currency_code: The unofficial_currency_code of this Holding.  # noqa: E501
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
        if not isinstance(other, Holding):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Holding):
            return True

        return self.to_dict() != other.to_dict()
