# TransactionOverride

Data to populate as test transaction data. If not specified, random transactions will be generated instead.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_date** | **str** | The date of the transaction, in ISO8601 (YYYY-MM-DD) format. Transaction dates in the past or present will result in posted transactions; transaction dates in the future will result in pending transactions. Transactions in Sandbox will move from pending to posted once their transaction date has been reached. | 
**posted_date** | **str** | The date the transaction posted, in ISO8601 (YYYY-MM-DD) format | 
**amount** | **float** | The transaction amount. Can be negative. | 
**description** | **str** | The transaction description. | 
**currency** | **str** | The ISO-4217 format currency code for the transaction. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


