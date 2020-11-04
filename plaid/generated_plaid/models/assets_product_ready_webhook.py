# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.0.11
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class AssetsProductReadyWebhook(object):
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
        'asset_report_id': 'str'
    }

    attribute_map = {
        'webhook_type': 'webhook_type',
        'webhook_code': 'webhook_code',
        'asset_report_id': 'asset_report_id'
    }

    def __init__(self, webhook_type=None, webhook_code=None, asset_report_id=None, local_vars_configuration=None):  # noqa: E501
        """AssetsProductReadyWebhook - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._webhook_type = None
        self._webhook_code = None
        self._asset_report_id = None
        self.discriminator = None

        if webhook_type is not None:
            self.webhook_type = webhook_type
        if webhook_code is not None:
            self.webhook_code = webhook_code
        if asset_report_id is not None:
            self.asset_report_id = asset_report_id

    @property
    def webhook_type(self):
        """Gets the webhook_type of this AssetsProductReadyWebhook.  # noqa: E501

        `ASSETS`  # noqa: E501

        :return: The webhook_type of this AssetsProductReadyWebhook.  # noqa: E501
        :rtype: str
        """
        return self._webhook_type

    @webhook_type.setter
    def webhook_type(self, webhook_type):
        """Sets the webhook_type of this AssetsProductReadyWebhook.

        `ASSETS`  # noqa: E501

        :param webhook_type: The webhook_type of this AssetsProductReadyWebhook.  # noqa: E501
        :type webhook_type: str
        """

        self._webhook_type = webhook_type

    @property
    def webhook_code(self):
        """Gets the webhook_code of this AssetsProductReadyWebhook.  # noqa: E501

        `PRODUCT_READY`  # noqa: E501

        :return: The webhook_code of this AssetsProductReadyWebhook.  # noqa: E501
        :rtype: str
        """
        return self._webhook_code

    @webhook_code.setter
    def webhook_code(self, webhook_code):
        """Sets the webhook_code of this AssetsProductReadyWebhook.

        `PRODUCT_READY`  # noqa: E501

        :param webhook_code: The webhook_code of this AssetsProductReadyWebhook.  # noqa: E501
        :type webhook_code: str
        """

        self._webhook_code = webhook_code

    @property
    def asset_report_id(self):
        """Gets the asset_report_id of this AssetsProductReadyWebhook.  # noqa: E501

        The `asset_report_id` that can be provided to `/asset_report/get` to retrieve the Asset Report.  # noqa: E501

        :return: The asset_report_id of this AssetsProductReadyWebhook.  # noqa: E501
        :rtype: str
        """
        return self._asset_report_id

    @asset_report_id.setter
    def asset_report_id(self, asset_report_id):
        """Sets the asset_report_id of this AssetsProductReadyWebhook.

        The `asset_report_id` that can be provided to `/asset_report/get` to retrieve the Asset Report.  # noqa: E501

        :param asset_report_id: The asset_report_id of this AssetsProductReadyWebhook.  # noqa: E501
        :type asset_report_id: str
        """

        self._asset_report_id = asset_report_id

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
        if not isinstance(other, AssetsProductReadyWebhook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetsProductReadyWebhook):
            return True

        return self.to_dict() != other.to_dict()
