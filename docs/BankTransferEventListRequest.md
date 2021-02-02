# BankTransferEventListRequest

BankTransferEventListRequest defines the request schema for `/bank_transfer/event/list`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 
**start_date** | **datetime, none_type** | The start datetime of bank transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] 
**end_date** | **datetime, none_type** | The end datetime of bank transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] 
**bank_transfer_id** | **str, none_type** | Plaid’s unique identifier for a bank transfer. | [optional] 
**account_id** | **str, none_type** | The account ID to get events for all transactions to/from an account. | [optional] 
**bank_transfer_type** | **str, none_type** | The type of bank transfer. This will be either &#x60;debit&#x60; or &#x60;credit&#x60;.  A &#x60;debit&#x60; indicates a transfer of money into your origination account; a &#x60;credit&#x60; indicates a transfer of money out of your origination account. | [optional] 
**event_types** | [**[BankTransferEventType]**](BankTransferEventType.md) | Filter events by event type. | [optional] 
**count** | **int, none_type** | The maximum number of bank transfer events to return. If the number of events matching the above parameters is greater than &#x60;count&#x60;, the most recent events will be returned. | [optional]  if omitted the server will use the default value of 25
**offset** | **int, none_type** | The offset into the list of bank transfer events. When &#x60;count&#x60;&#x3D;25 and &#x60;offset&#x60;&#x3D;0, the first 25 events will be returned. When &#x60;count&#x60;&#x3D;25 and &#x60;offset&#x60;&#x3D;25, the next 25 bank transfer events will be returned. | [optional]  if omitted the server will use the default value of 0
**origination_account_id** | **str, none_type** | The origination account ID to get events for transfers from a specific origination account. | [optional] 
**direction** | **str, none_type** | Indicates the direction of the transfer: &#x60;outbound&#x60; for API-initiated transfers, or &#x60;inbound&#x60; for payments received by the FBO account. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


