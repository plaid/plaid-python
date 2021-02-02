# MortgageLiability

Contains details about a mortgage account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | The account number of the loan. | 
**account_id** | **str, none_type** | The ID of the account that this liability belongs to. | [optional] 
**current_late_fee** | **float, none_type** | The current outstanding amount charged for late payment. | [optional] 
**escrow_balance** | **float, none_type** | Total amount held in escrow to pay taxes and insurance on behalf of the borrower. | [optional] 
**has_pmi** | **bool, none_type** | Indicates whether the borrower has private mortgage insurance in effect. | [optional] 
**has_prepayment_penalty** | **bool, none_type** | Indicates whether the borrower will pay a penalty for early payoff of mortgage. | [optional] 
**interest_rate** | [**MortgageInterestRate**](MortgageInterestRate.md) |  | [optional] 
**last_payment_amount** | **float, none_type** | The amount of the last payment. | [optional] 
**last_payment_date** | **str, none_type** | The date of the last payment. Dates are returned in an ISO 8601 format (YYYY-MM-DD). | [optional] 
**loan_type_description** | **str, none_type** | Type of mortgage (i.e. &#x60;conventional&#x60;, &#x60;fixed&#x60;, &#x60;variable&#x60;). | [optional] 
**loan_term** | **str, none_type** | Full duration of mortgage as at origination (e.g. &#x60;10 year&#x60;). | [optional] 
**maturity_date** | **str, none_type** | Original date on which mortgage is due in full. Dates are returned in an ISO 8601 format (YYYY-MM-DD). | [optional] 
**next_monthly_payment** | **float, none_type** | The amount of the next payment. | [optional] 
**next_payment_due_date** | **str, none_type** | The due date for the next payment. Dates are returned in an ISO 8601 format (YYYY-MM-DD). | [optional] 
**origination_date** | **str, none_type** | The date on which the loan was initially lent. Dates are returned in an ISO 8601 format (YYYY-MM-DD). | [optional] 
**origination_principal_amount** | **float, none_type** | The original principal balance of the mortgage. | [optional] 
**past_due_amount** | **float, none_type** | Amount of loan (principal + interest) past due for payment. | [optional] 
**property_address** | [**MortgagePropertyAddress**](MortgagePropertyAddress.md) |  | [optional] 
**ytd_interest_paid** | **float, none_type** | The year to date (YTD) interest paid. | [optional] 
**ytd_principal_paid** | **float, none_type** | The YTD principal paid. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


