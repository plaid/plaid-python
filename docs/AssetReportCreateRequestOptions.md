# AssetReportCreateRequestOptions

An optional object to filter `/asset_report/create` results. If provided, must be non-`null`. The optional `user` object is required for the report to be eligible for Fannie Mae's Day 1 Certainty program.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_report_id** | **str** | Client-generated identifier, which can be used by lenders to track loan applications. | [optional] 
**webhook** | **str** | URL to which Plaid will send Assets webhooks, for example when the requested Asset Report is ready. | [optional] 
**user** | [**AssetReportUser**](AssetReportUser.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


