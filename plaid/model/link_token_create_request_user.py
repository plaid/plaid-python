"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.586.4
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
    from plaid.model.link_token_create_request_user_address import LinkTokenCreateRequestUserAddress
    from plaid.model.link_token_create_request_user_id_number import LinkTokenCreateRequestUserIdNumber
    from plaid.model.link_token_create_request_user_name import LinkTokenCreateRequestUserName
    globals()['LinkTokenCreateRequestUserAddress'] = LinkTokenCreateRequestUserAddress
    globals()['LinkTokenCreateRequestUserIdNumber'] = LinkTokenCreateRequestUserIdNumber
    globals()['LinkTokenCreateRequestUserName'] = LinkTokenCreateRequestUserName


class LinkTokenCreateRequestUser(ModelNormal):
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
        ('client_user_id',): {
            'min_length': 1,
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
            'client_user_id': (str,),  # noqa: E501
            'legal_name': (str,),  # noqa: E501
            'name': (LinkTokenCreateRequestUserName,),  # noqa: E501
            'phone_number': (str,),  # noqa: E501
            'phone_number_verified_time': (datetime, none_type,),  # noqa: E501
            'email_address': (str,),  # noqa: E501
            'email_address_verified_time': (datetime, none_type,),  # noqa: E501
            'ssn': (str,),  # noqa: E501
            'date_of_birth': (date, none_type,),  # noqa: E501
            'address': (LinkTokenCreateRequestUserAddress,),  # noqa: E501
            'id_number': (LinkTokenCreateRequestUserIdNumber,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'client_user_id': 'client_user_id',  # noqa: E501
        'legal_name': 'legal_name',  # noqa: E501
        'name': 'name',  # noqa: E501
        'phone_number': 'phone_number',  # noqa: E501
        'phone_number_verified_time': 'phone_number_verified_time',  # noqa: E501
        'email_address': 'email_address',  # noqa: E501
        'email_address_verified_time': 'email_address_verified_time',  # noqa: E501
        'ssn': 'ssn',  # noqa: E501
        'date_of_birth': 'date_of_birth',  # noqa: E501
        'address': 'address',  # noqa: E501
        'id_number': 'id_number',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, client_user_id, *args, **kwargs):  # noqa: E501
        """LinkTokenCreateRequestUser - a model defined in OpenAPI

        Args:
            client_user_id (str): A unique ID representing the end user. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`. It is currently used as a means of searching logs for the given user in the Plaid Dashboard.

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
            legal_name (str): The user's full legal name, used for [micro-deposit based verification flows](https://plaid.com/docs/auth/coverage/). For a small number of customers on legacy flows, providing this field is required to enable micro-deposit-based flows. For all other customers, this field is optional. Providing the user's name in this field when using micro-deposit-based verification will streamline the end user experience, as the user will not be prompted to enter their name during the Link flow; Plaid will use the provided legal name instead.. [optional]  # noqa: E501
            name (LinkTokenCreateRequestUserName): [optional]  # noqa: E501
            phone_number (str): The user's phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format. If supplied, will be used when applicable to prefill phone number fields in Link for the [returning user flow](https://www.plaid.com/docs/link/returning-user) and the [Identity Verification flow](https://www.plaid.com/docs/identity-verification).. [optional]  # noqa: E501
            phone_number_verified_time (datetime, none_type): The date and time the phone number was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDThh:mm:ssZ`). This was previously an optional field used in the [returning user experience](https://plaid.com/docs/link/returning-user). This field is no longer required to enable the returning user experience.   Only pass a verification time for a phone number that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.   Example: `2020-01-01T00:00:00Z` . [optional]  # noqa: E501
            email_address (str): The user's email address. Can be used to prefill Link fields when used with [Identity Verification](https://www.plaid.com/docs/identity-verification).. [optional]  # noqa: E501
            email_address_verified_time (datetime, none_type): The date and time the email address was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDThh:mm:ssZ`). This was previously an optional field used in the [returning user experience](https://plaid.com/docs/link/returning-user). This field is no longer required to enable the returning user experience.   Only pass a verification time for an email address that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.   Example: `2020-01-01T00:00:00Z`. [optional]  # noqa: E501
            ssn (str): Deprecated and not currently used, use the `id_number` field instead.. [optional]  # noqa: E501
            date_of_birth (date, none_type): To be provided in the format \"yyyy-mm-dd\". Can be used to prefill Link fields when used with Identity Verification.. [optional]  # noqa: E501
            address (LinkTokenCreateRequestUserAddress): [optional]  # noqa: E501
            id_number (LinkTokenCreateRequestUserIdNumber): [optional]  # noqa: E501
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

        self.client_user_id = client_user_id
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
    def __init__(self, client_user_id, *args, **kwargs):  # noqa: E501
        """LinkTokenCreateRequestUser - a model defined in OpenAPI

        Args:
            client_user_id (str): A unique ID representing the end user. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`. It is currently used as a means of searching logs for the given user in the Plaid Dashboard.

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
            legal_name (str): The user's full legal name, used for [micro-deposit based verification flows](https://plaid.com/docs/auth/coverage/). For a small number of customers on legacy flows, providing this field is required to enable micro-deposit-based flows. For all other customers, this field is optional. Providing the user's name in this field when using micro-deposit-based verification will streamline the end user experience, as the user will not be prompted to enter their name during the Link flow; Plaid will use the provided legal name instead.. [optional]  # noqa: E501
            name (LinkTokenCreateRequestUserName): [optional]  # noqa: E501
            phone_number (str): The user's phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format. If supplied, will be used when applicable to prefill phone number fields in Link for the [returning user flow](https://www.plaid.com/docs/link/returning-user) and the [Identity Verification flow](https://www.plaid.com/docs/identity-verification).. [optional]  # noqa: E501
            phone_number_verified_time (datetime, none_type): The date and time the phone number was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDThh:mm:ssZ`). This was previously an optional field used in the [returning user experience](https://plaid.com/docs/link/returning-user). This field is no longer required to enable the returning user experience.   Only pass a verification time for a phone number that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.   Example: `2020-01-01T00:00:00Z` . [optional]  # noqa: E501
            email_address (str): The user's email address. Can be used to prefill Link fields when used with [Identity Verification](https://www.plaid.com/docs/identity-verification).. [optional]  # noqa: E501
            email_address_verified_time (datetime, none_type): The date and time the email address was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDThh:mm:ssZ`). This was previously an optional field used in the [returning user experience](https://plaid.com/docs/link/returning-user). This field is no longer required to enable the returning user experience.   Only pass a verification time for an email address that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.   Example: `2020-01-01T00:00:00Z`. [optional]  # noqa: E501
            ssn (str): Deprecated and not currently used, use the `id_number` field instead.. [optional]  # noqa: E501
            date_of_birth (date, none_type): To be provided in the format \"yyyy-mm-dd\". Can be used to prefill Link fields when used with Identity Verification.. [optional]  # noqa: E501
            address (LinkTokenCreateRequestUserAddress): [optional]  # noqa: E501
            id_number (LinkTokenCreateRequestUserIdNumber): [optional]  # noqa: E501
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

        self.client_user_id = client_user_id
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
