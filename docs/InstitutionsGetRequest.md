# InstitutionsGetRequest

InstitutionsGetRequest defines the request schema for `/institutions/get`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total number of Institutions to return. | 
**offset** | **int** | The number of Institutions to skip. | 
**country_codes** | [**[CountryCode]**](CountryCode.md) | Specify an array of Plaid-supported country codes this institution supports, using the ISO-3166-1 alpha-2 country code standard.  | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 
**options** | [**InstitutionsGetRequestOptions**](InstitutionsGetRequestOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


