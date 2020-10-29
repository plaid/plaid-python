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


class PaymentStatusUpdateWebhook(object):
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
        'webhook_type': 'str',
        'webhook_code': 'str',
        'payment_id': 'str',
        'new_payment_status': 'str',
        'old_payment_status': 'str',
        'timestamp': 'str',
        'error': 'Error'
    }

    attribute_map = {
        'webhook_type': 'webhook_type',
        'webhook_code': 'webhook_code',
        'payment_id': 'payment_id',
        'new_payment_status': 'new_payment_status',
        'old_payment_status': 'old_payment_status',
        'timestamp': 'timestamp',
        'error': 'error'
    }

    def __init__(self, webhook_type=None, webhook_code=None, payment_id=None, new_payment_status=None, old_payment_status=None, timestamp=None, error=None, local_vars_configuration=None):  # noqa: E501
        """PaymentStatusUpdateWebhook - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._webhook_type = None
        self._webhook_code = None
        self._payment_id = None
        self._new_payment_status = None
        self._old_payment_status = None
        self._timestamp = None
        self._error = None
        self.discriminator = None

        if webhook_type is not None:
            self.webhook_type = webhook_type
        if webhook_code is not None:
            self.webhook_code = webhook_code
        if payment_id is not None:
            self.payment_id = payment_id
        if new_payment_status is not None:
            self.new_payment_status = new_payment_status
        if old_payment_status is not None:
            self.old_payment_status = old_payment_status
        if timestamp is not None:
            self.timestamp = timestamp
        self.error = error

    @property
    def webhook_type(self):
        """Gets the webhook_type of this PaymentStatusUpdateWebhook.  # noqa: E501

        `PAYMENT_INITIATION`  # noqa: E501

        :return: The webhook_type of this PaymentStatusUpdateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._webhook_type

    @webhook_type.setter
    def webhook_type(self, webhook_type):
        """Sets the webhook_type of this PaymentStatusUpdateWebhook.

        `PAYMENT_INITIATION`  # noqa: E501

        :param webhook_type: The webhook_type of this PaymentStatusUpdateWebhook.  # noqa: E501
        :type webhook_type: str
        """

        self._webhook_type = webhook_type

    @property
    def webhook_code(self):
        """Gets the webhook_code of this PaymentStatusUpdateWebhook.  # noqa: E501

        `PAYMENT_STATUS_UPDATE`  # noqa: E501

        :return: The webhook_code of this PaymentStatusUpdateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._webhook_code

    @webhook_code.setter
    def webhook_code(self, webhook_code):
        """Sets the webhook_code of this PaymentStatusUpdateWebhook.

        `PAYMENT_STATUS_UPDATE`  # noqa: E501

        :param webhook_code: The webhook_code of this PaymentStatusUpdateWebhook.  # noqa: E501
        :type webhook_code: str
        """

        self._webhook_code = webhook_code

    @property
    def payment_id(self):
        """Gets the payment_id of this PaymentStatusUpdateWebhook.  # noqa: E501

        The `payment_id` for the payment being updated  # noqa: E501

        :return: The payment_id of this PaymentStatusUpdateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this PaymentStatusUpdateWebhook.

        The `payment_id` for the payment being updated  # noqa: E501

        :param payment_id: The payment_id of this PaymentStatusUpdateWebhook.  # noqa: E501
        :type payment_id: str
        """

        self._payment_id = payment_id

    @property
    def new_payment_status(self):
        """Gets the new_payment_status of this PaymentStatusUpdateWebhook.  # noqa: E501

        The new status of the payment. Possible values are:  `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.  `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.  `PAYMENT_STATUS_INITIATED`: The payment has been successfully initiated and is considered complete.   `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.  `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.  `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error is retryable once the root cause is resolved.  `PAYMENT_STATUS_BLOCKED`: The payment has been blocked. This is a retryable error.  `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.  # noqa: E501

        :return: The new_payment_status of this PaymentStatusUpdateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._new_payment_status

    @new_payment_status.setter
    def new_payment_status(self, new_payment_status):
        """Sets the new_payment_status of this PaymentStatusUpdateWebhook.

        The new status of the payment. Possible values are:  `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.  `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.  `PAYMENT_STATUS_INITIATED`: The payment has been successfully initiated and is considered complete.   `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.  `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.  `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error is retryable once the root cause is resolved.  `PAYMENT_STATUS_BLOCKED`: The payment has been blocked. This is a retryable error.  `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.  # noqa: E501

        :param new_payment_status: The new_payment_status of this PaymentStatusUpdateWebhook.  # noqa: E501
        :type new_payment_status: str
        """

        self._new_payment_status = new_payment_status

    @property
    def old_payment_status(self):
        """Gets the old_payment_status of this PaymentStatusUpdateWebhook.  # noqa: E501

        The previous status of the payment. Possible values are:  `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.  `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.  `PAYMENT_STATUS_INITIATED`: The payment has been successfully initiated and is considered complete.   `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.  `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.  `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error is retryable once the root cause is resolved.  `PAYMENT_STATUS_BLOCKED`: The payment has been blocked. This is a retryable error.  `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.  # noqa: E501

        :return: The old_payment_status of this PaymentStatusUpdateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._old_payment_status

    @old_payment_status.setter
    def old_payment_status(self, old_payment_status):
        """Sets the old_payment_status of this PaymentStatusUpdateWebhook.

        The previous status of the payment. Possible values are:  `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.  `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.  `PAYMENT_STATUS_INITIATED`: The payment has been successfully initiated and is considered complete.   `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.  `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.  `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error is retryable once the root cause is resolved.  `PAYMENT_STATUS_BLOCKED`: The payment has been blocked. This is a retryable error.  `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.  # noqa: E501

        :param old_payment_status: The old_payment_status of this PaymentStatusUpdateWebhook.  # noqa: E501
        :type old_payment_status: str
        """

        self._old_payment_status = old_payment_status

    @property
    def timestamp(self):
        """Gets the timestamp of this PaymentStatusUpdateWebhook.  # noqa: E501

        The timestamp of the update, in ISO 8601 format, e.g. `\"2017-09-14T14:42:19.350Z\"`  # noqa: E501

        :return: The timestamp of this PaymentStatusUpdateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PaymentStatusUpdateWebhook.

        The timestamp of the update, in ISO 8601 format, e.g. `\"2017-09-14T14:42:19.350Z\"`  # noqa: E501

        :param timestamp: The timestamp of this PaymentStatusUpdateWebhook.  # noqa: E501
        :type timestamp: str
        """

        self._timestamp = timestamp

    @property
    def error(self):
        """Gets the error of this PaymentStatusUpdateWebhook.  # noqa: E501


        :return: The error of this PaymentStatusUpdateWebhook.  # noqa: E501
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this PaymentStatusUpdateWebhook.


        :param error: The error of this PaymentStatusUpdateWebhook.  # noqa: E501
        :type error: Error
        """

        self._error = error

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
        if not isinstance(other, PaymentStatusUpdateWebhook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentStatusUpdateWebhook):
            return True

        return self.to_dict() != other.to_dict()
