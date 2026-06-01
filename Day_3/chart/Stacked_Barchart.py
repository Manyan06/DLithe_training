import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales_A = [20, 35, 30, 35, 27]
sales_B = [25, 32, 34, 20, 25]
sales_C = [15, 20, 18, 25, 22]
plt.bar(months, sales_A, label='Product A')
plt.bar(months, sales_B, bottom = sales_A, label='Product B')
bottom_C = [sales_A[i] + sales_B[i] for i in range(len(sales_A))]
plt.bar(months, sales_C, bottom=bottom_C, label='Product C')
plt.title('Stacked Bar Chart')
plt.xlabel('\nMonths')
plt.ylabel('Sales')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()