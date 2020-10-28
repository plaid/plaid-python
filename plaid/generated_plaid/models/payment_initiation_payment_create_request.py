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


class PaymentInitiationPaymentCreateRequest(object):
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
        'recipient_id': 'str',
        'reference': 'str',
        'amount': 'Amount',
        'schedule': 'PaymentInitiationPaymentCreateRequestSchedule'
    }

    attribute_map = {
        'client_id': 'client_id',
        'secret': 'secret',
        'recipient_id': 'recipient_id',
        'reference': 'reference',
        'amount': 'amount',
        'schedule': 'schedule'
    }

    def __init__(self, client_id=None, secret=None, recipient_id=None, reference=None, amount=None, schedule=None, local_vars_configuration=None):  # noqa: E501
        """PaymentInitiationPaymentCreateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._secret = None
        self._recipient_id = None
        self._reference = None
        self._amount = None
        self._schedule = None
        self.discriminator = None

        self.client_id = client_id
        self.secret = secret
        self.recipient_id = recipient_id
        self.reference = reference
        self.amount = amount
        if schedule is not None:
            self.schedule = schedule

    @property
    def client_id(self):
        """Gets the client_id of this PaymentInitiationPaymentCreateRequest.  # noqa: E501

        Your Plaid API `client_id`.  # noqa: E501

        :return: The client_id of this PaymentInitiationPaymentCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this PaymentInitiationPaymentCreateRequest.

        Your Plaid API `client_id`.  # noqa: E501

        :param client_id: The client_id of this PaymentInitiationPaymentCreateRequest.  # noqa: E501
        :type client_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def secret(self):
        """Gets the secret of this PaymentInitiationPaymentCreateRequest.  # noqa: E501

        Your Plaid API `secret`.  # noqa: E501

        :return: The secret of this PaymentInitiationPaymentCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this PaymentInitiationPaymentCreateRequest.

        Your Plaid API `secret`.  # noqa: E501

        :param secret: The secret of this PaymentInitiationPaymentCreateRequest.  # noqa: E501
        :type secret: str
        """
        if self.local_vars_configuration.client_side_validation and secret is None:  # noqa: E501
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def recipient_id(self):
        """Gets the recipient_id of this PaymentInitiationPaymentCreateRequest.  # noqa: E501

        The ID of the recipient the payment is for.  # noqa: E501

        :return: The recipient_id of this PaymentInitiationPaymentCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this PaymentInitiationPaymentCreateRequest.

        The ID of the recipient the payment is for.  # noqa: E501

        :param recipient_id: The recipient_id of this PaymentInitiationPaymentCreateRequest.  # noqa: E501
        :type recipient_id: str
        """
        if self.local_vars_configuration.client_side_validation and recipient_id is None:  # noqa: E501
            raise ValueError("Invalid value for `recipient_id`, must not be `None`")  # noqa: E501

        self._recipient_id = recipient_id

    @property
    def reference(self):
        """Gets the reference of this PaymentInitiationPaymentCreateRequest.  # noqa: E501

        A reference for the payment. This should not contain special characters (since not all institutions support them).  # noqa: E501

        :return: The reference of this PaymentInitiationPaymentCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PaymentInitiationPaymentCreateRequest.

        A reference for the payment. This should not contain special characters (since not all institutions support them).  # noqa: E501

        :param reference: The reference of this PaymentInitiationPaymentCreateRequest.  # noqa: E501
        :type reference: str
        """
        if self.local_vars_configuration.client_side_validation and reference is None:  # noqa: E501
            raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501

        self._reference = reference

    @property
    def amount(self):
        """Gets the amount of this PaymentInitiationPaymentCreateRequest.  # noqa: E501


        :return: The amount of this PaymentInitiationPaymentCreateRequest.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentInitiationPaymentCreateRequest.


        :param amount: The amount of this PaymentInitiationPaymentCreateRequest.  # noqa: E501
        :type amount: Amount
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def schedule(self):
        """Gets the schedule of this PaymentInitiationPaymentCreateRequest.  # noqa: E501


        :return: The schedule of this PaymentInitiationPaymentCreateRequest.  # noqa: E501
        :rtype: PaymentInitiationPaymentCreateRequestSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this PaymentInitiationPaymentCreateRequest.


        :param schedule: The schedule of this PaymentInitiationPaymentCreateRequest.  # noqa: E501
        :type schedule: PaymentInitiationPaymentCreateRequestSchedule
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
        if not isinstance(other, PaymentInitiationPaymentCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentInitiationPaymentCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
