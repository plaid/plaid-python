"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.610.1
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



class TransactionsGetRequestOptions(ModelNormal):
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
        ('count',): {
            'inclusive_maximum': 500,
            'inclusive_minimum': 1,
        },
        ('offset',): {
            'inclusive_minimum': 0,
        },
        ('days_requested',): {
            'inclusive_maximum': 730,
            'inclusive_minimum': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
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
        return {
            'account_ids': ([str],),  # noqa: E501
            'count': (int,),  # noqa: E501
            'offset': (int,),  # noqa: E501
            'include_original_description': (bool, none_type,),  # noqa: E501
            'include_personal_finance_category_beta': (bool,),  # noqa: E501
            'include_personal_finance_category': (bool,),  # noqa: E501
            'include_logo_and_counterparty_beta': (bool,),  # noqa: E501
            'days_requested': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'account_ids': 'account_ids',  # noqa: E501
        'count': 'count',  # noqa: E501
        'offset': 'offset',  # noqa: E501
        'include_original_description': 'include_original_description',  # noqa: E501
        'include_personal_finance_category_beta': 'include_personal_finance_category_beta',  # noqa: E501
        'include_personal_finance_category': 'include_personal_finance_category',  # noqa: E501
        'include_logo_and_counterparty_beta': 'include_logo_and_counterparty_beta',  # noqa: E501
        'days_requested': 'days_requested',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """TransactionsGetRequestOptions - a model defined in OpenAPI

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
            account_ids ([str]): A list of `account_ids` to retrieve for the Item  Note: An error will be returned if a provided `account_id` is not associated with the Item.. [optional]  # noqa: E501
            count (int): The number of transactions to fetch.. [optional] if omitted the server will use the default value of 100  # noqa: E501
            offset (int): The number of transactions to skip. The default value is 0.. [optional] if omitted the server will use the default value of 0  # noqa: E501
            include_original_description (bool, none_type): Include the raw unparsed transaction description from the financial institution.. [optional] if omitted the server will use the default value of False  # noqa: E501
            include_personal_finance_category_beta (bool): Personal finance categories are now returned by default.. [optional] if omitted the server will use the default value of False  # noqa: E501
            include_personal_finance_category (bool): Personal finance categories are now returned by default.. [optional] if omitted the server will use the default value of False  # noqa: E501
            include_logo_and_counterparty_beta (bool): Counterparties and extra merchant fields are now returned by default.. [optional] if omitted the server will use the default value of False  # noqa: E501
            days_requested (int): This field only applies to calls for Items where the Transactions product has not already been initialized (i.e. by specifying `transactions` in the `products`, `optional_products`, or `required_if_consented_products` array when calling `/link/token/create` or by making a previous call to `/transactions/sync` or `/transactions/get`). In those cases, the field controls the maximum number of days of transaction history that Plaid will request from the financial institution. The more transaction history is requested, the longer the historical update poll will take. If no value is specified, 90 days of history will be requested by default. If a value under 30 is provided, a minimum of 30 days of history will be requested.  If you are initializing your Items with transactions during the `/link/token/create` call (e.g. by including `transactions` in the `/link/token/create` `products` array), you must use the [`transactions.days_requested`](https://plaid.com/docs/api/link/#link-token-create-request-transactions-days-requested) field in the `/link/token/create` request instead of in the `/transactions/get` request.  If the Item has already been initialized with the Transactions product, this field will have no effect. The maximum amount of transaction history to request on an Item cannot be updated if Transactions has already been added to the Item. To request older transaction history on an Item where Transactions has already been added, you must delete the Item via `/item/remove` and send the user through Link to create a new Item.   Customers using [Recurring Transactions](https://plaid.com/docs/api/products/transactions/#transactionsrecurringget) should request at least 180 days of history for optimal results.. [optional] if omitted the server will use the default value of 90  # noqa: E501
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """TransactionsGetRequestOptions - a model defined in OpenAPI

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
            account_ids ([str]): A list of `account_ids` to retrieve for the Item  Note: An error will be returned if a provided `account_id` is not associated with the Item.. [optional]  # noqa: E501
            count (int): The number of transactions to fetch.. [optional] if omitted the server will use the default value of 100  # noqa: E501
            offset (int): The number of transactions to skip. The default value is 0.. [optional] if omitted the server will use the default value of 0  # noqa: E501
            include_original_description (bool, none_type): Include the raw unparsed transaction description from the financial institution.. [optional] if omitted the server will use the default value of False  # noqa: E501
            include_personal_finance_category_beta (bool): Personal finance categories are now returned by default.. [optional] if omitted the server will use the default value of False  # noqa: E501
            include_personal_finance_category (bool): Personal finance categories are now returned by default.. [optional] if omitted the server will use the default value of False  # noqa: E501
            include_logo_and_counterparty_beta (bool): Counterparties and extra merchant fields are now returned by default.. [optional] if omitted the server will use the default value of False  # noqa: E501
            days_requested (int): This field only applies to calls for Items where the Transactions product has not already been initialized (i.e. by specifying `transactions` in the `products`, `optional_products`, or `required_if_consented_products` array when calling `/link/token/create` or by making a previous call to `/transactions/sync` or `/transactions/get`). In those cases, the field controls the maximum number of days of transaction history that Plaid will request from the financial institution. The more transaction history is requested, the longer the historical update poll will take. If no value is specified, 90 days of history will be requested by default. If a value under 30 is provided, a minimum of 30 days of history will be requested.  If you are initializing your Items with transactions during the `/link/token/create` call (e.g. by including `transactions` in the `/link/token/create` `products` array), you must use the [`transactions.days_requested`](https://plaid.com/docs/api/link/#link-token-create-request-transactions-days-requested) field in the `/link/token/create` request instead of in the `/transactions/get` request.  If the Item has already been initialized with the Transactions product, this field will have no effect. The maximum amount of transaction history to request on an Item cannot be updated if Transactions has already been added to the Item. To request older transaction history on an Item where Transactions has already been added, you must delete the Item via `/item/remove` and send the user through Link to create a new Item.   Customers using [Recurring Transactions](https://plaid.com/docs/api/products/transactions/#transactionsrecurringget) should request at least 180 days of history for optimal results.. [optional] if omitted the server will use the default value of 90  # noqa: E501
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
