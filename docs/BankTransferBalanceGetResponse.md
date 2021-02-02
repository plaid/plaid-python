# BankTransferBalanceGetResponse

BankTransferBalanceGetResponse defines the response schema for `/bank_transfer/balance/get`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**BankTransferBalance**](BankTransferBalance.md) |  | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**origination_account_id** | **str, none_type** | The ID of the origination account that this balance belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


