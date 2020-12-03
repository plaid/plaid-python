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


class AssetReportAuditCopyCreateResponse(object):
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
        'audit_copy_token': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'audit_copy_token': 'audit_copy_token',
        'request_id': 'request_id'
    }

    def __init__(self, audit_copy_token=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """AssetReportAuditCopyCreateResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._audit_copy_token = None
        self._request_id = None
        self.discriminator = None

        if audit_copy_token is not None:
            self.audit_copy_token = audit_copy_token
        if request_id is not None:
            self.request_id = request_id

    @property
    def audit_copy_token(self):
        """Gets the audit_copy_token of this AssetReportAuditCopyCreateResponse.  # noqa: E501

        A token that can be shared with a third party auditor to allow them to obtain access to the Asset Report. This token should be stored securely.  # noqa: E501

        :return: The audit_copy_token of this AssetReportAuditCopyCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._audit_copy_token

    @audit_copy_token.setter
    def audit_copy_token(self, audit_copy_token):
        """Sets the audit_copy_token of this AssetReportAuditCopyCreateResponse.

        A token that can be shared with a third party auditor to allow them to obtain access to the Asset Report. This token should be stored securely.  # noqa: E501

        :param audit_copy_token: The audit_copy_token of this AssetReportAuditCopyCreateResponse.  # noqa: E501
        :type audit_copy_token: str
        """

        self._audit_copy_token = audit_copy_token

    @property
    def request_id(self):
        """Gets the request_id of this AssetReportAuditCopyCreateResponse.  # noqa: E501

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :return: The request_id of this AssetReportAuditCopyCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this AssetReportAuditCopyCreateResponse.

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :param request_id: The request_id of this AssetReportAuditCopyCreateResponse.  # noqa: E501
        :type request_id: str
        """

        self._request_id = request_id

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
        if not isinstance(other, AssetReportAuditCopyCreateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetReportAuditCopyCreateResponse):
            return True

        return self.to_dict() != other.to_dict()
