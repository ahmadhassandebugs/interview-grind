# matrix [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# binary search on the last ele of each row log(n) u,d,bet while u<d
# binary seach on the down row log(m)

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        # binary search on rows i.e., vertical
        up, down = 0, m - 1
        while up < down:
            mid = (up + down) // 2
            if target < matrix[mid][-1]: down = mid
            elif target > matrix[mid][-1]: up = mid + 1
            else: return True
                
        # binary search on column i.e., horizontal
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if target < matrix[down][mid]: r = mid
            elif target > matrix[down][mid]: l = mid + 1
            else: return True
        
        return target == matrix[down][l]
    
if __name__=="__main__":
    tc1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 0
    tc2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13
    sol = Solution()
    print(sol.searchMatrix(*tc1))
    print(sol.searchMatrix(*tc2))
