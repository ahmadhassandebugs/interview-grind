# height = [1,8,6,2,5,4,8,3,7] 49
# volume = min(left, right) * (right-left)
# n*n comparisons take a lot of time
# note that if l and r are two pointers and
#   min(height[l], height[r]) * (r-l) is their
#   volume, moving the taller tower to the left
#   or right is not going to increase the volume.
#   so we should move the shorter tower.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = -1
        l, r = 0, len(height)-1
        while l < r:
            cur_vol = min(height[l], height[r]) * (r-l)
            if cur_vol > max_vol: max_vol = cur_vol
            
            if height[l] < height[r]: l += 1
            else: r -= 1
        return max_vol
        
    def maxArea_v1(self, height: List[int]) -> int:
        lines = len(height)
        max_vol = -1
        for l in range(lines):
            for r in range(l, lines):
                cur_vol = min(height[l], height[r]) * (r-l)
                print(f"l:{l} r:{r} vol:{cur_vol}")
                if cur_vol > max_vol: max_vol = cur_vol
        return max_vol

if __name__=="__main__":
    tc1 = [1,8,6,2,5,4,8,3,7]
    tc2 = [1,1]
    sol = Solution()
    print(sol.maxArea(tc1))
    print(sol.maxArea(tc2))
