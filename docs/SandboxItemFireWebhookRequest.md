# SandboxItemFireWebhookRequest

SandboxItemFireWebhookRequest defines the request schema for `/sandbox/item/fire_webhook`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token associated with the Item data is being requested for. | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 
**webhook_code** | **str** | The following values for &#x60;webhook_code&#x60; are supported:  * &#x60;DEFAULT_UPDATE&#x60; | [optional]  if omitted the server will use the default value of "DEFAULT_UPDATE"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


