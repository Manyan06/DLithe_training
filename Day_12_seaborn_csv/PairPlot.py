import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("stock_data.csv")
data['Market_Status'] = np.where(
  data['Close'] > data['Open'],
  'Level1',
  'Level2'
)

sns.pairplot(
  data[['Open', 'High', 'Low', 'Close', 'Market_Status']],
  hue='Market_Status'
)
plt.show()