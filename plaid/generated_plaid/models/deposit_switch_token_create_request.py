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


class DepositSwitchTokenCreateRequest(object):
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
        'deposit_switch_id': 'str'
    }

    attribute_map = {
        'client_id': 'client_id',
        'secret': 'secret',
        'deposit_switch_id': 'deposit_switch_id'
    }

    def __init__(self, client_id=None, secret=None, deposit_switch_id=None, local_vars_configuration=None):  # noqa: E501
        """DepositSwitchTokenCreateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._secret = None
        self._deposit_switch_id = None
        self.discriminator = None

        self.client_id = client_id
        self.secret = secret
        self.deposit_switch_id = deposit_switch_id

    @property
    def client_id(self):
        """Gets the client_id of this DepositSwitchTokenCreateRequest.  # noqa: E501

        Your Plaid API `client_id`.  # noqa: E501

        :return: The client_id of this DepositSwitchTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this DepositSwitchTokenCreateRequest.

        Your Plaid API `client_id`.  # noqa: E501

        :param client_id: The client_id of this DepositSwitchTokenCreateRequest.  # noqa: E501
        :type client_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def secret(self):
        """Gets the secret of this DepositSwitchTokenCreateRequest.  # noqa: E501

        Your Plaid API `secret`.  # noqa: E501

        :return: The secret of this DepositSwitchTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this DepositSwitchTokenCreateRequest.

        Your Plaid API `secret`.  # noqa: E501

        :param secret: The secret of this DepositSwitchTokenCreateRequest.  # noqa: E501
        :type secret: str
        """
        if self.local_vars_configuration.client_side_validation and secret is None:  # noqa: E501
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def deposit_switch_id(self):
        """Gets the deposit_switch_id of this DepositSwitchTokenCreateRequest.  # noqa: E501

        The ID of the Deposit Switch  # noqa: E501

        :return: The deposit_switch_id of this DepositSwitchTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._deposit_switch_id

    @deposit_switch_id.setter
    def deposit_switch_id(self, deposit_switch_id):
        """Sets the deposit_switch_id of this DepositSwitchTokenCreateRequest.

        The ID of the Deposit Switch  # noqa: E501

        :param deposit_switch_id: The deposit_switch_id of this DepositSwitchTokenCreateRequest.  # noqa: E501
        :type deposit_switch_id: str
        """
        if self.local_vars_configuration.client_side_validation and deposit_switch_id is None:  # noqa: E501
            raise ValueError("Invalid value for `deposit_switch_id`, must not be `None`")  # noqa: E501

        self._deposit_switch_id = deposit_switch_id

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
        if not isinstance(other, DepositSwitchTokenCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DepositSwitchTokenCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
