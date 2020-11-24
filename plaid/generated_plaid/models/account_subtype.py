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


class AccountSubtype(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    _401A = "401a"
    _401K = "401k"
    _403B = "403B"
    _457B = "457b"
    _529 = "529"
    BROKERAGE = "brokerage"
    CASH_ISA = "cash isa"
    EDUCATION_SAVINGS_ACCOUNT = "education savings account"
    GIC = "gic"
    HEALTH_REIMBURSEMENT_ARRANGEMENT = "health reimbursement arrangement"
    HSA = "hsa"
    ISA = "isa"
    IRA = "ira"
    LIF = "lif"
    LIRA = "lira"
    LRIF = "lrif"
    LRSP = "lrsp"
    NON_TAXABLE_BROKERAGE_ACCOUNT = "non-taxable brokerage account"
    OTHER = "other"
    PRIF = "prif"
    RDSP = "rdsp"
    RESP = "resp"
    RLIF = "rlif"
    RRIF = "rrif"
    PENSION = "pension"
    PROFIT_SHARING_PLAN = "profit sharing plan"
    RETIREMENT = "retirement"
    ROTH = "roth"
    ROTH_401K = "roth 401k"
    RRSP = "rrsp"
    SEP_IRA = "sep ira"
    SIMPLE_IRA = "simple ira"
    SIPP = "sipp"
    STOCK_PLAN = "stock plan"
    THRIFT_SAVINGS_PLAN = "thrift savings plan"
    TFSA = "tfsa"
    TRUST = "trust"
    UGMA = "ugma"
    UTMA = "utma"
    VARIABLE_ANNUITY = "variable annuity"
    CREDIT_CARD = "credit card"
    PAYPAL = "paypal"
    CD = "cd"
    CHECKING = "checking"
    SAVINGS = "savings"
    MONEY_MARKET = "money market"
    PREPAID = "prepaid"
    AUTO = "auto"
    COMMERCIAL = "commercial"
    CONSTRUCTION = "construction"
    CONSUMER = "consumer"
    HOME = "home"
    HOME_EQUITY = "home equity"
    LOAN = "loan"
    MORTGAGE = "mortgage"
    OVERDRAFT = "overdraft"
    LINE_OF_CREDIT = "line of credit"
    STUDENT = "student"
    CASH_MANAGEMENT = "cash management"
    KEOGH = "keogh"
    MUTUAL_FUND = "mutual fund"
    RECURRING = "recurring"
    REWARDS = "rewards"
    SAFE_DEPOSIT = "safe deposit"
    SARSEP = "sarsep"

    allowable_values = [_401A, _401K, _403B, _457B, _529, BROKERAGE, CASH_ISA, EDUCATION_SAVINGS_ACCOUNT, GIC, HEALTH_REIMBURSEMENT_ARRANGEMENT, HSA, ISA, IRA, LIF, LIRA, LRIF, LRSP, NON_TAXABLE_BROKERAGE_ACCOUNT, OTHER, PRIF, RDSP, RESP, RLIF, RRIF, PENSION, PROFIT_SHARING_PLAN, RETIREMENT, ROTH, ROTH_401K, RRSP, SEP_IRA, SIMPLE_IRA, SIPP, STOCK_PLAN, THRIFT_SAVINGS_PLAN, TFSA, TRUST, UGMA, UTMA, VARIABLE_ANNUITY, CREDIT_CARD, PAYPAL, CD, CHECKING, SAVINGS, MONEY_MARKET, PREPAID, AUTO, COMMERCIAL, CONSTRUCTION, CONSUMER, HOME, HOME_EQUITY, LOAN, MORTGAGE, OVERDRAFT, LINE_OF_CREDIT, STUDENT, CASH_MANAGEMENT, KEOGH, MUTUAL_FUND, RECURRING, REWARDS, SAFE_DEPOSIT, SARSEP]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """AccountSubtype - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, AccountSubtype):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountSubtype):
            return True

        return self.to_dict() != other.to_dict()
