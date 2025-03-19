from typing import List

# if sum == target: a&r
# if sum > target: r
# [2,3,5]
#                              []
# [2]                          [3]                      [5]
#                                             [2,2]
#         [2,2,2]                            [2,2,3]                         [2,2,5]
# [2,2,2,2] [2,2,2,3] [2,2,2,5]   [2,2,3,2] [2,2,3,3] [2,2,3,5]   [2,2,5,2] [2,2,5,3] [2,2,5,5]
# a&r          r          r           r         r        r           r          r         r


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        answer = []
        
        def backtrack(start: int, path: List[int]):
            if sum(path) == target:  # append
                answer.append(path[:])
            if sum(path) >= target: return  # since further adding will be greater
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path)  # since repeat elements are allowed
                path.pop()
        
        backtrack(0, [])
        return answer

if __name__ == "__main__":
    
    sol = Solution()
    tc1 = [2,3,6,7], 7
    tc2 = [2,3,5], 8
    tc3 = [2], 1
    print(sol.combinationSum(*tc1))
    print(sol.combinationSum(*tc2))
    print(sol.combinationSum(*tc3))
