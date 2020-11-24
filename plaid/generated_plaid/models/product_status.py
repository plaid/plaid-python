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


class ProductStatus(object):
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
        'status': 'str',
        'last_status_change': 'str',
        'breakdown': 'ProductStatusBreakdown'
    }

    attribute_map = {
        'status': 'status',
        'last_status_change': 'last_status_change',
        'breakdown': 'breakdown'
    }

    def __init__(self, status=None, last_status_change=None, breakdown=None, local_vars_configuration=None):  # noqa: E501
        """ProductStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._last_status_change = None
        self._breakdown = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if last_status_change is not None:
            self.last_status_change = last_status_change
        if breakdown is not None:
            self.breakdown = breakdown

    @property
    def status(self):
        """Gets the status of this ProductStatus.  # noqa: E501

        `HEALTHY`: the majority of requests are successful `DEGRADED`: only some requests are successful `DOWN`: all requests are failing  # noqa: E501

        :return: The status of this ProductStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProductStatus.

        `HEALTHY`: the majority of requests are successful `DEGRADED`: only some requests are successful `DOWN`: all requests are failing  # noqa: E501

        :param status: The status of this ProductStatus.  # noqa: E501
        :type status: str
        """
        allowed_values = ["HEALTHY", "DEGRADED", "DOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def last_status_change(self):
        """Gets the last_status_change of this ProductStatus.  # noqa: E501

        ISO 8601 formatted timestamp of the last status change for the institution.  # noqa: E501

        :return: The last_status_change of this ProductStatus.  # noqa: E501
        :rtype: str
        """
        return self._last_status_change

    @last_status_change.setter
    def last_status_change(self, last_status_change):
        """Sets the last_status_change of this ProductStatus.

        ISO 8601 formatted timestamp of the last status change for the institution.  # noqa: E501

        :param last_status_change: The last_status_change of this ProductStatus.  # noqa: E501
        :type last_status_change: str
        """

        self._last_status_change = last_status_change

    @property
    def breakdown(self):
        """Gets the breakdown of this ProductStatus.  # noqa: E501


        :return: The breakdown of this ProductStatus.  # noqa: E501
        :rtype: ProductStatusBreakdown
        """
        return self._breakdown

    @breakdown.setter
    def breakdown(self, breakdown):
        """Sets the breakdown of this ProductStatus.


        :param breakdown: The breakdown of this ProductStatus.  # noqa: E501
        :type breakdown: ProductStatusBreakdown
        """

        self._breakdown = breakdown

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
        if not isinstance(other, ProductStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductStatus):
            return True

        return self.to_dict() != other.to_dict()
