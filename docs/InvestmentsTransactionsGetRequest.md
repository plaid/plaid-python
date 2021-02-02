# InvestmentsTransactionsGetRequest

InvestmentsTransactionsGetRequest defines the request schema for `/investments/transactions/get`
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token associated with the Item data is being requested for. | 
**start_date** | **date** | The earliest date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD. | 
**end_date** | **date** | The most recent date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD. | 
**client_id** | **str** | Your Plaid API &#x60;client_id&#x60;. | [optional] 
**secret** | **str** | Your Plaid API &#x60;secret&#x60;. | [optional] 
**options** | [**InvestmentsTransactionsGetRequestOptions**](InvestmentsTransactionsGetRequestOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


