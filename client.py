import requests
import json
import hmac
import hashlib
import time
from datetime import datetime
API_URL= "https://api.bitcoinrd.do/v2/"

def get_ticker(symbol):
    url = f"{API_URL}ticker?symbol={symbol.lower()}"
    resp = requests.get(url)
    data = resp.json()
    return data

def get_tickers():
    url = f"{API_URL}tickers"
    resp = requests.get(url)
    data = resp.json()
    return data

def get_orderbook(symbol):
    url = f"{API_URL}orderbook?symbol={symbol.lower()}"
    resp = requests.get(url)
    data = resp.json()
    return data

def get_orderbooks():
    url = f"{API_URL}orderbooks"
    resp = requests.get(url)
    data = resp.json()
    return data

def get_trades():
    url = f"{API_URL}trades"
    resp = requests.get(url)
    data = resp.json()
    return data

# initialize the following variables: method, patßh and api_expires.
def get_api_expires():
    return str(int(time.time() + 60))

def init_signature():
    method = "GET"
    path = "/v2/user/balance"
    api_expires = get_api_expires()
    return method, path, api_expires

def auth_me(api_key, api_secret, method, path):
    signature = generate_signature(method, path, get_api_expires(), api_secret)
    api_expires = get_api_expires()
    headers = {
        "api-key": api_key,
        "api-signature": signature,
        "api-expires": api_expires
    }
    return headers

def generate_signature(method, path, api_expires, api_secret):
    string_to_encode = method + path + api_expires
    signature = hmac.new(api_secret.encode(),string_to_encode.encode(),hashlib.sha256).hexdigest()
    return signature

#User balance function

def get_balance(api_key, api_secret):
    method, path, api_expires = init_signature()
    headers = auth_me(api_key, api_secret, method, path)
    response = requests.get("https://api.bitcoinrd.do/v2/user/balance", headers=headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print("Error: " + str(response.status_code))
        return "Error: " + str(response.status_code)

def get_trades(api_key, api_secret):
    method = "GET"
    path = "/v2/user/trades"
    api_expires = get_api_expires()
    signature = generate_signature(method, path, api_expires)
    headers = {
        "api-key": api_key,
        "api-signature": signature,
        "api-expires": api_expires
    }
    response = requests.get("https://api.bitcoinrd.do" + path, headers=headers)

    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print("Error: " + str(response.status_code))
        return "Error: " + str(response.status_code)
