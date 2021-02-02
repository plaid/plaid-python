# LinkTokenCreateRequestAccountSubtypes

By default, Link will only display account types that are compatible with all products supplied in the `products` parameter of `/link/token/create`. You can further limit the accounts shown in Link by using `account_filters` to specify the account subtypes to be shown in Link. Only the specified subtypes will be shown. This filtering applies to both the Account Select view (if enabled) and the Institution Select view. Institutions that do not support the selected subtypes will be omitted from Link. To indicate that all subtypes should be shown, use the value `\"all\"`. If the `account_filters` filter is used, any account type for which a filter is not specified will be entirely omitted from Link.  For a full list of valid types and subtypes, see the [Account schema](/docs/api/accounts#accounts-schema).  For institutions using OAuth, the filter will not affect the list of institutions or accounts shown by the bank in the OAuth window. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depository** | [**LinkTokenCreateRequestAccountSubtypesDepository**](LinkTokenCreateRequestAccountSubtypesDepository.md) |  | [optional] 
**credit** | [**LinkTokenCreateRequestAccountSubtypesCredit**](LinkTokenCreateRequestAccountSubtypesCredit.md) |  | [optional] 
**loan** | [**LinkTokenCreateRequestAccountSubtypesLoan**](LinkTokenCreateRequestAccountSubtypesLoan.md) |  | [optional] 
**investment** | [**LinkTokenCreateRequestAccountSubtypesInvestment**](LinkTokenCreateRequestAccountSubtypesInvestment.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


