# DepositSwitchCreateRequest

DepositSwitchCreateRequest defines the request schema for `/deposit_switch/create`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_access_token** | **str** | Access token for the target Item, typically provided in the Import Item response.  | 
**target_account_id** | **str** | Plaid Account ID that specifies the target bank account. This account will become the recipient for a user&#39;s direct deposit. | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


