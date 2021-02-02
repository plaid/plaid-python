# AssetReportRefreshResponse

AssetReportRefreshResponse defines the response schema for `/asset_report/refresh`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_report_id** | **str** | A unique ID identifying an Asset Report. Like all Plaid identifiers, this ID is case sensitive. | 
**asset_report_token** | **str** | A token that can be provided to endpoints such as &#x60;/asset_report/get&#x60; or &#x60;/asset_report/pdf/get&#x60; to fetch or update an Asset Report. | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


