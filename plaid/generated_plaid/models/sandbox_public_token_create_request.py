# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.0.10
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class SandboxPublicTokenCreateRequest(object):
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
        'initial_products': 'list[str]',
        'options': 'SandboxPublicTokenCreateRequestOptions'
    }

    attribute_map = {
        'client_id': 'client_id',
        'secret': 'secret',
        'institution_id': 'institution_id',
        'initial_products': 'initial_products',
        'options': 'options'
    }

    def __init__(self, client_id=None, secret=None, institution_id=None, initial_products=None, options=None, local_vars_configuration=None):  # noqa: E501
        """SandboxPublicTokenCreateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._secret = None
        self._institution_id = None
        self._initial_products = None
        self._options = None
        self.discriminator = None

        self.client_id = client_id
        self.secret = secret
        self.institution_id = institution_id
        self.initial_products = initial_products
        if options is not None:
            self.options = options

    @property
    def client_id(self):
        """Gets the client_id of this SandboxPublicTokenCreateRequest.  # noqa: E501

        Your `client_id`.  # noqa: E501

        :return: The client_id of this SandboxPublicTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this SandboxPublicTokenCreateRequest.

        Your `client_id`.  # noqa: E501

        :param client_id: The client_id of this SandboxPublicTokenCreateRequest.  # noqa: E501
        :type client_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def secret(self):
        """Gets the secret of this SandboxPublicTokenCreateRequest.  # noqa: E501

        Your Plaid API secret.  # noqa: E501

        :return: The secret of this SandboxPublicTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this SandboxPublicTokenCreateRequest.

        Your Plaid API secret.  # noqa: E501

        :param secret: The secret of this SandboxPublicTokenCreateRequest.  # noqa: E501
        :type secret: str
        """
        if self.local_vars_configuration.client_side_validation and secret is None:  # noqa: E501
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def institution_id(self):
        """Gets the institution_id of this SandboxPublicTokenCreateRequest.  # noqa: E501

        The ID of the institution the Item will be associated with  # noqa: E501

        :return: The institution_id of this SandboxPublicTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this SandboxPublicTokenCreateRequest.

        The ID of the institution the Item will be associated with  # noqa: E501

        :param institution_id: The institution_id of this SandboxPublicTokenCreateRequest.  # noqa: E501
        :type institution_id: str
        """
        if self.local_vars_configuration.client_side_validation and institution_id is None:  # noqa: E501
            raise ValueError("Invalid value for `institution_id`, must not be `None`")  # noqa: E501

        self._institution_id = institution_id

    @property
    def initial_products(self):
        """Gets the initial_products of this SandboxPublicTokenCreateRequest.  # noqa: E501

        The products to initially pull for the Item. May be any products that the specified `institution_id`  supports. This array may not be empty.  # noqa: E501

        :return: The initial_products of this SandboxPublicTokenCreateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._initial_products

    @initial_products.setter
    def initial_products(self, initial_products):
        """Sets the initial_products of this SandboxPublicTokenCreateRequest.

        The products to initially pull for the Item. May be any products that the specified `institution_id`  supports. This array may not be empty.  # noqa: E501

        :param initial_products: The initial_products of this SandboxPublicTokenCreateRequest.  # noqa: E501
        :type initial_products: list[str]
        """
        if self.local_vars_configuration.client_side_validation and initial_products is None:  # noqa: E501
            raise ValueError("Invalid value for `initial_products`, must not be `None`")  # noqa: E501

        self._initial_products = initial_products

    @property
    def options(self):
        """Gets the options of this SandboxPublicTokenCreateRequest.  # noqa: E501


        :return: The options of this SandboxPublicTokenCreateRequest.  # noqa: E501
        :rtype: SandboxPublicTokenCreateRequestOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this SandboxPublicTokenCreateRequest.


        :param options: The options of this SandboxPublicTokenCreateRequest.  # noqa: E501
        :type options: SandboxPublicTokenCreateRequestOptions
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
        if not isinstance(other, SandboxPublicTokenCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SandboxPublicTokenCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
