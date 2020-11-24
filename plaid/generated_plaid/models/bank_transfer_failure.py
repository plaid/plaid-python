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


class BankTransferFailure(object):
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
        'ach_return_code': 'str',
        'description': 'str'
    }

    attribute_map = {
        'ach_return_code': 'ach_return_code',
        'description': 'description'
    }

    def __init__(self, ach_return_code=None, description=None, local_vars_configuration=None):  # noqa: E501
        """BankTransferFailure - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ach_return_code = None
        self._description = None
        self.discriminator = None

        if ach_return_code is not None:
            self.ach_return_code = ach_return_code
        if description is not None:
            self.description = description

    @property
    def ach_return_code(self):
        """Gets the ach_return_code of this BankTransferFailure.  # noqa: E501

        The ACH return code, e.g. `R01`.  For a full listing of ACH return codes, see [Bank Transfers errors](/docs/errors/bank-transfers/#ach-return-codes).  # noqa: E501

        :return: The ach_return_code of this BankTransferFailure.  # noqa: E501
        :rtype: str
        """
        return self._ach_return_code

    @ach_return_code.setter
    def ach_return_code(self, ach_return_code):
        """Sets the ach_return_code of this BankTransferFailure.

        The ACH return code, e.g. `R01`.  For a full listing of ACH return codes, see [Bank Transfers errors](/docs/errors/bank-transfers/#ach-return-codes).  # noqa: E501

        :param ach_return_code: The ach_return_code of this BankTransferFailure.  # noqa: E501
        :type ach_return_code: str
        """

        self._ach_return_code = ach_return_code

    @property
    def description(self):
        """Gets the description of this BankTransferFailure.  # noqa: E501

        A human-readable description of the reason for the failure or reversal.  # noqa: E501

        :return: The description of this BankTransferFailure.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BankTransferFailure.

        A human-readable description of the reason for the failure or reversal.  # noqa: E501

        :param description: The description of this BankTransferFailure.  # noqa: E501
        :type description: str
        """

        self._description = description

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
        if not isinstance(other, BankTransferFailure):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BankTransferFailure):
            return True

        return self.to_dict() != other.to_dict()
