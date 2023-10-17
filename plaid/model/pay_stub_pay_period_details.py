"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.457.0
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
    from plaid.model.credit_pay_stub_pay_basis_type import CreditPayStubPayBasisType
    from plaid.model.pay_stub_distribution_breakdown import PayStubDistributionBreakdown
    globals()['CreditPayStubPayBasisType'] = CreditPayStubPayBasisType
    globals()['PayStubDistributionBreakdown'] = PayStubDistributionBreakdown


class PayStubPayPeriodDetails(ModelNormal):
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
            'pay_amount': (float, none_type,),  # noqa: E501
            'distribution_breakdown': ([PayStubDistributionBreakdown],),  # noqa: E501
            'end_date': (date, none_type,),  # noqa: E501
            'gross_earnings': (float, none_type,),  # noqa: E501
            'iso_currency_code': (str, none_type,),  # noqa: E501
            'pay_date': (date, none_type,),  # noqa: E501
            'pay_frequency': (str, none_type,),  # noqa: E501
            'start_date': (date, none_type,),  # noqa: E501
            'unofficial_currency_code': (str, none_type,),  # noqa: E501
            'pay_basis': (CreditPayStubPayBasisType,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'pay_amount': 'pay_amount',  # noqa: E501
        'distribution_breakdown': 'distribution_breakdown',  # noqa: E501
        'end_date': 'end_date',  # noqa: E501
        'gross_earnings': 'gross_earnings',  # noqa: E501
        'iso_currency_code': 'iso_currency_code',  # noqa: E501
        'pay_date': 'pay_date',  # noqa: E501
        'pay_frequency': 'pay_frequency',  # noqa: E501
        'start_date': 'start_date',  # noqa: E501
        'unofficial_currency_code': 'unofficial_currency_code',  # noqa: E501
        'pay_basis': 'pay_basis',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, pay_amount, distribution_breakdown, end_date, gross_earnings, iso_currency_code, pay_date, pay_frequency, start_date, unofficial_currency_code, *args, **kwargs):  # noqa: E501
        """PayStubPayPeriodDetails - a model defined in OpenAPI

        Args:
            pay_amount (float, none_type): The amount of the paycheck.
            distribution_breakdown ([PayStubDistributionBreakdown]):
            end_date (date, none_type): The date on which the pay period ended, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\"yyyy-mm-dd\").
            gross_earnings (float, none_type): Total earnings before tax/deductions.
            iso_currency_code (str, none_type): The ISO-4217 currency code of the net pay. Always `null` if `unofficial_currency_code` is non-null.
            pay_date (date, none_type): The date on which the pay stub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\"yyyy-mm-dd\").
            pay_frequency (str, none_type): The frequency at which an individual is paid.
            start_date (date, none_type): The date on which the pay period started, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\"yyyy-mm-dd\").
            unofficial_currency_code (str, none_type): The unofficial currency code associated with the net pay. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.

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
            pay_basis (CreditPayStubPayBasisType): [optional]  # noqa: E501
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

        self.pay_amount = pay_amount
        self.distribution_breakdown = distribution_breakdown
        self.end_date = end_date
        self.gross_earnings = gross_earnings
        self.iso_currency_code = iso_currency_code
        self.pay_date = pay_date
        self.pay_frequency = pay_frequency
        self.start_date = start_date
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
    def __init__(self, pay_amount, distribution_breakdown, end_date, gross_earnings, iso_currency_code, pay_date, pay_frequency, start_date, unofficial_currency_code, *args, **kwargs):  # noqa: E501
        """PayStubPayPeriodDetails - a model defined in OpenAPI

        Args:
            pay_amount (float, none_type): The amount of the paycheck.
            distribution_breakdown ([PayStubDistributionBreakdown]):
            end_date (date, none_type): The date on which the pay period ended, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\"yyyy-mm-dd\").
            gross_earnings (float, none_type): Total earnings before tax/deductions.
            iso_currency_code (str, none_type): The ISO-4217 currency code of the net pay. Always `null` if `unofficial_currency_code` is non-null.
            pay_date (date, none_type): The date on which the pay stub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\"yyyy-mm-dd\").
            pay_frequency (str, none_type): The frequency at which an individual is paid.
            start_date (date, none_type): The date on which the pay period started, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (\"yyyy-mm-dd\").
            unofficial_currency_code (str, none_type): The unofficial currency code associated with the net pay. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.

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
            pay_basis (CreditPayStubPayBasisType): [optional]  # noqa: E501
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

        self.pay_amount = pay_amount
        self.distribution_breakdown = distribution_breakdown
        self.end_date = end_date
        self.gross_earnings = gross_earnings
        self.iso_currency_code = iso_currency_code
        self.pay_date = pay_date
        self.pay_frequency = pay_frequency
        self.start_date = start_date
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
