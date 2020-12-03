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


class Warning(object):
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
        'warning_type': 'str',
        'warning_code': 'str',
        'cause': 'Cause'
    }

    attribute_map = {
        'warning_type': 'warning_type',
        'warning_code': 'warning_code',
        'cause': 'cause'
    }

    def __init__(self, warning_type=None, warning_code=None, cause=None, local_vars_configuration=None):  # noqa: E501
        """Warning - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._warning_type = None
        self._warning_code = None
        self._cause = None
        self.discriminator = None

        if warning_type is not None:
            self.warning_type = warning_type
        if warning_code is not None:
            self.warning_code = warning_code
        if cause is not None:
            self.cause = cause

    @property
    def warning_type(self):
        """Gets the warning_type of this Warning.  # noqa: E501

        The warning type, which will always be `ASSET_REPORT_WARNING`  # noqa: E501

        :return: The warning_type of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._warning_type

    @warning_type.setter
    def warning_type(self, warning_type):
        """Sets the warning_type of this Warning.

        The warning type, which will always be `ASSET_REPORT_WARNING`  # noqa: E501

        :param warning_type: The warning_type of this Warning.  # noqa: E501
        :type warning_type: str
        """

        self._warning_type = warning_type

    @property
    def warning_code(self):
        """Gets the warning_code of this Warning.  # noqa: E501

        The warning code identifies a specific kind of warning. Currently, the only possible warning code is `OWNERS_UNAVAILABLE`, which indicates that account-owner information is not available.  # noqa: E501

        :return: The warning_code of this Warning.  # noqa: E501
        :rtype: str
        """
        return self._warning_code

    @warning_code.setter
    def warning_code(self, warning_code):
        """Sets the warning_code of this Warning.

        The warning code identifies a specific kind of warning. Currently, the only possible warning code is `OWNERS_UNAVAILABLE`, which indicates that account-owner information is not available.  # noqa: E501

        :param warning_code: The warning_code of this Warning.  # noqa: E501
        :type warning_code: str
        """

        self._warning_code = warning_code

    @property
    def cause(self):
        """Gets the cause of this Warning.  # noqa: E501


        :return: The cause of this Warning.  # noqa: E501
        :rtype: Cause
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this Warning.


        :param cause: The cause of this Warning.  # noqa: E501
        :type cause: Cause
        """

        self._cause = cause

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
        if not isinstance(other, Warning):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Warning):
            return True

        return self.to_dict() != other.to_dict()
