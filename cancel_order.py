import requests

def cancel_order(order_id):

    url = f'https://restful.bitcoinrd.do/api/v1/orders/{order_id}'


    params = {
        'order_id': order_id
    }


    response = requests.delete(url, params=params)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print(f'Error cancelling order: {response.text}')
        return None
