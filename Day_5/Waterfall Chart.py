import matplotlib.pyplot as plt
import numpy as np

categories = ["Start", "Sales", "Costs", "Marketing", "Tasks","End"]
values  = [1000, 500, -300, -150, -200, 850] 
cumulative = [values[0]]
for val in values[1:]:
  cumulative.append(cumulative[-1] + val)

colors = ["blue"] + ["Green" if v >= 0 else "red" for v in values[1:]]

plt.figure(figsize = (8,5))
plt.bar(categories, values, color = colors)

# Add cumulative line
plt.plot(categories, cumulative, marker="o", color="black", linestyle="--")

#Labels
for i, val in enumerate(values):
  plt.text(i, values[i] + (50 if val >= 0 else -50), str(values[i]), ha="center")
  plt.title("Waterfall Chart Example")
  plt.xlabel("Date")
  plt.ylabel("Value")

  plt.show()