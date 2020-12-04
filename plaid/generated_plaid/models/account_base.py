# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class AccountBase(object):
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
        'account_id': 'str',
        'balances': 'AccountBalance',
        'mask': 'str',
        'name': 'str',
        'official_name': 'str',
        'type': 'AccountType',
        'subtype': 'AccountSubtype',
        'verification_status': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'balances': 'balances',
        'mask': 'mask',
        'name': 'name',
        'official_name': 'official_name',
        'type': 'type',
        'subtype': 'subtype',
        'verification_status': 'verification_status'
    }

    def __init__(self, account_id=None, balances=None, mask=None, name=None, official_name=None, type=None, subtype=None, verification_status=None, local_vars_configuration=None):  # noqa: E501
        """AccountBase - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._balances = None
        self._mask = None
        self._name = None
        self._official_name = None
        self._type = None
        self._subtype = None
        self._verification_status = None
        self.discriminator = None

        self.account_id = account_id
        self.balances = balances
        self.mask = mask
        self.name = name
        self.official_name = official_name
        self.type = type
        self.subtype = subtype
        self.verification_status = verification_status

    @property
    def account_id(self):
        """Gets the account_id of this AccountBase.  # noqa: E501

        Plaid’s unique identifier for the account. This value will not change unless Plaid can't reconcile the account with the data returned by the financial institution. This may occur, for example, when the name of the account changes. If this happens a new `account_id` will be assigned to the account.  The `account_id` can also change if the `access_token` is deleted and the same credentials that were used to generate that `access_token` are used to generate a new `access_token` on a later date. In that case, the new `account_id` will be different from the old `account_id`.  Like all Plaid identifiers, the `account_id` is case sensitive.  # noqa: E501

        :return: The account_id of this AccountBase.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountBase.

        Plaid’s unique identifier for the account. This value will not change unless Plaid can't reconcile the account with the data returned by the financial institution. This may occur, for example, when the name of the account changes. If this happens a new `account_id` will be assigned to the account.  The `account_id` can also change if the `access_token` is deleted and the same credentials that were used to generate that `access_token` are used to generate a new `access_token` on a later date. In that case, the new `account_id` will be different from the old `account_id`.  Like all Plaid identifiers, the `account_id` is case sensitive.  # noqa: E501

        :param account_id: The account_id of this AccountBase.  # noqa: E501
        :type account_id: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def balances(self):
        """Gets the balances of this AccountBase.  # noqa: E501


        :return: The balances of this AccountBase.  # noqa: E501
        :rtype: AccountBalance
        """
        return self._balances

    @balances.setter
    def balances(self, balances):
        """Sets the balances of this AccountBase.


        :param balances: The balances of this AccountBase.  # noqa: E501
        :type balances: AccountBalance
        """
        if self.local_vars_configuration.client_side_validation and balances is None:  # noqa: E501
            raise ValueError("Invalid value for `balances`, must not be `None`")  # noqa: E501

        self._balances = balances

    @property
    def mask(self):
        """Gets the mask of this AccountBase.  # noqa: E501

        The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user.  # noqa: E501

        :return: The mask of this AccountBase.  # noqa: E501
        :rtype: str
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        """Sets the mask of this AccountBase.

        The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user.  # noqa: E501

        :param mask: The mask of this AccountBase.  # noqa: E501
        :type mask: str
        """

        self._mask = mask

    @property
    def name(self):
        """Gets the name of this AccountBase.  # noqa: E501

        The name of the account, either assigned by the user or by the financial institution itself  # noqa: E501

        :return: The name of this AccountBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountBase.

        The name of the account, either assigned by the user or by the financial institution itself  # noqa: E501

        :param name: The name of this AccountBase.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def official_name(self):
        """Gets the official_name of this AccountBase.  # noqa: E501

        The official name of the account as given by the financial institution  # noqa: E501

        :return: The official_name of this AccountBase.  # noqa: E501
        :rtype: str
        """
        return self._official_name

    @official_name.setter
    def official_name(self, official_name):
        """Sets the official_name of this AccountBase.

        The official name of the account as given by the financial institution  # noqa: E501

        :param official_name: The official_name of this AccountBase.  # noqa: E501
        :type official_name: str
        """

        self._official_name = official_name

    @property
    def type(self):
        """Gets the type of this AccountBase.  # noqa: E501


        :return: The type of this AccountBase.  # noqa: E501
        :rtype: AccountType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountBase.


        :param type: The type of this AccountBase.  # noqa: E501
        :type type: AccountType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def subtype(self):
        """Gets the subtype of this AccountBase.  # noqa: E501


        :return: The subtype of this AccountBase.  # noqa: E501
        :rtype: AccountSubtype
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this AccountBase.


        :param subtype: The subtype of this AccountBase.  # noqa: E501
        :type subtype: AccountSubtype
        """
        if self.local_vars_configuration.client_side_validation and subtype is None:  # noqa: E501
            raise ValueError("Invalid value for `subtype`, must not be `None`")  # noqa: E501

        self._subtype = subtype

    @property
    def verification_status(self):
        """Gets the verification_status of this AccountBase.  # noqa: E501

        The current verification status of an Auth Item initiated through Automated or Manual micro-deposits.  Returned for Auth Items only.   `pending_automatic_verification`: The Item is pending automatic verification  `pending_manual_verification`: The Item is pending manual micro-deposit verification. Items remain in this state until the user successfully verifies the two amounts.  `automatically_verified`: The Item has successfully been automatically verified   `manually_verified`: The Item has successfully been manually verified  `verification_expired`: Plaid was unable to automatically verify the deposit within 7 calendar days and will no longer attempt to validate the Item. Users may retry by submitting their information again through Link.  `verification_failed`: The Item failed manual microdeposit verification because the user exhausted all 3 verification attempts. Users may retry by submitting their information again through Link.     # noqa: E501

        :return: The verification_status of this AccountBase.  # noqa: E501
        :rtype: str
        """
        return self._verification_status

    @verification_status.setter
    def verification_status(self, verification_status):
        """Sets the verification_status of this AccountBase.

        The current verification status of an Auth Item initiated through Automated or Manual micro-deposits.  Returned for Auth Items only.   `pending_automatic_verification`: The Item is pending automatic verification  `pending_manual_verification`: The Item is pending manual micro-deposit verification. Items remain in this state until the user successfully verifies the two amounts.  `automatically_verified`: The Item has successfully been automatically verified   `manually_verified`: The Item has successfully been manually verified  `verification_expired`: Plaid was unable to automatically verify the deposit within 7 calendar days and will no longer attempt to validate the Item. Users may retry by submitting their information again through Link.  `verification_failed`: The Item failed manual microdeposit verification because the user exhausted all 3 verification attempts. Users may retry by submitting their information again through Link.     # noqa: E501

        :param verification_status: The verification_status of this AccountBase.  # noqa: E501
        :type verification_status: str
        """
        allowed_values = [None,"pending_automatic_verification", "pending_manual_verification", "manually_verified", "verification_expired", "verification_failed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and verification_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `verification_status` ({0}), must be one of {1}"  # noqa: E501
                .format(verification_status, allowed_values)
            )

        self._verification_status = verification_status

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
        if not isinstance(other, AccountBase):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountBase):
            return True

        return self.to_dict() != other.to_dict()
