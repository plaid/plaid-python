# TransactionsGetRequest

TransactionsGetRequest defines the request schema for `/transactions/get`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token associated with the Item data is being requested for. | 
**start_date** | **date** | The earliest date for which data should be returned. Dates should be formatted as YYYY-MM-DD. | 
**end_date** | **date** | The latest date for which data should be returned. Dates should be formatted as YYYY-MM-DD. | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**options** | [**TransactionsGetRequestOptions**](TransactionsGetRequestOptions.md) |  | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


