from typing import List

# This is like finding the number of connected components in
#   a graph. 1s are connected by adjacent vertices (l,r,u,d)
# For each 1, we can run a dfs and count connected 1s.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                grid[r][c] != "1"
            ): return
            
            visited.add((r, c))
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right
            
        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    island_count += 1
        return island_count            
        

if __name__=="__main__":
    tc1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    tc2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    sol = Solution()
    print(sol.numIslands(tc1))
    print(sol.numIslands(tc2))
