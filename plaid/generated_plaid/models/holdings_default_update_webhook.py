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


class HoldingsDefaultUpdateWebhook(object):
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
        'error': 'Error',
        'new_holdings': 'float',
        'updated_holdings': 'float'
    }

    attribute_map = {
        'webhook_type': 'webhook_type',
        'webhook_code': 'webhook_code',
        'item_id': 'item_id',
        'error': 'error',
        'new_holdings': 'new_holdings',
        'updated_holdings': 'updated_holdings'
    }

    def __init__(self, webhook_type=None, webhook_code=None, item_id=None, error=None, new_holdings=None, updated_holdings=None, local_vars_configuration=None):  # noqa: E501
        """HoldingsDefaultUpdateWebhook - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._webhook_type = None
        self._webhook_code = None
        self._item_id = None
        self._error = None
        self._new_holdings = None
        self._updated_holdings = None
        self.discriminator = None

        if webhook_type is not None:
            self.webhook_type = webhook_type
        if webhook_code is not None:
            self.webhook_code = webhook_code
        if item_id is not None:
            self.item_id = item_id
        self.error = error
        if new_holdings is not None:
            self.new_holdings = new_holdings
        if updated_holdings is not None:
            self.updated_holdings = updated_holdings

    @property
    def webhook_type(self):
        """Gets the webhook_type of this HoldingsDefaultUpdateWebhook.  # noqa: E501

        `HOLDINGS`  # noqa: E501

        :return: The webhook_type of this HoldingsDefaultUpdateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._webhook_type

    @webhook_type.setter
    def webhook_type(self, webhook_type):
        """Sets the webhook_type of this HoldingsDefaultUpdateWebhook.

        `HOLDINGS`  # noqa: E501

        :param webhook_type: The webhook_type of this HoldingsDefaultUpdateWebhook.  # noqa: E501
        :type webhook_type: str
        """

        self._webhook_type = webhook_type

    @property
    def webhook_code(self):
        """Gets the webhook_code of this HoldingsDefaultUpdateWebhook.  # noqa: E501

        `DEFAULT_UPDATE`  # noqa: E501

        :return: The webhook_code of this HoldingsDefaultUpdateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._webhook_code

    @webhook_code.setter
    def webhook_code(self, webhook_code):
        """Sets the webhook_code of this HoldingsDefaultUpdateWebhook.

        `DEFAULT_UPDATE`  # noqa: E501

        :param webhook_code: The webhook_code of this HoldingsDefaultUpdateWebhook.  # noqa: E501
        :type webhook_code: str
        """

        self._webhook_code = webhook_code

    @property
    def item_id(self):
        """Gets the item_id of this HoldingsDefaultUpdateWebhook.  # noqa: E501

        The `item_id` of the Item associated with this webhook, warning, or error  # noqa: E501

        :return: The item_id of this HoldingsDefaultUpdateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this HoldingsDefaultUpdateWebhook.

        The `item_id` of the Item associated with this webhook, warning, or error  # noqa: E501

        :param item_id: The item_id of this HoldingsDefaultUpdateWebhook.  # noqa: E501
        :type item_id: str
        """

        self._item_id = item_id

    @property
    def error(self):
        """Gets the error of this HoldingsDefaultUpdateWebhook.  # noqa: E501


        :return: The error of this HoldingsDefaultUpdateWebhook.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this HoldingsDefaultUpdateWebhook.


        :param error: The error of this HoldingsDefaultUpdateWebhook.  # noqa: E501
        :type error: Error
        """

        self._error = error

    @property
    def new_holdings(self):
        """Gets the new_holdings of this HoldingsDefaultUpdateWebhook.  # noqa: E501

        The number of new holdings reported since the last time this webhook was fired.  # noqa: E501

        :return: The new_holdings of this HoldingsDefaultUpdateWebhook.  # noqa: E501
        :rtype: float
        """
        return self._new_holdings

    @new_holdings.setter
    def new_holdings(self, new_holdings):
        """Sets the new_holdings of this HoldingsDefaultUpdateWebhook.

        The number of new holdings reported since the last time this webhook was fired.  # noqa: E501

        :param new_holdings: The new_holdings of this HoldingsDefaultUpdateWebhook.  # noqa: E501
        :type new_holdings: float
        """

        self._new_holdings = new_holdings

    @property
    def updated_holdings(self):
        """Gets the updated_holdings of this HoldingsDefaultUpdateWebhook.  # noqa: E501

        The number of updated holdings reported since the last time this webhook was fired.  # noqa: E501

        :return: The updated_holdings of this HoldingsDefaultUpdateWebhook.  # noqa: E501
        :rtype: float
        """
        return self._updated_holdings

    @updated_holdings.setter
    def updated_holdings(self, updated_holdings):
        """Sets the updated_holdings of this HoldingsDefaultUpdateWebhook.

        The number of updated holdings reported since the last time this webhook was fired.  # noqa: E501

        :param updated_holdings: The updated_holdings of this HoldingsDefaultUpdateWebhook.  # noqa: E501
        :type updated_holdings: float
        """

        self._updated_holdings = updated_holdings

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
        if not isinstance(other, HoldingsDefaultUpdateWebhook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HoldingsDefaultUpdateWebhook):
            return True

        return self.to_dict() != other.to_dict()
