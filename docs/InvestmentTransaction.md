# InvestmentTransaction

A transaction within an investment account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investment_transaction_id** | **str** | The ID of the Investment transaction, unique across all Plaid transactions. Like all Plaid identifiers, the &#x60;investment_transaction_id&#x60; is case sensitive. | 
**account_id** | **str** | The &#x60;account_id&#x60; of the account against which this transaction posted. | 
**date** | **str** | The ISO-8601 posting date for the transaction, or transacted date for pending transactions. | 
**name** | **str** | The institution’s description of the transaction. | 
**quantity** | **float** | The number of units of the security involved in this transactions | 
**amount** | **float** | The complete value of the transaction. Positive values when cash is debited, e.g. purchases of stock; negative values when cash is credited, e.g. sales of stock. Treatment remains the same for cash-only movements unassociated with securities. | 
**price** | **float** | The price of the security at which this transaction occurred. | 
**type** | **str** | Value is one of the following: &#x60;buy&#x60;: Buying an investment &#x60;sell&#x60;: Selling an investment &#x60;cancel&#x60;: A cancellation of a pending transaction  &#x60;cash&#x60;: Activity that modifies a cash position &#x60;fee&#x60;: A fee on the account &#x60;transfer&#x60;: Activity which modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer | 
**subtype** | **str** | For descriptions of possible transaction subtypes, see [Investment transaction subtypes schema](/docs/api/accounts/#investment-transaction-subtypes-schema). | 
**cancel_transaction_id** | **str, none_type** |  | [optional] 
**security_id** | **str, none_type** | The &#x60;security_id&#x60; to which this transaction is related. | [optional] 
**fees** | **float, none_type** | The combined value of all fees applied to this transaction | [optional] 
**iso_currency_code** | **str, none_type** | The ISO-4217 currency code of the transaction. Always &#x60;null&#x60; if &#x60;unofficial_currency_code&#x60; is non-&#x60;null&#x60;. | [optional] 
**unofficial_currency_code** | **str, none_type** | The unofficial currency code associated with the holding. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-&#x60;null&#x60;. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](/docs/api/accounts#currency-code-schema) for a full listing of supported &#x60;iso_currency_code&#x60;s. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


