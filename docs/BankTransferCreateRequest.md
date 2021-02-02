# BankTransferCreateRequest

BankTransferCreateRequest defines the request schema for `/bank_transfer/create`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idempotency_key** | **str** | A random key provided by the client, per unique bank transfer. Maximum of 50 characters.  The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create a bank transfer fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single bank transfer is created. | 
**access_token** | **str** | The Plaid &#x60;access_token&#x60; for the account that will be debited or credited. | 
**account_id** | **str** | The Plaid &#x60;account_id&#x60; for the account that will be debited or credited. | 
**type** | [**BankTransferType**](BankTransferType.md) |  | 
**network** | [**BankTransferNetwork**](BankTransferNetwork.md) |  | 
**amount** | **str** | The transfer amount (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**iso_currency_code** | **str** | The currency of the transfer amount – should be set to \&quot;USD\&quot;. | 
**description** | **str** | The transfer description. Maximum of 10 characters. | 
**user** | [**BankTransferUser**](BankTransferUser.md) |  | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 
**ach_class** | [**ACHClass**](ACHClass.md) |  | [optional] 
**custom_tag** | **str** | An arbitrary string provided by the client for storage with the bank transfer. Will be returned in all &#x60;BankTransfer&#x60; objects. May be up to 100 characters. | [optional] 
**metadata** | [**BankTransferMetadata**](BankTransferMetadata.md) |  | [optional] 
**origination_account_id** | **str** | Plaid’s unique identifier for the origination account for this transfer. If you have more than one origination account, this value must be specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


