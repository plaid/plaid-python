# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    <!--
    Prevent massive diffs on generated code.

    The version of the OpenAPI document: 2020-09-14_1.1.1
     -->
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class DepositSwitchCreateRequest(object):
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
        'target_access_token': 'str',
        'target_account_id': 'str'
    }

    attribute_map = {
        'client_id': 'client_id',
        'secret': 'secret',
        'target_access_token': 'target_access_token',
        'target_account_id': 'target_account_id'
    }

    def __init__(self, client_id=None, secret=None, target_access_token=None, target_account_id=None, local_vars_configuration=None):  # noqa: E501
        """DepositSwitchCreateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._secret = None
        self._target_access_token = None
        self._target_account_id = None
        self.discriminator = None

        self.client_id = client_id
        self.secret = secret
        self.target_access_token = target_access_token
        self.target_account_id = target_account_id

    @property
    def client_id(self):
        """Gets the client_id of this DepositSwitchCreateRequest.  # noqa: E501

        Your Plaid API `client_id`.  # noqa: E501

        :return: The client_id of this DepositSwitchCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this DepositSwitchCreateRequest.

        Your Plaid API `client_id`.  # noqa: E501

        :param client_id: The client_id of this DepositSwitchCreateRequest.  # noqa: E501
        :type client_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def secret(self):
        """Gets the secret of this DepositSwitchCreateRequest.  # noqa: E501

        Your Plaid API `secret`.  # noqa: E501

        :return: The secret of this DepositSwitchCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this DepositSwitchCreateRequest.

        Your Plaid API `secret`.  # noqa: E501

        :param secret: The secret of this DepositSwitchCreateRequest.  # noqa: E501
        :type secret: str
        """
        if self.local_vars_configuration.client_side_validation and secret is None:  # noqa: E501
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def target_access_token(self):
        """Gets the target_access_token of this DepositSwitchCreateRequest.  # noqa: E501

        Access token for the target Item, typically provided in the Import Item response.   # noqa: E501

        :return: The target_access_token of this DepositSwitchCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_access_token

    @target_access_token.setter
    def target_access_token(self, target_access_token):
        """Sets the target_access_token of this DepositSwitchCreateRequest.

        Access token for the target Item, typically provided in the Import Item response.   # noqa: E501

        :param target_access_token: The target_access_token of this DepositSwitchCreateRequest.  # noqa: E501
        :type target_access_token: str
        """
        if self.local_vars_configuration.client_side_validation and target_access_token is None:  # noqa: E501
            raise ValueError("Invalid value for `target_access_token`, must not be `None`")  # noqa: E501

        self._target_access_token = target_access_token

    @property
    def target_account_id(self):
        """Gets the target_account_id of this DepositSwitchCreateRequest.  # noqa: E501

        Plaid Account ID that specifies the target bank account. This account will become the recipient for a user's direct deposit.  # noqa: E501

        :return: The target_account_id of this DepositSwitchCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_account_id

    @target_account_id.setter
    def target_account_id(self, target_account_id):
        """Sets the target_account_id of this DepositSwitchCreateRequest.

        Plaid Account ID that specifies the target bank account. This account will become the recipient for a user's direct deposit.  # noqa: E501

        :param target_account_id: The target_account_id of this DepositSwitchCreateRequest.  # noqa: E501
        :type target_account_id: str
        """
        if self.local_vars_configuration.client_side_validation and target_account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `target_account_id`, must not be `None`")  # noqa: E501

        self._target_account_id = target_account_id

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
        if not isinstance(other, DepositSwitchCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DepositSwitchCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
