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


class Meta(object):
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
        'name': 'str',
        'official_name': 'str',
        'limit': 'float'
    }

    attribute_map = {
        'name': 'name',
        'official_name': 'official_name',
        'limit': 'limit'
    }

    def __init__(self, name=None, official_name=None, limit=None, local_vars_configuration=None):  # noqa: E501
        """Meta - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._official_name = None
        self._limit = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if official_name is not None:
            self.official_name = official_name
        if limit is not None:
            self.limit = limit

    @property
    def name(self):
        """Gets the name of this Meta.  # noqa: E501

        The account's name  # noqa: E501

        :return: The name of this Meta.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Meta.

        The account's name  # noqa: E501

        :param name: The name of this Meta.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def official_name(self):
        """Gets the official_name of this Meta.  # noqa: E501

        The account's official name  # noqa: E501

        :return: The official_name of this Meta.  # noqa: E501
        :rtype: str
        """
        return self._official_name

    @official_name.setter
    def official_name(self, official_name):
        """Sets the official_name of this Meta.

        The account's official name  # noqa: E501

        :param official_name: The official_name of this Meta.  # noqa: E501
        :type official_name: str
        """

        self._official_name = official_name

    @property
    def limit(self):
        """Gets the limit of this Meta.  # noqa: E501

        The account's limit  # noqa: E501

        :return: The limit of this Meta.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this Meta.

        The account's limit  # noqa: E501

        :param limit: The limit of this Meta.  # noqa: E501
        :type limit: float
        """

        self._limit = limit

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
        if not isinstance(other, Meta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Meta):
            return True

        return self.to_dict() != other.to_dict()
