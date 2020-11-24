# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.1.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class BankTransferCreateRequest(object):
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
        'idempotency_key': 'str',
        'access_token': 'str',
        'account_id': 'str',
        'type': 'BankTransferType',
        'network': 'BankTransferNetwork',
        'amount': 'str',
        'iso_currency_code': 'str',
        'description': 'str',
        'ach_class': 'ACHClass',
        'user': 'BankTransferUser',
        'custom_tag': 'str',
        'metadata': 'dict(str, str)',
        'origination_account_id': 'str'
    }

    attribute_map = {
        'client_id': 'client_id',
        'secret': 'secret',
        'idempotency_key': 'idempotency_key',
        'access_token': 'access_token',
        'account_id': 'account_id',
        'type': 'type',
        'network': 'network',
        'amount': 'amount',
        'iso_currency_code': 'iso_currency_code',
        'description': 'description',
        'ach_class': 'ach_class',
        'user': 'user',
        'custom_tag': 'custom_tag',
        'metadata': 'metadata',
        'origination_account_id': 'origination_account_id'
    }

    def __init__(self, client_id=None, secret=None, idempotency_key=None, access_token=None, account_id=None, type=None, network=None, amount=None, iso_currency_code=None, description=None, ach_class=None, user=None, custom_tag=None, metadata=None, origination_account_id=None, local_vars_configuration=None):  # noqa: E501
        """BankTransferCreateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._secret = None
        self._idempotency_key = None
        self._access_token = None
        self._account_id = None
        self._type = None
        self._network = None
        self._amount = None
        self._iso_currency_code = None
        self._description = None
        self._ach_class = None
        self._user = None
        self._custom_tag = None
        self._metadata = None
        self._origination_account_id = None
        self.discriminator = None

        self.client_id = client_id
        self.secret = secret
        self.idempotency_key = idempotency_key
        self.access_token = access_token
        self.account_id = account_id
        self.type = type
        self.network = network
        self.amount = amount
        self.iso_currency_code = iso_currency_code
        self.description = description
        if ach_class is not None:
            self.ach_class = ach_class
        self.user = user
        if custom_tag is not None:
            self.custom_tag = custom_tag
        self.metadata = metadata
        if origination_account_id is not None:
            self.origination_account_id = origination_account_id

    @property
    def client_id(self):
        """Gets the client_id of this BankTransferCreateRequest.  # noqa: E501

        Your Plaid API `client_id`.  # noqa: E501

        :return: The client_id of this BankTransferCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this BankTransferCreateRequest.

        Your Plaid API `client_id`.  # noqa: E501

        :param client_id: The client_id of this BankTransferCreateRequest.  # noqa: E501
        :type client_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def secret(self):
        """Gets the secret of this BankTransferCreateRequest.  # noqa: E501

        Your Plaid API `secret`.  # noqa: E501

        :return: The secret of this BankTransferCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this BankTransferCreateRequest.

        Your Plaid API `secret`.  # noqa: E501

        :param secret: The secret of this BankTransferCreateRequest.  # noqa: E501
        :type secret: str
        """
        if self.local_vars_configuration.client_side_validation and secret is None:  # noqa: E501
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def idempotency_key(self):
        """Gets the idempotency_key of this BankTransferCreateRequest.  # noqa: E501

        A random key provided by the client, per unique bank transfer. Maximum of 50 characters.  The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create a bank transfer fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single bank transfer is created.  # noqa: E501

        :return: The idempotency_key of this BankTransferCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._idempotency_key

    @idempotency_key.setter
    def idempotency_key(self, idempotency_key):
        """Sets the idempotency_key of this BankTransferCreateRequest.

        A random key provided by the client, per unique bank transfer. Maximum of 50 characters.  The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create a bank transfer fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single bank transfer is created.  # noqa: E501

        :param idempotency_key: The idempotency_key of this BankTransferCreateRequest.  # noqa: E501
        :type idempotency_key: str
        """
        if self.local_vars_configuration.client_side_validation and idempotency_key is None:  # noqa: E501
            raise ValueError("Invalid value for `idempotency_key`, must not be `None`")  # noqa: E501

        self._idempotency_key = idempotency_key

    @property
    def access_token(self):
        """Gets the access_token of this BankTransferCreateRequest.  # noqa: E501

        The Plaid `access_token` for the account that will be debited or credited.  # noqa: E501

        :return: The access_token of this BankTransferCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this BankTransferCreateRequest.

        The Plaid `access_token` for the account that will be debited or credited.  # noqa: E501

        :param access_token: The access_token of this BankTransferCreateRequest.  # noqa: E501
        :type access_token: str
        """
        if self.local_vars_configuration.client_side_validation and access_token is None:  # noqa: E501
            raise ValueError("Invalid value for `access_token`, must not be `None`")  # noqa: E501

        self._access_token = access_token

    @property
    def account_id(self):
        """Gets the account_id of this BankTransferCreateRequest.  # noqa: E501

        The Plaid `account_id` for the account that will be debited or credited.  # noqa: E501

        :return: The account_id of this BankTransferCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this BankTransferCreateRequest.

        The Plaid `account_id` for the account that will be debited or credited.  # noqa: E501

        :param account_id: The account_id of this BankTransferCreateRequest.  # noqa: E501
        :type account_id: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def type(self):
        """Gets the type of this BankTransferCreateRequest.  # noqa: E501


        :return: The type of this BankTransferCreateRequest.  # noqa: E501
        :rtype: BankTransferType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BankTransferCreateRequest.


        :param type: The type of this BankTransferCreateRequest.  # noqa: E501
        :type type: BankTransferType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def network(self):
        """Gets the network of this BankTransferCreateRequest.  # noqa: E501


        :return: The network of this BankTransferCreateRequest.  # noqa: E501
        :rtype: BankTransferNetwork
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this BankTransferCreateRequest.


        :param network: The network of this BankTransferCreateRequest.  # noqa: E501
        :type network: BankTransferNetwork
        """
        if self.local_vars_configuration.client_side_validation and network is None:  # noqa: E501
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def amount(self):
        """Gets the amount of this BankTransferCreateRequest.  # noqa: E501

        The transfer amount (decimal string with two digits of precision e.g. \"10.00\").  # noqa: E501

        :return: The amount of this BankTransferCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BankTransferCreateRequest.

        The transfer amount (decimal string with two digits of precision e.g. \"10.00\").  # noqa: E501

        :param amount: The amount of this BankTransferCreateRequest.  # noqa: E501
        :type amount: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def iso_currency_code(self):
        """Gets the iso_currency_code of this BankTransferCreateRequest.  # noqa: E501

        The currency of the transfer amount – should be set to \"USD\".  # noqa: E501

        :return: The iso_currency_code of this BankTransferCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._iso_currency_code

    @iso_currency_code.setter
    def iso_currency_code(self, iso_currency_code):
        """Sets the iso_currency_code of this BankTransferCreateRequest.

        The currency of the transfer amount – should be set to \"USD\".  # noqa: E501

        :param iso_currency_code: The iso_currency_code of this BankTransferCreateRequest.  # noqa: E501
        :type iso_currency_code: str
        """
        if self.local_vars_configuration.client_side_validation and iso_currency_code is None:  # noqa: E501
            raise ValueError("Invalid value for `iso_currency_code`, must not be `None`")  # noqa: E501

        self._iso_currency_code = iso_currency_code

    @property
    def description(self):
        """Gets the description of this BankTransferCreateRequest.  # noqa: E501

        The transfer description. Maximum of 8 characters.  # noqa: E501

        :return: The description of this BankTransferCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BankTransferCreateRequest.

        The transfer description. Maximum of 8 characters.  # noqa: E501

        :param description: The description of this BankTransferCreateRequest.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def ach_class(self):
        """Gets the ach_class of this BankTransferCreateRequest.  # noqa: E501


        :return: The ach_class of this BankTransferCreateRequest.  # noqa: E501
        :rtype: ACHClass
        """
        return self._ach_class

    @ach_class.setter
    def ach_class(self, ach_class):
        """Sets the ach_class of this BankTransferCreateRequest.


        :param ach_class: The ach_class of this BankTransferCreateRequest.  # noqa: E501
        :type ach_class: ACHClass
        """

        self._ach_class = ach_class

    @property
    def user(self):
        """Gets the user of this BankTransferCreateRequest.  # noqa: E501


        :return: The user of this BankTransferCreateRequest.  # noqa: E501
        :rtype: BankTransferUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BankTransferCreateRequest.


        :param user: The user of this BankTransferCreateRequest.  # noqa: E501
        :type user: BankTransferUser
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def custom_tag(self):
        """Gets the custom_tag of this BankTransferCreateRequest.  # noqa: E501

        An arbitrary string provided by the client for storage with the bank transfer. Will be returned in all `BankTransfer` objects. May be up to 100 characters.  # noqa: E501

        :return: The custom_tag of this BankTransferCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._custom_tag

    @custom_tag.setter
    def custom_tag(self, custom_tag):
        """Sets the custom_tag of this BankTransferCreateRequest.

        An arbitrary string provided by the client for storage with the bank transfer. Will be returned in all `BankTransfer` objects. May be up to 100 characters.  # noqa: E501

        :param custom_tag: The custom_tag of this BankTransferCreateRequest.  # noqa: E501
        :type custom_tag: str
        """

        self._custom_tag = custom_tag

    @property
    def metadata(self):
        """Gets the metadata of this BankTransferCreateRequest.  # noqa: E501

        The Metadata object is a mapping of client-provided String fields to any String value. The following limitations apply: - The JSON values must be Strings (no nested JSON objects allowed) - Only ASCII characters may be used - Maximum of 50 key/value pairs - Maximum key length of 40 characters - Maximum value length of 500 characters   # noqa: E501

        :return: The metadata of this BankTransferCreateRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this BankTransferCreateRequest.

        The Metadata object is a mapping of client-provided String fields to any String value. The following limitations apply: - The JSON values must be Strings (no nested JSON objects allowed) - Only ASCII characters may be used - Maximum of 50 key/value pairs - Maximum key length of 40 characters - Maximum value length of 500 characters   # noqa: E501

        :param metadata: The metadata of this BankTransferCreateRequest.  # noqa: E501
        :type metadata: dict(str, str)
        """

        self._metadata = metadata

    @property
    def origination_account_id(self):
        """Gets the origination_account_id of this BankTransferCreateRequest.  # noqa: E501

        Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified.  # noqa: E501

        :return: The origination_account_id of this BankTransferCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._origination_account_id

    @origination_account_id.setter
    def origination_account_id(self, origination_account_id):
        """Sets the origination_account_id of this BankTransferCreateRequest.

        Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified.  # noqa: E501

        :param origination_account_id: The origination_account_id of this BankTransferCreateRequest.  # noqa: E501
        :type origination_account_id: str
        """

        self._origination_account_id = origination_account_id

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
        if not isinstance(other, BankTransferCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BankTransferCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
