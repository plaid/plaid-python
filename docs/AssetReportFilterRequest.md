# AssetReportFilterRequest

AssetReportFilterRequest defines the request schema for `/asset_report/filter`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_report_token** | **str** | A token that can be provided to endpoints such as &#x60;/asset_report/get&#x60; or &#x60;/asset_report/pdf/get&#x60; to fetch or update an Asset Report. | 
**account_ids_to_exclude** | **[str]** | The accounts to exclude from the Asset Report, identified by &#x60;account_id&#x60;. | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


