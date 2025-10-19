## Subarray Sum
nums = [-1, 0, 2, 4, -5, 1, 5]
cumm_sum, curr_sum = [], 0
for i in range(len(nums)):
    curr_sum += nums[i] 
    cumm_sum.append(curr_sum)
print(nums)
print(cumm_sum)
