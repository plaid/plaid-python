# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class ItemStatusLastWebhook(object):
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
        'sent_at': 'str',
        'code_sent': 'str'
    }

    attribute_map = {
        'sent_at': 'sent_at',
        'code_sent': 'code_sent'
    }

    def __init__(self, sent_at=None, code_sent=None, local_vars_configuration=None):  # noqa: E501
        """ItemStatusLastWebhook - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sent_at = None
        self._code_sent = None
        self.discriminator = None

        self.sent_at = sent_at
        self.code_sent = code_sent

    @property
    def sent_at(self):
        """Gets the sent_at of this ItemStatusLastWebhook.  # noqa: E501

        ISO 8601 timestamp of when the webhook was fired.  # noqa: E501

        :return: The sent_at of this ItemStatusLastWebhook.  # noqa: E501
        :rtype: str
        """
        return self._sent_at

    @sent_at.setter
    def sent_at(self, sent_at):
        """Sets the sent_at of this ItemStatusLastWebhook.

        ISO 8601 timestamp of when the webhook was fired.  # noqa: E501

        :param sent_at: The sent_at of this ItemStatusLastWebhook.  # noqa: E501
        :type sent_at: str
        """

        self._sent_at = sent_at

    @property
    def code_sent(self):
        """Gets the code_sent of this ItemStatusLastWebhook.  # noqa: E501

        The last webhook code sent.  # noqa: E501

        :return: The code_sent of this ItemStatusLastWebhook.  # noqa: E501
        :rtype: str
        """
        return self._code_sent

    @code_sent.setter
    def code_sent(self, code_sent):
        """Sets the code_sent of this ItemStatusLastWebhook.

        The last webhook code sent.  # noqa: E501

        :param code_sent: The code_sent of this ItemStatusLastWebhook.  # noqa: E501
        :type code_sent: str
        """

        self._code_sent = code_sent

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
        if not isinstance(other, ItemStatusLastWebhook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemStatusLastWebhook):
            return True

        return self.to_dict() != other.to_dict()
