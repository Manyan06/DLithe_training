import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load Excel File
data = pd.read_csv("stock_data.csv")
#Correlation Matrix
corr_matrix = data[
  ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
].corr()

#Heat Map
plt.figure(figsize=(10,6))
sns.heatmap(
  corr_matrix,
  annot=True,
  cmap='coolwarm',
  fmt='.2f'
)

plt.title("Stock Market Correlation Heatmap")
plt.show()