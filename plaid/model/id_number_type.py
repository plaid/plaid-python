"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.394.0
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



class IDNumberType(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            'AR_DNI': "ar_dni",
            'AU_DRIVERS_LICENSE': "au_drivers_license",
            'AU_PASSPORT': "au_passport",
            'BR_CPF': "br_cpf",
            'CA_SIN': "ca_sin",
            'CL_RUN': "cl_run",
            'CN_RESIDENT_CARD': "cn_resident_card",
            'CO_NIT': "co_nit",
            'DK_CPR': "dk_cpr",
            'EG_NATIONAL_ID': "eg_national_id",
            'ES_DNI': "es_dni",
            'ES_NIE': "es_nie",
            'HK_HKID': "hk_hkid",
            'IN_PAN': "in_pan",
            'IT_CF': "it_cf",
            'JO_CIVIL_ID': "jo_civil_id",
            'JP_MY_NUMBER': "jp_my_number",
            'KE_HUDUMA_NAMBA': "ke_huduma_namba",
            'KW_CIVIL_ID': "kw_civil_id",
            'MX_CURP': "mx_curp",
            'MX_RFC': "mx_rfc",
            'MY_NRIC': "my_nric",
            'NG_NIN': "ng_nin",
            'NZ_DRIVERS_LICENSE': "nz_drivers_license",
            'OM_CIVIL_ID': "om_civil_id",
            'PH_PSN': "ph_psn",
            'PL_PESEL': "pl_pesel",
            'RO_CNP': "ro_cnp",
            'SA_NATIONAL_ID': "sa_national_id",
            'SE_PIN': "se_pin",
            'SG_NRIC': "sg_nric",
            'TR_TC_KIMLIK': "tr_tc_kimlik",
            'US_SSN': "us_ssn",
            'US_SSN_LAST_4': "us_ssn_last_4",
            'ZA_SMART_ID': "za_smart_id",
        },
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
        return {
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    read_only_vars = set()

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """IDNumberType - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): A globally unique and human readable ID type, specific to the country and document category. For more context on this field, see [Hybrid Input Validation](https://plaid.com/docs/identity-verification/hybrid-input-validation).., must be one of ["ar_dni", "au_drivers_license", "au_passport", "br_cpf", "ca_sin", "cl_run", "cn_resident_card", "co_nit", "dk_cpr", "eg_national_id", "es_dni", "es_nie", "hk_hkid", "in_pan", "it_cf", "jo_civil_id", "jp_my_number", "ke_huduma_namba", "kw_civil_id", "mx_curp", "mx_rfc", "my_nric", "ng_nin", "nz_drivers_license", "om_civil_id", "ph_psn", "pl_pesel", "ro_cnp", "sa_national_id", "se_pin", "sg_nric", "tr_tc_kimlik", "us_ssn", "us_ssn_last_4", "za_smart_id", ]  # noqa: E501

        Keyword Args:
            value (str): A globally unique and human readable ID type, specific to the country and document category. For more context on this field, see [Hybrid Input Validation](https://plaid.com/docs/identity-verification/hybrid-input-validation).., must be one of ["ar_dni", "au_drivers_license", "au_passport", "br_cpf", "ca_sin", "cl_run", "cn_resident_card", "co_nit", "dk_cpr", "eg_national_id", "es_dni", "es_nie", "hk_hkid", "in_pan", "it_cf", "jo_civil_id", "jp_my_number", "ke_huduma_namba", "kw_civil_id", "mx_curp", "mx_rfc", "my_nric", "ng_nin", "nz_drivers_license", "om_civil_id", "ph_psn", "pl_pesel", "ro_cnp", "sa_national_id", "se_pin", "sg_nric", "tr_tc_kimlik", "us_ssn", "us_ssn_last_4", "za_smart_id", ]  # noqa: E501
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
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):
        """IDNumberType - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): A globally unique and human readable ID type, specific to the country and document category. For more context on this field, see [Hybrid Input Validation](https://plaid.com/docs/identity-verification/hybrid-input-validation).., must be one of ["ar_dni", "au_drivers_license", "au_passport", "br_cpf", "ca_sin", "cl_run", "cn_resident_card", "co_nit", "dk_cpr", "eg_national_id", "es_dni", "es_nie", "hk_hkid", "in_pan", "it_cf", "jo_civil_id", "jp_my_number", "ke_huduma_namba", "kw_civil_id", "mx_curp", "mx_rfc", "my_nric", "ng_nin", "nz_drivers_license", "om_civil_id", "ph_psn", "pl_pesel", "ro_cnp", "sa_national_id", "se_pin", "sg_nric", "tr_tc_kimlik", "us_ssn", "us_ssn_last_4", "za_smart_id", ]  # noqa: E501

        Keyword Args:
            value (str): A globally unique and human readable ID type, specific to the country and document category. For more context on this field, see [Hybrid Input Validation](https://plaid.com/docs/identity-verification/hybrid-input-validation).., must be one of ["ar_dni", "au_drivers_license", "au_passport", "br_cpf", "ca_sin", "cl_run", "cn_resident_card", "co_nit", "dk_cpr", "eg_national_id", "es_dni", "es_nie", "hk_hkid", "in_pan", "it_cf", "jo_civil_id", "jp_my_number", "ke_huduma_namba", "kw_civil_id", "mx_curp", "mx_rfc", "my_nric", "ng_nin", "nz_drivers_license", "om_civil_id", "ph_psn", "pl_pesel", "ro_cnp", "sa_national_id", "se_pin", "sg_nric", "tr_tc_kimlik", "us_ssn", "us_ssn_last_4", "za_smart_id", ]  # noqa: E501
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
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        return self
