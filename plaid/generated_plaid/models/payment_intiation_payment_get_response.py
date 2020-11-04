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


class PaymentIntiationPaymentGetResponse(object):
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
        'payment_id': 'str',
        'request_id': 'str',
        'amount': 'PaymentAmount',
        'status': 'str',
        'recipient_id': 'str',
        'reference': 'str',
        'last_status_update': 'str',
        'schedule': 'PaymentIntiationPaymentGetResponseSchedule'
    }

    attribute_map = {
        'payment_id': 'payment_id',
        'request_id': 'request_id',
        'amount': 'amount',
        'status': 'status',
        'recipient_id': 'recipient_id',
        'reference': 'reference',
        'last_status_update': 'last_status_update',
        'schedule': 'schedule'
    }

    def __init__(self, payment_id=None, request_id=None, amount=None, status=None, recipient_id=None, reference=None, last_status_update=None, schedule=None, local_vars_configuration=None):  # noqa: E501
        """PaymentIntiationPaymentGetResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._payment_id = None
        self._request_id = None
        self._amount = None
        self._status = None
        self._recipient_id = None
        self._reference = None
        self._last_status_update = None
        self._schedule = None
        self.discriminator = None

        if payment_id is not None:
            self.payment_id = payment_id
        if request_id is not None:
            self.request_id = request_id
        if amount is not None:
            self.amount = amount
        if status is not None:
            self.status = status
        if recipient_id is not None:
            self.recipient_id = recipient_id
        if reference is not None:
            self.reference = reference
        if last_status_update is not None:
            self.last_status_update = last_status_update
        self.schedule = schedule

    @property
    def payment_id(self):
        """Gets the payment_id of this PaymentIntiationPaymentGetResponse.  # noqa: E501

        The ID of the payment. Like all Plaid identifiers, the `payment_id` is case sensitive.  # noqa: E501

        :return: The payment_id of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this PaymentIntiationPaymentGetResponse.

        The ID of the payment. Like all Plaid identifiers, the `payment_id` is case sensitive.  # noqa: E501

        :param payment_id: The payment_id of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :type payment_id: str
        """

        self._payment_id = payment_id

    @property
    def request_id(self):
        """Gets the request_id of this PaymentIntiationPaymentGetResponse.  # noqa: E501

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :return: The request_id of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this PaymentIntiationPaymentGetResponse.

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :param request_id: The request_id of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :type request_id: str
        """

        self._request_id = request_id

    @property
    def amount(self):
        """Gets the amount of this PaymentIntiationPaymentGetResponse.  # noqa: E501


        :return: The amount of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :rtype: PaymentAmount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentIntiationPaymentGetResponse.


        :param amount: The amount of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :type amount: PaymentAmount
        """

        self._amount = amount

    @property
    def status(self):
        """Gets the status of this PaymentIntiationPaymentGetResponse.  # noqa: E501

        The status of the payment.   `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.  `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.  `PAYMENT_STATUS_INITIATED`: The payment has been successfully initiated and is considered complete.   `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.  `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.  `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error is retryable once the root cause is resolved.  `PAYMENT_STATUS_BLOCKED`: The payment has been blocked. This is a retryable error.  `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.  # noqa: E501

        :return: The status of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentIntiationPaymentGetResponse.

        The status of the payment.   `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.  `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.  `PAYMENT_STATUS_INITIATED`: The payment has been successfully initiated and is considered complete.   `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.  `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.  `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error is retryable once the root cause is resolved.  `PAYMENT_STATUS_BLOCKED`: The payment has been blocked. This is a retryable error.  `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.  # noqa: E501

        :param status: The status of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :type status: str
        """
        allowed_values = ["PAYMENT_STATUS_INPUT_NEEDED", "PAYMENT_STATUS_PROCESSING", "PAYMENT_STATUS_INITIATED", "PAYMENT_STATUS_COMPLETED", "PAYMENT_STATUS_INSUFFICIENT_FUNDS", "PAYMENT_STATUS_FAILED", "PAYMENT_STATUS_BLOCKED", "PAYMENT_STATUS_UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def recipient_id(self):
        """Gets the recipient_id of this PaymentIntiationPaymentGetResponse.  # noqa: E501

        The ID of the recipient  # noqa: E501

        :return: The recipient_id of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this PaymentIntiationPaymentGetResponse.

        The ID of the recipient  # noqa: E501

        :param recipient_id: The recipient_id of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :type recipient_id: str
        """

        self._recipient_id = recipient_id

    @property
    def reference(self):
        """Gets the reference of this PaymentIntiationPaymentGetResponse.  # noqa: E501

        A reference for the payment.  # noqa: E501

        :return: The reference of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PaymentIntiationPaymentGetResponse.

        A reference for the payment.  # noqa: E501

        :param reference: The reference of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :type reference: str
        """

        self._reference = reference

    @property
    def last_status_update(self):
        """Gets the last_status_update of this PaymentIntiationPaymentGetResponse.  # noqa: E501

        The date and time of the last time the `status` was updated, in IS0 8601 format  # noqa: E501

        :return: The last_status_update of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_status_update

    @last_status_update.setter
    def last_status_update(self, last_status_update):
        """Sets the last_status_update of this PaymentIntiationPaymentGetResponse.

        The date and time of the last time the `status` was updated, in IS0 8601 format  # noqa: E501

        :param last_status_update: The last_status_update of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :type last_status_update: str
        """

        self._last_status_update = last_status_update

    @property
    def schedule(self):
        """Gets the schedule of this PaymentIntiationPaymentGetResponse.  # noqa: E501


        :return: The schedule of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :rtype: PaymentIntiationPaymentGetResponseSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this PaymentIntiationPaymentGetResponse.


        :param schedule: The schedule of this PaymentIntiationPaymentGetResponse.  # noqa: E501
        :type schedule: PaymentIntiationPaymentGetResponseSchedule
        """

        self._schedule = schedule

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
        if not isinstance(other, PaymentIntiationPaymentGetResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentIntiationPaymentGetResponse):
            return True

        return self.to_dict() != other.to_dict()
