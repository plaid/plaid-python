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



class DepositSwitchGetResponse(ModelNormal):
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
        ('state',): {
            'INITIALIZED': "initialized",
            'PROCESSING': "processing",
            'COMPLETED': "completed",
            'ERROR': "error",
        },
        ('switch_method',): {
            'None': None,
            'INSTANT': "instant",
            'MAIL': "mail",
            'PDF': "pdf",
            'NULL': "null",
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
            'deposit_switch_id': (str,),  # noqa: E501
            'target_account_id': (str, none_type,),  # noqa: E501
            'target_item_id': (str, none_type,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'account_has_multiple_allocations': (bool, none_type,),  # noqa: E501
            'is_allocated_remainder': (bool, none_type,),  # noqa: E501
            'percent_allocated': (float, none_type,),  # noqa: E501
            'amount_allocated': (float, none_type,),  # noqa: E501
            'date_created': (date,),  # noqa: E501
            'date_completed': (date, none_type,),  # noqa: E501
            'request_id': (str,),  # noqa: E501
            'switch_method': (str, none_type,),  # noqa: E501
            'employer_name': (str, none_type,),  # noqa: E501
            'employer_id': (str, none_type,),  # noqa: E501
            'institution_name': (str, none_type,),  # noqa: E501
            'institution_id': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'deposit_switch_id': 'deposit_switch_id',  # noqa: E501
        'target_account_id': 'target_account_id',  # noqa: E501
        'target_item_id': 'target_item_id',  # noqa: E501
        'state': 'state',  # noqa: E501
        'account_has_multiple_allocations': 'account_has_multiple_allocations',  # noqa: E501
        'is_allocated_remainder': 'is_allocated_remainder',  # noqa: E501
        'percent_allocated': 'percent_allocated',  # noqa: E501
        'amount_allocated': 'amount_allocated',  # noqa: E501
        'date_created': 'date_created',  # noqa: E501
        'date_completed': 'date_completed',  # noqa: E501
        'request_id': 'request_id',  # noqa: E501
        'switch_method': 'switch_method',  # noqa: E501
        'employer_name': 'employer_name',  # noqa: E501
        'employer_id': 'employer_id',  # noqa: E501
        'institution_name': 'institution_name',  # noqa: E501
        'institution_id': 'institution_id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, deposit_switch_id, target_account_id, target_item_id, state, account_has_multiple_allocations, is_allocated_remainder, percent_allocated, amount_allocated, date_created, date_completed, request_id, *args, **kwargs):  # noqa: E501
        """DepositSwitchGetResponse - a model defined in OpenAPI

        Args:
            deposit_switch_id (str): The ID of the deposit switch.
            target_account_id (str, none_type): The ID of the bank account the direct deposit was switched to.
            target_item_id (str, none_type): The ID of the Item the direct deposit was switched to.
            state (str):  The state, or status, of the deposit switch.  - `initialized` – The deposit switch has been initialized with the user entering the information required to submit the deposit switch request.  - `processing` – The deposit switch request has been submitted and is being processed.  - `completed` – The user's employer has fulfilled the deposit switch request.  - `error` – There was an error processing the deposit switch request.
            account_has_multiple_allocations (bool, none_type): When `true`, user’s direct deposit goes to multiple banks. When false, user’s direct deposit only goes to the target account. Always `null` if the deposit switch has not been completed.
            is_allocated_remainder (bool, none_type): When `true`, the target account is allocated the remainder of direct deposit after all other allocations have been deducted. When `false`, user’s direct deposit is allocated as a percent or amount. Always `null` if the deposit switch has not been completed.
            percent_allocated (float, none_type): The percentage of direct deposit allocated to the target account. Always `null` if the target account is not allocated a percentage or if the deposit switch has not been completed or if `is_allocated_remainder` is true.
            amount_allocated (float, none_type): The dollar amount of direct deposit allocated to the target account. Always `null` if the target account is not allocated an amount or if the deposit switch has not been completed.
            date_created (date): [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date the deposit switch was created. 
            date_completed (date, none_type): [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date the deposit switch was completed. Always `null` if the deposit switch has not been completed. 
            request_id (str): A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.

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
            switch_method (str, none_type): The method used to make the deposit switch.  - `instant` – User instantly switched their direct deposit to a new or existing bank account by connecting their payroll or employer account.  - `mail` – User requested that Plaid contact their employer by mail to make the direct deposit switch.  - `pdf` – User generated a PDF or email to be sent to their employer with the information necessary to make the deposit switch.'. [optional]  # noqa: E501
            employer_name (str, none_type): The name of the employer selected by the user. If the user did not select an employer, the value returned is `null`.. [optional]  # noqa: E501
            employer_id (str, none_type): The ID of the employer selected by the user. If the user did not select an employer, the value returned is `null`.. [optional]  # noqa: E501
            institution_name (str, none_type): The name of the institution selected by the user. If the user did not select an institution, the value returned is `null`.. [optional]  # noqa: E501
            institution_id (str, none_type): The ID of the institution selected by the user. If the user did not select an institution, the value returned is `null`.. [optional]  # noqa: E501
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

        self.deposit_switch_id = deposit_switch_id
        self.target_account_id = target_account_id
        self.target_item_id = target_item_id
        self.state = state
        self.account_has_multiple_allocations = account_has_multiple_allocations
        self.is_allocated_remainder = is_allocated_remainder
        self.percent_allocated = percent_allocated
        self.amount_allocated = amount_allocated
        self.date_created = date_created
        self.date_completed = date_completed
        self.request_id = request_id
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
    def __init__(self, deposit_switch_id, target_account_id, target_item_id, state, account_has_multiple_allocations, is_allocated_remainder, percent_allocated, amount_allocated, date_created, date_completed, request_id, *args, **kwargs):  # noqa: E501
        """DepositSwitchGetResponse - a model defined in OpenAPI

        Args:
            deposit_switch_id (str): The ID of the deposit switch.
            target_account_id (str, none_type): The ID of the bank account the direct deposit was switched to.
            target_item_id (str, none_type): The ID of the Item the direct deposit was switched to.
            state (str):  The state, or status, of the deposit switch.  - `initialized` – The deposit switch has been initialized with the user entering the information required to submit the deposit switch request.  - `processing` – The deposit switch request has been submitted and is being processed.  - `completed` – The user's employer has fulfilled the deposit switch request.  - `error` – There was an error processing the deposit switch request.
            account_has_multiple_allocations (bool, none_type): When `true`, user’s direct deposit goes to multiple banks. When false, user’s direct deposit only goes to the target account. Always `null` if the deposit switch has not been completed.
            is_allocated_remainder (bool, none_type): When `true`, the target account is allocated the remainder of direct deposit after all other allocations have been deducted. When `false`, user’s direct deposit is allocated as a percent or amount. Always `null` if the deposit switch has not been completed.
            percent_allocated (float, none_type): The percentage of direct deposit allocated to the target account. Always `null` if the target account is not allocated a percentage or if the deposit switch has not been completed or if `is_allocated_remainder` is true.
            amount_allocated (float, none_type): The dollar amount of direct deposit allocated to the target account. Always `null` if the target account is not allocated an amount or if the deposit switch has not been completed.
            date_created (date): [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date the deposit switch was created. 
            date_completed (date, none_type): [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date the deposit switch was completed. Always `null` if the deposit switch has not been completed. 
            request_id (str): A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.

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
            switch_method (str, none_type): The method used to make the deposit switch.  - `instant` – User instantly switched their direct deposit to a new or existing bank account by connecting their payroll or employer account.  - `mail` – User requested that Plaid contact their employer by mail to make the direct deposit switch.  - `pdf` – User generated a PDF or email to be sent to their employer with the information necessary to make the deposit switch.'. [optional]  # noqa: E501
            employer_name (str, none_type): The name of the employer selected by the user. If the user did not select an employer, the value returned is `null`.. [optional]  # noqa: E501
            employer_id (str, none_type): The ID of the employer selected by the user. If the user did not select an employer, the value returned is `null`.. [optional]  # noqa: E501
            institution_name (str, none_type): The name of the institution selected by the user. If the user did not select an institution, the value returned is `null`.. [optional]  # noqa: E501
            institution_id (str, none_type): The ID of the institution selected by the user. If the user did not select an institution, the value returned is `null`.. [optional]  # noqa: E501
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

        self.deposit_switch_id = deposit_switch_id
        self.target_account_id = target_account_id
        self.target_item_id = target_item_id
        self.state = state
        self.account_has_multiple_allocations = account_has_multiple_allocations
        self.is_allocated_remainder = is_allocated_remainder
        self.percent_allocated = percent_allocated
        self.amount_allocated = amount_allocated
        self.date_created = date_created
        self.date_completed = date_completed
        self.request_id = request_id
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
