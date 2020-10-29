import plaid

CLIENT_ID = '5ec4123eba7c950013a7e35c'
SECRET = '7edaf4dc444ded372afd2a9b3314bb'
SANDBOX_INSTITUTION = 'ins_109508'

client = plaid.Client(CLIENT_ID, SECRET, environment='sandbox')
pt_response = client.Sandbox.public_token.create(
    SANDBOX_INSTITUTION, ['identity'])
exchange_response = client.Item.public_token.exchange(
    pt_response['public_token'])
access_token = exchange_response['access_token']

resp = client.Identity.get(access_token)
# print(client.handle_request(client.generated_api.categories_get, {}))
