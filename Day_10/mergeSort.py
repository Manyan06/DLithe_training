import time
import sys
def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  return merge(left, right)

def merge(left, right):
  result, i, j, = [], 0, 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i]); i += 1
    else:
      result.append(right[j]); j+= 1
  return result + left[i:] + right[j:]
print("\nMERGE SORT")

arr = [5 ,2, 9, 1, 6, 3]
start = time.perf_counter()
sorted_arr = merge_sort(arr)
end = time.perf_counter()

print("Original: ", arr)
print("Sorted: ", sorted_arr)
print(f"Time taken: {(end - start) * 1_000_000:.2f} microsecond")
print(f"Space used: {sys.getsizeof(arr)}")