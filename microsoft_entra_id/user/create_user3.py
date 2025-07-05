from msgraph.graph_service_client import GraphServiceClient
from azure.identity import ClientSecretCredential
from msgraph.generated.models.user import User
from msgraph.generated.models.password_profile import PasswordProfile
import asyncio
import os
import argparse
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python

parser = argparse.ArgumentParser(description='Pass arguments to create azure user')
parser.add_argument('--displayname', '-dn')
parser.add_argument('--nickname', '-nn')
parser.add_argument('--domain', '-d')
args = parser.parse_args()

azure_display_username = args.displayname
azure_nick_username = args.nickname
azure_domain_url = args.domain
azure_user_principal_name = f"{azure_nick_username} {azure_domain_url}"

tenant_id = os.getenv('tenant_id')
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

scopes = ['https://graph.microsoft.com/.default']

# azure.identity
# credential = DeviceCodeCredential(
#     tenant_id=tenant_id,
#     client_id=client_id)

credential = ClientSecretCredential(
      tenant_id,
      client_id,
      client_secret 
  )

graph_client = GraphServiceClient(credential, scopes)

async def create_user():
    try:
        print(f"Creating User Display name: {azure_display_username} Nick name: {azure_nick_username} User Principal name: {azure_user_principal_name}")
        request_body = User(
            account_enabled = True,
            display_name = azure_display_username,
            mail_nickname = azure_nick_username,
            user_principal_name = azure_user_principal_name,
            password_profile = PasswordProfile(
                force_change_password_next_sign_in = True,
                password = "eequei7queL1ai",
            ),
        )

        print("Sending request to Microsoft Graph...")
        result = await graph_client.users.post(request_body)
        print("User created successfully!")
        return result
    except Exception as e:
        print(f"Error occurred: {type(e).__name__}: {e}")
        raise

if __name__ == "__main__":
    result = asyncio.run(create_user())
    print(result)