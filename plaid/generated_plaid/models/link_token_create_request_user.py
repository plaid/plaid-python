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


class LinkTokenCreateRequestUser(object):
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
        'client_user_id': 'str',
        'legal_name': 'str',
        'phone_number': 'str',
        'phone_number_verified_time': 'str',
        'email_address': 'str',
        'email_address_verified_time': 'str'
    }

    attribute_map = {
        'client_user_id': 'client_user_id',
        'legal_name': 'legal_name',
        'phone_number': 'phone_number',
        'phone_number_verified_time': 'phone_number_verified_time',
        'email_address': 'email_address',
        'email_address_verified_time': 'email_address_verified_time'
    }

    def __init__(self, client_user_id=None, legal_name=None, phone_number=None, phone_number_verified_time=None, email_address=None, email_address_verified_time=None, local_vars_configuration=None):  # noqa: E501
        """LinkTokenCreateRequestUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_user_id = None
        self._legal_name = None
        self._phone_number = None
        self._phone_number_verified_time = None
        self._email_address = None
        self._email_address_verified_time = None
        self.discriminator = None

        self.client_user_id = client_user_id
        if legal_name is not None:
            self.legal_name = legal_name
        if phone_number is not None:
            self.phone_number = phone_number
        if phone_number_verified_time is not None:
            self.phone_number_verified_time = phone_number_verified_time
        if email_address is not None:
            self.email_address = email_address
        if email_address_verified_time is not None:
            self.email_address_verified_time = email_address_verified_time

    @property
    def client_user_id(self):
        """Gets the client_user_id of this LinkTokenCreateRequestUser.  # noqa: E501

        A unique ID representing the end user. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`.  # noqa: E501

        :return: The client_user_id of this LinkTokenCreateRequestUser.  # noqa: E501
        :rtype: str
        """
        return self._client_user_id

    @client_user_id.setter
    def client_user_id(self, client_user_id):
        """Sets the client_user_id of this LinkTokenCreateRequestUser.

        A unique ID representing the end user. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`.  # noqa: E501

        :param client_user_id: The client_user_id of this LinkTokenCreateRequestUser.  # noqa: E501
        :type client_user_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_user_id`, must not be `None`")  # noqa: E501

        self._client_user_id = client_user_id

    @property
    def legal_name(self):
        """Gets the legal_name of this LinkTokenCreateRequestUser.  # noqa: E501

        The user's full legal name. This is an optional field used in the [returning user experience](/docs/link/returning-user) to associate Items to the user.  # noqa: E501

        :return: The legal_name of this LinkTokenCreateRequestUser.  # noqa: E501
        :rtype: str
        """
        return self._legal_name

    @legal_name.setter
    def legal_name(self, legal_name):
        """Sets the legal_name of this LinkTokenCreateRequestUser.

        The user's full legal name. This is an optional field used in the [returning user experience](/docs/link/returning-user) to associate Items to the user.  # noqa: E501

        :param legal_name: The legal_name of this LinkTokenCreateRequestUser.  # noqa: E501
        :type legal_name: str
        """

        self._legal_name = legal_name

    @property
    def phone_number(self):
        """Gets the phone_number of this LinkTokenCreateRequestUser.  # noqa: E501

        The user's phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format. This field is optional, but required to enable the [returning user experience](/docs/link/returning-user).  # noqa: E501

        :return: The phone_number of this LinkTokenCreateRequestUser.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this LinkTokenCreateRequestUser.

        The user's phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format. This field is optional, but required to enable the [returning user experience](/docs/link/returning-user).  # noqa: E501

        :param phone_number: The phone_number of this LinkTokenCreateRequestUser.  # noqa: E501
        :type phone_number: str
        """

        self._phone_number = phone_number

    @property
    def phone_number_verified_time(self):
        """Gets the phone_number_verified_time of this LinkTokenCreateRequestUser.  # noqa: E501

         The date and time the phone number was verified in ISO 8601 format (`YYYY-MM-DDThh:mm:ssZ`). This field is optional, but required to enable any [returning user experience](/docs/link/returning-user).   Only pass a verification time for a phone number that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.   Example: `2020-01-01T00:00:00Z`   # noqa: E501

        :return: The phone_number_verified_time of this LinkTokenCreateRequestUser.  # noqa: E501
        :rtype: str
        """
        return self._phone_number_verified_time

    @phone_number_verified_time.setter
    def phone_number_verified_time(self, phone_number_verified_time):
        """Sets the phone_number_verified_time of this LinkTokenCreateRequestUser.

         The date and time the phone number was verified in ISO 8601 format (`YYYY-MM-DDThh:mm:ssZ`). This field is optional, but required to enable any [returning user experience](/docs/link/returning-user).   Only pass a verification time for a phone number that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.   Example: `2020-01-01T00:00:00Z`   # noqa: E501

        :param phone_number_verified_time: The phone_number_verified_time of this LinkTokenCreateRequestUser.  # noqa: E501
        :type phone_number_verified_time: str
        """

        self._phone_number_verified_time = phone_number_verified_time

    @property
    def email_address(self):
        """Gets the email_address of this LinkTokenCreateRequestUser.  # noqa: E501

        The user's email address. This field is optional, but required to enable the [pre-authenticated returning user flow](/docs/link/returning-user/#enabling-the-returning-user-experience).  # noqa: E501

        :return: The email_address of this LinkTokenCreateRequestUser.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this LinkTokenCreateRequestUser.

        The user's email address. This field is optional, but required to enable the [pre-authenticated returning user flow](/docs/link/returning-user/#enabling-the-returning-user-experience).  # noqa: E501

        :param email_address: The email_address of this LinkTokenCreateRequestUser.  # noqa: E501
        :type email_address: str
        """

        self._email_address = email_address

    @property
    def email_address_verified_time(self):
        """Gets the email_address_verified_time of this LinkTokenCreateRequestUser.  # noqa: E501

        The date and time the email address was verified in ISO 8601 format (`YYYY-MM-DDThh:mm:ssZ`). This is an optional field used in the [returning user experience](/docs/link/returning-user).   Only pass a verification time for an email address that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.   Example: `2020-01-01T00:00:00Z`   # noqa: E501

        :return: The email_address_verified_time of this LinkTokenCreateRequestUser.  # noqa: E501
        :rtype: str
        """
        return self._email_address_verified_time

    @email_address_verified_time.setter
    def email_address_verified_time(self, email_address_verified_time):
        """Sets the email_address_verified_time of this LinkTokenCreateRequestUser.

        The date and time the email address was verified in ISO 8601 format (`YYYY-MM-DDThh:mm:ssZ`). This is an optional field used in the [returning user experience](/docs/link/returning-user).   Only pass a verification time for an email address that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.   Example: `2020-01-01T00:00:00Z`   # noqa: E501

        :param email_address_verified_time: The email_address_verified_time of this LinkTokenCreateRequestUser.  # noqa: E501
        :type email_address_verified_time: str
        """

        self._email_address_verified_time = email_address_verified_time

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
        if not isinstance(other, LinkTokenCreateRequestUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LinkTokenCreateRequestUser):
            return True

        return self.to_dict() != other.to_dict()
