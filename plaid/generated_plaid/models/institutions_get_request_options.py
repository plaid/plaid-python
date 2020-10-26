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


class InstitutionsGetRequestOptions(object):
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
        'products': 'list[str]',
        'routing_numbers': 'list[str]',
        'oauth': 'bool',
        'include_optional_metadata': 'bool'
    }

    attribute_map = {
        'products': 'products',
        'routing_numbers': 'routing_numbers',
        'oauth': 'oauth',
        'include_optional_metadata': 'include_optional_metadata'
    }

    def __init__(self, products=None, routing_numbers=None, oauth=None, include_optional_metadata=None, local_vars_configuration=None):  # noqa: E501
        """InstitutionsGetRequestOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._products = None
        self._routing_numbers = None
        self._oauth = None
        self._include_optional_metadata = None
        self.discriminator = None

        if products is not None:
            self.products = products
        if routing_numbers is not None:
            self.routing_numbers = routing_numbers
        if oauth is not None:
            self.oauth = oauth
        if include_optional_metadata is not None:
            self.include_optional_metadata = include_optional_metadata

    @property
    def products(self):
        """Gets the products of this InstitutionsGetRequestOptions.  # noqa: E501

        Filter the Institutions based on which products they support.   # noqa: E501

        :return: The products of this InstitutionsGetRequestOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this InstitutionsGetRequestOptions.

        Filter the Institutions based on which products they support.   # noqa: E501

        :param products: The products of this InstitutionsGetRequestOptions.  # noqa: E501
        :type products: list[str]
        """

        self._products = products

    @property
    def routing_numbers(self):
        """Gets the routing_numbers of this InstitutionsGetRequestOptions.  # noqa: E501

        Specify an array of routing numbers to filter institutions.  # noqa: E501

        :return: The routing_numbers of this InstitutionsGetRequestOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._routing_numbers

    @routing_numbers.setter
    def routing_numbers(self, routing_numbers):
        """Sets the routing_numbers of this InstitutionsGetRequestOptions.

        Specify an array of routing numbers to filter institutions.  # noqa: E501

        :param routing_numbers: The routing_numbers of this InstitutionsGetRequestOptions.  # noqa: E501
        :type routing_numbers: list[str]
        """

        self._routing_numbers = routing_numbers

    @property
    def oauth(self):
        """Gets the oauth of this InstitutionsGetRequestOptions.  # noqa: E501

        Limit results to institutions with or without OAuth login flows. This is primarily relevant to institutions with European country codes.  # noqa: E501

        :return: The oauth of this InstitutionsGetRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._oauth

    @oauth.setter
    def oauth(self, oauth):
        """Sets the oauth of this InstitutionsGetRequestOptions.

        Limit results to institutions with or without OAuth login flows. This is primarily relevant to institutions with European country codes.  # noqa: E501

        :param oauth: The oauth of this InstitutionsGetRequestOptions.  # noqa: E501
        :type oauth: bool
        """

        self._oauth = oauth

    @property
    def include_optional_metadata(self):
        """Gets the include_optional_metadata of this InstitutionsGetRequestOptions.  # noqa: E501

        When `true`, return the institution's homepage URL, logo and primary brand color.   Note that Plaid does not own any of the logos shared by the API, and that by accessing or using these logos, you agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied warranties with respect to the logos.  # noqa: E501

        :return: The include_optional_metadata of this InstitutionsGetRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._include_optional_metadata

    @include_optional_metadata.setter
    def include_optional_metadata(self, include_optional_metadata):
        """Sets the include_optional_metadata of this InstitutionsGetRequestOptions.

        When `true`, return the institution's homepage URL, logo and primary brand color.   Note that Plaid does not own any of the logos shared by the API, and that by accessing or using these logos, you agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied warranties with respect to the logos.  # noqa: E501

        :param include_optional_metadata: The include_optional_metadata of this InstitutionsGetRequestOptions.  # noqa: E501
        :type include_optional_metadata: bool
        """

        self._include_optional_metadata = include_optional_metadata

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
        if not isinstance(other, InstitutionsGetRequestOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstitutionsGetRequestOptions):
            return True

        return self.to_dict() != other.to_dict()
