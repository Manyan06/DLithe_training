def binary_search(arr, target):
  left,right = 0, len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1

#Examples
nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
result = binary_search(nums, target)
print("Found at index: ",result if result != -1 else "Not Found")