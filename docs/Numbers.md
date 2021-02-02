# Numbers

Account and bank identifier number data used to configure the test account. All values are optional.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Will be used for the account number. | 
**ach_routing** | **str** | Must be a valid ACH routing number. | 
**ach_wire_routing** | **str** | Must be a valid wire transfer routing number. | 
**eft_institution** | **str** | EFT institution number. Must be specified alongside &#x60;eft_branch&#x60;. | 
**eft_branch** | **str** | EFT branch number. Must be specified alongside &#x60;eft_institution&#x60;. | 
**international_bic** | **str** | Bank identifier code (BIC). Must be specified alongside &#x60;international_iban&#x60;. | 
**international_iban** | **str** | International bank account number (IBAN). If no account number is specified via &#x60;account&#x60;, will also be used as the account number by default. Must be specified alongside &#x60;international_bic&#x60;. | 
**bacs_sort_code** | **str** | BACS sort code | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


