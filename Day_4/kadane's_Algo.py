#Max Subarray Sum

def max_subarray(nums):
  current_sum = nums[0]
  max_sum = nums[0]
  for i in range(1, len(nums)):
    current_sum = max(nums[i], current_sum + nums[i])
    max_sum = max(max_sum, current_sum)
  return max_sum

n = int(input("Enter number of elements: "))
nums = []
print("Enter the elements : ")
for i in range(n):
  nums.append(int(input()))
result = max_subarray(nums)
print("Maximum Subarray Sum: ",result)