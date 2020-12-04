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


class Institution(object):
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
        'institution_id': 'str',
        'name': 'str',
        'products': 'list[Products]',
        'country_codes': 'list[str]',
        'url': 'str',
        'primary_color': 'str',
        'logo': 'str',
        'routing_numbers': 'list[str]',
        'oauth': 'bool',
        'status': 'InstitutionStatus'
    }

    attribute_map = {
        'institution_id': 'institution_id',
        'name': 'name',
        'products': 'products',
        'country_codes': 'country_codes',
        'url': 'url',
        'primary_color': 'primary_color',
        'logo': 'logo',
        'routing_numbers': 'routing_numbers',
        'oauth': 'oauth',
        'status': 'status'
    }

    def __init__(self, institution_id=None, name=None, products=None, country_codes=None, url=None, primary_color=None, logo=None, routing_numbers=None, oauth=None, status=None, local_vars_configuration=None):  # noqa: E501
        """Institution - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._institution_id = None
        self._name = None
        self._products = None
        self._country_codes = None
        self._url = None
        self._primary_color = None
        self._logo = None
        self._routing_numbers = None
        self._oauth = None
        self._status = None
        self.discriminator = None

        if institution_id is not None:
            self.institution_id = institution_id
        if name is not None:
            self.name = name
        if products is not None:
            self.products = products
        if country_codes is not None:
            self.country_codes = country_codes
        self.url = url
        self.primary_color = primary_color
        self.logo = logo
        self.routing_numbers = routing_numbers
        if oauth is not None:
            self.oauth = oauth
        if status is not None:
            self.status = status

    @property
    def institution_id(self):
        """Gets the institution_id of this Institution.  # noqa: E501

        Unique identifier for the institution  # noqa: E501

        :return: The institution_id of this Institution.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this Institution.

        Unique identifier for the institution  # noqa: E501

        :param institution_id: The institution_id of this Institution.  # noqa: E501
        :type institution_id: str
        """

        self._institution_id = institution_id

    @property
    def name(self):
        """Gets the name of this Institution.  # noqa: E501

        The official name of the institution  # noqa: E501

        :return: The name of this Institution.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Institution.

        The official name of the institution  # noqa: E501

        :param name: The name of this Institution.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def products(self):
        """Gets the products of this Institution.  # noqa: E501

        A list of the Plaid products supported by the institution  # noqa: E501

        :return: The products of this Institution.  # noqa: E501
        :rtype: list[Products]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this Institution.

        A list of the Plaid products supported by the institution  # noqa: E501

        :param products: The products of this Institution.  # noqa: E501
        :type products: list[Products]
        """

        self._products = products

    @property
    def country_codes(self):
        """Gets the country_codes of this Institution.  # noqa: E501

        A list of the Plaid products supported by the institution  # noqa: E501

        :return: The country_codes of this Institution.  # noqa: E501
        :rtype: list[str]
        """
        return self._country_codes

    @country_codes.setter
    def country_codes(self, country_codes):
        """Sets the country_codes of this Institution.

        A list of the Plaid products supported by the institution  # noqa: E501

        :param country_codes: The country_codes of this Institution.  # noqa: E501
        :type country_codes: list[str]
        """

        self._country_codes = country_codes

    @property
    def url(self):
        """Gets the url of this Institution.  # noqa: E501

        The URL for the institution's website  # noqa: E501

        :return: The url of this Institution.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Institution.

        The URL for the institution's website  # noqa: E501

        :param url: The url of this Institution.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def primary_color(self):
        """Gets the primary_color of this Institution.  # noqa: E501

        Hexadecimal representation of the primary color used by the institution  # noqa: E501

        :return: The primary_color of this Institution.  # noqa: E501
        :rtype: str
        """
        return self._primary_color

    @primary_color.setter
    def primary_color(self, primary_color):
        """Sets the primary_color of this Institution.

        Hexadecimal representation of the primary color used by the institution  # noqa: E501

        :param primary_color: The primary_color of this Institution.  # noqa: E501
        :type primary_color: str
        """

        self._primary_color = primary_color

    @property
    def logo(self):
        """Gets the logo of this Institution.  # noqa: E501

        Base64 encoded representation of the institution's logo  # noqa: E501

        :return: The logo of this Institution.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Institution.

        Base64 encoded representation of the institution's logo  # noqa: E501

        :param logo: The logo of this Institution.  # noqa: E501
        :type logo: str
        """

        self._logo = logo

    @property
    def routing_numbers(self):
        """Gets the routing_numbers of this Institution.  # noqa: E501

        A partial list of routing numbers associated with the institution. This list is provided for the purpose of looking up institutions by routing number. It is not comprehensive and should never be used as a complete list of routing numbers for an institution.  # noqa: E501

        :return: The routing_numbers of this Institution.  # noqa: E501
        :rtype: list[str]
        """
        return self._routing_numbers

    @routing_numbers.setter
    def routing_numbers(self, routing_numbers):
        """Sets the routing_numbers of this Institution.

        A partial list of routing numbers associated with the institution. This list is provided for the purpose of looking up institutions by routing number. It is not comprehensive and should never be used as a complete list of routing numbers for an institution.  # noqa: E501

        :param routing_numbers: The routing_numbers of this Institution.  # noqa: E501
        :type routing_numbers: list[str]
        """

        self._routing_numbers = routing_numbers

    @property
    def oauth(self):
        """Gets the oauth of this Institution.  # noqa: E501

        Indicates that the institution has an OAuth login flow. This is primarily relevant to institutions with European country codes.  # noqa: E501

        :return: The oauth of this Institution.  # noqa: E501
        :rtype: bool
        """
        return self._oauth

    @oauth.setter
    def oauth(self, oauth):
        """Sets the oauth of this Institution.

        Indicates that the institution has an OAuth login flow. This is primarily relevant to institutions with European country codes.  # noqa: E501

        :param oauth: The oauth of this Institution.  # noqa: E501
        :type oauth: bool
        """

        self._oauth = oauth

    @property
    def status(self):
        """Gets the status of this Institution.  # noqa: E501


        :return: The status of this Institution.  # noqa: E501
        :rtype: InstitutionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Institution.


        :param status: The status of this Institution.  # noqa: E501
        :type status: InstitutionStatus
        """

        self._status = status

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
        if not isinstance(other, Institution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Institution):
            return True

        return self.to_dict() != other.to_dict()
