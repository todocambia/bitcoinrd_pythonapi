import json
import requests
import time
import hmac
import hashlib

API_SECRET = "your_secret"
API_KEY= "your_key"
def get_api_expires():
        return str(int(time.time() + 60))
    
def generate_signature(PATH_URL, METHOD, api_expires, params=None):
    string_to_encode = METHOD + PATH_URL + api_expires
    if params != None:
        string_to_encode += json.dumps(params, separators=(',', ':'))
    signature = hmac.new(API_SECRET.encode(),string_to_encode.encode(),hashlib.sha256).hexdigest()
    return signature
def init_signature( PATH_URL, METHOD, is_ws):
    if is_ws:
        method = "CONNECT"
        path = '/stream'
        api_expires = get_api_expires()
        return method, path, api_expires
    else:   
        method = METHOD
        path = f"/v2{PATH_URL}"
        api_expires = get_api_expires()
        return method, path, api_expires

def auth_me( PATH_URL, METHOD, is_ws=False, params=None):
    method, path, api_expires = init_signature(PATH_URL, METHOD, is_ws)
    signature = generate_signature(path, method, api_expires, params=params)
    headers = {
        "api-key": API_KEY,
        "api-signature": signature,
        "api-expires": api_expires
    }
    return headers


def create_order( market, amount, price, side):
    url = 'https://api.bitcoinrd.do/v2/order'
    params = {
        'symbol': market,
        'size': amount,
        'price': price,
        'side': side,
        'type': 'limit' # or 'market' for a market order
    }
    headers = auth_me("/order", "POST", params=params)
    response = requests.post(url, json=params, headers=headers)
    if response.status_code == 200:
        order_id = response.json().get('id')
        return order_id
    else:
        print(f'Error creating order: {response.text}')
        return None


create_order("matic-usdt", 1, 1, "buy")

