# DefaultUpdateWebhook

Fired when new transaction data is available for an Item. Plaid will typically check for new transaction data several times a day. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;TRANSACTIONS&#x60; | 
**webhook_code** | **str** | &#x60;DEFAULT_UPDATE&#x60; | 
**new_transactions** | **float** | The number of new transactions detected since the last time this webhook was fired. | 
**item_id** | **str** | The &#x60;item_id&#x60; of the Item the webhook relates to. | 
**error** | [**Error**](Error.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


