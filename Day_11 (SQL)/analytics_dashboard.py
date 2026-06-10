import numpy as np
import matplotlib.pyplot as plt

#Monthly sales Data
months = np.array([
  "Jan", "Feb", "Mar", "Apr",
  "May", "Jun", "Jul", "Aug",
  "Sep", "Oct", "Nov", "Dec"
])
sales = np.array([
  45000, 52000, 48000, 61000,
  70000, 65000, 72000, 68000,
  75000, 80000, 85000, 90000
])
print("SALES ANALYSIS DASHBOARD")
print("\nMonthly Sales: ")
for month, amount in zip(months,sales):
  print(f"{month}: Rs.{amount}")
print("\nTotal Annual Sales: Rs.",np.sum(sales))
print("\nAverage Monthly Sales: Rs.",round(np.mean(sales), 2))
print("Highest Sales: Rs.",np.max(sales))
print("Lowest Sales: Rs.",np.min(sales))
best_month = months[np.argmax(sales)]
print("Best Performing Month: ", best_month)

#Create Dashboard
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', linewidth=2)
plt.title("Sales Analytics Dashboard")
plt.xlabel("Months")
plt.ylabel("Sales Amount(Rs.)")
plt.grid(True)
plt.show()