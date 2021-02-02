# InvestmentsDefaultUpdateWebhook

Fired when new or canceled transactions have been detected on an investment account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;INVESTMENTS_TRANSACTIONS&#x60; | 
**webhook_code** | **str** | &#x60;DEFAULT_UPDATE&#x60; | 
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**new_investments_transactions** | **float** | The number of new transactions reported since the last time this webhook was fired. | 
**canceled_investments_transactions** | **float** | The number of canceled transactions reported since the last time this webhook was fired. | 
**error** | [**Error**](Error.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


