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


class StandaloneAccountType(object):
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
        'depository': 'str',
        'credit': 'str',
        'loan': 'str',
        'investment': 'str',
        'other': 'str'
    }

    attribute_map = {
        'depository': 'depository',
        'credit': 'credit',
        'loan': 'loan',
        'investment': 'investment',
        'other': 'other'
    }

    def __init__(self, depository=None, credit=None, loan=None, investment=None, other=None, local_vars_configuration=None):  # noqa: E501
        """StandaloneAccountType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._depository = None
        self._credit = None
        self._loan = None
        self._investment = None
        self._other = None
        self.discriminator = None

        if depository is not None:
            self.depository = depository
        if credit is not None:
            self.credit = credit
        if loan is not None:
            self.loan = loan
        if investment is not None:
            self.investment = investment
        if other is not None:
            self.other = other

    @property
    def depository(self):
        """Gets the depository of this StandaloneAccountType.  # noqa: E501

        An account type holding cash, in which funds are deposited. Supported products for `depository` accounts are: Auth, Balance, Transactions, Identity, Payment Initiation, and Assets.  # noqa: E501

        :return: The depository of this StandaloneAccountType.  # noqa: E501
        :rtype: str
        """
        return self._depository

    @depository.setter
    def depository(self, depository):
        """Sets the depository of this StandaloneAccountType.

        An account type holding cash, in which funds are deposited. Supported products for `depository` accounts are: Auth, Balance, Transactions, Identity, Payment Initiation, and Assets.  # noqa: E501

        :param depository: The depository of this StandaloneAccountType.  # noqa: E501
        :type depository: str
        """

        self._depository = depository

    @property
    def credit(self):
        """Gets the credit of this StandaloneAccountType.  # noqa: E501

        A credit card type account. Supported products for `credit` accounts are: Balance, Transactions, Identity, and Liabilities.  # noqa: E501

        :return: The credit of this StandaloneAccountType.  # noqa: E501
        :rtype: str
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """Sets the credit of this StandaloneAccountType.

        A credit card type account. Supported products for `credit` accounts are: Balance, Transactions, Identity, and Liabilities.  # noqa: E501

        :param credit: The credit of this StandaloneAccountType.  # noqa: E501
        :type credit: str
        """

        self._credit = credit

    @property
    def loan(self):
        """Gets the loan of this StandaloneAccountType.  # noqa: E501

        A loan type account. Supported products for `loan` accounts are: Balance, Liabilities, and Transactions.  # noqa: E501

        :return: The loan of this StandaloneAccountType.  # noqa: E501
        :rtype: str
        """
        return self._loan

    @loan.setter
    def loan(self, loan):
        """Sets the loan of this StandaloneAccountType.

        A loan type account. Supported products for `loan` accounts are: Balance, Liabilities, and Transactions.  # noqa: E501

        :param loan: The loan of this StandaloneAccountType.  # noqa: E501
        :type loan: str
        """

        self._loan = loan

    @property
    def investment(self):
        """Gets the investment of this StandaloneAccountType.  # noqa: E501

        An investment account. Supported products for `investment` accounts are: Balance and Investments.  # noqa: E501

        :return: The investment of this StandaloneAccountType.  # noqa: E501
        :rtype: str
        """
        return self._investment

    @investment.setter
    def investment(self, investment):
        """Sets the investment of this StandaloneAccountType.

        An investment account. Supported products for `investment` accounts are: Balance and Investments.  # noqa: E501

        :param investment: The investment of this StandaloneAccountType.  # noqa: E501
        :type investment: str
        """

        self._investment = investment

    @property
    def other(self):
        """Gets the other of this StandaloneAccountType.  # noqa: E501

        Other or unknown account type. Supported products for `other` accounts are: Balance, Transactions, Identity, and Assets.  # noqa: E501

        :return: The other of this StandaloneAccountType.  # noqa: E501
        :rtype: str
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this StandaloneAccountType.

        Other or unknown account type. Supported products for `other` accounts are: Balance, Transactions, Identity, and Assets.  # noqa: E501

        :param other: The other of this StandaloneAccountType.  # noqa: E501
        :type other: str
        """

        self._other = other

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
        if not isinstance(other, StandaloneAccountType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StandaloneAccountType):
            return True

        return self.to_dict() != other.to_dict()
