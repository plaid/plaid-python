# UserCustomPassword

Custom test accounts are configured with a JSON configuration object formulated according to the schema below. All fields are optional. Sending an empty object as a configuration will result in an account configured with random balances and transaction history.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seed** | **str** | A seed, in the form of a string, that will be used to randomly generate account and transaction data, if this data is not specified using the &#x60;override_accounts&#x60; argument. If no seed is specified, the randomly generated data will be different each time.  Note that transactions data is generated relative to the Item&#39;s creation date. Different Items created on different dates with the same seed for transactions data will have different dates for the transactions. The number of days between each transaction and the Item creation will remain constant. For example, an Item created on December 15 might show a transaction on December 14. An Item created on December 20, using the same seed, would show that same transaction occurring on December 19. | 
**override_accounts** | [**[OverrideAccounts]**](OverrideAccounts.md) | An array of account overrides to configure the accounts for the Item. By default, if no override is specified, transactions and account data will be randomly generated based on the account type and subtype, and other products will have fixed or empty data. | 
**mfa** | [**MFA**](MFA.md) |  | 
**recaptcha** | **str** | You may trigger a reCAPTCHA in Plaid Link in the Sandbox environment by using the recaptcha field. Possible values are &#x60;good&#x60; or &#x60;bad&#x60;. A value of &#x60;good&#x60; will result in successful Item creation and &#x60;bad&#x60; will result in a &#x60;RECAPTCHA_BAD&#x60; error to simulate a failed reCAPTCHA. Both values require the reCAPTCHA to be manually solved within Plaid Link. | 
**force_error** | **str** | An error code to force on Item creation. Possible values are:  &#x60;\&quot;INSTITUTION_NOT_RESPONDING\&quot;&#x60; &#x60;\&quot;INSTITUTION_NO_LONGER_SUPPORTED\&quot;&#x60; &#x60;\&quot;INVALID_CREDENTIALS\&quot;&#x60; &#x60;\&quot;INVALID_MFA\&quot;&#x60; &#x60;\&quot;ITEM_LOCKED\&quot;&#x60; &#x60;\&quot;ITEM_LOGIN_REQUIRED\&quot;&#x60; &#x60;\&quot;ITEM_NOT_SUPPORTED\&quot;&#x60; &#x60;\&quot;INVALID_LINK_TOKEN\&quot;&#x60; &#x60;\&quot;MFA_NOT_SUPPORTED\&quot;&#x60; &#x60;\&quot;NO_ACCOUNTS\&quot;&#x60; &#x60;\&quot;PLAID_ERROR\&quot;&#x60; &#x60;\&quot;PRODUCTS_NOT_SUPPORTED\&quot;&#x60; &#x60;\&quot;USER_SETUP_REQUIRED\&quot;&#x60; | 
**version** | **str, none_type** | The version of the password schema to use, possible values are 1 or 2. The default value is 2. You should only specify 1 if you know it is necessary for your test suite. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


