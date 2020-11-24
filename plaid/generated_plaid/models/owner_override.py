# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    <!--
    Prevent massive diffs on generated code.

    The version of the OpenAPI document: 2020-09-14_1.1.1
     -->
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class OwnerOverride(object):
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
        'names': 'list[str]',
        'phone_numbers': 'list[PhoneNumber]',
        'emails': 'list[Email]',
        'addresses': 'list[Address]'
    }

    attribute_map = {
        'names': 'names',
        'phone_numbers': 'phone_numbers',
        'emails': 'emails',
        'addresses': 'addresses'
    }

    def __init__(self, names=None, phone_numbers=None, emails=None, addresses=None, local_vars_configuration=None):  # noqa: E501
        """OwnerOverride - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._names = None
        self._phone_numbers = None
        self._emails = None
        self._addresses = None
        self.discriminator = None

        if names is not None:
            self.names = names
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if emails is not None:
            self.emails = emails
        if addresses is not None:
            self.addresses = addresses

    @property
    def names(self):
        """Gets the names of this OwnerOverride.  # noqa: E501

        A list of names associated with the account by the financial institution. These should always be the names of individuals, even for business accounts. Note that the same name data will be used for all accounts associated with an Item.  # noqa: E501

        :return: The names of this OwnerOverride.  # noqa: E501
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this OwnerOverride.

        A list of names associated with the account by the financial institution. These should always be the names of individuals, even for business accounts. Note that the same name data will be used for all accounts associated with an Item.  # noqa: E501

        :param names: The names of this OwnerOverride.  # noqa: E501
        :type names: list[str]
        """

        self._names = names

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this OwnerOverride.  # noqa: E501

        A list of phone numbers associated with the account.  # noqa: E501

        :return: The phone_numbers of this OwnerOverride.  # noqa: E501
        :rtype: list[PhoneNumber]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this OwnerOverride.

        A list of phone numbers associated with the account.  # noqa: E501

        :param phone_numbers: The phone_numbers of this OwnerOverride.  # noqa: E501
        :type phone_numbers: list[PhoneNumber]
        """

        self._phone_numbers = phone_numbers

    @property
    def emails(self):
        """Gets the emails of this OwnerOverride.  # noqa: E501

        A list of email addresses associated with the account.  # noqa: E501

        :return: The emails of this OwnerOverride.  # noqa: E501
        :rtype: list[Email]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this OwnerOverride.

        A list of email addresses associated with the account.  # noqa: E501

        :param emails: The emails of this OwnerOverride.  # noqa: E501
        :type emails: list[Email]
        """

        self._emails = emails

    @property
    def addresses(self):
        """Gets the addresses of this OwnerOverride.  # noqa: E501

        Data about the various addresses associated with the account.  # noqa: E501

        :return: The addresses of this OwnerOverride.  # noqa: E501
        :rtype: list[Address]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this OwnerOverride.

        Data about the various addresses associated with the account.  # noqa: E501

        :param addresses: The addresses of this OwnerOverride.  # noqa: E501
        :type addresses: list[Address]
        """

        self._addresses = addresses

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
        if not isinstance(other, OwnerOverride):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OwnerOverride):
            return True

        return self.to_dict() != other.to_dict()
