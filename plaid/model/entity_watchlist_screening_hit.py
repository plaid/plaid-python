"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
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
)

def lazy_import():
    from plaid.model.entity_screening_hit_analysis import EntityScreeningHitAnalysis
    from plaid.model.entity_screening_hit_data import EntityScreeningHitData
    from plaid.model.entity_watchlist_code import EntityWatchlistCode
    from plaid.model.source_uid import SourceUID
    from plaid.model.watchlist_screening_hit_status import WatchlistScreeningHitStatus
    globals()['EntityScreeningHitAnalysis'] = EntityScreeningHitAnalysis
    globals()['EntityScreeningHitData'] = EntityScreeningHitData
    globals()['EntityWatchlistCode'] = EntityWatchlistCode
    globals()['SourceUID'] = SourceUID
    globals()['WatchlistScreeningHitStatus'] = WatchlistScreeningHitStatus


class EntityWatchlistScreeningHit(ModelNormal):
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

    additional_properties_type = None

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
            'id': (str,),  # noqa: E501
            'review_status': (WatchlistScreeningHitStatus,),  # noqa: E501
            'first_active': (datetime,),  # noqa: E501
            'inactive_since': (datetime, none_type,),  # noqa: E501
            'historical_since': (datetime, none_type,),  # noqa: E501
            'list_code': (EntityWatchlistCode,),  # noqa: E501
            'plaid_uid': (str,),  # noqa: E501
            'source_uid': (SourceUID,),  # noqa: E501
            'analysis': (EntityScreeningHitAnalysis,),  # noqa: E501
            'data': (EntityScreeningHitData,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'review_status': 'review_status',  # noqa: E501
        'first_active': 'first_active',  # noqa: E501
        'inactive_since': 'inactive_since',  # noqa: E501
        'historical_since': 'historical_since',  # noqa: E501
        'list_code': 'list_code',  # noqa: E501
        'plaid_uid': 'plaid_uid',  # noqa: E501
        'source_uid': 'source_uid',  # noqa: E501
        'analysis': 'analysis',  # noqa: E501
        'data': 'data',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, id, review_status, first_active, inactive_since, historical_since, list_code, plaid_uid, source_uid, *args, **kwargs):  # noqa: E501
        """EntityWatchlistScreeningHit - a model defined in OpenAPI

        Args:
            id (str): ID of the associated entity screening hit.
            review_status (WatchlistScreeningHitStatus):
            first_active (datetime): An ISO8601 formatted timestamp.
            inactive_since (datetime, none_type): An ISO8601 formatted timestamp.
            historical_since (datetime, none_type): An ISO8601 formatted timestamp.
            list_code (EntityWatchlistCode):
            plaid_uid (str): A universal identifier for a watchlist individual that is stable across searches and updates.
            source_uid (SourceUID):

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
            analysis (EntityScreeningHitAnalysis): [optional]  # noqa: E501
            data (EntityScreeningHitData): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
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

        self.id = id
        self.review_status = review_status
        self.first_active = first_active
        self.inactive_since = inactive_since
        self.historical_since = historical_since
        self.list_code = list_code
        self.plaid_uid = plaid_uid
        self.source_uid = source_uid
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
