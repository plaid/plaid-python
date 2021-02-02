# AssetReportItem

A representation of an Item within an Asset Report.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**institution_name** | **str** | The full financial institution name associated with the Item. | 
**institution_id** | **str** | The id of the financial institution associated with the Item. | 
**date_last_updated** | **str** | The date and time when this Item’s data was last retrieved from the financial institution, in ISO 8601 format. | 
**accounts** | [**[AccountAssets]**](AccountAssets.md) | Data about each of the accounts open on the Item. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


