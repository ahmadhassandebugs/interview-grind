# nums = [2,7,11,15], target = 9
# store elements in set and find target-num

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for idx, num in enumerate(nums):
            if target - num in num_dict:
                return [idx, num_dict[target - num]]
            num_dict[num] = idx
            