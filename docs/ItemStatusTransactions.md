# ItemStatusTransactions

Information about the last successful and failed transactions update for the Item.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_successful_update** | **str, none_type** | ISO 8601 timestamp of the last successful transactions update for the Item. The status will update each time Plaid successfully connects with the institution, regardless of whether any new data is available in the update. | [optional] 
**last_failed_update** | **str, none_type** | ISO 8601 timestamp of the last failed transactions update for the Item. The status will update each time Plaid fails an attempt to connect with the institution, regardless of whether any new data is available in the update. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


