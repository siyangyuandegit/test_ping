binance_api_key = ''
binance_secret_key = ''

import time

from binance.spot import Spot as Client

client = Client(base_url='https://api.binance.com', api_key=binance_api_key, api_secret=binance_secret_key)

start_time = time.time()
print(client.ping())
end_time = time.time()
print(end_time - start_time)