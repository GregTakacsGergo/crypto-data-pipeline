# A short 60-second data extraction using concurrent.futures module 
# to put price and time extraction tasks on two concurrent worker threads

import requests
import concurrent.futures
import time


duration = 60 
start_time = time.time()

while time.time() - start_time < duration:
# API endpoint URLs
    price_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    server_time_url = "https://api.binance.com/api/v3/time"
  
# Save price and time get request results in response 
    def fetch_price():
        response = requests.get(price_url)
        return response.json()

    def fetch_time():
        response = requests.get(server_time_url)
        return response.json()

# Submitting and then retrieving the results 
    with concurrent.futures.ThreadPoolExecutor() as executor:
        price_future = executor.submit(fetch_price)
        time_future = executor.submit(fetch_time)

        price_data = price_future.result()
        btc_price = price_data["price"]

        time_data = time_future.result()
        server_time = time_data["serverTime"]
 
    print(f"Bitcoin (BTC) price: {btc_price}")
    print(f"Server Time: {server_time}")
    time.sleep(1)
