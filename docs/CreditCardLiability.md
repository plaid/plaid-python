# CreditCardLiability

An object representing a credit card account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aprs** | [**[APR]**](APR.md) | The various interest rates that apply to the account. | 
**last_payment_amount** | **float** | The amount of the last payment. | 
**last_payment_date** | **str** | The date of the last payment. Dates are returned in an ISO 8601 format (YYYY-MM-DD). Availability for this field is limited. | 
**last_statement_balance** | **float** | The outstanding balance on the last statement. Availability for this field is limited. | 
**last_statement_issue_date** | **str** | The date of the last statement. Dates are returned in an ISO 8601 format (YYYY-MM-DD). | 
**minimum_payment_amount** | **float** | The minimum payment due for the next billing cycle. | 
**next_payment_due_date** | **str** | The due date for the next payment. The due date is &#x60;null&#x60; if a payment is not expected. Dates are returned in an ISO 8601 format (YYYY-MM-DD). | 
**account_id** | **str, none_type** | The ID of the account that this liability belongs to. | [optional] 
**is_overdue** | **bool, none_type** | true if a payment is currently overdue. Availability for this field is limited. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


