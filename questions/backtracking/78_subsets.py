from typing import List

# [1,2,3]
# decision tree
#                       []
#      [1]              [2]                 [3]
#  [1,2]  [1,3]        [2,3]
#  [1,2,3]
# start with empty path and index 0
# add that to the set
# loop over all elements
# add each element to path
# recurse on that element
# remove that element from path
# (kinda like dfs)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        
        def backtrack(start: int, path: List[int]):
            # append path to the answer
            answer.append(path[:])
            
            # iterate over rest of the elements
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0, [])
        return answer

if __name__ == "__main__":
    sol = Solution()
    tc1 = [1,2,3]
    tc2 = [1,2,3,4]
    tc3 = [1]
    tc4 = [1,2]
    print(sol.subsets(tc1))
    print(sol.subsets(tc2))
    print(sol.subsets(tc3))
    print(sol.subsets(tc4))
