import quandl
import numpy as np

data = quandl.get("NSE/KOTAKNIFTY", authtoken="qAsk6MJV-VXWMqoWDJQk")

print(data)
