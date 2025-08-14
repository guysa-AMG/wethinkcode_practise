import requests as req
import sys
import requests
from requests import RequestException

API = "f1a9d60b90628a3952531003a4ebfafca3bd7b15cc8b879f565402d695febf3a"

def  get(num):
    try:
        data =  requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API}")
        currentPrice=data.json()["data"]["priceUsd"]
        value=num*float(currentPrice)
        return value
    except RequestException :
        print(RequestException)

if len(sys.argv) ==2:

    value=sys.argv[1]

    try:
        num=float(value)
        print(f"${get(num):,.4f}")
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

elif len(sys.argv)>2:
    print("Got more than one command-line argument")
    sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)