import pandas as pd
import numpy as np

np.random.seed(42)
n = 500
dates = pd.date_range(start='2024-01-01', periods=n)
open_price = np.random.uniform(100, 500, n)
high_price = open_price + np.random.uniform(1, 30 ,n)
low_price = open_price + np.random.uniform(1, 30 ,n)
close_price = np.random.uniform(low_price, high_price)
adj_close = close_price + np.random.uniform(-2, 2, n)
volume = np.random.randint(10000, 5000000, n)

data = pd.DataFrame({
  'Date' : dates,
  'Open' : open_price.round(2),
  'High' : high_price.round(2),
  'Low' : low_price.round(2),
  'Close' : close_price.round(2),
  'Adj Close' : adj_close.round(2),
  'Volume' : volume
  })

data.to_csv("stock_data.csv", index = False)
print("Dataset Created Successfully! \n")
print(data.head)