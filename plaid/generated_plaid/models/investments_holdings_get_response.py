# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.1.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class InvestmentsHoldingsGetResponse(object):
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
        'holdings': 'list[Holding]',
        'securities': 'list[Security]',
        'item': 'Item',
        'request_id': 'str'
    }

    attribute_map = {
        'accounts': 'accounts',
        'holdings': 'holdings',
        'securities': 'securities',
        'item': 'item',
        'request_id': 'request_id'
    }

    def __init__(self, accounts=None, holdings=None, securities=None, item=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """InvestmentsHoldingsGetResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._accounts = None
        self._holdings = None
        self._securities = None
        self._item = None
        self._request_id = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if holdings is not None:
            self.holdings = holdings
        if securities is not None:
            self.securities = securities
        if item is not None:
            self.item = item
        if request_id is not None:
            self.request_id = request_id

    @property
    def accounts(self):
        """Gets the accounts of this InvestmentsHoldingsGetResponse.  # noqa: E501

        The accounts associated with the Item  # noqa: E501

        :return: The accounts of this InvestmentsHoldingsGetResponse.  # noqa: E501
        :rtype: list[AccountBase]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this InvestmentsHoldingsGetResponse.

        The accounts associated with the Item  # noqa: E501

        :param accounts: The accounts of this InvestmentsHoldingsGetResponse.  # noqa: E501
        :type accounts: list[AccountBase]
        """

        self._accounts = accounts

    @property
    def holdings(self):
        """Gets the holdings of this InvestmentsHoldingsGetResponse.  # noqa: E501

        The holdings belonging to investment accounts associated with the Item. Details of the securities in the holdings are provided in the `securities` field.   # noqa: E501

        :return: The holdings of this InvestmentsHoldingsGetResponse.  # noqa: E501
        :rtype: list[Holding]
        """
        return self._holdings

    @holdings.setter
    def holdings(self, holdings):
        """Sets the holdings of this InvestmentsHoldingsGetResponse.

        The holdings belonging to investment accounts associated with the Item. Details of the securities in the holdings are provided in the `securities` field.   # noqa: E501

        :param holdings: The holdings of this InvestmentsHoldingsGetResponse.  # noqa: E501
        :type holdings: list[Holding]
        """

        self._holdings = holdings

    @property
    def securities(self):
        """Gets the securities of this InvestmentsHoldingsGetResponse.  # noqa: E501

        Objects describing the securities held in the accounts associated with the Item.   # noqa: E501

        :return: The securities of this InvestmentsHoldingsGetResponse.  # noqa: E501
        :rtype: list[Security]
        """
        return self._securities

    @securities.setter
    def securities(self, securities):
        """Sets the securities of this InvestmentsHoldingsGetResponse.

        Objects describing the securities held in the accounts associated with the Item.   # noqa: E501

        :param securities: The securities of this InvestmentsHoldingsGetResponse.  # noqa: E501
        :type securities: list[Security]
        """

        self._securities = securities

    @property
    def item(self):
        """Gets the item of this InvestmentsHoldingsGetResponse.  # noqa: E501


        :return: The item of this InvestmentsHoldingsGetResponse.  # noqa: E501
        :rtype: Item
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this InvestmentsHoldingsGetResponse.


        :param item: The item of this InvestmentsHoldingsGetResponse.  # noqa: E501
        :type item: Item
        """

        self._item = item

    @property
    def request_id(self):
        """Gets the request_id of this InvestmentsHoldingsGetResponse.  # noqa: E501

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :return: The request_id of this InvestmentsHoldingsGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this InvestmentsHoldingsGetResponse.

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :param request_id: The request_id of this InvestmentsHoldingsGetResponse.  # noqa: E501
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
        if not isinstance(other, InvestmentsHoldingsGetResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvestmentsHoldingsGetResponse):
            return True

        return self.to_dict() != other.to_dict()
