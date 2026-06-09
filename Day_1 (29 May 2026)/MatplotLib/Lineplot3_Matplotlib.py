import matplotlib.pyplot as plt
x = [5,7,8,7,6,9,5,6]
y = [99,86,87,88,100,86,103,87]

plt.scatter(x,y, color = 'orange', marker = 'x')
plt.title("Basic Scatter plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()