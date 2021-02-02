# PaymentInitiationAddress

The optional address of the payment recipient. This object is not currently required to make payments from UK institutions and should not be populated, though may be necessary for future European expansion.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **[str]** | An array of length 1-2 representing the street address where the recipient is located. Maximum of 70 characters. | [optional] 
**city** | **str** | The city where the recipient is located. Maximum of 35 characters. | [optional] 
**postal_code** | **str** | The postal code where the recipient is located. Maximum of 16 characters. | [optional] 
**country** | **str** | The ISO 3166-1 alpha-2 country code where the recipient is located. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


