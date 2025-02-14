# [3,4,5,1,2] w/ rotation
# [5,1,2,3,4] w/ rotation
# if nums[r] < nums[l] rotated
#   find mid
#   if nums[mid] < nums[l] min is in left half
#   else in right half
# else not rotated
#   return nums[l]
# TIPS: elif and else equal condition causes problems
#   base case should be non-rotated

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
                
        l, r = 0, len(nums) - 1
        
        while l < r:
            if nums[l] > nums[r]:  # rotated
                mid = (l + r) // 2
                if nums[mid] < nums[l]: r = mid
                else: l = mid + 1
            else:  # not rotated
                return nums[l]
        
        return nums[l]
    
if __name__=="__main__":
    tc1 = [3,4,5,1,2]
    tc2 = [4,5,6,7,0,1,2]
    tc3 = [11,13,15,17]
    tc4 = [1]
    sol = Solution()
    print(sol.findMin(tc1))
    print(sol.findMin(tc2))
    print(sol.findMin(tc3))
    print(sol.findMin(tc4))
