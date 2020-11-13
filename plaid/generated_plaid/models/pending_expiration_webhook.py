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


class PendingExpirationWebhook(object):
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
        'webhook_type': 'str',
        'webhook_code': 'str',
        'item_id': 'str',
        'consent_expiration_time': 'str'
    }

    attribute_map = {
        'webhook_type': 'webhook_type',
        'webhook_code': 'webhook_code',
        'item_id': 'item_id',
        'consent_expiration_time': 'consent_expiration_time'
    }

    def __init__(self, webhook_type=None, webhook_code=None, item_id=None, consent_expiration_time=None, local_vars_configuration=None):  # noqa: E501
        """PendingExpirationWebhook - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._webhook_type = None
        self._webhook_code = None
        self._item_id = None
        self._consent_expiration_time = None
        self.discriminator = None

        if webhook_type is not None:
            self.webhook_type = webhook_type
        if webhook_code is not None:
            self.webhook_code = webhook_code
        if item_id is not None:
            self.item_id = item_id
        if consent_expiration_time is not None:
            self.consent_expiration_time = consent_expiration_time

    @property
    def webhook_type(self):
        """Gets the webhook_type of this PendingExpirationWebhook.  # noqa: E501

        `ITEM`  # noqa: E501

        :return: The webhook_type of this PendingExpirationWebhook.  # noqa: E501
        :rtype: str
        """
        return self._webhook_type

    @webhook_type.setter
    def webhook_type(self, webhook_type):
        """Sets the webhook_type of this PendingExpirationWebhook.

        `ITEM`  # noqa: E501

        :param webhook_type: The webhook_type of this PendingExpirationWebhook.  # noqa: E501
        :type webhook_type: str
        """

        self._webhook_type = webhook_type

    @property
    def webhook_code(self):
        """Gets the webhook_code of this PendingExpirationWebhook.  # noqa: E501

        `PENDING_EXPIRATION`  # noqa: E501

        :return: The webhook_code of this PendingExpirationWebhook.  # noqa: E501
        :rtype: str
        """
        return self._webhook_code

    @webhook_code.setter
    def webhook_code(self, webhook_code):
        """Sets the webhook_code of this PendingExpirationWebhook.

        `PENDING_EXPIRATION`  # noqa: E501

        :param webhook_code: The webhook_code of this PendingExpirationWebhook.  # noqa: E501
        :type webhook_code: str
        """

        self._webhook_code = webhook_code

    @property
    def item_id(self):
        """Gets the item_id of this PendingExpirationWebhook.  # noqa: E501

        The `item_id` of the Item associated with this webhook, warning, or error  # noqa: E501

        :return: The item_id of this PendingExpirationWebhook.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this PendingExpirationWebhook.

        The `item_id` of the Item associated with this webhook, warning, or error  # noqa: E501

        :param item_id: The item_id of this PendingExpirationWebhook.  # noqa: E501
        :type item_id: str
        """

        self._item_id = item_id

    @property
    def consent_expiration_time(self):
        """Gets the consent_expiration_time of this PendingExpirationWebhook.  # noqa: E501

        The date and time at which the Item's access consent will expire, in ISO 8601 format  # noqa: E501

        :return: The consent_expiration_time of this PendingExpirationWebhook.  # noqa: E501
        :rtype: str
        """
        return self._consent_expiration_time

    @consent_expiration_time.setter
    def consent_expiration_time(self, consent_expiration_time):
        """Sets the consent_expiration_time of this PendingExpirationWebhook.

        The date and time at which the Item's access consent will expire, in ISO 8601 format  # noqa: E501

        :param consent_expiration_time: The consent_expiration_time of this PendingExpirationWebhook.  # noqa: E501
        :type consent_expiration_time: str
        """

        self._consent_expiration_time = consent_expiration_time

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
        if not isinstance(other, PendingExpirationWebhook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PendingExpirationWebhook):
            return True

        return self.to_dict() != other.to_dict()
