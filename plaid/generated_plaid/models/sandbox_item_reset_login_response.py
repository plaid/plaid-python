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


class SandboxItemResetLoginResponse(object):
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
        'reset_login': 'bool',
        'request_id': 'str'
    }

    attribute_map = {
        'reset_login': 'reset_login',
        'request_id': 'request_id'
    }

    def __init__(self, reset_login=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """SandboxItemResetLoginResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._reset_login = None
        self._request_id = None
        self.discriminator = None

        if reset_login is not None:
            self.reset_login = reset_login
        if request_id is not None:
            self.request_id = request_id

    @property
    def reset_login(self):
        """Gets the reset_login of this SandboxItemResetLoginResponse.  # noqa: E501

        `true` if the call succeeded  # noqa: E501

        :return: The reset_login of this SandboxItemResetLoginResponse.  # noqa: E501
        :rtype: bool
        """
        return self._reset_login

    @reset_login.setter
    def reset_login(self, reset_login):
        """Sets the reset_login of this SandboxItemResetLoginResponse.

        `true` if the call succeeded  # noqa: E501

        :param reset_login: The reset_login of this SandboxItemResetLoginResponse.  # noqa: E501
        :type reset_login: bool
        """

        self._reset_login = reset_login

    @property
    def request_id(self):
        """Gets the request_id of this SandboxItemResetLoginResponse.  # noqa: E501

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :return: The request_id of this SandboxItemResetLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this SandboxItemResetLoginResponse.

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :param request_id: The request_id of this SandboxItemResetLoginResponse.  # noqa: E501
        :type request_id: str
        """

        self._request_id = request_id

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
        if not isinstance(other, SandboxItemResetLoginResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SandboxItemResetLoginResponse):
            return True

        return self.to_dict() != other.to_dict()
