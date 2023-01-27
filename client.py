import requests
import json
import hmac
import hashlib
import time

def get_ticker():
    url = "https://api.bitcoinrd.do/v2/ticker?symbol=${symbol}"
    resp = requests.get(url)
    data = resp.json()
    return data

def get_tickers():
    resp = requests.get("https://api.bitcoinrd.do/v2/tickers")
    data = resp.json()
    return data

def get_orderbook():
    resp = requests.get("https://api.bitcoinrd.do/v2/orderbook?symbol=${symbol}")
    data = resp.json()
    return data

def get_orderbooks():
    resp = requests.get("https://api.bitcoinrd.do/v2/orderbooks")
    data = resp.json()
    return data

def get_trades():
    resp = requests.get("https://api.bitcoinrd.do/v2/trades")
    data = resp.json()
    return data



tickers_data = get_tickers()
print(json.dumps(tickers_data, indent=10))



api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"


method = "GET"
path = "/v2/user/balance"
api_expires = str(int(time.time() + 60))


string_to_encode = method + path + api_expires


signature = hmac.new(api_secret.encode(), string_to_encode.encode(), hashlib.sha256).hexdigest()

headers = {
    "api-key": api_key,
    "api-signature": signature,
    "api-expires": api_expires
}


response = requests.get("https://api.bitcoinrd.do" + path, headers=headers)

print(response.json())





