# Item

Metadata about the Item.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | The Plaid Item ID. The &#x60;item_id&#x60; is always unique; linking the same account at the same institution twice will result in two Items with different &#x60;item_id&#x60; values. Like all Plaid identifiers, the &#x60;item_id&#x60; is case-sensitive. | 
**available_products** | [**[Products]**](Products.md) | A list of products available for the Item that have not yet been accessed. | 
**billed_products** | [**[Products]**](Products.md) | A list of products that have been billed for the Item. Note - &#x60;billed_products&#x60; is populated in all environments but only requests in Production are billed.  | 
**has_perpetual_otp** | **bool** | TODO! | 
**institution_id** | **str, none_type** | The Plaid Institution ID associated with the Item. Field is &#x60;null&#x60; for Items created via Same Day Micro-deposits. | [optional] 
**webhook** | **str, none_type** | The URL registered to receive webhooks for the Item. | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**consent_expiration_time** | **str, none_type** | The RFC 3339 timestamp after which the consent provided by the end user will expire. Upon consent expiration, the item will enter the &#x60;ITEM_LOGIN_REQUIRED&#x60; error state. To circumvent the &#x60;ITEM_LOGIN_REQUIRED&#x60; error and maintain continuous consent, the end user can reauthenticate via Link’s update mode in advance of the consent expiration time.  Note - This is only relevant for European institutions subject to PSD2 regulations mandating a 90-day consent window. For all other institutions, this field will be null.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


