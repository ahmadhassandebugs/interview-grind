from typing import List

# if start == len(nums): a&r
#                        [1,2,3]
#     0[1,2,3]          0[2,1,3]             0[3,2,1]
# 1[1,2,3] 1[1,3,2]  1[2,1,3] 1[2,3,1]  1[3,2,1] 1[3,1,2]  
# 2[1,2,3] 2[1,3,2]  2[2,1,3] 2[2,3,1]  2[3,2,1] 2[3,1,2]
#  a&r        a&r       a&r      a&r        a&r      a&r


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        
        def backtrack(start: int):
            if start == len(nums):
                answer.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]  # swap
                backtrack(start+1)
                nums[i], nums[start] = nums[start], nums[i]  # swap back
        
        backtrack(0)
        return answer

if __name__ == "__main__":
    sol = Solution()
    tc1 = [1,2,3]
    tc2 = [1,2,3,4]
    tc3 = [1]
    tc4 = [1,2]
    print(sol.permute(tc1))
    print(sol.permute(tc2))
    print(sol.permute(tc3))
    print(sol.permute(tc4))
