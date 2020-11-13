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


class InvestmentsTransactionsGetResponse(object):
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
        'item': 'Item',
        'accounts': 'list[AccountBase]',
        'securities': 'list[Security]',
        'investment_transactions': 'list[InvestmentTransaction]',
        'total_investment_transactions': 'float',
        'request_id': 'str'
    }

    attribute_map = {
        'item': 'item',
        'accounts': 'accounts',
        'securities': 'securities',
        'investment_transactions': 'investment_transactions',
        'total_investment_transactions': 'total_investment_transactions',
        'request_id': 'request_id'
    }

    def __init__(self, item=None, accounts=None, securities=None, investment_transactions=None, total_investment_transactions=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """InvestmentsTransactionsGetResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._item = None
        self._accounts = None
        self._securities = None
        self._investment_transactions = None
        self._total_investment_transactions = None
        self._request_id = None
        self.discriminator = None

        if item is not None:
            self.item = item
        if accounts is not None:
            self.accounts = accounts
        if securities is not None:
            self.securities = securities
        if investment_transactions is not None:
            self.investment_transactions = investment_transactions
        if total_investment_transactions is not None:
            self.total_investment_transactions = total_investment_transactions
        if request_id is not None:
            self.request_id = request_id

    @property
    def item(self):
        """Gets the item of this InvestmentsTransactionsGetResponse.  # noqa: E501


        :return: The item of this InvestmentsTransactionsGetResponse.  # noqa: E501
        :rtype: Item
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this InvestmentsTransactionsGetResponse.


        :param item: The item of this InvestmentsTransactionsGetResponse.  # noqa: E501
        :type item: Item
        """

        self._item = item

    @property
    def accounts(self):
        """Gets the accounts of this InvestmentsTransactionsGetResponse.  # noqa: E501

        The accounts for which transaction history is being fetched.  # noqa: E501

        :return: The accounts of this InvestmentsTransactionsGetResponse.  # noqa: E501
        :rtype: list[AccountBase]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this InvestmentsTransactionsGetResponse.

        The accounts for which transaction history is being fetched.  # noqa: E501

        :param accounts: The accounts of this InvestmentsTransactionsGetResponse.  # noqa: E501
        :type accounts: list[AccountBase]
        """

        self._accounts = accounts

    @property
    def securities(self):
        """Gets the securities of this InvestmentsTransactionsGetResponse.  # noqa: E501

        All securities for which there is a corresponding transaction being fetched.  # noqa: E501

        :return: The securities of this InvestmentsTransactionsGetResponse.  # noqa: E501
        :rtype: list[Security]
        """
        return self._securities

    @securities.setter
    def securities(self, securities):
        """Sets the securities of this InvestmentsTransactionsGetResponse.

        All securities for which there is a corresponding transaction being fetched.  # noqa: E501

        :param securities: The securities of this InvestmentsTransactionsGetResponse.  # noqa: E501
        :type securities: list[Security]
        """

        self._securities = securities

    @property
    def investment_transactions(self):
        """Gets the investment_transactions of this InvestmentsTransactionsGetResponse.  # noqa: E501

        The transactions being fetched  # noqa: E501

        :return: The investment_transactions of this InvestmentsTransactionsGetResponse.  # noqa: E501
        :rtype: list[InvestmentTransaction]
        """
        return self._investment_transactions

    @investment_transactions.setter
    def investment_transactions(self, investment_transactions):
        """Sets the investment_transactions of this InvestmentsTransactionsGetResponse.

        The transactions being fetched  # noqa: E501

        :param investment_transactions: The investment_transactions of this InvestmentsTransactionsGetResponse.  # noqa: E501
        :type investment_transactions: list[InvestmentTransaction]
        """

        self._investment_transactions = investment_transactions

    @property
    def total_investment_transactions(self):
        """Gets the total_investment_transactions of this InvestmentsTransactionsGetResponse.  # noqa: E501

        The total number of transactions available within the date range specified. If `total_investment_transactions` is larger than the size of the `transactions` array, more transactions are available and can be fetched via manipulating the `offset` parameter.'  # noqa: E501

        :return: The total_investment_transactions of this InvestmentsTransactionsGetResponse.  # noqa: E501
        :rtype: float
        """
        return self._total_investment_transactions

    @total_investment_transactions.setter
    def total_investment_transactions(self, total_investment_transactions):
        """Sets the total_investment_transactions of this InvestmentsTransactionsGetResponse.

        The total number of transactions available within the date range specified. If `total_investment_transactions` is larger than the size of the `transactions` array, more transactions are available and can be fetched via manipulating the `offset` parameter.'  # noqa: E501

        :param total_investment_transactions: The total_investment_transactions of this InvestmentsTransactionsGetResponse.  # noqa: E501
        :type total_investment_transactions: float
        """

        self._total_investment_transactions = total_investment_transactions

    @property
    def request_id(self):
        """Gets the request_id of this InvestmentsTransactionsGetResponse.  # noqa: E501

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :return: The request_id of this InvestmentsTransactionsGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this InvestmentsTransactionsGetResponse.

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :param request_id: The request_id of this InvestmentsTransactionsGetResponse.  # noqa: E501
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
        if not isinstance(other, InvestmentsTransactionsGetResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvestmentsTransactionsGetResponse):
            return True

        return self.to_dict() != other.to_dict()
