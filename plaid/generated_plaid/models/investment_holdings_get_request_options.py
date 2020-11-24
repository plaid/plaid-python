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


class InvestmentHoldingsGetRequestOptions(object):
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
        'account_ids': 'list[str]'
    }

    attribute_map = {
        'account_ids': 'account_ids'
    }

    def __init__(self, account_ids=None, local_vars_configuration=None):  # noqa: E501
        """InvestmentHoldingsGetRequestOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_ids = None
        self.discriminator = None

        self.account_ids = account_ids

    @property
    def account_ids(self):
        """Gets the account_ids of this InvestmentHoldingsGetRequestOptions.  # noqa: E501

        An array of `account_id`s to retrieve for the Item. An error will be returned if a provided `account_id` is not associated with the Item.  # noqa: E501

        :return: The account_ids of this InvestmentHoldingsGetRequestOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._account_ids

    @account_ids.setter
    def account_ids(self, account_ids):
        """Sets the account_ids of this InvestmentHoldingsGetRequestOptions.

        An array of `account_id`s to retrieve for the Item. An error will be returned if a provided `account_id` is not associated with the Item.  # noqa: E501

        :param account_ids: The account_ids of this InvestmentHoldingsGetRequestOptions.  # noqa: E501
        :type account_ids: list[str]
        """
        if self.local_vars_configuration.client_side_validation and account_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `account_ids`, must not be `None`")  # noqa: E501

        self._account_ids = account_ids

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
        if not isinstance(other, InvestmentHoldingsGetRequestOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvestmentHoldingsGetRequestOptions):
            return True

        return self.to_dict() != other.to_dict()
