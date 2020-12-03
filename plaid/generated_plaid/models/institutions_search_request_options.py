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


class InstitutionsSearchRequestOptions(object):
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
        'oauth': 'bool',
        'include_optional_metadata': 'bool'
    }

    attribute_map = {
        'oauth': 'oauth',
        'include_optional_metadata': 'include_optional_metadata'
    }

    def __init__(self, oauth=None, include_optional_metadata=None, local_vars_configuration=None):  # noqa: E501
        """InstitutionsSearchRequestOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._oauth = None
        self._include_optional_metadata = None
        self.discriminator = None

        if oauth is not None:
            self.oauth = oauth
        if include_optional_metadata is not None:
            self.include_optional_metadata = include_optional_metadata

    @property
    def oauth(self):
        """Gets the oauth of this InstitutionsSearchRequestOptions.  # noqa: E501

        Limit results to institutions with or without OAuth login flows. This is primarily relevant to institutions with European country codes  # noqa: E501

        :return: The oauth of this InstitutionsSearchRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._oauth

    @oauth.setter
    def oauth(self, oauth):
        """Sets the oauth of this InstitutionsSearchRequestOptions.

        Limit results to institutions with or without OAuth login flows. This is primarily relevant to institutions with European country codes  # noqa: E501

        :param oauth: The oauth of this InstitutionsSearchRequestOptions.  # noqa: E501
        :type oauth: bool
        """

        self._oauth = oauth

    @property
    def include_optional_metadata(self):
        """Gets the include_optional_metadata of this InstitutionsSearchRequestOptions.  # noqa: E501

        When true, return the institution's homepage URL, logo and primary brand color. Learn more  # noqa: E501

        :return: The include_optional_metadata of this InstitutionsSearchRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._include_optional_metadata

    @include_optional_metadata.setter
    def include_optional_metadata(self, include_optional_metadata):
        """Sets the include_optional_metadata of this InstitutionsSearchRequestOptions.

        When true, return the institution's homepage URL, logo and primary brand color. Learn more  # noqa: E501

        :param include_optional_metadata: The include_optional_metadata of this InstitutionsSearchRequestOptions.  # noqa: E501
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
        if not isinstance(other, InstitutionsSearchRequestOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstitutionsSearchRequestOptions):
            return True

        return self.to_dict() != other.to_dict()
