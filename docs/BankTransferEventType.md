# BankTransferEventType

`pending`: A new transfer was created; it is in the pending state.  `cancelled`: The transfer was cancelled by the client.  `failed`: The transfer failed, no funds were moved.  `posted`: The transfer has been successfully submitted to the payment network.  `reversed`: A posted transfer was reversed.  `receiver_pending`: The matching transfer was found as a pending transaction in the receiver's account  `receiver_posted`: The matching transfer was found as a posted transaction in the receiver's account
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | &#x60;pending&#x60;: A new transfer was created; it is in the pending state.  &#x60;cancelled&#x60;: The transfer was cancelled by the client.  &#x60;failed&#x60;: The transfer failed, no funds were moved.  &#x60;posted&#x60;: The transfer has been successfully submitted to the payment network.  &#x60;reversed&#x60;: A posted transfer was reversed.  &#x60;receiver_pending&#x60;: The matching transfer was found as a pending transaction in the receiver&#39;s account  &#x60;receiver_posted&#x60;: The matching transfer was found as a posted transaction in the receiver&#39;s account |  must be one of ["pending", "cancelled", "failed", "posted", "reversed", "receiver_pending", "receiver_posted", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


