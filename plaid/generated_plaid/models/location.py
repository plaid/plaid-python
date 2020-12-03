# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class Location(object):
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
        'address': 'str',
        'city': 'str',
        'region': 'str',
        'postal_code': 'str',
        'country': 'str',
        'lat': 'float',
        'long': 'float',
        'store_number': 'str'
    }

    attribute_map = {
        'address': 'address',
        'city': 'city',
        'region': 'region',
        'postal_code': 'postal_code',
        'country': 'country',
        'lat': 'lat',
        'long': 'long',
        'store_number': 'store_number'
    }

    def __init__(self, address=None, city=None, region=None, postal_code=None, country=None, lat=None, long=None, store_number=None, local_vars_configuration=None):  # noqa: E501
        """Location - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._city = None
        self._region = None
        self._postal_code = None
        self._country = None
        self._lat = None
        self._long = None
        self._store_number = None
        self.discriminator = None

        self.address = address
        self.city = city
        self.region = region
        if postal_code is not None:
            self.postal_code = postal_code
        self.country = country
        self.lat = lat
        self.long = long
        self.store_number = store_number

    @property
    def address(self):
        """Gets the address of this Location.  # noqa: E501

        The street address where the transaction occurred.  # noqa: E501

        :return: The address of this Location.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Location.

        The street address where the transaction occurred.  # noqa: E501

        :param address: The address of this Location.  # noqa: E501
        :type address: str
        """

        self._address = address

    @property
    def city(self):
        """Gets the city of this Location.  # noqa: E501

        The city where the transaction occurred.  # noqa: E501

        :return: The city of this Location.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Location.

        The city where the transaction occurred.  # noqa: E501

        :param city: The city of this Location.  # noqa: E501
        :type city: str
        """

        self._city = city

    @property
    def region(self):
        """Gets the region of this Location.  # noqa: E501

        The region or state where the transaction occurred.  # noqa: E501

        :return: The region of this Location.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Location.

        The region or state where the transaction occurred.  # noqa: E501

        :param region: The region of this Location.  # noqa: E501
        :type region: str
        """

        self._region = region

    @property
    def postal_code(self):
        """Gets the postal_code of this Location.  # noqa: E501

        The postal code where the transaction occurred.  # noqa: E501

        :return: The postal_code of this Location.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Location.

        The postal code where the transaction occurred.  # noqa: E501

        :param postal_code: The postal_code of this Location.  # noqa: E501
        :type postal_code: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this Location.  # noqa: E501

        The ISO 3166-1 alpha-2 country code where the transaction occurred.  # noqa: E501

        :return: The country of this Location.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Location.

        The ISO 3166-1 alpha-2 country code where the transaction occurred.  # noqa: E501

        :param country: The country of this Location.  # noqa: E501
        :type country: str
        """

        self._country = country

    @property
    def lat(self):
        """Gets the lat of this Location.  # noqa: E501

        The latitude where the transaction occurred.  # noqa: E501

        :return: The lat of this Location.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this Location.

        The latitude where the transaction occurred.  # noqa: E501

        :param lat: The lat of this Location.  # noqa: E501
        :type lat: float
        """

        self._lat = lat

    @property
    def long(self):
        """Gets the long of this Location.  # noqa: E501

        The longitude where the transaction occurred.  # noqa: E501

        :return: The long of this Location.  # noqa: E501
        :rtype: float
        """
        return self._long

    @long.setter
    def long(self, long):
        """Sets the long of this Location.

        The longitude where the transaction occurred.  # noqa: E501

        :param long: The long of this Location.  # noqa: E501
        :type long: float
        """

        self._long = long

    @property
    def store_number(self):
        """Gets the store_number of this Location.  # noqa: E501

        The merchant defined store number where the transaction occurred.  # noqa: E501

        :return: The store_number of this Location.  # noqa: E501
        :rtype: str
        """
        return self._store_number

    @store_number.setter
    def store_number(self, store_number):
        """Sets the store_number of this Location.

        The merchant defined store number where the transaction occurred.  # noqa: E501

        :param store_number: The store_number of this Location.  # noqa: E501
        :type store_number: str
        """

        self._store_number = store_number

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
        if not isinstance(other, Location):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Location):
            return True

        return self.to_dict() != other.to_dict()
