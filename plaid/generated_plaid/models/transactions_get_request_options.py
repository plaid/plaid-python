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


class TransactionsGetRequestOptions(object):
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
        'account_ids': 'list[str]',
        'count': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'account_ids': 'account_ids',
        'count': 'count',
        'offset': 'offset'
    }

    def __init__(self, account_ids=None, count=100, offset=0, local_vars_configuration=None):  # noqa: E501
        """TransactionsGetRequestOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_ids = None
        self._count = None
        self._offset = None
        self.discriminator = None

        if account_ids is not None:
            self.account_ids = account_ids
        if count is not None:
            self.count = count
        if offset is not None:
            self.offset = offset

    @property
    def account_ids(self):
        """Gets the account_ids of this TransactionsGetRequestOptions.  # noqa: E501

        A list of `account_ids` to retrieve for the Item  Note: An error will be returned if a provided `account_id` is not associated with the Item.  # noqa: E501

        :return: The account_ids of this TransactionsGetRequestOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._account_ids

    @account_ids.setter
    def account_ids(self, account_ids):
        """Sets the account_ids of this TransactionsGetRequestOptions.

        A list of `account_ids` to retrieve for the Item  Note: An error will be returned if a provided `account_id` is not associated with the Item.  # noqa: E501

        :param account_ids: The account_ids of this TransactionsGetRequestOptions.  # noqa: E501
        :type account_ids: list[str]
        """

        self._account_ids = account_ids

    @property
    def count(self):
        """Gets the count of this TransactionsGetRequestOptions.  # noqa: E501

        The number of transactions to fetch.  # noqa: E501

        :return: The count of this TransactionsGetRequestOptions.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this TransactionsGetRequestOptions.

        The number of transactions to fetch.  # noqa: E501

        :param count: The count of this TransactionsGetRequestOptions.  # noqa: E501
        :type count: int
        """
        if (self.local_vars_configuration.client_side_validation and
                count is not None and count > 500):  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value less than or equal to `500`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                count is not None and count < 0):  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._count = count

    @property
    def offset(self):
        """Gets the offset of this TransactionsGetRequestOptions.  # noqa: E501

        The number of transactions to skip. The default value is 0.  # noqa: E501

        :return: The offset of this TransactionsGetRequestOptions.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TransactionsGetRequestOptions.

        The number of transactions to skip. The default value is 0.  # noqa: E501

        :param offset: The offset of this TransactionsGetRequestOptions.  # noqa: E501
        :type offset: int
        """
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset < 0):  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

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
        if not isinstance(other, TransactionsGetRequestOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionsGetRequestOptions):
            return True

        return self.to_dict() != other.to_dict()
