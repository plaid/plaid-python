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


def lazy_import():
    from plaid.model.external_payment_refund_details import ExternalPaymentRefundDetails
    from plaid.model.external_payment_schedule_get import ExternalPaymentScheduleGet
    from plaid.model.payment_amount import PaymentAmount
    from plaid.model.payment_amount_refunded import PaymentAmountRefunded
    from plaid.model.payment_initiation_payment_status import PaymentInitiationPaymentStatus
    from plaid.model.payment_scheme import PaymentScheme
    from plaid.model.sender_bacs_nullable import SenderBACSNullable
    globals()['ExternalPaymentRefundDetails'] = ExternalPaymentRefundDetails
    globals()['ExternalPaymentScheduleGet'] = ExternalPaymentScheduleGet
    globals()['PaymentAmount'] = PaymentAmount
    globals()['PaymentAmountRefunded'] = PaymentAmountRefunded
    globals()['PaymentInitiationPaymentStatus'] = PaymentInitiationPaymentStatus
    globals()['PaymentScheme'] = PaymentScheme
    globals()['SenderBACSNullable'] = SenderBACSNullable


class PaymentInitiationPayment(ModelNormal):
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
            'payment_id': (str,),  # noqa: E501
            'amount': (PaymentAmount,),  # noqa: E501
            'status': (PaymentInitiationPaymentStatus,),  # noqa: E501
            'recipient_id': (str,),  # noqa: E501
            'reference': (str,),  # noqa: E501
            'last_status_update': (datetime,),  # noqa: E501
            'bacs': (SenderBACSNullable,),  # noqa: E501
            'iban': (str, none_type,),  # noqa: E501
            'adjusted_reference': (str, none_type,),  # noqa: E501
            'schedule': (ExternalPaymentScheduleGet,),  # noqa: E501
            'refund_details': (ExternalPaymentRefundDetails,),  # noqa: E501
            'refund_ids': ([str], none_type,),  # noqa: E501
            'amount_refunded': (PaymentAmountRefunded,),  # noqa: E501
            'wallet_id': (str, none_type,),  # noqa: E501
            'scheme': (PaymentScheme,),  # noqa: E501
            'adjusted_scheme': (PaymentScheme,),  # noqa: E501
            'consent_id': (str, none_type,),  # noqa: E501
            'transaction_id': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'payment_id': 'payment_id',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'status': 'status',  # noqa: E501
        'recipient_id': 'recipient_id',  # noqa: E501
        'reference': 'reference',  # noqa: E501
        'last_status_update': 'last_status_update',  # noqa: E501
        'bacs': 'bacs',  # noqa: E501
        'iban': 'iban',  # noqa: E501
        'adjusted_reference': 'adjusted_reference',  # noqa: E501
        'schedule': 'schedule',  # noqa: E501
        'refund_details': 'refund_details',  # noqa: E501
        'refund_ids': 'refund_ids',  # noqa: E501
        'amount_refunded': 'amount_refunded',  # noqa: E501
        'wallet_id': 'wallet_id',  # noqa: E501
        'scheme': 'scheme',  # noqa: E501
        'adjusted_scheme': 'adjusted_scheme',  # noqa: E501
        'consent_id': 'consent_id',  # noqa: E501
        'transaction_id': 'transaction_id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, payment_id, amount, status, recipient_id, reference, last_status_update, bacs, iban, *args, **kwargs):  # noqa: E501
        """PaymentInitiationPayment - a model defined in OpenAPI

        Args:
            payment_id (str): The ID of the payment. Like all Plaid identifiers, the `payment_id` is case sensitive.
            amount (PaymentAmount):
            status (PaymentInitiationPaymentStatus):
            recipient_id (str): The ID of the recipient
            reference (str): A reference for the payment.
            last_status_update (datetime): The date and time of the last time the `status` was updated, in IS0 8601 format
            bacs (SenderBACSNullable):
            iban (str, none_type): The International Bank Account Number (IBAN) for the sender, if specified in the `/payment_initiation/payment/create` call.

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
            adjusted_reference (str, none_type): The value of the reference sent to the bank after adjustment to pass bank validation rules.. [optional]  # noqa: E501
            schedule (ExternalPaymentScheduleGet): [optional]  # noqa: E501
            refund_details (ExternalPaymentRefundDetails): [optional]  # noqa: E501
            refund_ids ([str], none_type): Refund IDs associated with the payment.. [optional]  # noqa: E501
            amount_refunded (PaymentAmountRefunded): [optional]  # noqa: E501
            wallet_id (str, none_type): The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests.. [optional]  # noqa: E501
            scheme (PaymentScheme): [optional]  # noqa: E501
            adjusted_scheme (PaymentScheme): [optional]  # noqa: E501
            consent_id (str, none_type): The payment consent ID that this payment was initiated with. Is present only when payment was initiated using the payment consent.. [optional]  # noqa: E501
            transaction_id (str, none_type): The transaction ID that this payment is associated with, if any. This is present only when a payment was initiated using virtual accounts.. [optional]  # noqa: E501
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

        self.payment_id = payment_id
        self.amount = amount
        self.status = status
        self.recipient_id = recipient_id
        self.reference = reference
        self.last_status_update = last_status_update
        self.bacs = bacs
        self.iban = iban
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
    def __init__(self, payment_id, amount, status, recipient_id, reference, last_status_update, bacs, iban, *args, **kwargs):  # noqa: E501
        """PaymentInitiationPayment - a model defined in OpenAPI

        Args:
            payment_id (str): The ID of the payment. Like all Plaid identifiers, the `payment_id` is case sensitive.
            amount (PaymentAmount):
            status (PaymentInitiationPaymentStatus):
            recipient_id (str): The ID of the recipient
            reference (str): A reference for the payment.
            last_status_update (datetime): The date and time of the last time the `status` was updated, in IS0 8601 format
            bacs (SenderBACSNullable):
            iban (str, none_type): The International Bank Account Number (IBAN) for the sender, if specified in the `/payment_initiation/payment/create` call.

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
            adjusted_reference (str, none_type): The value of the reference sent to the bank after adjustment to pass bank validation rules.. [optional]  # noqa: E501
            schedule (ExternalPaymentScheduleGet): [optional]  # noqa: E501
            refund_details (ExternalPaymentRefundDetails): [optional]  # noqa: E501
            refund_ids ([str], none_type): Refund IDs associated with the payment.. [optional]  # noqa: E501
            amount_refunded (PaymentAmountRefunded): [optional]  # noqa: E501
            wallet_id (str, none_type): The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests.. [optional]  # noqa: E501
            scheme (PaymentScheme): [optional]  # noqa: E501
            adjusted_scheme (PaymentScheme): [optional]  # noqa: E501
            consent_id (str, none_type): The payment consent ID that this payment was initiated with. Is present only when payment was initiated using the payment consent.. [optional]  # noqa: E501
            transaction_id (str, none_type): The transaction ID that this payment is associated with, if any. This is present only when a payment was initiated using virtual accounts.. [optional]  # noqa: E501
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

        self.payment_id = payment_id
        self.amount = amount
        self.status = status
        self.recipient_id = recipient_id
        self.reference = reference
        self.last_status_update = last_status_update
        self.bacs = bacs
        self.iban = iban
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
