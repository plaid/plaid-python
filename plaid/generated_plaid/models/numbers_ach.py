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


class NumbersACH(object):
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
        'account_id': 'str',
        'account': 'str',
        'routing': 'str',
        'wire_routing': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account': 'account',
        'routing': 'routing',
        'wire_routing': 'wire_routing'
    }

    def __init__(self, account_id=None, account=None, routing=None, wire_routing=None, local_vars_configuration=None):  # noqa: E501
        """NumbersACH - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._account = None
        self._routing = None
        self._wire_routing = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account is not None:
            self.account = account
        if routing is not None:
            self.routing = routing
        self.wire_routing = wire_routing

    @property
    def account_id(self):
        """Gets the account_id of this NumbersACH.  # noqa: E501

        The Plaid account ID associated with the account numbers  # noqa: E501

        :return: The account_id of this NumbersACH.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this NumbersACH.

        The Plaid account ID associated with the account numbers  # noqa: E501

        :param account_id: The account_id of this NumbersACH.  # noqa: E501
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def account(self):
        """Gets the account of this NumbersACH.  # noqa: E501

        The ACH account number for the account  # noqa: E501

        :return: The account of this NumbersACH.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this NumbersACH.

        The ACH account number for the account  # noqa: E501

        :param account: The account of this NumbersACH.  # noqa: E501
        :type account: str
        """

        self._account = account

    @property
    def routing(self):
        """Gets the routing of this NumbersACH.  # noqa: E501

        The ACH routing number for the account  # noqa: E501

        :return: The routing of this NumbersACH.  # noqa: E501
        :rtype: str
        """
        return self._routing

    @routing.setter
    def routing(self, routing):
        """Sets the routing of this NumbersACH.

        The ACH routing number for the account  # noqa: E501

        :param routing: The routing of this NumbersACH.  # noqa: E501
        :type routing: str
        """

        self._routing = routing

    @property
    def wire_routing(self):
        """Gets the wire_routing of this NumbersACH.  # noqa: E501

        The wire transfer routing number for the account, if available  # noqa: E501

        :return: The wire_routing of this NumbersACH.  # noqa: E501
        :rtype: str
        """
        return self._wire_routing

    @wire_routing.setter
    def wire_routing(self, wire_routing):
        """Sets the wire_routing of this NumbersACH.

        The wire transfer routing number for the account, if available  # noqa: E501

        :param wire_routing: The wire_routing of this NumbersACH.  # noqa: E501
        :type wire_routing: str
        """

        self._wire_routing = wire_routing

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
        if not isinstance(other, NumbersACH):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NumbersACH):
            return True

        return self.to_dict() != other.to_dict()
