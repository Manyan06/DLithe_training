import matplotlib.pyplot as plt
data = [22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]

plt.hist(data, bins = 5, color ='cyan' , edgecolor='black')
plt.title("Basic Histogram")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.show()