# SandboxBankTransferSimulateRequest

SandboxBankTransferSimulateRequest defines the request schema for `/sandbox/bank_transfer/simulate`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_transfer_id** | **str** | Plaid’s unique identifier for a bank transfer. | 
**event_type** | **str** | The asynchronous event to be simulated. May be: &#x60;posted&#x60;, &#x60;failed&#x60;, or &#x60;reversed&#x60;.  An error will be returned if the event type is incompatible with the current transfer status. Compatible status --&gt; event type transitions include:  &#x60;pending&#x60; --&gt; &#x60;failed&#x60;  &#x60;pending&#x60; --&gt; &#x60;posted&#x60;  &#x60;posted&#x60; --&gt; &#x60;reversed&#x60;  | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 
**failure_reason** | [**BankTransferFailure**](BankTransferFailure.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


