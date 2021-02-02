# ItemImportRequest

ItemImportRequest defines the request schema for `/item/import`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | **[str]** | Array of product strings. For Deposit Switch, this should be &#x60;[\&quot;auth\&quot;, \&quot;identity\&quot;]&#x60; | 
**user_auth** | [**ItemImportRequestUserAuth**](ItemImportRequestUserAuth.md) |  | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 
**options** | [**ItemImportRequestOptions**](ItemImportRequestOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


