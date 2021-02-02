# PaymentInitiationPaymentTokenCreateResponse

PaymentInitiationPaymentTokenCreateResponse defines the response schema for `/payment_initiation/payment/token/create`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_token** | **str** | A &#x60;payment_token&#x60; that can be provided to Link initialization to enter the payment initiation flow | 
**payment_token_expiration_time** | **str** | The date and time at which the token will expire, in ISO 8601 format. A &#x60;payment_token&#x60; expires after 15 minutes. | 
**request_id** | **str** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


