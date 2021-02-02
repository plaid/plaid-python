# AccountType

`investment:` Investment account  `credit:` Credit card  `depository:` Depository account  `loan:` Loan account  `brokerage`: An investment account. Used for `/assets/` endpoints only; other endpoints use `investment`.  `other:` Non-specified account type  See the [Account type schema](/docs/api/accounts#account-type-schema) for a full listing of account types and corresponding subtypes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | &#x60;investment:&#x60; Investment account  &#x60;credit:&#x60; Credit card  &#x60;depository:&#x60; Depository account  &#x60;loan:&#x60; Loan account  &#x60;brokerage&#x60;: An investment account. Used for &#x60;/assets/&#x60; endpoints only; other endpoints use &#x60;investment&#x60;.  &#x60;other:&#x60; Non-specified account type  See the [Account type schema](/docs/api/accounts#account-type-schema) for a full listing of account types and corresponding subtypes. |  must be one of ["investment", "credit", "depository", "loan", "brokerage", "other", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


