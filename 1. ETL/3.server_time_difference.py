'''
This scripts will show an error. I am demonstrating, that price_data_url endpoint 
is also not a good option, because .get() cannot use a parameter. Sadly this way I 
won't be able to extract at real-time with the level of accuracy that I want. But 
it can clearly show the time difference between local and binance server time.
'''
import requests
import time

server_time_url = "https://api.binance.com/api/v3/time"
price_data_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

# Retrieve server time
server_time_response = requests.get(server_time_url)
server_time = server_time_response.json()["serverTime"]

# Get local system time
local_system_time = int(time.time() * 1000)  # Convert to milliseconds

# Calculate time difference
time_difference = server_time - local_system_time

# Adjust local system time with time difference
adjusted_local_time = local_system_time + time_difference

#Show these time values in microseconds
server_times = [local_system_time, server_time, time_difference, adjusted_local_time]
print(server_times)

# Make API call with adjusted local time
price_data_response = requests.get(price_data_url, params = adjusted_local_time )
price_data = price_data_response.json()
print(price_data)
    
