# AccountAssetsAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owners** | [**[Owner]**](Owner.md) | Data returned by the financial institution about the account owner or owners. Only returned by Identity or Assets endpoints. Multiple owners on a single account will be represented in the same &#x60;owner&#x60; object, not in multiple owner objects within the array. | 
**days_available** | **float, none_type** | The duration of transaction history available for this Item, typically defined as the time since the date of the earliest transaction in that account. Only returned by Assets endpoints. | [optional] 
**transactions** | [**[AssetReportTransaction], none_type**](AssetReportTransaction.md) | Transaction history associated with the account. Only returned by Assets endpoints. Transaction history returned by endpoints such as &#x60;/transactions/get&#x60; or &#x60;/investments/transactions/get&#x60; will be returned in the top-level &#x60;transactions&#x60; field instead. | [optional] 
**historical_balances** | [**[HistoricalBalance], none_type**](HistoricalBalance.md) | Calculated data about the historical balances on the account. Only returned by Assets endpoints. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


