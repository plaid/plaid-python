# StandaloneAccountType

The schema below describes the various `types` and corresponding `subtypes` that Plaid recognizes and reports for financial institution accounts.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depository** | **str** | An account type holding cash, in which funds are deposited. Supported products for &#x60;depository&#x60; accounts are: Auth, Balance, Transactions, Identity, Payment Initiation, and Assets. | 
**credit** | **str** | A credit card type account. Supported products for &#x60;credit&#x60; accounts are: Balance, Transactions, Identity, and Liabilities. | 
**loan** | **str** | A loan type account. Supported products for &#x60;loan&#x60; accounts are: Balance, Liabilities, and Transactions. | 
**investment** | **str** | An investment account. Supported products for &#x60;investment&#x60; accounts are: Balance and Investments. | 
**other** | **str** | Other or unknown account type. Supported products for &#x60;other&#x60; accounts are: Balance, Transactions, Identity, and Assets. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


