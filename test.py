import os
import sys

import shioaji as sj
from dotenv import load_dotenv

# api = sj.Shioaji(simulation=True)
api = sj.Shioaji()
load_dotenv()

api_key = os.getenv("api_key", None)
secret_key = os.getenv("secret_key", None)
if api_key == None:
    print("Specify api_key as environment variable.")
    sys.exit(1)

if secret_key == None:
    print("Specify secret_key as environment variable.")
    sys.exit(1)

accounts =  api.login(api_key, secret_key)
print(accounts)

print(api.account_balance())


api.logout()