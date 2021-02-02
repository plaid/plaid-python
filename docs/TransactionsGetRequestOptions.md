# TransactionsGetRequestOptions

An optional object to be used with the request. If specified, `options` must not be `null`.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **[str]** | A list of &#x60;account_ids&#x60; to retrieve for the Item  Note: An error will be returned if a provided &#x60;account_id&#x60; is not associated with the Item. | [optional] 
**count** | **int** | The number of transactions to fetch. | [optional]  if omitted the server will use the default value of 100
**offset** | **int** | The number of transactions to skip. The default value is 0. | [optional]  if omitted the server will use the default value of 0

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


