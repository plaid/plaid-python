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



class BalancePlusAttributes(ModelNormal):
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
            'unauthorized_transactions_count_7d': (int, none_type,),  # noqa: E501
            'unauthorized_transactions_count_30d': (int, none_type,),  # noqa: E501
            'unauthorized_transactions_count_60d': (int, none_type,),  # noqa: E501
            'unauthorized_transactions_count_90d': (int, none_type,),  # noqa: E501
            'nsf_overdraft_transactions_count_7d': (int, none_type,),  # noqa: E501
            'nsf_overdraft_transactions_count_30d': (int, none_type,),  # noqa: E501
            'nsf_overdraft_transactions_count_60d': (int, none_type,),  # noqa: E501
            'nsf_overdraft_transactions_count_90d': (int, none_type,),  # noqa: E501
            'days_since_first_plaid_connection': (int, none_type,),  # noqa: E501
            'plaid_connections_count_7d': (int, none_type,),  # noqa: E501
            'plaid_connections_count_30d': (int, none_type,),  # noqa: E501
            'total_plaid_connections_count': (int, none_type,),  # noqa: E501
            'is_savings_or_money_market_account': (bool, none_type,),  # noqa: E501
            'phone_change_count_28d': (int, none_type,),  # noqa: E501
            'phone_change_count_90d': (int, none_type,),  # noqa: E501
            'email_change_count_28d': (int, none_type,),  # noqa: E501
            'email_change_count_90d': (int, none_type,),  # noqa: E501
            'address_change_count_28d': (int, none_type,),  # noqa: E501
            'address_change_count_90d': (int, none_type,),  # noqa: E501
            'plaid_non_oauth_authentication_attempts_count_3d': (int, none_type,),  # noqa: E501
            'plaid_non_oauth_authentication_attempts_count_7d': (int, none_type,),  # noqa: E501
            'plaid_non_oauth_authentication_attempts_count_30d': (int, none_type,),  # noqa: E501
            'failed_plaid_non_oauth_authentication_attempts_count_3d': (int, none_type,),  # noqa: E501
            'failed_plaid_non_oauth_authentication_attempts_count_7d': (int, none_type,),  # noqa: E501
            'failed_plaid_non_oauth_authentication_attempts_count_30d': (int, none_type,),  # noqa: E501
            'is_account_closed': (bool, none_type,),  # noqa: E501
            'is_account_frozen_or_restricted': (bool, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'unauthorized_transactions_count_7d': 'unauthorized_transactions_count_7d',  # noqa: E501
        'unauthorized_transactions_count_30d': 'unauthorized_transactions_count_30d',  # noqa: E501
        'unauthorized_transactions_count_60d': 'unauthorized_transactions_count_60d',  # noqa: E501
        'unauthorized_transactions_count_90d': 'unauthorized_transactions_count_90d',  # noqa: E501
        'nsf_overdraft_transactions_count_7d': 'nsf_overdraft_transactions_count_7d',  # noqa: E501
        'nsf_overdraft_transactions_count_30d': 'nsf_overdraft_transactions_count_30d',  # noqa: E501
        'nsf_overdraft_transactions_count_60d': 'nsf_overdraft_transactions_count_60d',  # noqa: E501
        'nsf_overdraft_transactions_count_90d': 'nsf_overdraft_transactions_count_90d',  # noqa: E501
        'days_since_first_plaid_connection': 'days_since_first_plaid_connection',  # noqa: E501
        'plaid_connections_count_7d': 'plaid_connections_count_7d',  # noqa: E501
        'plaid_connections_count_30d': 'plaid_connections_count_30d',  # noqa: E501
        'total_plaid_connections_count': 'total_plaid_connections_count',  # noqa: E501
        'is_savings_or_money_market_account': 'is_savings_or_money_market_account',  # noqa: E501
        'phone_change_count_28d': 'phone_change_count_28d',  # noqa: E501
        'phone_change_count_90d': 'phone_change_count_90d',  # noqa: E501
        'email_change_count_28d': 'email_change_count_28d',  # noqa: E501
        'email_change_count_90d': 'email_change_count_90d',  # noqa: E501
        'address_change_count_28d': 'address_change_count_28d',  # noqa: E501
        'address_change_count_90d': 'address_change_count_90d',  # noqa: E501
        'plaid_non_oauth_authentication_attempts_count_3d': 'plaid_non_oauth_authentication_attempts_count_3d',  # noqa: E501
        'plaid_non_oauth_authentication_attempts_count_7d': 'plaid_non_oauth_authentication_attempts_count_7d',  # noqa: E501
        'plaid_non_oauth_authentication_attempts_count_30d': 'plaid_non_oauth_authentication_attempts_count_30d',  # noqa: E501
        'failed_plaid_non_oauth_authentication_attempts_count_3d': 'failed_plaid_non_oauth_authentication_attempts_count_3d',  # noqa: E501
        'failed_plaid_non_oauth_authentication_attempts_count_7d': 'failed_plaid_non_oauth_authentication_attempts_count_7d',  # noqa: E501
        'failed_plaid_non_oauth_authentication_attempts_count_30d': 'failed_plaid_non_oauth_authentication_attempts_count_30d',  # noqa: E501
        'is_account_closed': 'is_account_closed',  # noqa: E501
        'is_account_frozen_or_restricted': 'is_account_frozen_or_restricted',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """BalancePlusAttributes - a model defined in OpenAPI

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
            unauthorized_transactions_count_7d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 7 days from the account that will be debited.. [optional]  # noqa: E501
            unauthorized_transactions_count_30d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 30 days from the account that will be debited.. [optional]  # noqa: E501
            unauthorized_transactions_count_60d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 60 days from the account that will be debited.. [optional]  # noqa: E501
            unauthorized_transactions_count_90d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 90 days from the account that will be debited.. [optional]  # noqa: E501
            nsf_overdraft_transactions_count_7d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 7 days from the account that will be debited.. [optional]  # noqa: E501
            nsf_overdraft_transactions_count_30d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 30 days from the account that will be debited.. [optional]  # noqa: E501
            nsf_overdraft_transactions_count_60d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 60 days from the account that will be debited.. [optional]  # noqa: E501
            nsf_overdraft_transactions_count_90d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 90 days from the account that will be debited.. [optional]  # noqa: E501
            days_since_first_plaid_connection (int, none_type): The number of days since the first time the Item was connected to an application via Plaid. [optional]  # noqa: E501
            plaid_connections_count_7d (int, none_type): The number of times the Item has been connected to applications via Plaid over the past 7 days. [optional]  # noqa: E501
            plaid_connections_count_30d (int, none_type): The number of times the Item has been connected to applications via Plaid over the past 30 days. [optional]  # noqa: E501
            total_plaid_connections_count (int, none_type): The total number of times the Item has been connected to applications via Plaid. [optional]  # noqa: E501
            is_savings_or_money_market_account (bool, none_type): Indicates if the ACH transaction funding account is a savings/money market account. [optional]  # noqa: E501
            phone_change_count_28d (int, none_type): The number of times the account's phone numbers on file have changed over the past 28 days. [optional]  # noqa: E501
            phone_change_count_90d (int, none_type): The number of times the account's phone numbers on file have changed over the past 90 days. [optional]  # noqa: E501
            email_change_count_28d (int, none_type): The number of times the account's email addresses on file have changed over the past 28 days. [optional]  # noqa: E501
            email_change_count_90d (int, none_type): The number of times the account's email addresses on file have changed over the past 90 days. [optional]  # noqa: E501
            address_change_count_28d (int, none_type): The number of times the account's addresses on file have changed over the past 28 days. [optional]  # noqa: E501
            address_change_count_90d (int, none_type): The number of times the account's addresses on file have changed over the past 90 days. [optional]  # noqa: E501
            plaid_non_oauth_authentication_attempts_count_3d (int, none_type): The number of non-OAuth authentication attempts via Plaid for this bank account over the past 3 days. [optional]  # noqa: E501
            plaid_non_oauth_authentication_attempts_count_7d (int, none_type): The number of non-OAuth authentication attempts via Plaid for this bank account over the past 7 days. [optional]  # noqa: E501
            plaid_non_oauth_authentication_attempts_count_30d (int, none_type): The number of non-OAuth authentication attempts via Plaid for this bank account over the past 30 days. [optional]  # noqa: E501
            failed_plaid_non_oauth_authentication_attempts_count_3d (int, none_type): The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 3 days. [optional]  # noqa: E501
            failed_plaid_non_oauth_authentication_attempts_count_7d (int, none_type): The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 7 days. [optional]  # noqa: E501
            failed_plaid_non_oauth_authentication_attempts_count_30d (int, none_type): The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 30 days. [optional]  # noqa: E501
            is_account_closed (bool, none_type): Indicates if the receiver bank account is closed. [optional]  # noqa: E501
            is_account_frozen_or_restricted (bool, none_type): Indicates if the receiver bank account is either frozen or restricted. [optional]  # noqa: E501
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
        """BalancePlusAttributes - a model defined in OpenAPI

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
            unauthorized_transactions_count_7d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 7 days from the account that will be debited.. [optional]  # noqa: E501
            unauthorized_transactions_count_30d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 30 days from the account that will be debited.. [optional]  # noqa: E501
            unauthorized_transactions_count_60d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 60 days from the account that will be debited.. [optional]  # noqa: E501
            unauthorized_transactions_count_90d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to unauthorized transactions over the past 90 days from the account that will be debited.. [optional]  # noqa: E501
            nsf_overdraft_transactions_count_7d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 7 days from the account that will be debited.. [optional]  # noqa: E501
            nsf_overdraft_transactions_count_30d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 30 days from the account that will be debited.. [optional]  # noqa: E501
            nsf_overdraft_transactions_count_60d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 60 days from the account that will be debited.. [optional]  # noqa: E501
            nsf_overdraft_transactions_count_90d (int, none_type): We parse and analyze historical transaction metadata to identify the number of possible past returns due to non-sufficient funds/overdrafts over the past 90 days from the account that will be debited.. [optional]  # noqa: E501
            days_since_first_plaid_connection (int, none_type): The number of days since the first time the Item was connected to an application via Plaid. [optional]  # noqa: E501
            plaid_connections_count_7d (int, none_type): The number of times the Item has been connected to applications via Plaid over the past 7 days. [optional]  # noqa: E501
            plaid_connections_count_30d (int, none_type): The number of times the Item has been connected to applications via Plaid over the past 30 days. [optional]  # noqa: E501
            total_plaid_connections_count (int, none_type): The total number of times the Item has been connected to applications via Plaid. [optional]  # noqa: E501
            is_savings_or_money_market_account (bool, none_type): Indicates if the ACH transaction funding account is a savings/money market account. [optional]  # noqa: E501
            phone_change_count_28d (int, none_type): The number of times the account's phone numbers on file have changed over the past 28 days. [optional]  # noqa: E501
            phone_change_count_90d (int, none_type): The number of times the account's phone numbers on file have changed over the past 90 days. [optional]  # noqa: E501
            email_change_count_28d (int, none_type): The number of times the account's email addresses on file have changed over the past 28 days. [optional]  # noqa: E501
            email_change_count_90d (int, none_type): The number of times the account's email addresses on file have changed over the past 90 days. [optional]  # noqa: E501
            address_change_count_28d (int, none_type): The number of times the account's addresses on file have changed over the past 28 days. [optional]  # noqa: E501
            address_change_count_90d (int, none_type): The number of times the account's addresses on file have changed over the past 90 days. [optional]  # noqa: E501
            plaid_non_oauth_authentication_attempts_count_3d (int, none_type): The number of non-OAuth authentication attempts via Plaid for this bank account over the past 3 days. [optional]  # noqa: E501
            plaid_non_oauth_authentication_attempts_count_7d (int, none_type): The number of non-OAuth authentication attempts via Plaid for this bank account over the past 7 days. [optional]  # noqa: E501
            plaid_non_oauth_authentication_attempts_count_30d (int, none_type): The number of non-OAuth authentication attempts via Plaid for this bank account over the past 30 days. [optional]  # noqa: E501
            failed_plaid_non_oauth_authentication_attempts_count_3d (int, none_type): The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 3 days. [optional]  # noqa: E501
            failed_plaid_non_oauth_authentication_attempts_count_7d (int, none_type): The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 7 days. [optional]  # noqa: E501
            failed_plaid_non_oauth_authentication_attempts_count_30d (int, none_type): The number of failed non-OAuth authentication attempts via Plaid for this bank account over the past 30 days. [optional]  # noqa: E501
            is_account_closed (bool, none_type): Indicates if the receiver bank account is closed. [optional]  # noqa: E501
            is_account_frozen_or_restricted (bool, none_type): Indicates if the receiver bank account is either frozen or restricted. [optional]  # noqa: E501
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