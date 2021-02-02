# AssetReportRefreshRequestOptions

An optional object to filter `/asset_report/refresh` results. If provided, cannot be `null`. If not specified, the `options` from the original call to `/asset_report/create` will be used.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_report_id** | **str** | Client-generated identifier, which can be used by lenders to track loan applications. | [optional] 
**webhook** | **str** | URL to which Plaid will send Assets webhooks, for example when the requested Asset Report is ready. | [optional] 
**user** | [**AssetReportUser**](AssetReportUser.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


