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


class StudentLoanStatus(object):
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
        'end_date': 'str',
        'type': 'str'
    }

    attribute_map = {
        'end_date': 'end_date',
        'type': 'type'
    }

    def __init__(self, end_date=None, type=None, local_vars_configuration=None):  # noqa: E501
        """StudentLoanStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._end_date = None
        self._type = None
        self.discriminator = None

        self.end_date = end_date
        self.type = type

    @property
    def end_date(self):
        """Gets the end_date of this StudentLoanStatus.  # noqa: E501

        The date until which the loan will be in its current status. Dates are returned in an ISO 8601 format (YYYY-MM-DD).   # noqa: E501

        :return: The end_date of this StudentLoanStatus.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this StudentLoanStatus.

        The date until which the loan will be in its current status. Dates are returned in an ISO 8601 format (YYYY-MM-DD).   # noqa: E501

        :param end_date: The end_date of this StudentLoanStatus.  # noqa: E501
        :type end_date: str
        """

        self._end_date = end_date

    @property
    def type(self):
        """Gets the type of this StudentLoanStatus.  # noqa: E501

        Possible values: `\"cancelled\"`, `\"charged off\"`, `\"claim\"`, `\"consolidated\"`, `\"deferment\"`, `\"delinquent\"`, `\"discharged\"`, `\"extension\"`, `\"forbearance\"`, `\"in grace\"`, `\"in military\"`, `\"in school\"`, `\"not fully disbursed\"`, `\"other\"`, `\"paid in full\"`, `\"refunded\"`, `\"repayment\"`, or `transferred`.  # noqa: E501

        :return: The type of this StudentLoanStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StudentLoanStatus.

        Possible values: `\"cancelled\"`, `\"charged off\"`, `\"claim\"`, `\"consolidated\"`, `\"deferment\"`, `\"delinquent\"`, `\"discharged\"`, `\"extension\"`, `\"forbearance\"`, `\"in grace\"`, `\"in military\"`, `\"in school\"`, `\"not fully disbursed\"`, `\"other\"`, `\"paid in full\"`, `\"refunded\"`, `\"repayment\"`, or `transferred`.  # noqa: E501

        :param type: The type of this StudentLoanStatus.  # noqa: E501
        :type type: str
        """

        self._type = type

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
        if not isinstance(other, StudentLoanStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StudentLoanStatus):
            return True

        return self.to_dict() != other.to_dict()
