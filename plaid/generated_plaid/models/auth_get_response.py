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


class AuthGetResponse(object):
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
        'accounts': 'list[AccountBase]',
        'numbers': 'AuthGetNumbers',
        'item': 'Item',
        'request_id': 'str'
    }

    attribute_map = {
        'accounts': 'accounts',
        'numbers': 'numbers',
        'item': 'item',
        'request_id': 'request_id'
    }

    def __init__(self, accounts=None, numbers=None, item=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """AuthGetResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._accounts = None
        self._numbers = None
        self._item = None
        self._request_id = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if numbers is not None:
            self.numbers = numbers
        if item is not None:
            self.item = item
        if request_id is not None:
            self.request_id = request_id

    @property
    def accounts(self):
        """Gets the accounts of this AuthGetResponse.  # noqa: E501

        The `accounts` for which numbers are being retrieved.  # noqa: E501

        :return: The accounts of this AuthGetResponse.  # noqa: E501
        :rtype: list[AccountBase]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this AuthGetResponse.

        The `accounts` for which numbers are being retrieved.  # noqa: E501

        :param accounts: The accounts of this AuthGetResponse.  # noqa: E501
        :type accounts: list[AccountBase]
        """

        self._accounts = accounts

    @property
    def numbers(self):
        """Gets the numbers of this AuthGetResponse.  # noqa: E501


        :return: The numbers of this AuthGetResponse.  # noqa: E501
        :rtype: AuthGetNumbers
        """
        return self._numbers

    @numbers.setter
    def numbers(self, numbers):
        """Sets the numbers of this AuthGetResponse.


        :param numbers: The numbers of this AuthGetResponse.  # noqa: E501
        :type numbers: AuthGetNumbers
        """

        self._numbers = numbers

    @property
    def item(self):
        """Gets the item of this AuthGetResponse.  # noqa: E501


        :return: The item of this AuthGetResponse.  # noqa: E501
        :rtype: Item
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this AuthGetResponse.


        :param item: The item of this AuthGetResponse.  # noqa: E501
        :type item: Item
        """

        self._item = item

    @property
    def request_id(self):
        """Gets the request_id of this AuthGetResponse.  # noqa: E501

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :return: The request_id of this AuthGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this AuthGetResponse.

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :param request_id: The request_id of this AuthGetResponse.  # noqa: E501
        :type request_id: str
        """

        self._request_id = request_id

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
        if not isinstance(other, AuthGetResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthGetResponse):
            return True

        return self.to_dict() != other.to_dict()
