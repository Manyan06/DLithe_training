import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x,y,marker='o',color = 'blue')
plt.title("Basic line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()