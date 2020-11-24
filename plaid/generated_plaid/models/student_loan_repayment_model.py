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


class StudentLoanRepaymentModel(object):
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
        'type': 'str',
        'non_repayment_months': 'float',
        'repayment_months': 'float'
    }

    attribute_map = {
        'type': 'type',
        'non_repayment_months': 'non_repayment_months',
        'repayment_months': 'repayment_months'
    }

    def __init__(self, type=None, non_repayment_months=None, repayment_months=None, local_vars_configuration=None):  # noqa: E501
        """StudentLoanRepaymentModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._non_repayment_months = None
        self._repayment_months = None
        self.discriminator = None

        self.type = type
        self.non_repayment_months = non_repayment_months
        self.repayment_months = repayment_months

    @property
    def type(self):
        """Gets the type of this StudentLoanRepaymentModel.  # noqa: E501

        The only currently supported value for this field is `standard`.  # noqa: E501

        :return: The type of this StudentLoanRepaymentModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StudentLoanRepaymentModel.

        The only currently supported value for this field is `standard`.  # noqa: E501

        :param type: The type of this StudentLoanRepaymentModel.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def non_repayment_months(self):
        """Gets the non_repayment_months of this StudentLoanRepaymentModel.  # noqa: E501

        Configures the number of months before repayment starts.  # noqa: E501

        :return: The non_repayment_months of this StudentLoanRepaymentModel.  # noqa: E501
        :rtype: float
        """
        return self._non_repayment_months

    @non_repayment_months.setter
    def non_repayment_months(self, non_repayment_months):
        """Sets the non_repayment_months of this StudentLoanRepaymentModel.

        Configures the number of months before repayment starts.  # noqa: E501

        :param non_repayment_months: The non_repayment_months of this StudentLoanRepaymentModel.  # noqa: E501
        :type non_repayment_months: float
        """
        if self.local_vars_configuration.client_side_validation and non_repayment_months is None:  # noqa: E501
            raise ValueError("Invalid value for `non_repayment_months`, must not be `None`")  # noqa: E501

        self._non_repayment_months = non_repayment_months

    @property
    def repayment_months(self):
        """Gets the repayment_months of this StudentLoanRepaymentModel.  # noqa: E501

        Configures the number of months of repayments before the loan is paid off.  # noqa: E501

        :return: The repayment_months of this StudentLoanRepaymentModel.  # noqa: E501
        :rtype: float
        """
        return self._repayment_months

    @repayment_months.setter
    def repayment_months(self, repayment_months):
        """Sets the repayment_months of this StudentLoanRepaymentModel.

        Configures the number of months of repayments before the loan is paid off.  # noqa: E501

        :param repayment_months: The repayment_months of this StudentLoanRepaymentModel.  # noqa: E501
        :type repayment_months: float
        """
        if self.local_vars_configuration.client_side_validation and repayment_months is None:  # noqa: E501
            raise ValueError("Invalid value for `repayment_months`, must not be `None`")  # noqa: E501

        self._repayment_months = repayment_months

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
        if not isinstance(other, StudentLoanRepaymentModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StudentLoanRepaymentModel):
            return True

        return self.to_dict() != other.to_dict()
