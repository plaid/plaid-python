# VerificationExpiredWebhook

Fired when an Item was not verified via micro-deposits after ten days since the micro-deposit was made.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;AUTH&#x60; | 
**webhook_code** | **str** | &#x60;VERIFICATION_EXPIRED&#x60; | 
**item_id** | **str** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**account_id** | **str** | The &#x60;account_id&#x60; of the account associated with the webhook | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


