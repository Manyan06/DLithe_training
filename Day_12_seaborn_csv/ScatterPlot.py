import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#Load CSV file
data = pd.read_csv("stock_data.csv")

#Create Market Status
data['Market_Status'] = np.where(
  data['Close'] > data['Open'],
  'Level1',
  'Level2'
)

# Scatter Plot
sns.scatterplot(
  data=data,
  x='Open',
  y='Close',
  hue='Market_Status',
  style='Market_Status',
  s=100
)
plt.title("Open Price VS Close Price by Market Status")
plt.xlabel("Open Price")
plt.ylabel("Close Price")
plt.show()