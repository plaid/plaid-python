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


class ServicerAddressData(object):
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
        'city': 'str',
        'region': 'str',
        'street': 'str',
        'postal_code': 'str',
        'country': 'str'
    }

    attribute_map = {
        'city': 'city',
        'region': 'region',
        'street': 'street',
        'postal_code': 'postal_code',
        'country': 'country'
    }

    def __init__(self, city=None, region=None, street=None, postal_code=None, country=None, local_vars_configuration=None):  # noqa: E501
        """ServicerAddressData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._city = None
        self._region = None
        self._street = None
        self._postal_code = None
        self._country = None
        self.discriminator = None

        self.city = city
        self.region = region
        self.street = street
        self.postal_code = postal_code
        self.country = country

    @property
    def city(self):
        """Gets the city of this ServicerAddressData.  # noqa: E501

        The full city name  # noqa: E501

        :return: The city of this ServicerAddressData.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ServicerAddressData.

        The full city name  # noqa: E501

        :param city: The city of this ServicerAddressData.  # noqa: E501
        :type city: str
        """

        self._city = city

    @property
    def region(self):
        """Gets the region of this ServicerAddressData.  # noqa: E501

        The region or state Example: `\"NC\"`  # noqa: E501

        :return: The region of this ServicerAddressData.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ServicerAddressData.

        The region or state Example: `\"NC\"`  # noqa: E501

        :param region: The region of this ServicerAddressData.  # noqa: E501
        :type region: str
        """

        self._region = region

    @property
    def street(self):
        """Gets the street of this ServicerAddressData.  # noqa: E501

        The full street address Example: `\"564 Main Street, APT 15\"` nullable: true  # noqa: E501

        :return: The street of this ServicerAddressData.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this ServicerAddressData.

        The full street address Example: `\"564 Main Street, APT 15\"` nullable: true  # noqa: E501

        :param street: The street of this ServicerAddressData.  # noqa: E501
        :type street: str
        """
        if self.local_vars_configuration.client_side_validation and street is None:  # noqa: E501
            raise ValueError("Invalid value for `street`, must not be `None`")  # noqa: E501

        self._street = street

    @property
    def postal_code(self):
        """Gets the postal_code of this ServicerAddressData.  # noqa: E501

        The postal code  # noqa: E501

        :return: The postal_code of this ServicerAddressData.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this ServicerAddressData.

        The postal code  # noqa: E501

        :param postal_code: The postal_code of this ServicerAddressData.  # noqa: E501
        :type postal_code: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this ServicerAddressData.  # noqa: E501

        The ISO 3166-1 alpha-2 country code  # noqa: E501

        :return: The country of this ServicerAddressData.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ServicerAddressData.

        The ISO 3166-1 alpha-2 country code  # noqa: E501

        :param country: The country of this ServicerAddressData.  # noqa: E501
        :type country: str
        """

        self._country = country

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
        if not isinstance(other, ServicerAddressData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServicerAddressData):
            return True

        return self.to_dict() != other.to_dict()
