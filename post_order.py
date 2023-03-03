import requests

def create_order( market, amount, price, side):
    url = 'https://restful.bitcoinrd.do/api/v1/order/create'

    params = {
        'symbol': market,
        'size': amount,
        'price': price,
        'side': side,
        'type': 'limit' # or 'market' for a market order
    }

    response = requests.post(url, params=params)

    if response.status_code == 200:

        order_id = response.json().get('order_id')
        return order_id
    else:
    
        print(f'Error creating order: {response.text}')
        return None
