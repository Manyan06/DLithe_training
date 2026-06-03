def remove_duplicates(arr):
  if not arr:
    return []
  arr.sort()  # sort first
  slow = 0
  for fast in range(1, len(arr)):
    if arr[fast] != arr[slow]:
      slow += 1
      arr[slow] = arr[fast]
  return arr[:slow + 1]

n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter the elements: " " separated by space: ").split()))
print(remove_duplicates(nums))