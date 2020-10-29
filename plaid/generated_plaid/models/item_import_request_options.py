# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.0.10
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class ItemImportRequestOptions(object):
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
        'webhook': 'str'
    }

    attribute_map = {
        'webhook': 'webhook'
    }

    def __init__(self, webhook=None, local_vars_configuration=None):  # noqa: E501
        """ItemImportRequestOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._webhook = None
        self.discriminator = None

        if webhook is not None:
            self.webhook = webhook

    @property
    def webhook(self):
        """Gets the webhook of this ItemImportRequestOptions.  # noqa: E501

        Specifies a webhook URL to associate with an Item. Plaid fires a webhook if credentials fail.   # noqa: E501

        :return: The webhook of this ItemImportRequestOptions.  # noqa: E501
        :rtype: str
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this ItemImportRequestOptions.

        Specifies a webhook URL to associate with an Item. Plaid fires a webhook if credentials fail.   # noqa: E501

        :param webhook: The webhook of this ItemImportRequestOptions.  # noqa: E501
        :type webhook: str
        """

        self._webhook = webhook

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
        if not isinstance(other, ItemImportRequestOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemImportRequestOptions):
            return True

        return self.to_dict() != other.to_dict()
