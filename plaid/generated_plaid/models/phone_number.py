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


class PhoneNumber(object):
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
        'data': 'str',
        'primary': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'data': 'data',
        'primary': 'primary',
        'type': 'type'
    }

    def __init__(self, data=None, primary=None, type=None, local_vars_configuration=None):  # noqa: E501
        """PhoneNumber - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data = None
        self._primary = None
        self._type = None
        self.discriminator = None

        if data is not None:
            self.data = data
        self.primary = primary
        self.type = type

    @property
    def data(self):
        """Gets the data of this PhoneNumber.  # noqa: E501

        The phone number.  # noqa: E501

        :return: The data of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PhoneNumber.

        The phone number.  # noqa: E501

        :param data: The data of this PhoneNumber.  # noqa: E501
        :type data: str
        """

        self._data = data

    @property
    def primary(self):
        """Gets the primary of this PhoneNumber.  # noqa: E501

        When `true`, identifies the phone number as the primary number on an account.  # noqa: E501

        :return: The primary of this PhoneNumber.  # noqa: E501
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this PhoneNumber.

        When `true`, identifies the phone number as the primary number on an account.  # noqa: E501

        :param primary: The primary of this PhoneNumber.  # noqa: E501
        :type primary: bool
        """

        self._primary = primary

    @property
    def type(self):
        """Gets the type of this PhoneNumber.  # noqa: E501

        The type of phone number.  # noqa: E501

        :return: The type of this PhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PhoneNumber.

        The type of phone number.  # noqa: E501

        :param type: The type of this PhoneNumber.  # noqa: E501
        :type type: str
        """
        allowed_values = [None,"home", "work", "office", "mobile", "mobile1", "other"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

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
        if not isinstance(other, PhoneNumber):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PhoneNumber):
            return True

        return self.to_dict() != other.to_dict()
