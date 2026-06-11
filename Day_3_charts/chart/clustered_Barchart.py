import matplotlib.pyplot as plt
import numpy as np
categories = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
product_A = [20, 35, 30, 35, 27]
product_B = [25, 32, 34, 20, 25]
product_C = [15, 20, 18, 25, 22]
y = np.arange(len(categories))
bar_width = 0.25
plt.barh(y - bar_width, product_A, height=bar_width, label='Product A')
plt.barh(y, product_B, height=bar_width, label='Product B')
plt.barh(y + bar_width, product_C, height=bar_width, label='Product C')
plt.yticks(y, categories)
plt.title('Clustered Bar Chart')
plt.xlabel('Sales')
plt.ylabel('Months')
plt.legend()
plt.show()