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


class PaymentInitiationAddress(object):
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
        'street': 'list[str]',
        'city': 'str',
        'postal_code': 'str',
        'country': 'str'
    }

    attribute_map = {
        'street': 'street',
        'city': 'city',
        'postal_code': 'postal_code',
        'country': 'country'
    }

    def __init__(self, street=None, city=None, postal_code=None, country=None, local_vars_configuration=None):  # noqa: E501
        """PaymentInitiationAddress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._street = None
        self._city = None
        self._postal_code = None
        self._country = None
        self.discriminator = None

        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.country = country

    @property
    def street(self):
        """Gets the street of this PaymentInitiationAddress.  # noqa: E501

        An array of length 1-2 representing the street address where the recipient is located.  # noqa: E501

        :return: The street of this PaymentInitiationAddress.  # noqa: E501
        :rtype: list[str]
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this PaymentInitiationAddress.

        An array of length 1-2 representing the street address where the recipient is located.  # noqa: E501

        :param street: The street of this PaymentInitiationAddress.  # noqa: E501
        :type street: list[str]
        """
        if self.local_vars_configuration.client_side_validation and street is None:  # noqa: E501
            raise ValueError("Invalid value for `street`, must not be `None`")  # noqa: E501

        self._street = street

    @property
    def city(self):
        """Gets the city of this PaymentInitiationAddress.  # noqa: E501

        The city where the recipient is located.  # noqa: E501

        :return: The city of this PaymentInitiationAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this PaymentInitiationAddress.

        The city where the recipient is located.  # noqa: E501

        :param city: The city of this PaymentInitiationAddress.  # noqa: E501
        :type city: str
        """
        if self.local_vars_configuration.client_side_validation and city is None:  # noqa: E501
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def postal_code(self):
        """Gets the postal_code of this PaymentInitiationAddress.  # noqa: E501

        The postal code where the recipient is located.  # noqa: E501

        :return: The postal_code of this PaymentInitiationAddress.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this PaymentInitiationAddress.

        The postal code where the recipient is located.  # noqa: E501

        :param postal_code: The postal_code of this PaymentInitiationAddress.  # noqa: E501
        :type postal_code: str
        """
        if self.local_vars_configuration.client_side_validation and postal_code is None:  # noqa: E501
            raise ValueError("Invalid value for `postal_code`, must not be `None`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this PaymentInitiationAddress.  # noqa: E501

        The ISO 3166-1 alpha-2 country code where the recipient is located.  # noqa: E501

        :return: The country of this PaymentInitiationAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PaymentInitiationAddress.

        The ISO 3166-1 alpha-2 country code where the recipient is located.  # noqa: E501

        :param country: The country of this PaymentInitiationAddress.  # noqa: E501
        :type country: str
        """
        if self.local_vars_configuration.client_side_validation and country is None:  # noqa: E501
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, PaymentInitiationAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentInitiationAddress):
            return True

        return self.to_dict() != other.to_dict()
