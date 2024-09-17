"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.565.0
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
    from plaid.model.item_consented_data_scope import ItemConsentedDataScope
    from plaid.model.plaid_error import PlaidError
    from plaid.model.products import Products
    globals()['ItemConsentedDataScope'] = ItemConsentedDataScope
    globals()['PlaidError'] = PlaidError
    globals()['Products'] = Products


class Item(ModelNormal):
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
        ('update_type',): {
            'BACKGROUND': "background",
            'USER_PRESENT_REQUIRED': "user_present_required",
        },
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
            'item_id': (str,),  # noqa: E501
            'webhook': (str, none_type,),  # noqa: E501
            'error': (PlaidError,),  # noqa: E501
            'available_products': ([Products],),  # noqa: E501
            'billed_products': ([Products],),  # noqa: E501
            'consent_expiration_time': (datetime, none_type,),  # noqa: E501
            'update_type': (str,),  # noqa: E501
            'institution_id': (str, none_type,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'products': ([Products],),  # noqa: E501
            'consented_products': ([Products],),  # noqa: E501
            'consented_use_cases': ([str],),  # noqa: E501
            'consented_data_scopes': ([ItemConsentedDataScope],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'item_id': 'item_id',  # noqa: E501
        'webhook': 'webhook',  # noqa: E501
        'error': 'error',  # noqa: E501
        'available_products': 'available_products',  # noqa: E501
        'billed_products': 'billed_products',  # noqa: E501
        'consent_expiration_time': 'consent_expiration_time',  # noqa: E501
        'update_type': 'update_type',  # noqa: E501
        'institution_id': 'institution_id',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'products': 'products',  # noqa: E501
        'consented_products': 'consented_products',  # noqa: E501
        'consented_use_cases': 'consented_use_cases',  # noqa: E501
        'consented_data_scopes': 'consented_data_scopes',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, item_id, webhook, error, available_products, billed_products, consent_expiration_time, update_type, *args, **kwargs):  # noqa: E501
        """Item - a model defined in OpenAPI

        Args:
            item_id (str): The Plaid Item ID. The `item_id` is always unique; linking the same account at the same institution twice will result in two Items with different `item_id` values. Like all Plaid identifiers, the `item_id` is case-sensitive.
            webhook (str, none_type): The URL registered to receive webhooks for the Item.
            error (PlaidError):
            available_products ([Products]): A list of products available for the Item that have not yet been accessed. The contents of this array will be mutually exclusive with `billed_products`.
            billed_products ([Products]): A list of products that have been billed for the Item. The contents of this array will be mutually exclusive with `available_products`. Note - `billed_products` is populated in all environments but only requests in Production are billed. Also note that products that are billed on a pay-per-call basis rather than a pay-per-Item basis, such as `balance`, will not appear here. 
            consent_expiration_time (datetime, none_type): The date and time at which the Item's access consent will expire, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format
            update_type (str): Indicates whether an Item requires user interaction to be updated, which can be the case for Items with some forms of two-factor authentication.  `background` - Item can be updated in the background  `user_present_required` - Item requires user interaction to be updated

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
            institution_id (str, none_type): The Plaid Institution ID associated with the Item. Field is `null` for Items created via Same Day Micro-deposits.. [optional]  # noqa: E501
            created_at (datetime): The date and time when the Item was created, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.. [optional]  # noqa: E501
            products ([Products]): A list of products added to the Item. In almost all cases, this will be the same as the `billed_products` field. For some products, it is possible for the product to be added to an Item but not yet billed (e.g. Assets, before `/asset_report/create` has been called, or Auth or Identity when added as Optional Products but before their endpoints have been called), in which case the product may appear in `products` but not in `billed_products`. . [optional]  # noqa: E501
            consented_products ([Products]): A list of products that the user has consented to for the Item via [Data Transparency Messaging](/docs/link/data-transparency-messaging-migration-guide). This will consist of all products where both of the following are true: the user has consented to the required data scopes for that product and you have Production access for that product. . [optional]  # noqa: E501
            consented_use_cases ([str]): A list of use cases that the user has consented to for the Item via [Data Transparency Messaging](/docs/link/data-transparency-messaging-migration-guide).   You can see the full list of use cases or update the list of use cases to request at any time via the Link Customization section of the [Plaid Dashboard](https://dashboard.plaid.com/link/data-transparency-v5).. [optional]  # noqa: E501
            consented_data_scopes ([ItemConsentedDataScope]): A list of data scopes that the user has consented to for the Item via [Data Transparency Messaging](/docs/link/data-transparency-messaging-migration-guide). These are based on the `consented_products`; see the [full mapping](/docs/link/data-transparency-messaging-migration-guide/#data-scopes-by-product) of data scopes and products.. [optional]  # noqa: E501
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

        self.item_id = item_id
        self.webhook = webhook
        self.error = error
        self.available_products = available_products
        self.billed_products = billed_products
        self.consent_expiration_time = consent_expiration_time
        self.update_type = update_type
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
    def __init__(self, item_id, webhook, error, available_products, billed_products, consent_expiration_time, update_type, *args, **kwargs):  # noqa: E501
        """Item - a model defined in OpenAPI

        Args:
            item_id (str): The Plaid Item ID. The `item_id` is always unique; linking the same account at the same institution twice will result in two Items with different `item_id` values. Like all Plaid identifiers, the `item_id` is case-sensitive.
            webhook (str, none_type): The URL registered to receive webhooks for the Item.
            error (PlaidError):
            available_products ([Products]): A list of products available for the Item that have not yet been accessed. The contents of this array will be mutually exclusive with `billed_products`.
            billed_products ([Products]): A list of products that have been billed for the Item. The contents of this array will be mutually exclusive with `available_products`. Note - `billed_products` is populated in all environments but only requests in Production are billed. Also note that products that are billed on a pay-per-call basis rather than a pay-per-Item basis, such as `balance`, will not appear here. 
            consent_expiration_time (datetime, none_type): The date and time at which the Item's access consent will expire, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format
            update_type (str): Indicates whether an Item requires user interaction to be updated, which can be the case for Items with some forms of two-factor authentication.  `background` - Item can be updated in the background  `user_present_required` - Item requires user interaction to be updated

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
            institution_id (str, none_type): The Plaid Institution ID associated with the Item. Field is `null` for Items created via Same Day Micro-deposits.. [optional]  # noqa: E501
            created_at (datetime): The date and time when the Item was created, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.. [optional]  # noqa: E501
            products ([Products]): A list of products added to the Item. In almost all cases, this will be the same as the `billed_products` field. For some products, it is possible for the product to be added to an Item but not yet billed (e.g. Assets, before `/asset_report/create` has been called, or Auth or Identity when added as Optional Products but before their endpoints have been called), in which case the product may appear in `products` but not in `billed_products`. . [optional]  # noqa: E501
            consented_products ([Products]): A list of products that the user has consented to for the Item via [Data Transparency Messaging](/docs/link/data-transparency-messaging-migration-guide). This will consist of all products where both of the following are true: the user has consented to the required data scopes for that product and you have Production access for that product. . [optional]  # noqa: E501
            consented_use_cases ([str]): A list of use cases that the user has consented to for the Item via [Data Transparency Messaging](/docs/link/data-transparency-messaging-migration-guide).   You can see the full list of use cases or update the list of use cases to request at any time via the Link Customization section of the [Plaid Dashboard](https://dashboard.plaid.com/link/data-transparency-v5).. [optional]  # noqa: E501
            consented_data_scopes ([ItemConsentedDataScope]): A list of data scopes that the user has consented to for the Item via [Data Transparency Messaging](/docs/link/data-transparency-messaging-migration-guide). These are based on the `consented_products`; see the [full mapping](/docs/link/data-transparency-messaging-migration-guide/#data-scopes-by-product) of data scopes and products.. [optional]  # noqa: E501
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

        self.item_id = item_id
        self.webhook = webhook
        self.error = error
        self.available_products = available_products
        self.billed_products = billed_products
        self.consent_expiration_time = consent_expiration_time
        self.update_type = update_type
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
