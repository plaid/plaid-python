# JWKPublicKey

A JSON Web Key (JWK) that can be used in conjunction with [JWT libraries](https://jwt.io/#libraries-io) to verify Plaid webhooks
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | The alg member identifies the cryptographic algorithm family used with the key. | [optional] 
**crv** | **str** | The crv member identifies the cryptographic curve used with the key. | [optional] 
**kid** | **str** | The kid (Key ID) member can be used to match a specific key. This can be used, for instance, to choose among a set of keys within the JWK during key rollover. | [optional] 
**kty** | **str** | The kty (key type) parameter identifies the cryptographic algorithm family used with the key, such as RSA or EC. | [optional] 
**use** | **str** | The use (public key use) parameter identifies the intended use of the public key. | [optional] 
**x** | **str** | The x member contains the x coordinate for the elliptic curve point. | [optional] 
**y** | **str** | The y member contains the y coordinate for the elliptic curve point. | [optional] 
**created_at** | **int** |  | [optional] 
**expired_at** | **int, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


