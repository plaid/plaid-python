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
    from plaid.model.transfer_create_idempotency_key import TransferCreateIdempotencyKey
    from plaid.model.transfer_metadata import TransferMetadata
    from plaid.model.transfer_user_in_request_deprecated import TransferUserInRequestDeprecated
    globals()['TransferCreateIdempotencyKey'] = TransferCreateIdempotencyKey
    globals()['TransferMetadata'] = TransferMetadata
    globals()['TransferUserInRequestDeprecated'] = TransferUserInRequestDeprecated


class TransferCreateRequest(ModelNormal):
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
        ('description',): {
            'max_length': 15,
        },
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
            'access_token': (str,),  # noqa: E501
            'account_id': (str,),  # noqa: E501
            'authorization_id': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'client_id': (str,),  # noqa: E501
            'secret': (str,),  # noqa: E501
            'idempotency_key': (TransferCreateIdempotencyKey,),  # noqa: E501
            'type': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'network': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'amount': (str,),  # noqa: E501
            'ach_class': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'user': (TransferUserInRequestDeprecated,),  # noqa: E501
            'metadata': (TransferMetadata,),  # noqa: E501
            'origination_account_id': (str, none_type,),  # noqa: E501
            'iso_currency_code': (str,),  # noqa: E501
            'test_clock_id': (str, none_type,),  # noqa: E501
            'facilitator_fee': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'access_token': 'access_token',  # noqa: E501
        'account_id': 'account_id',  # noqa: E501
        'authorization_id': 'authorization_id',  # noqa: E501
        'description': 'description',  # noqa: E501
        'client_id': 'client_id',  # noqa: E501
        'secret': 'secret',  # noqa: E501
        'idempotency_key': 'idempotency_key',  # noqa: E501
        'type': 'type',  # noqa: E501
        'network': 'network',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'ach_class': 'ach_class',  # noqa: E501
        'user': 'user',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'origination_account_id': 'origination_account_id',  # noqa: E501
        'iso_currency_code': 'iso_currency_code',  # noqa: E501
        'test_clock_id': 'test_clock_id',  # noqa: E501
        'facilitator_fee': 'facilitator_fee',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, access_token, account_id, authorization_id, description, *args, **kwargs):  # noqa: E501
        """TransferCreateRequest - a model defined in OpenAPI

        Args:
            access_token (str): The Plaid `access_token` for the account that will be debited or credited.
            account_id (str): The Plaid `account_id` corresponding to the end-user account that will be debited or credited.
            authorization_id (str): Plaid’s unique identifier for a transfer authorization. This parameter also serves the purpose of acting as an idempotency identifier.
            description (str): The transfer description. Maximum of 15 characters. If reprocessing a returned transfer, please note that the `description` field must be `\"Retry 1\"` or `\"Retry 2\"` to indicate that it's a retry of a previously returned transfer. You may retry a transfer up to 2 times, within 180 days of creating the original transfer. Only transfers that were returned with code `R01` or `R09` may be retried. For a full listing of ACH return codes, see [Transfer errors](https://plaid.com/docs/errors/transfer/#ach-return-codes).

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
            idempotency_key (TransferCreateIdempotencyKey): [optional]  # noqa: E501
            type (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            network (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            amount (str): The amount of the transfer (decimal string with two digits of precision e.g. \"10.00\"). When calling `/transfer/authorization/create`, specify the maximum amount to authorize. When calling `/transfer/create`, specify the exact amount of the transfer, up to a maximum of the amount authorized. If this field is left blank when calling `/transfer/create`, the maximum amount authorized in the `authorization_id` will be sent.. [optional]  # noqa: E501
            ach_class (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            user (TransferUserInRequestDeprecated): [optional]  # noqa: E501
            metadata (TransferMetadata): [optional]  # noqa: E501
            origination_account_id (str, none_type): Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. Otherwise, this field should be left blank.. [optional]  # noqa: E501
            iso_currency_code (str): The currency of the transfer amount. The default value is \"USD\".. [optional]  # noqa: E501
            test_clock_id (str, none_type): Plaid’s unique identifier for a test clock. This field may only be used when using `sandbox` environment. If provided, the `transfer` is created at the `virtual_time` on the provided `test_clock`.. [optional]  # noqa: E501
            facilitator_fee (str): The amount to deduct from `transfer.amount` and distribute to the platform’s Ledger balance as a facilitator fee (decimal string with two digits of precision e.g. \"10.00\"). The remainder will go to the end-customer’s Ledger balance. This must be less than or equal to the `transfer.amount`.. [optional]  # noqa: E501
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

        self.access_token = access_token
        self.account_id = account_id
        self.authorization_id = authorization_id
        self.description = description
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
    def __init__(self, access_token, account_id, authorization_id, description, *args, **kwargs):  # noqa: E501
        """TransferCreateRequest - a model defined in OpenAPI

        Args:
            access_token (str): The Plaid `access_token` for the account that will be debited or credited.
            account_id (str): The Plaid `account_id` corresponding to the end-user account that will be debited or credited.
            authorization_id (str): Plaid’s unique identifier for a transfer authorization. This parameter also serves the purpose of acting as an idempotency identifier.
            description (str): The transfer description. Maximum of 15 characters. If reprocessing a returned transfer, please note that the `description` field must be `\"Retry 1\"` or `\"Retry 2\"` to indicate that it's a retry of a previously returned transfer. You may retry a transfer up to 2 times, within 180 days of creating the original transfer. Only transfers that were returned with code `R01` or `R09` may be retried. For a full listing of ACH return codes, see [Transfer errors](https://plaid.com/docs/errors/transfer/#ach-return-codes).

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
            idempotency_key (TransferCreateIdempotencyKey): [optional]  # noqa: E501
            type (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            network (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            amount (str): The amount of the transfer (decimal string with two digits of precision e.g. \"10.00\"). When calling `/transfer/authorization/create`, specify the maximum amount to authorize. When calling `/transfer/create`, specify the exact amount of the transfer, up to a maximum of the amount authorized. If this field is left blank when calling `/transfer/create`, the maximum amount authorized in the `authorization_id` will be sent.. [optional]  # noqa: E501
            ach_class (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            user (TransferUserInRequestDeprecated): [optional]  # noqa: E501
            metadata (TransferMetadata): [optional]  # noqa: E501
            origination_account_id (str, none_type): Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. Otherwise, this field should be left blank.. [optional]  # noqa: E501
            iso_currency_code (str): The currency of the transfer amount. The default value is \"USD\".. [optional]  # noqa: E501
            test_clock_id (str, none_type): Plaid’s unique identifier for a test clock. This field may only be used when using `sandbox` environment. If provided, the `transfer` is created at the `virtual_time` on the provided `test_clock`.. [optional]  # noqa: E501
            facilitator_fee (str): The amount to deduct from `transfer.amount` and distribute to the platform’s Ledger balance as a facilitator fee (decimal string with two digits of precision e.g. \"10.00\"). The remainder will go to the end-customer’s Ledger balance. This must be less than or equal to the `transfer.amount`.. [optional]  # noqa: E501
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

        self.access_token = access_token
        self.account_id = account_id
        self.authorization_id = authorization_id
        self.description = description
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
