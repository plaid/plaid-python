# BankTransferListRequest

BankTransferListRequest defines the request schema for `/bank_transfer/list`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 
**start_date** | **datetime, none_type** | The start datetime of bank transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] 
**end_date** | **datetime, none_type** | The end datetime of bank transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] 
**count** | **int** | The maximum number of bank transfers to return. | [optional]  if omitted the server will use the default value of 25
**offset** | **int** | The number of bank transfers to skip before returning results. | [optional]  if omitted the server will use the default value of 0
**origination_account_id** | **str, none_type** | Filter bank transfers to only those originated through the specified origination account. | [optional] 
**direction** | [**BankTransferDirection**](BankTransferDirection.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


