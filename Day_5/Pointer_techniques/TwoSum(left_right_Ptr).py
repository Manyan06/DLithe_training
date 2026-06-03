def find_pair(arr, target):
  left = 0
  right = len(arr) - 1
  while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
      return(arr[left], arr[right])
    elif current_sum < target:
      left += 1
    else:
      right -= 1
  return None

nums = list(map(int, input("Enter sorted numbers: ").split()))

target = int(input("Enter Target: "))
print(find_pair(nums, target))