# numbers = [2,7,11,15], target = 9
# 1. since the list is sorted, we can compare the
#   first and last elements and move left or
#   right (two pointers) based on their sum
#       if the sum is greater than target, moving
#       the right pointer to the left will make it
#       smaller and vice versa
# 2. we stop when the pointers pass each other.
#   shouldn't happen since there's exactly one solution

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return [l+1, r+1]
        
        raise KeyError("unexpected code reached")
    
if __name__=="__main__":
    pass
