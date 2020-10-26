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


class SandboxItemSetVerificationStatusRequest(object):
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
        'access_token': 'str',
        'account_id': 'str',
        'verification_status': 'str'
    }

    attribute_map = {
        'client_id': 'client_id',
        'secret': 'secret',
        'access_token': 'access_token',
        'account_id': 'account_id',
        'verification_status': 'verification_status'
    }

    def __init__(self, client_id=None, secret=None, access_token=None, account_id=None, verification_status=None, local_vars_configuration=None):  # noqa: E501
        """SandboxItemSetVerificationStatusRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._secret = None
        self._access_token = None
        self._account_id = None
        self._verification_status = None
        self.discriminator = None

        self.client_id = client_id
        self.secret = secret
        self.access_token = access_token
        self.account_id = account_id
        self.verification_status = verification_status

    @property
    def client_id(self):
        """Gets the client_id of this SandboxItemSetVerificationStatusRequest.  # noqa: E501

        Your Plaid API `client_id`.  # noqa: E501

        :return: The client_id of this SandboxItemSetVerificationStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this SandboxItemSetVerificationStatusRequest.

        Your Plaid API `client_id`.  # noqa: E501

        :param client_id: The client_id of this SandboxItemSetVerificationStatusRequest.  # noqa: E501
        :type client_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def secret(self):
        """Gets the secret of this SandboxItemSetVerificationStatusRequest.  # noqa: E501

        Your Plaid API `secret`.  # noqa: E501

        :return: The secret of this SandboxItemSetVerificationStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this SandboxItemSetVerificationStatusRequest.

        Your Plaid API `secret`.  # noqa: E501

        :param secret: The secret of this SandboxItemSetVerificationStatusRequest.  # noqa: E501
        :type secret: str
        """
        if self.local_vars_configuration.client_side_validation and secret is None:  # noqa: E501
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def access_token(self):
        """Gets the access_token of this SandboxItemSetVerificationStatusRequest.  # noqa: E501

        The access token associated with the Item data is being requested for.  # noqa: E501

        :return: The access_token of this SandboxItemSetVerificationStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this SandboxItemSetVerificationStatusRequest.

        The access token associated with the Item data is being requested for.  # noqa: E501

        :param access_token: The access_token of this SandboxItemSetVerificationStatusRequest.  # noqa: E501
        :type access_token: str
        """
        if self.local_vars_configuration.client_side_validation and access_token is None:  # noqa: E501
            raise ValueError("Invalid value for `access_token`, must not be `None`")  # noqa: E501

        self._access_token = access_token

    @property
    def account_id(self):
        """Gets the account_id of this SandboxItemSetVerificationStatusRequest.  # noqa: E501

        The `account_id` of the account whose verification status is to be modified  # noqa: E501

        :return: The account_id of this SandboxItemSetVerificationStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this SandboxItemSetVerificationStatusRequest.

        The `account_id` of the account whose verification status is to be modified  # noqa: E501

        :param account_id: The account_id of this SandboxItemSetVerificationStatusRequest.  # noqa: E501
        :type account_id: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def verification_status(self):
        """Gets the verification_status of this SandboxItemSetVerificationStatusRequest.  # noqa: E501

        The verification status to set the account to. One of `\"automatically_verified\"` or `\"verification_expired\"`.  # noqa: E501

        :return: The verification_status of this SandboxItemSetVerificationStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._verification_status

    @verification_status.setter
    def verification_status(self, verification_status):
        """Sets the verification_status of this SandboxItemSetVerificationStatusRequest.

        The verification status to set the account to. One of `\"automatically_verified\"` or `\"verification_expired\"`.  # noqa: E501

        :param verification_status: The verification_status of this SandboxItemSetVerificationStatusRequest.  # noqa: E501
        :type verification_status: str
        """
        if self.local_vars_configuration.client_side_validation and verification_status is None:  # noqa: E501
            raise ValueError("Invalid value for `verification_status`, must not be `None`")  # noqa: E501

        self._verification_status = verification_status

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
        if not isinstance(other, SandboxItemSetVerificationStatusRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SandboxItemSetVerificationStatusRequest):
            return True

        return self.to_dict() != other.to_dict()
