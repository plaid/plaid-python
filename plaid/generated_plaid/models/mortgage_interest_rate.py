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


class MortgageInterestRate(object):
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
        'percentage': 'float',
        'type': 'str'
    }

    attribute_map = {
        'percentage': 'percentage',
        'type': 'type'
    }

    def __init__(self, percentage=None, type=None, local_vars_configuration=None):  # noqa: E501
        """MortgageInterestRate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._percentage = None
        self._type = None
        self.discriminator = None

        self.percentage = percentage
        self.type = type

    @property
    def percentage(self):
        """Gets the percentage of this MortgageInterestRate.  # noqa: E501

        Percentage value (interest rate of current mortgage, not APR) of interest payable on a loan.  # noqa: E501

        :return: The percentage of this MortgageInterestRate.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this MortgageInterestRate.

        Percentage value (interest rate of current mortgage, not APR) of interest payable on a loan.  # noqa: E501

        :param percentage: The percentage of this MortgageInterestRate.  # noqa: E501
        :type percentage: float
        """

        self._percentage = percentage

    @property
    def type(self):
        """Gets the type of this MortgageInterestRate.  # noqa: E501

        The type of interest charged (fixed or variable).  # noqa: E501

        :return: The type of this MortgageInterestRate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MortgageInterestRate.

        The type of interest charged (fixed or variable).  # noqa: E501

        :param type: The type of this MortgageInterestRate.  # noqa: E501
        :type type: str
        """

        self._type = type

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
        if not isinstance(other, MortgageInterestRate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MortgageInterestRate):
            return True

        return self.to_dict() != other.to_dict()
