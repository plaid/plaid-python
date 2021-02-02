# DepositSwitchGetResponse

DepositSwitchGetResponse defines the response schema for `/deposit_switch/get`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit_switch_id** | **str** | The ID of the deposit switch | 
**target_account_id** | **str, none_type** | The ID of the bank account the direct deposit was switched to | 
**target_item_id** | **str, none_type** | The ID of the Item the direct deposit was switched to. | 
**state** | **str** | The state of the deposit switch. | 
**account_has_multiple_allocations** | **bool, none_type** | When &#x60;true&#x60;, user’s direct deposit goes to multiple banks. When false, user’s direct deposit only goes to the target account. Always &#x60;null&#x60; if the deposit switch has not been completed. | 
**is_allocated_remainder** | **bool, none_type** | When &#x60;true&#x60;, the target account is allocated the remainder of direct deposit after all other allocations have been deducted. When &#x60;false&#x60;, user’s direct deposit is allocated as a percent or amount. Always &#x60;null&#x60; if the deposit switch has not been completed. | 
**percent_allocated** | **float, none_type** | The percentage of direct deposit allocated to the target account. Always &#x60;null&#x60; if the target account is not allocated a percentage or if the deposit switch has not been completed or if &#x60;is_allocated_remainder&#x60; is true. | 
**amount_allocated** | **float, none_type** | The dollar amount of direct deposit allocated to the target account. Always &#x60;null&#x60; if the target account is not allocated an amount or if the deposit switch has not been completed. | 
**date_created** | **date** | ISO8601 date the deposit switch was created. | 
**date_completed** | **date, none_type** | ISO8601 date the deposit switch was completed. Always &#x60;null&#x60; if the deposit switch has not been completed. | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


