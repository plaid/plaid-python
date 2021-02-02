# IncomeVerificationStatusWebhook

Fired when the status of an income verification instance has changed. It will typically take several minutes for this webhook to fire after the end user has uploaded their documents, and may take up to 15 minutes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_type** | **str** | &#x60;\&quot;INCOME\&quot;&#x60; | 
**webhook_code** | **str** | &#x60;income_verification&#x60; | 
**income_verification_id** | **str** | The &#x60;income_verification_id&#x60; of the verification instance whose status is being reported. | 
**verification_status** | **str** | &#x60;VERIFICATION_STATUS_PROCESSING_COMPLETE&#x60;: The income verification status processing has completed.  &#x60;VERIFICATION_STATUS_UPLOAD_ERROR&#x60;: An upload error occurred when the end user attempted to upload their verification documentation.  &#x60;VERIFICATION_STATUS_INVALID_TYPE&#x60;: The end user attempted to upload verification documentation in an unsupported file format.  &#x60;VERIFICATION_STATUS_DOCUMENT_REJECTED&#x60;: The documentation uploaded by the end user was recognized as a supported file format, but not recognized as a valid paystub.  &#x60;VERIFICATION_STATUS_PROCESSING_FAILED&#x60;: A failure occurred when attempting to process the verification documentation. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


