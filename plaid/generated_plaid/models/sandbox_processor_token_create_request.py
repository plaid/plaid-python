# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class SandboxProcessorTokenCreateRequest(object):
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
        'client_id': 'str',
        'secret': 'str',
        'institution_id': 'str',
        'options': 'SandboxProcessorTokenCreateRequestOptions'
    }

    attribute_map = {
        'client_id': 'client_id',
        'secret': 'secret',
        'institution_id': 'institution_id',
        'options': 'options'
    }

    def __init__(self, client_id=None, secret=None, institution_id=None, options=None, local_vars_configuration=None):  # noqa: E501
        """SandboxProcessorTokenCreateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._secret = None
        self._institution_id = None
        self._options = None
        self.discriminator = None

        self.client_id = client_id
        self.secret = secret
        self.institution_id = institution_id
        if options is not None:
            self.options = options

    @property
    def client_id(self):
        """Gets the client_id of this SandboxProcessorTokenCreateRequest.  # noqa: E501

        Your Plaid API `client_id`.  # noqa: E501

        :return: The client_id of this SandboxProcessorTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this SandboxProcessorTokenCreateRequest.

        Your Plaid API `client_id`.  # noqa: E501

        :param client_id: The client_id of this SandboxProcessorTokenCreateRequest.  # noqa: E501
        :type client_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def secret(self):
        """Gets the secret of this SandboxProcessorTokenCreateRequest.  # noqa: E501

        Your Plaid API `secret`.  # noqa: E501

        :return: The secret of this SandboxProcessorTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this SandboxProcessorTokenCreateRequest.

        Your Plaid API `secret`.  # noqa: E501

        :param secret: The secret of this SandboxProcessorTokenCreateRequest.  # noqa: E501
        :type secret: str
        """
        if self.local_vars_configuration.client_side_validation and secret is None:  # noqa: E501
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def institution_id(self):
        """Gets the institution_id of this SandboxProcessorTokenCreateRequest.  # noqa: E501

        The ID of the institution the Item will be associated with  # noqa: E501

        :return: The institution_id of this SandboxProcessorTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this SandboxProcessorTokenCreateRequest.

        The ID of the institution the Item will be associated with  # noqa: E501

        :param institution_id: The institution_id of this SandboxProcessorTokenCreateRequest.  # noqa: E501
        :type institution_id: str
        """
        if self.local_vars_configuration.client_side_validation and institution_id is None:  # noqa: E501
            raise ValueError("Invalid value for `institution_id`, must not be `None`")  # noqa: E501

        self._institution_id = institution_id

    @property
    def options(self):
        """Gets the options of this SandboxProcessorTokenCreateRequest.  # noqa: E501


        :return: The options of this SandboxProcessorTokenCreateRequest.  # noqa: E501
        :rtype: SandboxProcessorTokenCreateRequestOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this SandboxProcessorTokenCreateRequest.


        :param options: The options of this SandboxProcessorTokenCreateRequest.  # noqa: E501
        :type options: SandboxProcessorTokenCreateRequestOptions
        """

        self._options = options

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
        if not isinstance(other, SandboxProcessorTokenCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SandboxProcessorTokenCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
