import numpy as np
data = np.random.randint(10,100,size = 20)
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
print("Data : ",data)
print("Mean : ",mean)
print("Median : ",median)
print("Standard Deviation : ",std_dev)