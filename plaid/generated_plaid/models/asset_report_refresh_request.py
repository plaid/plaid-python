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


class AssetReportRefreshRequest(object):
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
        'asset_report_token': 'str',
        'days_requested': 'float',
        'options': 'AssetReportRefreshRequestOptions'
    }

    attribute_map = {
        'client_id': 'client_id',
        'secret': 'secret',
        'asset_report_token': 'asset_report_token',
        'days_requested': 'days_requested',
        'options': 'options'
    }

    def __init__(self, client_id=None, secret=None, asset_report_token=None, days_requested=None, options=None, local_vars_configuration=None):  # noqa: E501
        """AssetReportRefreshRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._secret = None
        self._asset_report_token = None
        self._days_requested = None
        self._options = None
        self.discriminator = None

        self.client_id = client_id
        self.secret = secret
        self.asset_report_token = asset_report_token
        if days_requested is not None:
            self.days_requested = days_requested
        if options is not None:
            self.options = options

    @property
    def client_id(self):
        """Gets the client_id of this AssetReportRefreshRequest.  # noqa: E501

        Your Plaid API `client_id`.  # noqa: E501

        :return: The client_id of this AssetReportRefreshRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AssetReportRefreshRequest.

        Your Plaid API `client_id`.  # noqa: E501

        :param client_id: The client_id of this AssetReportRefreshRequest.  # noqa: E501
        :type client_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def secret(self):
        """Gets the secret of this AssetReportRefreshRequest.  # noqa: E501

        Your Plaid API `secret`.  # noqa: E501

        :return: The secret of this AssetReportRefreshRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this AssetReportRefreshRequest.

        Your Plaid API `secret`.  # noqa: E501

        :param secret: The secret of this AssetReportRefreshRequest.  # noqa: E501
        :type secret: str
        """
        if self.local_vars_configuration.client_side_validation and secret is None:  # noqa: E501
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def asset_report_token(self):
        """Gets the asset_report_token of this AssetReportRefreshRequest.  # noqa: E501

        The `asset_report_token` returned by the original call to `/asset_report/create`  # noqa: E501

        :return: The asset_report_token of this AssetReportRefreshRequest.  # noqa: E501
        :rtype: str
        """
        return self._asset_report_token

    @asset_report_token.setter
    def asset_report_token(self, asset_report_token):
        """Sets the asset_report_token of this AssetReportRefreshRequest.

        The `asset_report_token` returned by the original call to `/asset_report/create`  # noqa: E501

        :param asset_report_token: The asset_report_token of this AssetReportRefreshRequest.  # noqa: E501
        :type asset_report_token: str
        """
        if self.local_vars_configuration.client_side_validation and asset_report_token is None:  # noqa: E501
            raise ValueError("Invalid value for `asset_report_token`, must not be `None`")  # noqa: E501

        self._asset_report_token = asset_report_token

    @property
    def days_requested(self):
        """Gets the days_requested of this AssetReportRefreshRequest.  # noqa: E501

        The maximum number of days of history to include in the Asset Report. Must be an integer. If not specified, the value from the original call to `/asset_report/create` will be used.  # noqa: E501

        :return: The days_requested of this AssetReportRefreshRequest.  # noqa: E501
        :rtype: float
        """
        return self._days_requested

    @days_requested.setter
    def days_requested(self, days_requested):
        """Sets the days_requested of this AssetReportRefreshRequest.

        The maximum number of days of history to include in the Asset Report. Must be an integer. If not specified, the value from the original call to `/asset_report/create` will be used.  # noqa: E501

        :param days_requested: The days_requested of this AssetReportRefreshRequest.  # noqa: E501
        :type days_requested: float
        """
        if (self.local_vars_configuration.client_side_validation and
                days_requested is not None and days_requested > 730):  # noqa: E501
            raise ValueError("Invalid value for `days_requested`, must be a value less than or equal to `730`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                days_requested is not None and days_requested < 0):  # noqa: E501
            raise ValueError("Invalid value for `days_requested`, must be a value greater than or equal to `0`")  # noqa: E501

        self._days_requested = days_requested

    @property
    def options(self):
        """Gets the options of this AssetReportRefreshRequest.  # noqa: E501


        :return: The options of this AssetReportRefreshRequest.  # noqa: E501
        :rtype: AssetReportRefreshRequestOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this AssetReportRefreshRequest.


        :param options: The options of this AssetReportRefreshRequest.  # noqa: E501
        :type options: AssetReportRefreshRequestOptions
        """

        self._options = options

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
        if not isinstance(other, AssetReportRefreshRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetReportRefreshRequest):
            return True

        return self.to_dict() != other.to_dict()
