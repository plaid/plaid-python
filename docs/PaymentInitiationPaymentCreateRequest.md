# PaymentInitiationPaymentCreateRequest

PaymentInitiationPaymentCreateRequest defines the request schema for `/payment_initiation/payment/create`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **str** | The ID of the recipient the payment is for. | 
**reference** | **str** | A reference for the payment. This must be an alphanumeric string with at most 18 characters and must not contain any special characters (since not all institutions support them). | 
**amount** | [**Amount**](Amount.md) |  | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 
**schedule** | [**ExternalPaymentSchedule**](ExternalPaymentSchedule.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


