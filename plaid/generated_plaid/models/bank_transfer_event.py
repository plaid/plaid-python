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


class BankTransferEvent(object):
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
        'event_id': 'float',
        'timestamp': 'str',
        'event_type': 'BankTransferEventType',
        'account_id': 'str',
        'bank_transfer_id': 'str',
        'bank_transfer_type': 'BankTransferType',
        'bank_transfer_amount': 'str',
        'bank_transfer_iso_currency_code': 'str',
        'failure_reason': 'BankTransferFailure',
        'direction': 'BankTransferDirection',
        'receiver_details': 'BankTransferReceiverDetails'
    }

    attribute_map = {
        'event_id': 'event_id',
        'timestamp': 'timestamp',
        'event_type': 'event_type',
        'account_id': 'account_id',
        'bank_transfer_id': 'bank_transfer_id',
        'bank_transfer_type': 'bank_transfer_type',
        'bank_transfer_amount': 'bank_transfer_amount',
        'bank_transfer_iso_currency_code': 'bank_transfer_iso_currency_code',
        'failure_reason': 'failure_reason',
        'direction': 'direction',
        'receiver_details': 'receiver_details'
    }

    def __init__(self, event_id=None, timestamp=None, event_type=None, account_id=None, bank_transfer_id=None, bank_transfer_type=None, bank_transfer_amount=None, bank_transfer_iso_currency_code=None, failure_reason=None, direction=None, receiver_details=None, local_vars_configuration=None):  # noqa: E501
        """BankTransferEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._event_id = None
        self._timestamp = None
        self._event_type = None
        self._account_id = None
        self._bank_transfer_id = None
        self._bank_transfer_type = None
        self._bank_transfer_amount = None
        self._bank_transfer_iso_currency_code = None
        self._failure_reason = None
        self._direction = None
        self._receiver_details = None
        self.discriminator = None

        if event_id is not None:
            self.event_id = event_id
        if timestamp is not None:
            self.timestamp = timestamp
        if event_type is not None:
            self.event_type = event_type
        if account_id is not None:
            self.account_id = account_id
        if bank_transfer_id is not None:
            self.bank_transfer_id = bank_transfer_id
        if bank_transfer_type is not None:
            self.bank_transfer_type = bank_transfer_type
        if bank_transfer_amount is not None:
            self.bank_transfer_amount = bank_transfer_amount
        if bank_transfer_iso_currency_code is not None:
            self.bank_transfer_iso_currency_code = bank_transfer_iso_currency_code
        self.failure_reason = failure_reason
        if direction is not None:
            self.direction = direction
        self.receiver_details = receiver_details

    @property
    def event_id(self):
        """Gets the event_id of this BankTransferEvent.  # noqa: E501

        Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers.  # noqa: E501

        :return: The event_id of this BankTransferEvent.  # noqa: E501
        :rtype: float
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this BankTransferEvent.

        Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers.  # noqa: E501

        :param event_id: The event_id of this BankTransferEvent.  # noqa: E501
        :type event_id: float
        """

        self._event_id = event_id

    @property
    def timestamp(self):
        """Gets the timestamp of this BankTransferEvent.  # noqa: E501

        The datetime when this event occurred. This will be of the form `2006-01-02T15:04:05Z`.  # noqa: E501

        :return: The timestamp of this BankTransferEvent.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BankTransferEvent.

        The datetime when this event occurred. This will be of the form `2006-01-02T15:04:05Z`.  # noqa: E501

        :param timestamp: The timestamp of this BankTransferEvent.  # noqa: E501
        :type timestamp: str
        """

        self._timestamp = timestamp

    @property
    def event_type(self):
        """Gets the event_type of this BankTransferEvent.  # noqa: E501


        :return: The event_type of this BankTransferEvent.  # noqa: E501
        :rtype: BankTransferEventType
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this BankTransferEvent.


        :param event_type: The event_type of this BankTransferEvent.  # noqa: E501
        :type event_type: BankTransferEventType
        """

        self._event_type = event_type

    @property
    def account_id(self):
        """Gets the account_id of this BankTransferEvent.  # noqa: E501

        The account ID associated with the bank transfer.  # noqa: E501

        :return: The account_id of this BankTransferEvent.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this BankTransferEvent.

        The account ID associated with the bank transfer.  # noqa: E501

        :param account_id: The account_id of this BankTransferEvent.  # noqa: E501
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def bank_transfer_id(self):
        """Gets the bank_transfer_id of this BankTransferEvent.  # noqa: E501

        Plaid’s unique identifier for a bank transfer.  # noqa: E501

        :return: The bank_transfer_id of this BankTransferEvent.  # noqa: E501
        :rtype: str
        """
        return self._bank_transfer_id

    @bank_transfer_id.setter
    def bank_transfer_id(self, bank_transfer_id):
        """Sets the bank_transfer_id of this BankTransferEvent.

        Plaid’s unique identifier for a bank transfer.  # noqa: E501

        :param bank_transfer_id: The bank_transfer_id of this BankTransferEvent.  # noqa: E501
        :type bank_transfer_id: str
        """

        self._bank_transfer_id = bank_transfer_id

    @property
    def bank_transfer_type(self):
        """Gets the bank_transfer_type of this BankTransferEvent.  # noqa: E501


        :return: The bank_transfer_type of this BankTransferEvent.  # noqa: E501
        :rtype: BankTransferType
        """
        return self._bank_transfer_type

    @bank_transfer_type.setter
    def bank_transfer_type(self, bank_transfer_type):
        """Sets the bank_transfer_type of this BankTransferEvent.


        :param bank_transfer_type: The bank_transfer_type of this BankTransferEvent.  # noqa: E501
        :type bank_transfer_type: BankTransferType
        """

        self._bank_transfer_type = bank_transfer_type

    @property
    def bank_transfer_amount(self):
        """Gets the bank_transfer_amount of this BankTransferEvent.  # noqa: E501

        The bank transfer amount.  # noqa: E501

        :return: The bank_transfer_amount of this BankTransferEvent.  # noqa: E501
        :rtype: str
        """
        return self._bank_transfer_amount

    @bank_transfer_amount.setter
    def bank_transfer_amount(self, bank_transfer_amount):
        """Sets the bank_transfer_amount of this BankTransferEvent.

        The bank transfer amount.  # noqa: E501

        :param bank_transfer_amount: The bank_transfer_amount of this BankTransferEvent.  # noqa: E501
        :type bank_transfer_amount: str
        """

        self._bank_transfer_amount = bank_transfer_amount

    @property
    def bank_transfer_iso_currency_code(self):
        """Gets the bank_transfer_iso_currency_code of this BankTransferEvent.  # noqa: E501

        The currency of the bank transfer amount.  # noqa: E501

        :return: The bank_transfer_iso_currency_code of this BankTransferEvent.  # noqa: E501
        :rtype: str
        """
        return self._bank_transfer_iso_currency_code

    @bank_transfer_iso_currency_code.setter
    def bank_transfer_iso_currency_code(self, bank_transfer_iso_currency_code):
        """Sets the bank_transfer_iso_currency_code of this BankTransferEvent.

        The currency of the bank transfer amount.  # noqa: E501

        :param bank_transfer_iso_currency_code: The bank_transfer_iso_currency_code of this BankTransferEvent.  # noqa: E501
        :type bank_transfer_iso_currency_code: str
        """

        self._bank_transfer_iso_currency_code = bank_transfer_iso_currency_code

    @property
    def failure_reason(self):
        """Gets the failure_reason of this BankTransferEvent.  # noqa: E501


        :return: The failure_reason of this BankTransferEvent.  # noqa: E501
        :rtype: BankTransferFailure
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this BankTransferEvent.


        :param failure_reason: The failure_reason of this BankTransferEvent.  # noqa: E501
        :type failure_reason: BankTransferFailure
        """

        self._failure_reason = failure_reason

    @property
    def direction(self):
        """Gets the direction of this BankTransferEvent.  # noqa: E501


        :return: The direction of this BankTransferEvent.  # noqa: E501
        :rtype: BankTransferDirection
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this BankTransferEvent.


        :param direction: The direction of this BankTransferEvent.  # noqa: E501
        :type direction: BankTransferDirection
        """

        self._direction = direction

    @property
    def receiver_details(self):
        """Gets the receiver_details of this BankTransferEvent.  # noqa: E501


        :return: The receiver_details of this BankTransferEvent.  # noqa: E501
        :rtype: BankTransferReceiverDetails
        """
        return self._receiver_details

    @receiver_details.setter
    def receiver_details(self, receiver_details):
        """Sets the receiver_details of this BankTransferEvent.


        :param receiver_details: The receiver_details of this BankTransferEvent.  # noqa: E501
        :type receiver_details: BankTransferReceiverDetails
        """

        self._receiver_details = receiver_details

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
        if not isinstance(other, BankTransferEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BankTransferEvent):
            return True

        return self.to_dict() != other.to_dict()
