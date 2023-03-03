import requests

def get_trades(api_key, secret_key, symbol=None, limit=50, page=None, order_by=None, order=None, start_date=None, end_date=None, format=None):

    url = 'https://api.bitcoinrd.do/v2/user/trades'

    params = {
        'api_key': api_key,
        'secret_key': secret_key,
        'symbol': symbol,
        'limit': limit,
        'page': page,
        'order_by': order_by,
        'order': order,
        'start_date': start_date,
        'end_date': end_date,
        'format': format
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        result = response.json()
        return result
    else:

        print(f'Error getting trades: {response.text}')
        return None
