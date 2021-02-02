# ProductStatus

A representation of the status health of a request type. Auth requests, Balance requests, Identity requests, Transactions updates, Investments updates, and Item logins each have their own status object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | &#x60;HEALTHY&#x60;: the majority of requests are successful &#x60;DEGRADED&#x60;: only some requests are successful &#x60;DOWN&#x60;: all requests are failing | 
**last_status_change** | **str** | ISO 8601 formatted timestamp of the last status change for the institution. | 
**breakdown** | [**ProductStatusBreakdown**](ProductStatusBreakdown.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


