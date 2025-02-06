# [1,2,3,1]
# go over all nums and compare with the rest (n^2)
# go over numbers and store them in a set. if value 
#   already in set return False

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    nums_seen = {}
    for num in nums:
        if num in nums_seen:
            return True
        nums_seen[num] = 1
    return False
    
    