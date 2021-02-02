# Owner

Data returned from the financial institution about the owner or owners of an account. Only the `names` array must be non-empty.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **[str]** | A list of names associated with the account by the financial institution. These should always be the names of individuals, even for business accounts. If the name of a business is reported, please contact Plaid Support.  In the case of a joint account, the names of all account holders will be reported.  If an Item contains multiple accounts with different owner names, some institutions will report all names associated with the Item in each account&#39;s &#x60;names&#x60; array. | 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) | A list of phone numbers associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution. | 
**emails** | [**[Email]**](Email.md) | A list of email addresses associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution. | 
**addresses** | [**[Address]**](Address.md) | Data about the various addresses associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


