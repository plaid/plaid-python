# AssetReportTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique ID of the transaction. Like all Plaid identifiers, the &#x60;transaction_id&#x60; is case sensitive. | 
**pending** | **bool** | When &#x60;true&#x60;, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount, category ID) may change before they are settled. | 
**date** | **str** | For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted. Both dates are returned in an ISO 8601 format ( &#x60;YYYY-MM-DD&#x60; ). | 
**amount** | **float** | The settled value of the transaction, denominated in the account&#39;s currency, as stated in &#x60;iso_currency_code&#x60; or &#x60;unofficial_currency_code&#x60;. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative. | 
**account_id** | **str** | The ID of the account in which this transaction occurred. | 
**original_description** | **str** | The string returned by the financial institution to describe the transaction | 
**transaction_type** | **str** | Please use the &#x60;payment_channel&#x60; field, &#x60;transaction_type&#x60; will be deprecated in the future.  &#x60;digital:&#x60; transactions that took place online.  &#x60;place:&#x60; transactions that were made at a physical location.  &#x60;special:&#x60; transactions that relate to banks, e.g. fees or deposits.  &#x60;unresolved:&#x60; transactions that do not fit into the other three types.  | [optional] 
**account_owner** | **str, none_type** | The name of the account owner. This field is not typically populated and only relevant when dealing with sub-accounts. | [optional] 
**pending_transaction_id** | **str, none_type** | The ID of a posted transaction&#39;s associated pending transaction, where applicable. | [optional] 
**payment_channel** | **str** | The channel used to make a payment. &#x60;online:&#x60; transactions that took place online.  &#x60;in store:&#x60; transactions that were made at a physical location.  &#x60;other:&#x60; transactions that relate to banks, e.g. fees or deposits.  This field replaces the &#x60;transaction_type&#x60; field.  | [optional] 
**payment_meta** | [**PaymentMeta**](PaymentMeta.md) |  | [optional] 
**name** | **str** | The merchant name or transaction description.  If the &#x60;transaction&#x60; object was returned by a Transactions endpoint such as &#x60;/transactions/get&#x60;, this field will always appear. If the &#x60;transaction&#x60; object was returned by an Assets endpoint such as &#x60;/asset_report/get/&#x60; or &#x60;/asset_report/pdf/get&#x60;, this field will only appear in an Asset Report with Insights. | [optional] 
**merchant_name** | **str, none_type** | The merchant name, as extracted by Plaid from the &#x60;name&#x60; field. | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**authorized_date** | **str, none_type** | The date that the transaction was authorized. Dates are returned in an ISO 8601 format ( &#x60;YYYY-MM-DD&#x60; ). | [optional] 
**category_id** | **str** | The ID of the category to which this transaction belongs. See [Categories](https://plaid.com/docs/#category-overview).  If the &#x60;transaction&#x60; object was returned by an Assets endpoint such as &#x60;/asset_report/get/&#x60; or &#x60;/asset_report/pdf/get&#x60;, this field will only appear in an Asset Report with Insights. | [optional] 
**category** | **[str], none_type** | A hierarchical array of the categories to which this transaction belongs. See [Categories](https://plaid.com/docs/#category-overview).  If the &#x60;transaction&#x60; object was returned by an Assets endpoint such as &#x60;/asset_report/get/&#x60; or &#x60;/asset_report/pdf/get&#x60;, this field will only appear in an Asset Report with Insights. | [optional] 
**unofficial_currency_code** | **str, none_type** | The unofficial currency code associated with the transaction. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-&#x60;null&#x60;. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](/docs/api/accounts#currency-code-schema) for a full listing of supported &#x60;iso_currency_code&#x60;s. | [optional] 
**iso_currency_code** | **str, none_type** | The ISO-4217 currency code of the transaction. Always &#x60;null&#x60; if &#x60;unofficial_currency_code&#x60; is non-null. | [optional] 
**transaction_code** | [**TransactionCode**](TransactionCode.md) |  | [optional] 
**date_transacted** | **str, none_type** | The date on which the transaction took place, in IS0 8601 format. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


