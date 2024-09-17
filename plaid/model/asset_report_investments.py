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
    from plaid.model.investment_transaction_subtype import InvestmentTransactionSubtype
    from plaid.model.investment_transaction_type import InvestmentTransactionType
    globals()['InvestmentTransactionSubtype'] = InvestmentTransactionSubtype
    globals()['InvestmentTransactionType'] = InvestmentTransactionType


class AssetReportInvestments(ModelNormal):
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
            'investment_transaction_id': (str,),  # noqa: E501
            'account_id': (str,),  # noqa: E501
            'security_id': (str, none_type,),  # noqa: E501
            'date': (date,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'quantity': (float,),  # noqa: E501
            'vested_quantity': (float,),  # noqa: E501
            'vested_value': (float,),  # noqa: E501
            'amount': (float,),  # noqa: E501
            'price': (float,),  # noqa: E501
            'fees': (float, none_type,),  # noqa: E501
            'type': (InvestmentTransactionType,),  # noqa: E501
            'subtype': (InvestmentTransactionSubtype,),  # noqa: E501
            'iso_currency_code': (str, none_type,),  # noqa: E501
            'unofficial_currency_code': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'investment_transaction_id': 'investment_transaction_id',  # noqa: E501
        'account_id': 'account_id',  # noqa: E501
        'security_id': 'security_id',  # noqa: E501
        'date': 'date',  # noqa: E501
        'name': 'name',  # noqa: E501
        'quantity': 'quantity',  # noqa: E501
        'vested_quantity': 'vested_quantity',  # noqa: E501
        'vested_value': 'vested_value',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'price': 'price',  # noqa: E501
        'fees': 'fees',  # noqa: E501
        'type': 'type',  # noqa: E501
        'subtype': 'subtype',  # noqa: E501
        'iso_currency_code': 'iso_currency_code',  # noqa: E501
        'unofficial_currency_code': 'unofficial_currency_code',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, investment_transaction_id, account_id, security_id, date, name, quantity, vested_quantity, vested_value, amount, price, fees, type, subtype, iso_currency_code, unofficial_currency_code, *args, **kwargs):  # noqa: E501
        """AssetReportInvestments - a model defined in OpenAPI

        Args:
            investment_transaction_id (str): The ID of the Investment transaction, unique across all Plaid transactions. Like all Plaid identifiers, the `investment_transaction_id` is case sensitive.
            account_id (str): The `account_id` of the account against which this transaction posted.
            security_id (str, none_type): The `security_id` to which this transaction is related.
            date (date): The [ISO 8601](https://wikipedia.org/wiki/ISO_8601) posting date for the transaction.
            name (str): The institution’s description of the transaction.
            quantity (float): The number of units of the security involved in this transaction. Positive for buy transactions; negative for sell transactions.
            vested_quantity (float): The total quantity of vested assets held, as reported by the financial institution. Vested assets are only associated with [equities](https://plaid.com/docs/api/products/investments/#investments-holdings-get-response-securities-type).
            vested_value (float): The value of the vested holdings as reported by the institution.
            amount (float): The complete value of the transaction. Positive values when cash is debited, e.g. purchases of stock; negative values when cash is credited, e.g. sales of stock. Treatment remains the same for cash-only movements unassociated with securities.
            price (float): The price of the security at which this transaction occurred.
            fees (float, none_type): The combined value of all fees applied to this transaction
            type (InvestmentTransactionType):
            subtype (InvestmentTransactionSubtype):
            iso_currency_code (str, none_type): The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-`null`.
            unofficial_currency_code (str, none_type): The unofficial currency code associated with the holding. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.

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

        self.investment_transaction_id = investment_transaction_id
        self.account_id = account_id
        self.security_id = security_id
        self.date = date
        self.name = name
        self.quantity = quantity
        self.vested_quantity = vested_quantity
        self.vested_value = vested_value
        self.amount = amount
        self.price = price
        self.fees = fees
        self.type = type
        self.subtype = subtype
        self.iso_currency_code = iso_currency_code
        self.unofficial_currency_code = unofficial_currency_code
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
    def __init__(self, investment_transaction_id, account_id, security_id, date, name, quantity, vested_quantity, vested_value, amount, price, fees, type, subtype, iso_currency_code, unofficial_currency_code, *args, **kwargs):  # noqa: E501
        """AssetReportInvestments - a model defined in OpenAPI

        Args:
            investment_transaction_id (str): The ID of the Investment transaction, unique across all Plaid transactions. Like all Plaid identifiers, the `investment_transaction_id` is case sensitive.
            account_id (str): The `account_id` of the account against which this transaction posted.
            security_id (str, none_type): The `security_id` to which this transaction is related.
            date (date): The [ISO 8601](https://wikipedia.org/wiki/ISO_8601) posting date for the transaction.
            name (str): The institution’s description of the transaction.
            quantity (float): The number of units of the security involved in this transaction. Positive for buy transactions; negative for sell transactions.
            vested_quantity (float): The total quantity of vested assets held, as reported by the financial institution. Vested assets are only associated with [equities](https://plaid.com/docs/api/products/investments/#investments-holdings-get-response-securities-type).
            vested_value (float): The value of the vested holdings as reported by the institution.
            amount (float): The complete value of the transaction. Positive values when cash is debited, e.g. purchases of stock; negative values when cash is credited, e.g. sales of stock. Treatment remains the same for cash-only movements unassociated with securities.
            price (float): The price of the security at which this transaction occurred.
            fees (float, none_type): The combined value of all fees applied to this transaction
            type (InvestmentTransactionType):
            subtype (InvestmentTransactionSubtype):
            iso_currency_code (str, none_type): The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-`null`.
            unofficial_currency_code (str, none_type): The unofficial currency code associated with the holding. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.

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

        self.investment_transaction_id = investment_transaction_id
        self.account_id = account_id
        self.security_id = security_id
        self.date = date
        self.name = name
        self.quantity = quantity
        self.vested_quantity = vested_quantity
        self.vested_value = vested_value
        self.amount = amount
        self.price = price
        self.fees = fees
        self.type = type
        self.subtype = subtype
        self.iso_currency_code = iso_currency_code
        self.unofficial_currency_code = unofficial_currency_code
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
