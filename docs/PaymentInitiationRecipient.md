# PaymentInitiationRecipient

Information about a payment recipient configured for the Payment Initiation product
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_id** | **str** | The ID of the recipient. Like all Plaid identifiers, the &#x60;recipient_id&#x60; is case sensitive. | 
**name** | **str** | The name of the recipient | 
**address** | [**PaymentInitiationAddress**](PaymentInitiationAddress.md) |  | 
**iban** | **str, none_type** | The International Bank Account Number (IBAN) for the recipient. | [optional] 
**bacs** | [**PaymentInitiationRecipientBacs**](PaymentInitiationRecipientBacs.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


