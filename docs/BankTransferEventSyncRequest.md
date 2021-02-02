# BankTransferEventSyncRequest

BankTransferEventSyncRequest defines the request schema for `/bank_transfer/event/sync`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_id** | **int** | The latest (largest) &#x60;event_id&#x60; fetched via the sync endpoint, or 0 initially. | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 
**count** | **int, none_type** | The maximum number of bank transfer events to return. | [optional]  if omitted the server will use the default value of 25

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


