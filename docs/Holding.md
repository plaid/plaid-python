# Holding

A securities holding at an institution.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The Plaid &#x60;account_id&#x60; associated with the holding. | 
**security_id** | **str** | The Plaid &#x60;security_id&#x60; associated with the holding. | 
**institution_price** | **float** | The last price given by the institution for this security. | 
**institution_value** | **float** | The value of the holding, as reported by the institution. | 
**quantity** | **float** | The total quantity of the asset held, as reported by the financial institution. | 
**institution_price_as_of** | **str, none_type** | The date at which &#x60;institution_price&#x60; was current. | [optional] 
**cost_basis** | **float, none_type** | The cost basis of the holding. | [optional] 
**iso_currency_code** | **str, none_type** | The ISO-4217 currency code of the holding. Always &#x60;null&#x60; if &#x60;unofficial_currency_code&#x60; is non-&#x60;null&#x60;. | [optional] 
**unofficial_currency_code** | **str, none_type** | The unofficial currency code associated with the holding. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-&#x60;null&#x60;. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](/docs/api/accounts#currency-code-schema) for a full listing of supported &#x60;iso_currency_code&#x60;s.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


