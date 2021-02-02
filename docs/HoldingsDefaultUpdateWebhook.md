# HoldingsDefaultUpdateWebhook

Fired when new or updated holdings have been detected on an investment account. The webhook typically fires once per day, after market close, in response to any newly added holdings or price changes to existing holdings.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;HOLDINGS&#x60; | 
**webhook_code** | **str** | &#x60;DEFAULT_UPDATE&#x60; | 
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**new_holdings** | **float** | The number of new holdings reported since the last time this webhook was fired. | 
**updated_holdings** | **float** | The number of updated holdings reported since the last time this webhook was fired. | 
**error** | [**Error**](Error.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


