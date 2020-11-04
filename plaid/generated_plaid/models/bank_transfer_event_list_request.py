# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.0.11
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class BankTransferEventListRequest(object):
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
        'start_date': 'str',
        'end_date': 'str',
        'bank_transfer_id': 'str',
        'account_id': 'str',
        'bank_transfer_type': 'BankTransferType',
        'event_types': 'list[BankTransferEventType]',
        'count': 'float',
        'offset': 'float',
        'origination_account_id': 'str',
        'direction': 'BankTransferDirection'
    }

    attribute_map = {
        'client_id': 'client_id',
        'secret': 'secret',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'bank_transfer_id': 'bank_transfer_id',
        'account_id': 'account_id',
        'bank_transfer_type': 'bank_transfer_type',
        'event_types': 'event_types',
        'count': 'count',
        'offset': 'offset',
        'origination_account_id': 'origination_account_id',
        'direction': 'direction'
    }

    def __init__(self, client_id=None, secret=None, start_date=None, end_date=None, bank_transfer_id=None, account_id=None, bank_transfer_type=None, event_types=None, count=25, offset=0, origination_account_id=None, direction=None, local_vars_configuration=None):  # noqa: E501
        """BankTransferEventListRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._secret = None
        self._start_date = None
        self._end_date = None
        self._bank_transfer_id = None
        self._account_id = None
        self._bank_transfer_type = None
        self._event_types = None
        self._count = None
        self._offset = None
        self._origination_account_id = None
        self._direction = None
        self.discriminator = None

        self.client_id = client_id
        self.secret = secret
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if bank_transfer_id is not None:
            self.bank_transfer_id = bank_transfer_id
        if account_id is not None:
            self.account_id = account_id
        if bank_transfer_type is not None:
            self.bank_transfer_type = bank_transfer_type
        if event_types is not None:
            self.event_types = event_types
        if count is not None:
            self.count = count
        if offset is not None:
            self.offset = offset
        if origination_account_id is not None:
            self.origination_account_id = origination_account_id
        if direction is not None:
            self.direction = direction

    @property
    def client_id(self):
        """Gets the client_id of this BankTransferEventListRequest.  # noqa: E501

        Your Plaid API `client_id`.  # noqa: E501

        :return: The client_id of this BankTransferEventListRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this BankTransferEventListRequest.

        Your Plaid API `client_id`.  # noqa: E501

        :param client_id: The client_id of this BankTransferEventListRequest.  # noqa: E501
        :type client_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def secret(self):
        """Gets the secret of this BankTransferEventListRequest.  # noqa: E501

        Your Plaid API `secret`.  # noqa: E501

        :return: The secret of this BankTransferEventListRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this BankTransferEventListRequest.

        Your Plaid API `secret`.  # noqa: E501

        :param secret: The secret of this BankTransferEventListRequest.  # noqa: E501
        :type secret: str
        """
        if self.local_vars_configuration.client_side_validation and secret is None:  # noqa: E501
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def start_date(self):
        """Gets the start_date of this BankTransferEventListRequest.  # noqa: E501

        The start date of bank transfers to list, as ISO8601 datetime (YYYY-MM-DD).  # noqa: E501

        :return: The start_date of this BankTransferEventListRequest.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this BankTransferEventListRequest.

        The start date of bank transfers to list, as ISO8601 datetime (YYYY-MM-DD).  # noqa: E501

        :param start_date: The start_date of this BankTransferEventListRequest.  # noqa: E501
        :type start_date: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this BankTransferEventListRequest.  # noqa: E501

        The end date of bank transfers to list, as ISO8601 datetime (YYYY-MM-DD).  # noqa: E501

        :return: The end_date of this BankTransferEventListRequest.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this BankTransferEventListRequest.

        The end date of bank transfers to list, as ISO8601 datetime (YYYY-MM-DD).  # noqa: E501

        :param end_date: The end_date of this BankTransferEventListRequest.  # noqa: E501
        :type end_date: str
        """

        self._end_date = end_date

    @property
    def bank_transfer_id(self):
        """Gets the bank_transfer_id of this BankTransferEventListRequest.  # noqa: E501

        Plaid’s unique identifier for a bank transfer.  # noqa: E501

        :return: The bank_transfer_id of this BankTransferEventListRequest.  # noqa: E501
        :rtype: str
        """
        return self._bank_transfer_id

    @bank_transfer_id.setter
    def bank_transfer_id(self, bank_transfer_id):
        """Sets the bank_transfer_id of this BankTransferEventListRequest.

        Plaid’s unique identifier for a bank transfer.  # noqa: E501

        :param bank_transfer_id: The bank_transfer_id of this BankTransferEventListRequest.  # noqa: E501
        :type bank_transfer_id: str
        """

        self._bank_transfer_id = bank_transfer_id

    @property
    def account_id(self):
        """Gets the account_id of this BankTransferEventListRequest.  # noqa: E501

        The account ID to get events for all transactions to/from an account.  # noqa: E501

        :return: The account_id of this BankTransferEventListRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this BankTransferEventListRequest.

        The account ID to get events for all transactions to/from an account.  # noqa: E501

        :param account_id: The account_id of this BankTransferEventListRequest.  # noqa: E501
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def bank_transfer_type(self):
        """Gets the bank_transfer_type of this BankTransferEventListRequest.  # noqa: E501


        :return: The bank_transfer_type of this BankTransferEventListRequest.  # noqa: E501
        :rtype: BankTransferType
        """
        return self._bank_transfer_type

    @bank_transfer_type.setter
    def bank_transfer_type(self, bank_transfer_type):
        """Sets the bank_transfer_type of this BankTransferEventListRequest.


        :param bank_transfer_type: The bank_transfer_type of this BankTransferEventListRequest.  # noqa: E501
        :type bank_transfer_type: BankTransferType
        """

        self._bank_transfer_type = bank_transfer_type

    @property
    def event_types(self):
        """Gets the event_types of this BankTransferEventListRequest.  # noqa: E501

        Filter events by event type.  # noqa: E501

        :return: The event_types of this BankTransferEventListRequest.  # noqa: E501
        :rtype: list[BankTransferEventType]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """Sets the event_types of this BankTransferEventListRequest.

        Filter events by event type.  # noqa: E501

        :param event_types: The event_types of this BankTransferEventListRequest.  # noqa: E501
        :type event_types: list[BankTransferEventType]
        """

        self._event_types = event_types

    @property
    def count(self):
        """Gets the count of this BankTransferEventListRequest.  # noqa: E501

        The maximum number of bank transfer events to return. If the number of events matching the above parameters is greater than `count`, the most recent events will be returned.  # noqa: E501

        :return: The count of this BankTransferEventListRequest.  # noqa: E501
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BankTransferEventListRequest.

        The maximum number of bank transfer events to return. If the number of events matching the above parameters is greater than `count`, the most recent events will be returned.  # noqa: E501

        :param count: The count of this BankTransferEventListRequest.  # noqa: E501
        :type count: float
        """
        if (self.local_vars_configuration.client_side_validation and
                count is not None and count > 25):  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value less than or equal to `25`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                count is not None and count < 0):  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._count = count

    @property
    def offset(self):
        """Gets the offset of this BankTransferEventListRequest.  # noqa: E501

        The offset into the list of bank transfer events. When `count`=25 and `offset`=0, the first 25 events will be returned. When `count`=25 and `offset`=25, the next 25 bank transfer events will be returned.  # noqa: E501

        :return: The offset of this BankTransferEventListRequest.  # noqa: E501
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this BankTransferEventListRequest.

        The offset into the list of bank transfer events. When `count`=25 and `offset`=0, the first 25 events will be returned. When `count`=25 and `offset`=25, the next 25 bank transfer events will be returned.  # noqa: E501

        :param offset: The offset of this BankTransferEventListRequest.  # noqa: E501
        :type offset: float
        """
        if (self.local_vars_configuration.client_side_validation and
                offset is not None and offset < 0):  # noqa: E501
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._offset = offset

    @property
    def origination_account_id(self):
        """Gets the origination_account_id of this BankTransferEventListRequest.  # noqa: E501

        The origination account ID to get events for transfers from a specific origination account.  # noqa: E501

        :return: The origination_account_id of this BankTransferEventListRequest.  # noqa: E501
        :rtype: str
        """
        return self._origination_account_id

    @origination_account_id.setter
    def origination_account_id(self, origination_account_id):
        """Sets the origination_account_id of this BankTransferEventListRequest.

        The origination account ID to get events for transfers from a specific origination account.  # noqa: E501

        :param origination_account_id: The origination_account_id of this BankTransferEventListRequest.  # noqa: E501
        :type origination_account_id: str
        """

        self._origination_account_id = origination_account_id

    @property
    def direction(self):
        """Gets the direction of this BankTransferEventListRequest.  # noqa: E501


        :return: The direction of this BankTransferEventListRequest.  # noqa: E501
        :rtype: BankTransferDirection
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this BankTransferEventListRequest.


        :param direction: The direction of this BankTransferEventListRequest.  # noqa: E501
        :type direction: BankTransferDirection
        """

        self._direction = direction

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
        if not isinstance(other, BankTransferEventListRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BankTransferEventListRequest):
            return True

        return self.to_dict() != other.to_dict()
