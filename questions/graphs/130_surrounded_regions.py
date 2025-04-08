from typing import List

# we capture all regions marked with 'O' but we don't
#   capture regions that are connected to the edge of board
# first, we can iterate over edges and mark 'O' cells with
#   'E' that are connected to edges so that we can skip these
#   cells during DFS
# then, we go over the remaining board and run dfs on any 'O'
#   we can find, capturing the region (changing it to 'E')
#   DFS only goes deeper if there's an 'O' neighbor cell
# finally, we change the 'E's back to 'O's

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board), len(board[0])
        
        # dfs
        def dfs(r, c, replace):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != "O" or
                (r, c) in visited
            ): return
            
            visited.add((r, c))
            board[r][c] = replace
            dfs(r - 1, c, replace)
            dfs(r + 1, c, replace)
            dfs(r, c - 1, replace)
            dfs(r, c + 1, replace)
        
        # mark the edge 'O's with 'E's
        visited = set()
        for r in [0, rows - 1]:
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    dfs(r, c, "E")
        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == "O" and (r, c) not in visited:
                    dfs(r, c, "E")
                    
        # capture 'O's now
        visited = set()
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == "O" and (r, c) not in visited:
                    dfs(r, c, "X")
        
        # change back the 'E's to 'O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "E":
                    board[r][c] = "O"
                

if __name__=="__main__":
    sol = Solution()
    tc1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    tc2 = [["X"]]
    tc3 = [["O","X","X","X"],["X","X","X","X"],["X","O","O","X"],["X","X","X","X"]]
    tc4 = [["O","O","O","O"],["O","O","O","O"],["O","O","O","O"],["O","O","O","O"]]
    sol.solve(tc1)
    sol.solve(tc2)
    sol.solve(tc3)
    sol.solve(tc4)
    print(tc1)
    print(tc2)
    print(tc3)
    print(tc4)
    