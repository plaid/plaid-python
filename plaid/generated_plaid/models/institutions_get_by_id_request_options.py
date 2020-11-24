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


class InstitutionsGetByIdRequestOptions(object):
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
        'include_optional_metadata': 'bool',
        'include_status': 'bool'
    }

    attribute_map = {
        'include_optional_metadata': 'include_optional_metadata',
        'include_status': 'include_status'
    }

    def __init__(self, include_optional_metadata=False, include_status=False, local_vars_configuration=None):  # noqa: E501
        """InstitutionsGetByIdRequestOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._include_optional_metadata = None
        self._include_status = None
        self.discriminator = None

        if include_optional_metadata is not None:
            self.include_optional_metadata = include_optional_metadata
        if include_status is not None:
            self.include_status = include_status

    @property
    def include_optional_metadata(self):
        """Gets the include_optional_metadata of this InstitutionsGetByIdRequestOptions.  # noqa: E501

        When `true`, return an institution's logo, brand color, and URL. When available, the bank's logo is returned as a base64 encoded 152x152 PNG, the brand color is in hexadecimal format. The default value is `false`.  Note that Plaid does not own any of the logos shared by the API and that by accessing or using these logos, you agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied warranties with respect to the logos.  # noqa: E501

        :return: The include_optional_metadata of this InstitutionsGetByIdRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._include_optional_metadata

    @include_optional_metadata.setter
    def include_optional_metadata(self, include_optional_metadata):
        """Sets the include_optional_metadata of this InstitutionsGetByIdRequestOptions.

        When `true`, return an institution's logo, brand color, and URL. When available, the bank's logo is returned as a base64 encoded 152x152 PNG, the brand color is in hexadecimal format. The default value is `false`.  Note that Plaid does not own any of the logos shared by the API and that by accessing or using these logos, you agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied warranties with respect to the logos.  # noqa: E501

        :param include_optional_metadata: The include_optional_metadata of this InstitutionsGetByIdRequestOptions.  # noqa: E501
        :type include_optional_metadata: bool
        """

        self._include_optional_metadata = include_optional_metadata

    @property
    def include_status(self):
        """Gets the include_status of this InstitutionsGetByIdRequestOptions.  # noqa: E501

        If `true`, the response will include status information about the institution. Default value is `false`.  # noqa: E501

        :return: The include_status of this InstitutionsGetByIdRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._include_status

    @include_status.setter
    def include_status(self, include_status):
        """Sets the include_status of this InstitutionsGetByIdRequestOptions.

        If `true`, the response will include status information about the institution. Default value is `false`.  # noqa: E501

        :param include_status: The include_status of this InstitutionsGetByIdRequestOptions.  # noqa: E501
        :type include_status: bool
        """

        self._include_status = include_status

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
        if not isinstance(other, InstitutionsGetByIdRequestOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstitutionsGetByIdRequestOptions):
            return True

        return self.to_dict() != other.to_dict()
