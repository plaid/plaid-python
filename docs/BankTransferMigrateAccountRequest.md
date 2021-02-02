# BankTransferMigrateAccountRequest

BankTransferMigrateAccountRequest defines the request schema for `/bank_transfer/migrate_account`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | The user&#39;s account number. | 
**routing_number** | **str** | The user&#39;s routing number. | 
**account_type** | **str** | The type of the bank account (&#x60;checking&#x60; or &#x60;savings&#x60;). | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


