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


class AssetReportCreateRequestOptions(object):
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
        'client_report_id': 'str',
        'webhook': 'str',
        'user': 'AssetReportUser'
    }

    attribute_map = {
        'client_report_id': 'client_report_id',
        'webhook': 'webhook',
        'user': 'user'
    }

    def __init__(self, client_report_id=None, webhook=None, user=None, local_vars_configuration=None):  # noqa: E501
        """AssetReportCreateRequestOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_report_id = None
        self._webhook = None
        self._user = None
        self.discriminator = None

        if client_report_id is not None:
            self.client_report_id = client_report_id
        if webhook is not None:
            self.webhook = webhook
        if user is not None:
            self.user = user

    @property
    def client_report_id(self):
        """Gets the client_report_id of this AssetReportCreateRequestOptions.  # noqa: E501

        Client-generated identifier, which can be used by lenders to track loan applications.  # noqa: E501

        :return: The client_report_id of this AssetReportCreateRequestOptions.  # noqa: E501
        :rtype: str
        """
        return self._client_report_id

    @client_report_id.setter
    def client_report_id(self, client_report_id):
        """Sets the client_report_id of this AssetReportCreateRequestOptions.

        Client-generated identifier, which can be used by lenders to track loan applications.  # noqa: E501

        :param client_report_id: The client_report_id of this AssetReportCreateRequestOptions.  # noqa: E501
        :type client_report_id: str
        """

        self._client_report_id = client_report_id

    @property
    def webhook(self):
        """Gets the webhook of this AssetReportCreateRequestOptions.  # noqa: E501

        URL to which Plaid will send Assets webhooks, for example when the requested Asset Report is ready.  # noqa: E501

        :return: The webhook of this AssetReportCreateRequestOptions.  # noqa: E501
        :rtype: str
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this AssetReportCreateRequestOptions.

        URL to which Plaid will send Assets webhooks, for example when the requested Asset Report is ready.  # noqa: E501

        :param webhook: The webhook of this AssetReportCreateRequestOptions.  # noqa: E501
        :type webhook: str
        """

        self._webhook = webhook

    @property
    def user(self):
        """Gets the user of this AssetReportCreateRequestOptions.  # noqa: E501


        :return: The user of this AssetReportCreateRequestOptions.  # noqa: E501
        :rtype: AssetReportUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AssetReportCreateRequestOptions.


        :param user: The user of this AssetReportCreateRequestOptions.  # noqa: E501
        :type user: AssetReportUser
        """

        self._user = user

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
        if not isinstance(other, AssetReportCreateRequestOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetReportCreateRequestOptions):
            return True

        return self.to_dict() != other.to_dict()
