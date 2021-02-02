# PaymentInitiationPaymentListRequest

PaymentInitiationPaymentListRequest defines the request schema for `/payment_initiation/payment/list`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 
**count** | **int** | The maximum number of payments to return. If &#x60;count&#x60; is not specified, a maximum of 10 payments will be returned, beginning with the most recent payment before the cursor (if specified). | [optional]  if omitted the server will use the default value of 10
**cursor** | **str** | A string in RFC 3339 format (i.e. \&quot;2019-12-06T22:35:49Z\&quot;). Only payments created before the cursor will be returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


