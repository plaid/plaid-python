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


class DepositSwitchGetResponse(object):
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
        'deposit_switch_id': 'str',
        'target_account_id': 'str',
        'target_item_id': 'str',
        'state': 'str',
        'account_has_multiple_allocations': 'bool',
        'is_allocated_remainder': 'bool',
        'percent_allocated': 'bool',
        'amount_allocated': 'bool',
        'date_created': 'str',
        'date_completed': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'deposit_switch_id': 'deposit_switch_id',
        'target_account_id': 'target_account_id',
        'target_item_id': 'target_item_id',
        'state': 'state',
        'account_has_multiple_allocations': 'account_has_multiple_allocations',
        'is_allocated_remainder': 'is_allocated_remainder',
        'percent_allocated': 'percent_allocated',
        'amount_allocated': 'amount_allocated',
        'date_created': 'date_created',
        'date_completed': 'date_completed',
        'request_id': 'request_id'
    }

    def __init__(self, deposit_switch_id=None, target_account_id=None, target_item_id=None, state=None, account_has_multiple_allocations=None, is_allocated_remainder=None, percent_allocated=None, amount_allocated=None, date_created=None, date_completed=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """DepositSwitchGetResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._deposit_switch_id = None
        self._target_account_id = None
        self._target_item_id = None
        self._state = None
        self._account_has_multiple_allocations = None
        self._is_allocated_remainder = None
        self._percent_allocated = None
        self._amount_allocated = None
        self._date_created = None
        self._date_completed = None
        self._request_id = None
        self.discriminator = None

        if deposit_switch_id is not None:
            self.deposit_switch_id = deposit_switch_id
        if target_account_id is not None:
            self.target_account_id = target_account_id
        if target_item_id is not None:
            self.target_item_id = target_item_id
        if state is not None:
            self.state = state
        self.account_has_multiple_allocations = account_has_multiple_allocations
        self.is_allocated_remainder = is_allocated_remainder
        self.percent_allocated = percent_allocated
        if amount_allocated is not None:
            self.amount_allocated = amount_allocated
        if date_created is not None:
            self.date_created = date_created
        self.date_completed = date_completed
        if request_id is not None:
            self.request_id = request_id

    @property
    def deposit_switch_id(self):
        """Gets the deposit_switch_id of this DepositSwitchGetResponse.  # noqa: E501

        The ID of the Deposit Switch  # noqa: E501

        :return: The deposit_switch_id of this DepositSwitchGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._deposit_switch_id

    @deposit_switch_id.setter
    def deposit_switch_id(self, deposit_switch_id):
        """Sets the deposit_switch_id of this DepositSwitchGetResponse.

        The ID of the Deposit Switch  # noqa: E501

        :param deposit_switch_id: The deposit_switch_id of this DepositSwitchGetResponse.  # noqa: E501
        :type deposit_switch_id: str
        """

        self._deposit_switch_id = deposit_switch_id

    @property
    def target_account_id(self):
        """Gets the target_account_id of this DepositSwitchGetResponse.  # noqa: E501

        The ID of the bank account the direct deposit was switched to  # noqa: E501

        :return: The target_account_id of this DepositSwitchGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._target_account_id

    @target_account_id.setter
    def target_account_id(self, target_account_id):
        """Sets the target_account_id of this DepositSwitchGetResponse.

        The ID of the bank account the direct deposit was switched to  # noqa: E501

        :param target_account_id: The target_account_id of this DepositSwitchGetResponse.  # noqa: E501
        :type target_account_id: str
        """

        self._target_account_id = target_account_id

    @property
    def target_item_id(self):
        """Gets the target_item_id of this DepositSwitchGetResponse.  # noqa: E501

        The ID of the Item the direct deposit was switched to.  # noqa: E501

        :return: The target_item_id of this DepositSwitchGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._target_item_id

    @target_item_id.setter
    def target_item_id(self, target_item_id):
        """Sets the target_item_id of this DepositSwitchGetResponse.

        The ID of the Item the direct deposit was switched to.  # noqa: E501

        :param target_item_id: The target_item_id of this DepositSwitchGetResponse.  # noqa: E501
        :type target_item_id: str
        """

        self._target_item_id = target_item_id

    @property
    def state(self):
        """Gets the state of this DepositSwitchGetResponse.  # noqa: E501

        string enum. Initially, the set of states will include `initialized`, `completed`, and `error`.   # noqa: E501

        :return: The state of this DepositSwitchGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DepositSwitchGetResponse.

        string enum. Initially, the set of states will include `initialized`, `completed`, and `error`.   # noqa: E501

        :param state: The state of this DepositSwitchGetResponse.  # noqa: E501
        :type state: str
        """

        self._state = state

    @property
    def account_has_multiple_allocations(self):
        """Gets the account_has_multiple_allocations of this DepositSwitchGetResponse.  # noqa: E501

        When `true`, user’s direct deposit goes to multiple banks. When false, user’s direct deposit only goes to the target account. Always `null` if the Deposit Switch has not been completed.  # noqa: E501

        :return: The account_has_multiple_allocations of this DepositSwitchGetResponse.  # noqa: E501
        :rtype: bool
        """
        return self._account_has_multiple_allocations

    @account_has_multiple_allocations.setter
    def account_has_multiple_allocations(self, account_has_multiple_allocations):
        """Sets the account_has_multiple_allocations of this DepositSwitchGetResponse.

        When `true`, user’s direct deposit goes to multiple banks. When false, user’s direct deposit only goes to the target account. Always `null` if the Deposit Switch has not been completed.  # noqa: E501

        :param account_has_multiple_allocations: The account_has_multiple_allocations of this DepositSwitchGetResponse.  # noqa: E501
        :type account_has_multiple_allocations: bool
        """

        self._account_has_multiple_allocations = account_has_multiple_allocations

    @property
    def is_allocated_remainder(self):
        """Gets the is_allocated_remainder of this DepositSwitchGetResponse.  # noqa: E501

        When `true`, the target account is allocated the remainder of direct deposit after all other allocations have been deducted. When `false`, user’s direct deposit is allocated as a percent or amount. Always `null` if the Deposit Switch has not been completed.  # noqa: E501

        :return: The is_allocated_remainder of this DepositSwitchGetResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_allocated_remainder

    @is_allocated_remainder.setter
    def is_allocated_remainder(self, is_allocated_remainder):
        """Sets the is_allocated_remainder of this DepositSwitchGetResponse.

        When `true`, the target account is allocated the remainder of direct deposit after all other allocations have been deducted. When `false`, user’s direct deposit is allocated as a percent or amount. Always `null` if the Deposit Switch has not been completed.  # noqa: E501

        :param is_allocated_remainder: The is_allocated_remainder of this DepositSwitchGetResponse.  # noqa: E501
        :type is_allocated_remainder: bool
        """

        self._is_allocated_remainder = is_allocated_remainder

    @property
    def percent_allocated(self):
        """Gets the percent_allocated of this DepositSwitchGetResponse.  # noqa: E501

        The percentage of direct deposit allocated to the target account. Always `null` if the target account is not allocated a percentage or if the Deposit Switch has not been completed or if `is_allocated_remainder` is true.  # noqa: E501

        :return: The percent_allocated of this DepositSwitchGetResponse.  # noqa: E501
        :rtype: bool
        """
        return self._percent_allocated

    @percent_allocated.setter
    def percent_allocated(self, percent_allocated):
        """Sets the percent_allocated of this DepositSwitchGetResponse.

        The percentage of direct deposit allocated to the target account. Always `null` if the target account is not allocated a percentage or if the Deposit Switch has not been completed or if `is_allocated_remainder` is true.  # noqa: E501

        :param percent_allocated: The percent_allocated of this DepositSwitchGetResponse.  # noqa: E501
        :type percent_allocated: bool
        """

        self._percent_allocated = percent_allocated

    @property
    def amount_allocated(self):
        """Gets the amount_allocated of this DepositSwitchGetResponse.  # noqa: E501

        The dollar amount of direct deposit allocated to the target account. Always `null` if the target account is not allocated an amount or if the Deposit Switch has not been completed.  # noqa: E501

        :return: The amount_allocated of this DepositSwitchGetResponse.  # noqa: E501
        :rtype: bool
        """
        return self._amount_allocated

    @amount_allocated.setter
    def amount_allocated(self, amount_allocated):
        """Sets the amount_allocated of this DepositSwitchGetResponse.

        The dollar amount of direct deposit allocated to the target account. Always `null` if the target account is not allocated an amount or if the Deposit Switch has not been completed.  # noqa: E501

        :param amount_allocated: The amount_allocated of this DepositSwitchGetResponse.  # noqa: E501
        :type amount_allocated: bool
        """

        self._amount_allocated = amount_allocated

    @property
    def date_created(self):
        """Gets the date_created of this DepositSwitchGetResponse.  # noqa: E501

        ISO8601 date the Deposit Switch was created.  # noqa: E501

        :return: The date_created of this DepositSwitchGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this DepositSwitchGetResponse.

        ISO8601 date the Deposit Switch was created.  # noqa: E501

        :param date_created: The date_created of this DepositSwitchGetResponse.  # noqa: E501
        :type date_created: str
        """

        self._date_created = date_created

    @property
    def date_completed(self):
        """Gets the date_completed of this DepositSwitchGetResponse.  # noqa: E501

        ISO8601 date the Deposit Switch was completed. Always `null` if the Deposit Switch has not been completed.  # noqa: E501

        :return: The date_completed of this DepositSwitchGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._date_completed

    @date_completed.setter
    def date_completed(self, date_completed):
        """Sets the date_completed of this DepositSwitchGetResponse.

        ISO8601 date the Deposit Switch was completed. Always `null` if the Deposit Switch has not been completed.  # noqa: E501

        :param date_completed: The date_completed of this DepositSwitchGetResponse.  # noqa: E501
        :type date_completed: str
        """

        self._date_completed = date_completed

    @property
    def request_id(self):
        """Gets the request_id of this DepositSwitchGetResponse.  # noqa: E501

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :return: The request_id of this DepositSwitchGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this DepositSwitchGetResponse.

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :param request_id: The request_id of this DepositSwitchGetResponse.  # noqa: E501
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
        if not isinstance(other, DepositSwitchGetResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DepositSwitchGetResponse):
            return True

        return self.to_dict() != other.to_dict()