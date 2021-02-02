# AssetsErrorWebhook

Fired when Asset Report generation has failed. The resulting `error` will have an `error_type` of `ASSET_REPORT_ERROR`.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;ASSETS&#x60; | 
**webhook_code** | **str** | &#x60;ERROR&#x60; | 
**error** | [**Error**](Error.md) |  | 
**asset_report_id** | **str** | The ID associated with the Asset Report. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


