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


class LinkTokenCreateRequest(object):
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
        'client_name': 'str',
        'language': 'str',
        'country_codes': 'list[str]',
        'user': 'LinkTokenCreateRequestUser',
        'products': 'list[str]',
        'webhook': 'str',
        'access_token': 'str',
        'link_customization_name': 'str',
        'redirect_uri': 'str',
        'android_package_name': 'str',
        'account_filters': 'LinkTokenCreateRequestAccountFilters',
        'institution_id': 'str',
        'payment_initiation': 'LinkTokenCreateRequestPaymentInitiation'
    }

    attribute_map = {
        'client_id': 'client_id',
        'secret': 'secret',
        'client_name': 'client_name',
        'language': 'language',
        'country_codes': 'country_codes',
        'user': 'user',
        'products': 'products',
        'webhook': 'webhook',
        'access_token': 'access_token',
        'link_customization_name': 'link_customization_name',
        'redirect_uri': 'redirect_uri',
        'android_package_name': 'android_package_name',
        'account_filters': 'account_filters',
        'institution_id': 'institution_id',
        'payment_initiation': 'payment_initiation'
    }

    def __init__(self, client_id=None, secret=None, client_name=None, language=None, country_codes=None, user=None, products=None, webhook=None, access_token=None, link_customization_name=None, redirect_uri=None, android_package_name=None, account_filters=None, institution_id=None, payment_initiation=None, local_vars_configuration=None):  # noqa: E501
        """LinkTokenCreateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._secret = None
        self._client_name = None
        self._language = None
        self._country_codes = None
        self._user = None
        self._products = None
        self._webhook = None
        self._access_token = None
        self._link_customization_name = None
        self._redirect_uri = None
        self._android_package_name = None
        self._account_filters = None
        self._institution_id = None
        self._payment_initiation = None
        self.discriminator = None

        self.client_id = client_id
        self.secret = secret
        self.client_name = client_name
        self.language = language
        self.country_codes = country_codes
        self.user = user
        if products is not None:
            self.products = products
        if webhook is not None:
            self.webhook = webhook
        if access_token is not None:
            self.access_token = access_token
        if link_customization_name is not None:
            self.link_customization_name = link_customization_name
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri
        if android_package_name is not None:
            self.android_package_name = android_package_name
        if account_filters is not None:
            self.account_filters = account_filters
        if institution_id is not None:
            self.institution_id = institution_id
        if payment_initiation is not None:
            self.payment_initiation = payment_initiation

    @property
    def client_id(self):
        """Gets the client_id of this LinkTokenCreateRequest.  # noqa: E501

        Your Plaid API `client_id`.  # noqa: E501

        :return: The client_id of this LinkTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this LinkTokenCreateRequest.

        Your Plaid API `client_id`.  # noqa: E501

        :param client_id: The client_id of this LinkTokenCreateRequest.  # noqa: E501
        :type client_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def secret(self):
        """Gets the secret of this LinkTokenCreateRequest.  # noqa: E501

        Your Plaid API `secret`.  # noqa: E501

        :return: The secret of this LinkTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this LinkTokenCreateRequest.

        Your Plaid API `secret`.  # noqa: E501

        :param secret: The secret of this LinkTokenCreateRequest.  # noqa: E501
        :type secret: str
        """
        if self.local_vars_configuration.client_side_validation and secret is None:  # noqa: E501
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def client_name(self):
        """Gets the client_name of this LinkTokenCreateRequest.  # noqa: E501

        The name of your application, as it should be displayed in Link.  # noqa: E501

        :return: The client_name of this LinkTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this LinkTokenCreateRequest.

        The name of your application, as it should be displayed in Link.  # noqa: E501

        :param client_name: The client_name of this LinkTokenCreateRequest.  # noqa: E501
        :type client_name: str
        """
        if self.local_vars_configuration.client_side_validation and client_name is None:  # noqa: E501
            raise ValueError("Invalid value for `client_name`, must not be `None`")  # noqa: E501

        self._client_name = client_name

    @property
    def language(self):
        """Gets the language of this LinkTokenCreateRequest.  # noqa: E501

        The language that Link should be displayed in.  Supported languages are: - English (`'en'`) - French (`'fr'`) - Spanish (`'es'`) - Dutch (`'nl'`)  When using a Link customization, the language configured here must match the setting in the customization, or the customization will not be applied.  # noqa: E501

        :return: The language of this LinkTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this LinkTokenCreateRequest.

        The language that Link should be displayed in.  Supported languages are: - English (`'en'`) - French (`'fr'`) - Spanish (`'es'`) - Dutch (`'nl'`)  When using a Link customization, the language configured here must match the setting in the customization, or the customization will not be applied.  # noqa: E501

        :param language: The language of this LinkTokenCreateRequest.  # noqa: E501
        :type language: str
        """
        if self.local_vars_configuration.client_side_validation and language is None:  # noqa: E501
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def country_codes(self):
        """Gets the country_codes of this LinkTokenCreateRequest.  # noqa: E501

        Specify an array of Plaid-supported country codes using the ISO-3166-1 alpha-2 country code standard. Note that if you initialize with a European country code, your users will see the European consent panel during the Link flow. Supported country codes are: `US`, `CA`, `ES`, `FR`, `GB`, `IE`, `NL`. Example value: `['US', 'CA']`. If Link is launched with multiple country codes, only products that you are enabled for in all countries will be used by Link.  If using a Link customization, make sure the country codes in the customization match those specified in `country_codes`. If both `country_codes` and a Link customization are used, the value in `country_codes` may override the value in the customization.  # noqa: E501

        :return: The country_codes of this LinkTokenCreateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._country_codes

    @country_codes.setter
    def country_codes(self, country_codes):
        """Sets the country_codes of this LinkTokenCreateRequest.

        Specify an array of Plaid-supported country codes using the ISO-3166-1 alpha-2 country code standard. Note that if you initialize with a European country code, your users will see the European consent panel during the Link flow. Supported country codes are: `US`, `CA`, `ES`, `FR`, `GB`, `IE`, `NL`. Example value: `['US', 'CA']`. If Link is launched with multiple country codes, only products that you are enabled for in all countries will be used by Link.  If using a Link customization, make sure the country codes in the customization match those specified in `country_codes`. If both `country_codes` and a Link customization are used, the value in `country_codes` may override the value in the customization.  # noqa: E501

        :param country_codes: The country_codes of this LinkTokenCreateRequest.  # noqa: E501
        :type country_codes: list[str]
        """
        if self.local_vars_configuration.client_side_validation and country_codes is None:  # noqa: E501
            raise ValueError("Invalid value for `country_codes`, must not be `None`")  # noqa: E501

        self._country_codes = country_codes

    @property
    def user(self):
        """Gets the user of this LinkTokenCreateRequest.  # noqa: E501


        :return: The user of this LinkTokenCreateRequest.  # noqa: E501
        :rtype: LinkTokenCreateRequestUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this LinkTokenCreateRequest.


        :param user: The user of this LinkTokenCreateRequest.  # noqa: E501
        :type user: LinkTokenCreateRequestUser
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def products(self):
        """Gets the products of this LinkTokenCreateRequest.  # noqa: E501

        List of Plaid product(s) you wish to use. If launching Link in update mode, should be omitted; required otherwise. Valid products are:   `transactions`, `auth`, `identity`, `assets`, `investments`, `liabilities`, `payment_initiation`  Example: `['auth', 'transactions']`   `balance` is *not* a valid value, the Balance product does not require explicit initalization and will automatically be initialized when any other product is initialized. Only institutions that support *all* requested products will be shown in Link.   In Production, you will be billed for each product that you specify when initializing Link. Note that a product cannot be removed from an Item once the Item has been initialized with that product. To stop billing on an Item for subscription-based products, such as Liabilities, Investments, and Transactions, remove the Item via `/item/remove`.  # noqa: E501

        :return: The products of this LinkTokenCreateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this LinkTokenCreateRequest.

        List of Plaid product(s) you wish to use. If launching Link in update mode, should be omitted; required otherwise. Valid products are:   `transactions`, `auth`, `identity`, `assets`, `investments`, `liabilities`, `payment_initiation`  Example: `['auth', 'transactions']`   `balance` is *not* a valid value, the Balance product does not require explicit initalization and will automatically be initialized when any other product is initialized. Only institutions that support *all* requested products will be shown in Link.   In Production, you will be billed for each product that you specify when initializing Link. Note that a product cannot be removed from an Item once the Item has been initialized with that product. To stop billing on an Item for subscription-based products, such as Liabilities, Investments, and Transactions, remove the Item via `/item/remove`.  # noqa: E501

        :param products: The products of this LinkTokenCreateRequest.  # noqa: E501
        :type products: list[str]
        """

        self._products = products

    @property
    def webhook(self):
        """Gets the webhook of this LinkTokenCreateRequest.  # noqa: E501

        The destination URL to which any webhooks should be sent.  # noqa: E501

        :return: The webhook of this LinkTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this LinkTokenCreateRequest.

        The destination URL to which any webhooks should be sent.  # noqa: E501

        :param webhook: The webhook of this LinkTokenCreateRequest.  # noqa: E501
        :type webhook: str
        """

        self._webhook = webhook

    @property
    def access_token(self):
        """Gets the access_token of this LinkTokenCreateRequest.  # noqa: E501

        The `access_token` associated with the Item to update, used when updating or modifying an existing `access_token`. Used when launching Link in update mode or (optionally) when initializing Link as part of the Payment Initiation (Europe) flow.  # noqa: E501

        :return: The access_token of this LinkTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this LinkTokenCreateRequest.

        The `access_token` associated with the Item to update, used when updating or modifying an existing `access_token`. Used when launching Link in update mode or (optionally) when initializing Link as part of the Payment Initiation (Europe) flow.  # noqa: E501

        :param access_token: The access_token of this LinkTokenCreateRequest.  # noqa: E501
        :type access_token: str
        """

        self._access_token = access_token

    @property
    def link_customization_name(self):
        """Gets the link_customization_name of this LinkTokenCreateRequest.  # noqa: E501

        The name of the Link customization from the Plaid Dashboard to be applied to Link. If not specified, the `default` customization will be used. When using a Link customization, the language in the customization must match the language selected via the `language` parameter, and the countries in the customization should match the country codes selected via `country_codes`.  # noqa: E501

        :return: The link_customization_name of this LinkTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._link_customization_name

    @link_customization_name.setter
    def link_customization_name(self, link_customization_name):
        """Sets the link_customization_name of this LinkTokenCreateRequest.

        The name of the Link customization from the Plaid Dashboard to be applied to Link. If not specified, the `default` customization will be used. When using a Link customization, the language in the customization must match the language selected via the `language` parameter, and the countries in the customization should match the country codes selected via `country_codes`.  # noqa: E501

        :param link_customization_name: The link_customization_name of this LinkTokenCreateRequest.  # noqa: E501
        :type link_customization_name: str
        """

        self._link_customization_name = link_customization_name

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this LinkTokenCreateRequest.  # noqa: E501

        A URI indicating the destination where a user should be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. The `redirect_uri` should not contain any query parameters. If `android_package_name` is specified, this field should be left blank. For iOS integrations, `redirect_uri` should be left blank and the client-side `oauthRedirectUri` parameter should be used instead. Any redirect URI specified here must also be added under the \"Allowed redirect URIs\" configuration on the [developer dashboard](https://dashboard.plaid.com/team/api). In non-Sandbox (Production and Development) environments, the `redirect_uri` must begin with https.  # noqa: E501

        :return: The redirect_uri of this LinkTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this LinkTokenCreateRequest.

        A URI indicating the destination where a user should be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. The `redirect_uri` should not contain any query parameters. If `android_package_name` is specified, this field should be left blank. For iOS integrations, `redirect_uri` should be left blank and the client-side `oauthRedirectUri` parameter should be used instead. Any redirect URI specified here must also be added under the \"Allowed redirect URIs\" configuration on the [developer dashboard](https://dashboard.plaid.com/team/api). In non-Sandbox (Production and Development) environments, the `redirect_uri` must begin with https.  # noqa: E501

        :param redirect_uri: The redirect_uri of this LinkTokenCreateRequest.  # noqa: E501
        :type redirect_uri: str
        """

        self._redirect_uri = redirect_uri

    @property
    def android_package_name(self):
        """Gets the android_package_name of this LinkTokenCreateRequest.  # noqa: E501

        The name of your app's Android package. Required if using the `link_token` to initialize Link on Android. Any package name specified here must also be added to the Allowed Android package names setting on the [developer dashboard](https://dashboard.plaid.com/team/api).  # noqa: E501

        :return: The android_package_name of this LinkTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._android_package_name

    @android_package_name.setter
    def android_package_name(self, android_package_name):
        """Sets the android_package_name of this LinkTokenCreateRequest.

        The name of your app's Android package. Required if using the `link_token` to initialize Link on Android. Any package name specified here must also be added to the Allowed Android package names setting on the [developer dashboard](https://dashboard.plaid.com/team/api).  # noqa: E501

        :param android_package_name: The android_package_name of this LinkTokenCreateRequest.  # noqa: E501
        :type android_package_name: str
        """

        self._android_package_name = android_package_name

    @property
    def account_filters(self):
        """Gets the account_filters of this LinkTokenCreateRequest.  # noqa: E501


        :return: The account_filters of this LinkTokenCreateRequest.  # noqa: E501
        :rtype: LinkTokenCreateRequestAccountFilters
        """
        return self._account_filters

    @account_filters.setter
    def account_filters(self, account_filters):
        """Sets the account_filters of this LinkTokenCreateRequest.


        :param account_filters: The account_filters of this LinkTokenCreateRequest.  # noqa: E501
        :type account_filters: LinkTokenCreateRequestAccountFilters
        """

        self._account_filters = account_filters

    @property
    def institution_id(self):
        """Gets the institution_id of this LinkTokenCreateRequest.  # noqa: E501

        Used for certain legacy use cases  # noqa: E501

        :return: The institution_id of this LinkTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this LinkTokenCreateRequest.

        Used for certain legacy use cases  # noqa: E501

        :param institution_id: The institution_id of this LinkTokenCreateRequest.  # noqa: E501
        :type institution_id: str
        """

        self._institution_id = institution_id

    @property
    def payment_initiation(self):
        """Gets the payment_initiation of this LinkTokenCreateRequest.  # noqa: E501


        :return: The payment_initiation of this LinkTokenCreateRequest.  # noqa: E501
        :rtype: LinkTokenCreateRequestPaymentInitiation
        """
        return self._payment_initiation

    @payment_initiation.setter
    def payment_initiation(self, payment_initiation):
        """Sets the payment_initiation of this LinkTokenCreateRequest.


        :param payment_initiation: The payment_initiation of this LinkTokenCreateRequest.  # noqa: E501
        :type payment_initiation: LinkTokenCreateRequestPaymentInitiation
        """

        self._payment_initiation = payment_initiation

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
        if not isinstance(other, LinkTokenCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LinkTokenCreateRequest):
            return True

        return self.to_dict() != other.to_dict()