import requests
import time

duration = 61 
start_time = time.time()

while time.time() - start_time < duration:
	response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
	data = response.json()
	btc_price = data["bpi"]["USD"]["rate"]
	btc_time = data["time"]["updated"]
	print(f"BTC price (USD) at {btc_time} is:{btc_price}")
	time.sleep(1)

 
 
 
