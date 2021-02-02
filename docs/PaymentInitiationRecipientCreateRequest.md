# PaymentInitiationRecipientCreateRequest

PaymentInitiationRecipientCreateRequest defines the request schema for `/payment_initiation/recipient/create`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the recipient | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 
**iban** | **str** | The International Bank Account Number (IBAN) for the recipient. If BACS data is not provided, an IBAN is required. | [optional] 
**bacs** | [**NullableRecipientBACS**](NullableRecipientBACS.md) |  | [optional] 
**address** | [**PaymentInitiationAddress**](PaymentInitiationAddress.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


