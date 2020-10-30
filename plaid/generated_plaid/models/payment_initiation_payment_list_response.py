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


class PaymentInitiationPaymentListResponse(object):
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
        'payments': 'list[PaymentInitiationPayment]',
        'next_cursor': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'payments': 'payments',
        'next_cursor': 'next_cursor',
        'request_id': 'request_id'
    }

    def __init__(self, payments=None, next_cursor=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """PaymentInitiationPaymentListResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._payments = None
        self._next_cursor = None
        self._request_id = None
        self.discriminator = None

        if payments is not None:
            self.payments = payments
        if next_cursor is not None:
            self.next_cursor = next_cursor
        if request_id is not None:
            self.request_id = request_id

    @property
    def payments(self):
        """Gets the payments of this PaymentInitiationPaymentListResponse.  # noqa: E501

        An array of payments that have been created, associated with the given `client_id`.  # noqa: E501

        :return: The payments of this PaymentInitiationPaymentListResponse.  # noqa: E501
        :rtype: list[PaymentInitiationPayment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this PaymentInitiationPaymentListResponse.

        An array of payments that have been created, associated with the given `client_id`.  # noqa: E501

        :param payments: The payments of this PaymentInitiationPaymentListResponse.  # noqa: E501
        :type payments: list[PaymentInitiationPayment]
        """

        self._payments = payments

    @property
    def next_cursor(self):
        """Gets the next_cursor of this PaymentInitiationPaymentListResponse.  # noqa: E501

        The value that, when used as the optional `cursor` parameter to `/payment_initiation/payment/list`, will return the next unreturned payment as its first payment.  # noqa: E501

        :return: The next_cursor of this PaymentInitiationPaymentListResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_cursor

    @next_cursor.setter
    def next_cursor(self, next_cursor):
        """Sets the next_cursor of this PaymentInitiationPaymentListResponse.

        The value that, when used as the optional `cursor` parameter to `/payment_initiation/payment/list`, will return the next unreturned payment as its first payment.  # noqa: E501

        :param next_cursor: The next_cursor of this PaymentInitiationPaymentListResponse.  # noqa: E501
        :type next_cursor: str
        """

        self._next_cursor = next_cursor

    @property
    def request_id(self):
        """Gets the request_id of this PaymentInitiationPaymentListResponse.  # noqa: E501

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :return: The request_id of this PaymentInitiationPaymentListResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this PaymentInitiationPaymentListResponse.

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :param request_id: The request_id of this PaymentInitiationPaymentListResponse.  # noqa: E501
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
        if not isinstance(other, PaymentInitiationPaymentListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentInitiationPaymentListResponse):
            return True

        return self.to_dict() != other.to_dict()
