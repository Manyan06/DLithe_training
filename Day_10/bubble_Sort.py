import time
import sys

def bubble_sort(arr):
  n = len(arr)
  for i in range(n - 1):
    for j in range(n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr
print("\nBubble Sort")
arr= [64, 34, 25, 12, 22, 11, 90]
start = time.perf_counter()
sorted_arr = bubble_sort(arr.copy())
end = time.perf_counter()
print("Original: ",arr)
print("Sorted Array: ",sorted_arr)

print(f"Time taken: {(end - start) * 1_000_000:.2f} microsecond")
print(f"Space used: {sys.getsizeof(arr)} bytes")