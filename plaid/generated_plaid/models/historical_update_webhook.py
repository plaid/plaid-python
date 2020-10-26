# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.0.9
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class HistoricalUpdateWebhook(object):
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
        'error': 'Error',
        'new_transactions': 'float',
        'item_id': 'str'
    }

    attribute_map = {
        'webhook_type': 'webhook_type',
        'webhook_code': 'webhook_code',
        'error': 'error',
        'new_transactions': 'new_transactions',
        'item_id': 'item_id'
    }

    def __init__(self, webhook_type=None, webhook_code=None, error=None, new_transactions=None, item_id=None, local_vars_configuration=None):  # noqa: E501
        """HistoricalUpdateWebhook - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._webhook_type = None
        self._webhook_code = None
        self._error = None
        self._new_transactions = None
        self._item_id = None
        self.discriminator = None

        if webhook_type is not None:
            self.webhook_type = webhook_type
        if webhook_code is not None:
            self.webhook_code = webhook_code
        self.error = error
        if new_transactions is not None:
            self.new_transactions = new_transactions
        if item_id is not None:
            self.item_id = item_id

    @property
    def webhook_type(self):
        """Gets the webhook_type of this HistoricalUpdateWebhook.  # noqa: E501

        `TRANSACTIONS`  # noqa: E501

        :return: The webhook_type of this HistoricalUpdateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._webhook_type

    @webhook_type.setter
    def webhook_type(self, webhook_type):
        """Sets the webhook_type of this HistoricalUpdateWebhook.

        `TRANSACTIONS`  # noqa: E501

        :param webhook_type: The webhook_type of this HistoricalUpdateWebhook.  # noqa: E501
        :type webhook_type: str
        """

        self._webhook_type = webhook_type

    @property
    def webhook_code(self):
        """Gets the webhook_code of this HistoricalUpdateWebhook.  # noqa: E501

        `HISTORICAL_UPDATE`  # noqa: E501

        :return: The webhook_code of this HistoricalUpdateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._webhook_code

    @webhook_code.setter
    def webhook_code(self, webhook_code):
        """Sets the webhook_code of this HistoricalUpdateWebhook.

        `HISTORICAL_UPDATE`  # noqa: E501

        :param webhook_code: The webhook_code of this HistoricalUpdateWebhook.  # noqa: E501
        :type webhook_code: str
        """

        self._webhook_code = webhook_code

    @property
    def error(self):
        """Gets the error of this HistoricalUpdateWebhook.  # noqa: E501


        :return: The error of this HistoricalUpdateWebhook.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this HistoricalUpdateWebhook.


        :param error: The error of this HistoricalUpdateWebhook.  # noqa: E501
        :type error: Error
        """

        self._error = error

    @property
    def new_transactions(self):
        """Gets the new_transactions of this HistoricalUpdateWebhook.  # noqa: E501

        The number of new, unfetched transactions available  # noqa: E501

        :return: The new_transactions of this HistoricalUpdateWebhook.  # noqa: E501
        :rtype: float
        """
        return self._new_transactions

    @new_transactions.setter
    def new_transactions(self, new_transactions):
        """Sets the new_transactions of this HistoricalUpdateWebhook.

        The number of new, unfetched transactions available  # noqa: E501

        :param new_transactions: The new_transactions of this HistoricalUpdateWebhook.  # noqa: E501
        :type new_transactions: float
        """

        self._new_transactions = new_transactions

    @property
    def item_id(self):
        """Gets the item_id of this HistoricalUpdateWebhook.  # noqa: E501

        The `item_id` of the Item associated with this webhook, warning, or error  # noqa: E501

        :return: The item_id of this HistoricalUpdateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this HistoricalUpdateWebhook.

        The `item_id` of the Item associated with this webhook, warning, or error  # noqa: E501

        :param item_id: The item_id of this HistoricalUpdateWebhook.  # noqa: E501
        :type item_id: str
        """

        self._item_id = item_id

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
        if not isinstance(other, HistoricalUpdateWebhook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HistoricalUpdateWebhook):
            return True

        return self.to_dict() != other.to_dict()
