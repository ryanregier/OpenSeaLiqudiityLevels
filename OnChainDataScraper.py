import requests
import json
import pandas as pd
import os

MORALIS_API_KEY = os.getenv('MORALIS_API_KEY')

prefix = "https://deep-index.moralis.io/api/v2/"
headers = {
    "Accept": "application/json",
    "X-API-Key": MORALIS_API_KEY
}


def get_nft_collection(address):
    url = prefix + address + "/nft?chain=eth&format=decimal"
    response = requests.request("GET", url, headers=headers)
    response = response.json()
    df = pd.DataFrame(response["result"])
    print(response)

get_nft_collection("0x06012c8cf97BEaD5deAe237070F9587f8E7A266d")
