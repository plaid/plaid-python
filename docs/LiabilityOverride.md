# LiabilityOverride

Used to configure Sandbox test data for the Liabilities product
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the liability object, either &#x60;credit&#x60; or &#x60;student&#x60;. | 
**purchase_apr** | **float** | The purchase APR percentage value. For simplicity, this is the only interest rate used to calculate interest charges. Can only be set if &#x60;type&#x60; is &#x60;credit&#x60;. | 
**cash_apr** | **float** | The cash APR percentage value. Can only be set if &#x60;type&#x60; is &#x60;credit&#x60;. | 
**balance_transfer_apr** | **float** | The balance transfer APR percentage value. Can only be set if &#x60;type&#x60; is &#x60;credit&#x60;. Can only be set if &#x60;type&#x60; is &#x60;credit&#x60;. | 
**special_apr** | **float** | The special APR percentage value. Can only be set if &#x60;type&#x60; is &#x60;credit&#x60;. | 
**last_payment_amount** | **float** | Override the &#x60;last_payment_amount&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;credit&#x60;. | 
**last_statement_balance** | **float** | Override the &#x60;last_statement_balance&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;credit&#x60;. | 
**minimum_payment_amount** | **float** | Override the &#x60;minimum_payment_amount&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;credit&#x60;. | 
**is_overdue** | **bool** | Override the &#x60;is_overdue&#x60; field | 
**origination_date** | **str** | The date on which the loan was initially lent, in ISO 8601 (YYYY-MM-DD) format. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**principal** | **float** | The original loan principal. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**nominal_apr** | **float** | The interest rate on the loan as a percentage. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**interest_capitalization_grace_period_months** | **float** | If set, interest capitalization begins at the given number of months after loan origination. By default interest is never capitalized. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**repayment_model** | [**StudentLoanRepaymentModel**](StudentLoanRepaymentModel.md) |  | 
**expected_payoff_date** | **str** | Override the &#x60;expected_payoff_date&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**guarantor** | **str** | Override the &#x60;guarantor&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**is_federal** | **bool** | Override the &#x60;is_federal&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**loan_name** | **str** | Override the &#x60;loan_name&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**loan_status** | **str** | Override the &#x60;loan_status&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**payment_reference_number** | **str** | Override the &#x60;payment_reference_number&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**pslf_status** | **str** | Override the &#x60;pslf_status&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**repayment_plan_description** | **str** | Override the &#x60;repayment_plan.description&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**repayment_plan_type** | **str** | Override the &#x60;repayment_plan.type&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. Possible values are: &#x60;\&quot;extended graduated\&quot;&#x60;, &#x60;\&quot;extended standard\&quot;&#x60;, &#x60;\&quot;graduated\&quot;&#x60;, &#x60;\&quot;income-contingent repayment\&quot;&#x60;, &#x60;\&quot;income-based repayment\&quot;&#x60;, &#x60;\&quot;interest only\&quot;&#x60;, &#x60;\&quot;other\&quot;&#x60;, &#x60;\&quot;pay as you earn\&quot;&#x60;, &#x60;\&quot;revised pay as you earn\&quot;&#x60;, or &#x60;\&quot;standard\&quot;&#x60;. | 
**sequence_number** | **str** | Override the &#x60;sequence_number&#x60; field. Can only be set if &#x60;type&#x60; is &#x60;student&#x60;. | 
**servicer_address** | [**Address**](Address.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


