import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dates = pd.date_range("2026-01-01", periods=6, freq="ME")
data = pd.DataFrame({
  "Category A" : [20, 25, 30, 28, 26, 24],
  "Category B" : [30, 28, 25, 27, 29, 31],
  "Category C" : [50, 47, 45, 45, 45, 45]
}, index=dates)

#Plot stacked area
plt.figure(figsize=(8,5))
plt.stackplot(data.index, data.T, labels = data.columns, alpha=0.8)
plt.title("Ribbon Chart Example - Category shares over Time")
plt.xlabel("Date")
plt.ylabel("Percentage")
plt.legend(loc = "upper right")
plt.show()