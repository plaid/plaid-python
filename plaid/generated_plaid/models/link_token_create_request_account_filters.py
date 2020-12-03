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


class LinkTokenCreateRequestAccountFilters(object):
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
        'depository': 'LinkTokenCreateRequestAccountFiltersDepository',
        'credit': 'LinkTokenCreateRequestAccountFiltersCredit',
        'loan': 'LinkTokenCreateRequestAccountFiltersLoan',
        'investment': 'LinkTokenCreateRequestAccountFiltersInvestment'
    }

    attribute_map = {
        'depository': 'depository',
        'credit': 'credit',
        'loan': 'loan',
        'investment': 'investment'
    }

    def __init__(self, depository=None, credit=None, loan=None, investment=None, local_vars_configuration=None):  # noqa: E501
        """LinkTokenCreateRequestAccountFilters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._depository = None
        self._credit = None
        self._loan = None
        self._investment = None
        self.discriminator = None

        if depository is not None:
            self.depository = depository
        if credit is not None:
            self.credit = credit
        if loan is not None:
            self.loan = loan
        if investment is not None:
            self.investment = investment

    @property
    def depository(self):
        """Gets the depository of this LinkTokenCreateRequestAccountFilters.  # noqa: E501


        :return: The depository of this LinkTokenCreateRequestAccountFilters.  # noqa: E501
        :rtype: LinkTokenCreateRequestAccountFiltersDepository
        """
        return self._depository

    @depository.setter
    def depository(self, depository):
        """Sets the depository of this LinkTokenCreateRequestAccountFilters.


        :param depository: The depository of this LinkTokenCreateRequestAccountFilters.  # noqa: E501
        :type depository: LinkTokenCreateRequestAccountFiltersDepository
        """

        self._depository = depository

    @property
    def credit(self):
        """Gets the credit of this LinkTokenCreateRequestAccountFilters.  # noqa: E501


        :return: The credit of this LinkTokenCreateRequestAccountFilters.  # noqa: E501
        :rtype: LinkTokenCreateRequestAccountFiltersCredit
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """Sets the credit of this LinkTokenCreateRequestAccountFilters.


        :param credit: The credit of this LinkTokenCreateRequestAccountFilters.  # noqa: E501
        :type credit: LinkTokenCreateRequestAccountFiltersCredit
        """

        self._credit = credit

    @property
    def loan(self):
        """Gets the loan of this LinkTokenCreateRequestAccountFilters.  # noqa: E501


        :return: The loan of this LinkTokenCreateRequestAccountFilters.  # noqa: E501
        :rtype: LinkTokenCreateRequestAccountFiltersLoan
        """
        return self._loan

    @loan.setter
    def loan(self, loan):
        """Sets the loan of this LinkTokenCreateRequestAccountFilters.


        :param loan: The loan of this LinkTokenCreateRequestAccountFilters.  # noqa: E501
        :type loan: LinkTokenCreateRequestAccountFiltersLoan
        """

        self._loan = loan

    @property
    def investment(self):
        """Gets the investment of this LinkTokenCreateRequestAccountFilters.  # noqa: E501


        :return: The investment of this LinkTokenCreateRequestAccountFilters.  # noqa: E501
        :rtype: LinkTokenCreateRequestAccountFiltersInvestment
        """
        return self._investment

    @investment.setter
    def investment(self, investment):
        """Sets the investment of this LinkTokenCreateRequestAccountFilters.


        :param investment: The investment of this LinkTokenCreateRequestAccountFilters.  # noqa: E501
        :type investment: LinkTokenCreateRequestAccountFiltersInvestment
        """

        self._investment = investment

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
        if not isinstance(other, LinkTokenCreateRequestAccountFilters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LinkTokenCreateRequestAccountFilters):
            return True

        return self.to_dict() != other.to_dict()
