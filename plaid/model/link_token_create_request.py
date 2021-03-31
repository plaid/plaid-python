"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plaid.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from plaid.model.country_code import CountryCode
    from plaid.model.link_token_account_filters import LinkTokenAccountFilters
    from plaid.model.link_token_create_request_auth import LinkTokenCreateRequestAuth
    from plaid.model.link_token_create_request_deposit_switch import LinkTokenCreateRequestDepositSwitch
    from plaid.model.link_token_create_request_income_verification import LinkTokenCreateRequestIncomeVerification
    from plaid.model.link_token_create_request_payment_initiation import LinkTokenCreateRequestPaymentInitiation
    from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
    from plaid.model.products import Products
    globals()['CountryCode'] = CountryCode
    globals()['LinkTokenAccountFilters'] = LinkTokenAccountFilters
    globals()['LinkTokenCreateRequestAuth'] = LinkTokenCreateRequestAuth
    globals()['LinkTokenCreateRequestDepositSwitch'] = LinkTokenCreateRequestDepositSwitch
    globals()['LinkTokenCreateRequestIncomeVerification'] = LinkTokenCreateRequestIncomeVerification
    globals()['LinkTokenCreateRequestPaymentInitiation'] = LinkTokenCreateRequestPaymentInitiation
    globals()['LinkTokenCreateRequestUser'] = LinkTokenCreateRequestUser
    globals()['Products'] = Products


class LinkTokenCreateRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('country_codes',): {
            'min_items': 1,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'client_name': (str,),  # noqa: E501
            'language': (str,),  # noqa: E501
            'country_codes': ([CountryCode],),  # noqa: E501
            'user': (LinkTokenCreateRequestUser,),  # noqa: E501
            'client_id': (str,),  # noqa: E501
            'secret': (str,),  # noqa: E501
            'products': ([Products],),  # noqa: E501
            'webhook': (str,),  # noqa: E501
            'access_token': (str,),  # noqa: E501
            'link_customization_name': (str,),  # noqa: E501
            'redirect_uri': (str,),  # noqa: E501
            'android_package_name': (str,),  # noqa: E501
            'account_filters': (LinkTokenAccountFilters,),  # noqa: E501
            'institution_id': (str,),  # noqa: E501
            'payment_initiation': (LinkTokenCreateRequestPaymentInitiation,),  # noqa: E501
            'deposit_switch': (LinkTokenCreateRequestDepositSwitch,),  # noqa: E501
            'income_verification': (LinkTokenCreateRequestIncomeVerification,),  # noqa: E501
            'auth': (LinkTokenCreateRequestAuth,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'client_name': 'client_name',  # noqa: E501
        'language': 'language',  # noqa: E501
        'country_codes': 'country_codes',  # noqa: E501
        'user': 'user',  # noqa: E501
        'client_id': 'client_id',  # noqa: E501
        'secret': 'secret',  # noqa: E501
        'products': 'products',  # noqa: E501
        'webhook': 'webhook',  # noqa: E501
        'access_token': 'access_token',  # noqa: E501
        'link_customization_name': 'link_customization_name',  # noqa: E501
        'redirect_uri': 'redirect_uri',  # noqa: E501
        'android_package_name': 'android_package_name',  # noqa: E501
        'account_filters': 'account_filters',  # noqa: E501
        'institution_id': 'institution_id',  # noqa: E501
        'payment_initiation': 'payment_initiation',  # noqa: E501
        'deposit_switch': 'deposit_switch',  # noqa: E501
        'income_verification': 'income_verification',  # noqa: E501
        'auth': 'auth',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, client_name, language, country_codes, user, *args, **kwargs):  # noqa: E501
        """LinkTokenCreateRequest - a model defined in OpenAPI

        Args:
            client_name (str): The name of your application, as it should be displayed in Link.
            language (str): The language that Link should be displayed in.  Supported languages are: - English (`'en'`) - French (`'fr'`) - Spanish (`'es'`) - Dutch (`'nl'`)  When using a Link customization, the language configured here must match the setting in the customization, or the customization will not be applied.
            country_codes ([CountryCode]): Specify an array of Plaid-supported country codes using the ISO-3166-1 alpha-2 country code standard. Institutions from all listed countries will be shown.  Supported country codes are: `US`, `CA`, `ES`, `FR`, `GB`, `IE`, `NL`. Example value: `['US', 'CA']`.  If Link is launched with multiple country codes, only products that you are enabled for in all countries will be used by Link. Note that while all countries are enabled by default in Sandbox and Development, in Production only US and Canada are enabled by default. To gain access to European institutions in the Production environment, [file a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access) via the Plaid dashboard. If you initialize with a European country code, your users will see the European consent panel during the Link flow.  If using a Link customization, make sure the country codes in the customization match those specified in `country_codes`. If both `country_codes` and a Link customization are used, the value in `country_codes` may override the value in the customization.  If using the Auth features Instant Match, Same-day Micro-deposits, or Automated Micro-deposits, `country_codes` must be set to `['US']`.
            user (LinkTokenCreateRequestUser):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            client_id (str): Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.. [optional]  # noqa: E501
            secret (str): Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.. [optional]  # noqa: E501
            products ([Products]): List of Plaid product(s) you wish to use. If launching Link in update mode, should be omitted; required otherwise. Valid products are:  `transactions`, `auth`, `identity`, `assets`, `investments`, `liabilities`, `payment_initiation`, `deposit_switch`  Example: `['auth', 'transactions']`  `balance` is *not* a valid value, the Balance product does not require explicit initalization and will automatically be initialized when any other product is initialized.  Only institutions that support *all* requested products will be shown in Link; to maximize the number of institutions listed, it is recommended to initialize Link with the minimal product set required for your use case. Additional products can be added after Link initialization by calling the relevant endpoints. For details and exceptions, see [Choosing when to initialize products](/docs/link/best-practices/#choosing-when-to-initialize-products).  In Production, you will be billed for each product that you specify when initializing Link. Note that a product cannot be removed from an Item once the Item has been initialized with that product. To stop billing on an Item for subscription-based products, such as Liabilities, Investments, and Transactions, remove the Item via `/item/remove`.. [optional]  # noqa: E501
            webhook (str): The destination URL to which any webhooks should be sent.. [optional]  # noqa: E501
            access_token (str): The `access_token` associated with the Item to update, used when updating or modifying an existing `access_token`. Used when launching Link in update mode, when completing the Same-day (manual) Micro-deposit flow, or (optionally) when initializing Link as part of the Payment Initiation (UK and Europe) flow.. [optional]  # noqa: E501
            link_customization_name (str): The name of the Link customization from the Plaid Dashboard to be applied to Link. If not specified, the `default` customization will be used. When using a Link customization, the language in the customization must match the language selected via the `language` parameter, and the countries in the customization should match the country codes selected via `country_codes`.. [optional]  # noqa: E501
            redirect_uri (str): A URI indicating the destination where a user should be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. The `redirect_uri` should not contain any query parameters. If `android_package_name` is specified, this field should be left blank. Any redirect URI specified here must also be added under the \"Allowed redirect URIs\" configuration on the [developer dashboard](https://dashboard.plaid.com/team/api). In non-Sandbox (Production and Development) environments, the `redirect_uri` must begin with https.. [optional]  # noqa: E501
            android_package_name (str): The name of your app's Android package. Required if using the `link_token` to initialize Link on Android. When creating a `link_token` for initializing Link on other platforms, this field must be left blank. Any package name specified here must also be added to the Allowed Android package names setting on the [developer dashboard](https://dashboard.plaid.com/team/api). . [optional]  # noqa: E501
            account_filters (LinkTokenAccountFilters): [optional]  # noqa: E501
            institution_id (str): Used for certain legacy use cases. [optional]  # noqa: E501
            payment_initiation (LinkTokenCreateRequestPaymentInitiation): [optional]  # noqa: E501
            deposit_switch (LinkTokenCreateRequestDepositSwitch): [optional]  # noqa: E501
            income_verification (LinkTokenCreateRequestIncomeVerification): [optional]  # noqa: E501
            auth (LinkTokenCreateRequestAuth): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.client_name = client_name
        self.language = language
        self.country_codes = country_codes
        self.user = user
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
