import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May','June']
sales = [120, 150, 180, 170, 210, 250]
plt.fill_between(months,sales)
plt.title('Area Chart')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()