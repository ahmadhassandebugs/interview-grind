# nums = [-1,0,3,5,9,12], target = 9
# implement both recursive and iterative
# find mid point, if smaller the right index 
#   gets updated to mid, otherwise left index 
#   get updated to mid
# stopping condition: if left == right, return 
#   index if equal else -1

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def recursive(l, r):
            if l == r:
                if target == nums[l]: return l
                else: return -1
                
            mid  = (l + r) // 2
            if target < nums[mid]: return recursive(l, mid)
            elif target > nums[mid]: return recursive(mid + 1, r)
            else: return mid
            
        return recursive(0, len(nums) - 1)
        
        # l, r = 0, len(nums) - 1
        
        # while l < r:
        #     mid = (l + r) // 2
            
        #     if target < nums[mid]: r = mid
        #     elif target > nums[mid]: l = mid + 1
        #     else: return mid
        
        # if nums[l] == target:
        #         return l
        
        # return -1
        

if __name__=="__main__":
    tc1 = [-1,0,3,5,9,12], 9
    tc2 = [-1,0,3,5,9,12], 2
    sol = Solution()
    print(sol.search(*tc1))
    print(sol.search(*tc2))
