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


class LinkTokenGetResponse(object):
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
        'link_token': 'str',
        'created_at': 'str',
        'expiration': 'str',
        'metadata': 'LinkTokenGetResponseMetadata'
    }

    attribute_map = {
        'link_token': 'link_token',
        'created_at': 'created_at',
        'expiration': 'expiration',
        'metadata': 'metadata'
    }

    def __init__(self, link_token=None, created_at=None, expiration=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """LinkTokenGetResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._link_token = None
        self._created_at = None
        self._expiration = None
        self._metadata = None
        self.discriminator = None

        if link_token is not None:
            self.link_token = link_token
        if created_at is not None:
            self.created_at = created_at
        if expiration is not None:
            self.expiration = expiration
        if metadata is not None:
            self.metadata = metadata

    @property
    def link_token(self):
        """Gets the link_token of this LinkTokenGetResponse.  # noqa: E501

        A `link_token`, which can be supplied to Link in order to initialize it and receive a `public_token`, which can be exchanged for an `access_token`.  # noqa: E501

        :return: The link_token of this LinkTokenGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._link_token

    @link_token.setter
    def link_token(self, link_token):
        """Sets the link_token of this LinkTokenGetResponse.

        A `link_token`, which can be supplied to Link in order to initialize it and receive a `public_token`, which can be exchanged for an `access_token`.  # noqa: E501

        :param link_token: The link_token of this LinkTokenGetResponse.  # noqa: E501
        :type link_token: str
        """

        self._link_token = link_token

    @property
    def created_at(self):
        """Gets the created_at of this LinkTokenGetResponse.  # noqa: E501

        The creation date for the `link_token`, in ISO 8601 format.  # noqa: E501

        :return: The created_at of this LinkTokenGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LinkTokenGetResponse.

        The creation date for the `link_token`, in ISO 8601 format.  # noqa: E501

        :param created_at: The created_at of this LinkTokenGetResponse.  # noqa: E501
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def expiration(self):
        """Gets the expiration of this LinkTokenGetResponse.  # noqa: E501

        The expiration date for the `link_token`, in ISO 8601 format.  # noqa: E501

        :return: The expiration of this LinkTokenGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this LinkTokenGetResponse.

        The expiration date for the `link_token`, in ISO 8601 format.  # noqa: E501

        :param expiration: The expiration of this LinkTokenGetResponse.  # noqa: E501
        :type expiration: str
        """

        self._expiration = expiration

    @property
    def metadata(self):
        """Gets the metadata of this LinkTokenGetResponse.  # noqa: E501


        :return: The metadata of this LinkTokenGetResponse.  # noqa: E501
        :rtype: LinkTokenGetResponseMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this LinkTokenGetResponse.


        :param metadata: The metadata of this LinkTokenGetResponse.  # noqa: E501
        :type metadata: LinkTokenGetResponseMetadata
        """

        self._metadata = metadata

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
        if not isinstance(other, LinkTokenGetResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LinkTokenGetResponse):
            return True

        return self.to_dict() != other.to_dict()
