import matplotlib.pyplot as plt
categories = ['A','B','C','D']
values = [10,20,15,25]

plt.bar(categories,values,color=['red','green','blue','purple'])
plt.title("Basic bar chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()