# ProcessorTokenCreateRequest

ProcessorTokenCreateRequest defines the request schema for `/processor/token/create`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token associated with the Item data is being requested for. | 
**account_id** | **str** | The &#x60;account_id&#x60; value obtained from the &#x60;onSuccess&#x60; callback in Link | 
**processor** | **str** | The processor you are integrating with. Valid values are &#x60;\&quot;achq\&quot;&#x60;, &#x60;\&quot;checkbook\&quot;&#x60;, &#x60;\&quot;circle\&quot;&#x60;, &#x60;\&quot;drivewealth\&quot;&#x60;, &#x60;\&quot;dwolla\&quot;&#x60;, &#x60;\&quot;galileo\&quot;&#x60;, \&quot;&#x60;interactive_brokers&#x60;\&quot;, &#x60;\&quot;modern_treasury\&quot;&#x60;, &#x60;\&quot;ocrolus\&quot;&#x60;, &#x60;\&quot;prime_trust\&quot;&#x60;, &#x60;\&quot;velox\&quot;&#x60;, &#x60;\&quot;vesta\&quot;&#x60;, &#x60;\&quot;vopay\&quot;&#x60; | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


