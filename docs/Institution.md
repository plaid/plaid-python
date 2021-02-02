# Institution

Details relating to a specific financial institution
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_id** | **str** | Unique identifier for the institution | 
**name** | **str** | The official name of the institution | 
**products** | [**[Products]**](Products.md) | A list of the Plaid products supported by the institution | 
**country_codes** | [**[CountryCode]**](CountryCode.md) | A list of the country codes supported by the institution. | 
**oauth** | **bool** | Indicates that the institution has an OAuth login flow. This is primarily relevant to institutions with European country codes. | 
**url** | **str, none_type** | The URL for the institution&#39;s website | [optional] 
**primary_color** | **str, none_type** | Hexadecimal representation of the primary color used by the institution | [optional] 
**logo** | **str, none_type** | Base64 encoded representation of the institution&#39;s logo | [optional] 
**routing_numbers** | **[str], none_type** | A partial list of routing numbers associated with the institution. This list is provided for the purpose of looking up institutions by routing number. It is not comprehensive and should never be used as a complete list of routing numbers for an institution. | [optional] 
**status** | [**InstitutionStatus**](InstitutionStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


