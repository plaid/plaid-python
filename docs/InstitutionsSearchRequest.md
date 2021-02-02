# InstitutionsSearchRequest

InstitutionsSearchRequest defines the request schema for `/institutions/search`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The search query. Institutions with names matching the query are returned | 
**products** | [**[Products]**](Products.md) | Filter the Institutions based on whether they support all products listed in products. Provide &#x60;null&#x60; to get institutions regardless of supported products | 
**country_codes** | [**[CountryCode]**](CountryCode.md) | Specify an array of Plaid-supported country codes this institution supports, using the ISO-3166-1 alpha-2 country code standard.  | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 
**options** | [**InstitutionsSearchRequestOptions**](InstitutionsSearchRequestOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


