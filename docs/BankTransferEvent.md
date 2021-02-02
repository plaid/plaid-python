# BankTransferEvent

Represents an event in the Bank Transfers API.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **int** | Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers. | 
**timestamp** | **str** | The datetime when this event occurred. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60;. | 
**event_type** | [**BankTransferEventType**](BankTransferEventType.md) |  | 
**account_id** | **str** | The account ID associated with the bank transfer. | 
**bank_transfer_id** | **str** | Plaid’s unique identifier for a bank transfer. | 
**bank_transfer_type** | [**BankTransferType**](BankTransferType.md) |  | 
**bank_transfer_amount** | **str** | The bank transfer amount. | 
**bank_transfer_iso_currency_code** | **str** | The currency of the bank transfer amount. | 
**failure_reason** | [**BankTransferFailure**](BankTransferFailure.md) |  | 
**direction** | [**BankTransferDirection**](BankTransferDirection.md) |  | 
**receiver_details** | [**BankTransferReceiverDetails**](BankTransferReceiverDetails.md) |  | 
**origination_account_id** | **str, none_type** | The ID of the origination account that this balance belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


