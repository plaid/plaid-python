# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.1.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class ItemStatusInvestments(object):
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
        'last_successful_update': 'str',
        'last_failed_update': 'str'
    }

    attribute_map = {
        'last_successful_update': 'last_successful_update',
        'last_failed_update': 'last_failed_update'
    }

    def __init__(self, last_successful_update=None, last_failed_update=None, local_vars_configuration=None):  # noqa: E501
        """ItemStatusInvestments - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._last_successful_update = None
        self._last_failed_update = None
        self.discriminator = None

        self.last_successful_update = last_successful_update
        self.last_failed_update = last_failed_update

    @property
    def last_successful_update(self):
        """Gets the last_successful_update of this ItemStatusInvestments.  # noqa: E501

        ISO 8601 timestamp of the last successful investments update for the Item. The status will update each time Plaid successfully connects with the institution, regardless of whether any new data is available in the update.  # noqa: E501

        :return: The last_successful_update of this ItemStatusInvestments.  # noqa: E501
        :rtype: str
        """
        return self._last_successful_update

    @last_successful_update.setter
    def last_successful_update(self, last_successful_update):
        """Sets the last_successful_update of this ItemStatusInvestments.

        ISO 8601 timestamp of the last successful investments update for the Item. The status will update each time Plaid successfully connects with the institution, regardless of whether any new data is available in the update.  # noqa: E501

        :param last_successful_update: The last_successful_update of this ItemStatusInvestments.  # noqa: E501
        :type last_successful_update: str
        """

        self._last_successful_update = last_successful_update

    @property
    def last_failed_update(self):
        """Gets the last_failed_update of this ItemStatusInvestments.  # noqa: E501

        ISO 8601 timestamp of the last failed investments update for the Item. The status will update each time Plaid fails an attempt to connect with the institution, regardless of whether any new data is available in the update.  # noqa: E501

        :return: The last_failed_update of this ItemStatusInvestments.  # noqa: E501
        :rtype: str
        """
        return self._last_failed_update

    @last_failed_update.setter
    def last_failed_update(self, last_failed_update):
        """Sets the last_failed_update of this ItemStatusInvestments.

        ISO 8601 timestamp of the last failed investments update for the Item. The status will update each time Plaid fails an attempt to connect with the institution, regardless of whether any new data is available in the update.  # noqa: E501

        :param last_failed_update: The last_failed_update of this ItemStatusInvestments.  # noqa: E501
        :type last_failed_update: str
        """

        self._last_failed_update = last_failed_update

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
        if not isinstance(other, ItemStatusInvestments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemStatusInvestments):
            return True

        return self.to_dict() != other.to_dict()
