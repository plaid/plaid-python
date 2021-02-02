# LinkTokenCreateRequestIncomeVerification

Specifies options for initializing Link for use with the Income Verification (beta) product. This field is required if `income_verification` is included in the `product` array.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**income_verification_id** | **str** | The &#x60;income_verification_id&#x60; of the verification instance, as provided by &#x60;/income/verification/create&#x60;. | 
**asset_report_id** | **str, none_type** | The &#x60;asset_report_id&#x60; of an asset report associated with the user, as provided by &#x60;/asset_report/create&#x60;. Providing an &#x60;asset_report_id&#x60; is optional and can be used to verify the user through a streamlined flow. If provided, the bank linking flow will be skipped. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


