"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.503.0
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
    OpenApiModel
)
from plaid.exceptions import ApiAttributeError


def lazy_import():
    from plaid.model.partner_end_customer_address import PartnerEndCustomerAddress
    from plaid.model.partner_end_customer_assets_under_management import PartnerEndCustomerAssetsUnderManagement
    from plaid.model.partner_end_customer_billing_contact import PartnerEndCustomerBillingContact
    from plaid.model.partner_end_customer_customer_support_info import PartnerEndCustomerCustomerSupportInfo
    from plaid.model.partner_end_customer_technical_contact import PartnerEndCustomerTechnicalContact
    from plaid.model.products import Products
    globals()['PartnerEndCustomerAddress'] = PartnerEndCustomerAddress
    globals()['PartnerEndCustomerAssetsUnderManagement'] = PartnerEndCustomerAssetsUnderManagement
    globals()['PartnerEndCustomerBillingContact'] = PartnerEndCustomerBillingContact
    globals()['PartnerEndCustomerCustomerSupportInfo'] = PartnerEndCustomerCustomerSupportInfo
    globals()['PartnerEndCustomerTechnicalContact'] = PartnerEndCustomerTechnicalContact
    globals()['Products'] = Products


class PartnerCustomerCreateRequest(ModelNormal):
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
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

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
            'company_name': (str,),  # noqa: E501
            'is_diligence_attested': (bool,),  # noqa: E501
            'legal_entity_name': (str,),  # noqa: E501
            'website': (str,),  # noqa: E501
            'application_name': (str,),  # noqa: E501
            'address': (PartnerEndCustomerAddress,),  # noqa: E501
            'is_bank_addendum_completed': (bool,),  # noqa: E501
            'client_id': (str,),  # noqa: E501
            'secret': (str,),  # noqa: E501
            'products': ([Products],),  # noqa: E501
            'create_link_customization': (bool,),  # noqa: E501
            'logo': (str,),  # noqa: E501
            'technical_contact': (PartnerEndCustomerTechnicalContact,),  # noqa: E501
            'billing_contact': (PartnerEndCustomerBillingContact,),  # noqa: E501
            'customer_support_info': (PartnerEndCustomerCustomerSupportInfo,),  # noqa: E501
            'assets_under_management': (PartnerEndCustomerAssetsUnderManagement,),  # noqa: E501
            'redirect_uris': ([str],),  # noqa: E501
            'registration_number': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'company_name': 'company_name',  # noqa: E501
        'is_diligence_attested': 'is_diligence_attested',  # noqa: E501
        'legal_entity_name': 'legal_entity_name',  # noqa: E501
        'website': 'website',  # noqa: E501
        'application_name': 'application_name',  # noqa: E501
        'address': 'address',  # noqa: E501
        'is_bank_addendum_completed': 'is_bank_addendum_completed',  # noqa: E501
        'client_id': 'client_id',  # noqa: E501
        'secret': 'secret',  # noqa: E501
        'products': 'products',  # noqa: E501
        'create_link_customization': 'create_link_customization',  # noqa: E501
        'logo': 'logo',  # noqa: E501
        'technical_contact': 'technical_contact',  # noqa: E501
        'billing_contact': 'billing_contact',  # noqa: E501
        'customer_support_info': 'customer_support_info',  # noqa: E501
        'assets_under_management': 'assets_under_management',  # noqa: E501
        'redirect_uris': 'redirect_uris',  # noqa: E501
        'registration_number': 'registration_number',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, company_name, is_diligence_attested, legal_entity_name, website, application_name, address, is_bank_addendum_completed, *args, **kwargs):  # noqa: E501
        """PartnerCustomerCreateRequest - a model defined in OpenAPI

        Args:
            company_name (str): The company name of the end customer being created. This will be used to display the end customer in the Plaid Dashboard. It will not be shown to end users.
            is_diligence_attested (bool): Denotes whether or not the partner has completed attestation of diligence for the end customer to be created.
            legal_entity_name (str): The end customer's legal name. This will be shared with financial institutions as part of the OAuth registration process. It will not be shown to end users.
            website (str): The end customer's website.
            application_name (str): The name of the end customer's application. This will be shown to end users when they go through the Plaid Link flow.
            address (PartnerEndCustomerAddress):
            is_bank_addendum_completed (bool): Denotes whether the partner has forwarded the Plaid bank addendum to the end customer.

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
            products ([Products]): The products to be enabled for the end customer. If empty or `null`, this field will default to the products enabled for the reseller at the time this endpoint is called.. [optional]  # noqa: E501
            create_link_customization (bool): If `true`, the end customer's default Link customization will be set to match the partner's. You can always change the end customer's Link customization in the Plaid Dashboard. See the [Link Customization docs](https://plaid.com/docs/link/customization/) for more information.. [optional]  # noqa: E501
            logo (str): Base64-encoded representation of the end customer's logo. Must be a PNG of size 1024x1024 under 4MB. The logo will be shared with financial institutions and shown to the end user during Link flows. A logo is required if `create_link_customization` is `true`. If `create_link_customization` is `false` and the logo is omitted, the partner's logo will be used if one exists, otherwise a stock logo will be used.. [optional]  # noqa: E501
            technical_contact (PartnerEndCustomerTechnicalContact): [optional]  # noqa: E501
            billing_contact (PartnerEndCustomerBillingContact): [optional]  # noqa: E501
            customer_support_info (PartnerEndCustomerCustomerSupportInfo): [optional]  # noqa: E501
            assets_under_management (PartnerEndCustomerAssetsUnderManagement): [optional]  # noqa: E501
            redirect_uris ([str]): A list of URIs indicating the destination(s) where a user can be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. URIs should not contain any query parameters. When used in Production or Development, URIs must use https. To specify any subdomain, use `*` as a wildcard character, e.g. `https://*.example.com/oauth.html`. To modify redirect URIs for an end customer after creating them, go to the end customer's [API page](https://dashboard.plaid.com/team/api) in the Dashboard.. [optional]  # noqa: E501
            registration_number (str): The unique identifier assigned to a financial institution by regulatory authorities, if applicable. For banks, this is the FDIC Certificate Number. For credit unions, this is the Credit Union Charter Number.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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

        self.company_name = company_name
        self.is_diligence_attested = is_diligence_attested
        self.legal_entity_name = legal_entity_name
        self.website = website
        self.application_name = application_name
        self.address = address
        self.is_bank_addendum_completed = is_bank_addendum_completed
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, company_name, is_diligence_attested, legal_entity_name, website, application_name, address, is_bank_addendum_completed, *args, **kwargs):  # noqa: E501
        """PartnerCustomerCreateRequest - a model defined in OpenAPI

        Args:
            company_name (str): The company name of the end customer being created. This will be used to display the end customer in the Plaid Dashboard. It will not be shown to end users.
            is_diligence_attested (bool): Denotes whether or not the partner has completed attestation of diligence for the end customer to be created.
            legal_entity_name (str): The end customer's legal name. This will be shared with financial institutions as part of the OAuth registration process. It will not be shown to end users.
            website (str): The end customer's website.
            application_name (str): The name of the end customer's application. This will be shown to end users when they go through the Plaid Link flow.
            address (PartnerEndCustomerAddress):
            is_bank_addendum_completed (bool): Denotes whether the partner has forwarded the Plaid bank addendum to the end customer.

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
            products ([Products]): The products to be enabled for the end customer. If empty or `null`, this field will default to the products enabled for the reseller at the time this endpoint is called.. [optional]  # noqa: E501
            create_link_customization (bool): If `true`, the end customer's default Link customization will be set to match the partner's. You can always change the end customer's Link customization in the Plaid Dashboard. See the [Link Customization docs](https://plaid.com/docs/link/customization/) for more information.. [optional]  # noqa: E501
            logo (str): Base64-encoded representation of the end customer's logo. Must be a PNG of size 1024x1024 under 4MB. The logo will be shared with financial institutions and shown to the end user during Link flows. A logo is required if `create_link_customization` is `true`. If `create_link_customization` is `false` and the logo is omitted, the partner's logo will be used if one exists, otherwise a stock logo will be used.. [optional]  # noqa: E501
            technical_contact (PartnerEndCustomerTechnicalContact): [optional]  # noqa: E501
            billing_contact (PartnerEndCustomerBillingContact): [optional]  # noqa: E501
            customer_support_info (PartnerEndCustomerCustomerSupportInfo): [optional]  # noqa: E501
            assets_under_management (PartnerEndCustomerAssetsUnderManagement): [optional]  # noqa: E501
            redirect_uris ([str]): A list of URIs indicating the destination(s) where a user can be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. URIs should not contain any query parameters. When used in Production or Development, URIs must use https. To specify any subdomain, use `*` as a wildcard character, e.g. `https://*.example.com/oauth.html`. To modify redirect URIs for an end customer after creating them, go to the end customer's [API page](https://dashboard.plaid.com/team/api) in the Dashboard.. [optional]  # noqa: E501
            registration_number (str): The unique identifier assigned to a financial institution by regulatory authorities, if applicable. For banks, this is the FDIC Certificate Number. For credit unions, this is the Credit Union Charter Number.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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

        self.company_name = company_name
        self.is_diligence_attested = is_diligence_attested
        self.legal_entity_name = legal_entity_name
        self.website = website
        self.application_name = application_name
        self.address = address
        self.is_bank_addendum_completed = is_bank_addendum_completed
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")