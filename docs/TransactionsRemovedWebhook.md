# TransactionsRemovedWebhook

Fired when transaction(s) for an Item are deleted. The deleted transaction IDs are included in the webhook payload. Plaid will typically check for deleted transaction data several times a day.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;TRANSACTIONS&#x60; | 
**webhook_code** | **str** | &#x60;TRANSACTIONS_REMOVED&#x60; | 
**removed_transactions** | **[str]** | An array of &#x60;transaction_ids&#x60; corresponding to the removed transactions | 
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**error** | [**Error**](Error.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


