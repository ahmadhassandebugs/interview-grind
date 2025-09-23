"""
Backtracking Practice - Scaffold (no implementations) + Unit Tests

Rules:
- Do NOT implement the functions; fill them in yourself later.
- Run tests with:  python -m unittest backtracking_scaffold_and_tests.py

Coverage:
Easy:    subsets, permutations
Medium:  combination_sum, letter_combinations, word_search
Hard:    solve_n_queens, solve_sudoku
"""
from __future__ import annotations
import unittest
from typing import List

"""
def backtrack(path, choices):
    if goal_reached(path):
        record_solution(path)
        return
    for choice in choices:
        if not is_valid(choice, path):
            continue
        make_choice(path, choice)
        backtrack(path, choices)
        undo_choice(path, choice)  # backtrack

"""

# ---------------------------------
# Backtracking – Function Stubs ONLY
# ---------------------------------

# [] = []
# [1] = [], [1]
# [1,2] = [],[1],[2],[1,2]
# [1,2,3] = [],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]
def subsets(nums: List[int]) -> List[List[int]]:
    """Return all subsets (the power set) of nums. Order of subsets doesn't matter."""
    res = []
    path = []
    
    def backtrack(i):
        if i == len(nums):
            res.append(path[:])
            return
        
        # choice 1: exclude nums[i]
        backtrack(i + 1)
        # choice 2: include nums[i]
        path.append(nums[i])
        backtrack(i + 1)
        
        path.pop()  # undo
    
    backtrack(0)
    return res


def permutations(nums: List[int]) -> List[List[int]]:
    """Return all permutations of nums. Order of permutations doesn't matter."""
    res = []
    path = []
    used = [False] * len(nums)
    
    def backtrack():
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if used[i]: continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False
    
    backtrack()
    return res


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """Return all unique combinations where candidates can be used unlimited times to sum to target."""
    res = []
    path = []
    
    def backtrack(start):  # start avoids duplicates
        if sum(path) == target:
            res.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            if sum(path) + candidates[i] > target: continue
            path.append(candidates[i])
            backtrack(i)
            path.pop()
            
    backtrack(0)
    return res


def letter_combinations(digits: str) -> List[str]:
    """Return all possible letter combinations for a phone number string (2-9)."""
    if digits == "": return []
    res = []
    phone_dict = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno",
                  7: "pqrs", 8: "tuv", 9: "wxyz"}
    path = []
    
    def backtrack(i):
        if i == len(digits):
            res.append("".join(path))
            return
        
        for ch in phone_dict[int(digits[i])]:
            path.append(ch)
            backtrack(i + 1)
            path.pop()
        
    backtrack(0)
    return res


def word_search(board: List[List[str]], word: str) -> bool:
    """Return True if word exists in the 2D grid via adjacent cells (no reuse), else False."""
    rows, cols = len(board), len(board[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def dfs(i, j, k):
        if k == len(word) - 1: return board[i][j] == word[k]
        if board[i][j] != word[k]: return False
        
        visited[i][j] = True
        if i + 1 < rows and not visited[i + 1][j] and dfs(i + 1, j, k + 1): return True
        if i - 1 >= 0 and not visited[i - 1][j] and dfs(i - 1, j, k + 1): return True
        if j + 1 < cols and not visited[i][j + 1] and dfs(i, j + 1, k + 1): return True
        if j - 1 >= 0 and not visited[i][j - 1] and dfs(i, j - 1, k + 1): return True
        visited[i][j] = False
        
        return False
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True
    
    return False


def solve_n_queens(n: int) -> List[List[str]]:
    """Return all distinct solutions where 'Q' and '.' represent queens and empty.
    Each solution is a list of strings (board rows)."""
    board = [["."] * n for _ in range(n)]
    cols, diags, anti_diags = set(), set(), set()
    ans = []
    
    def make_board():
        res = []
        for row in board: res.append("".join(row))
        return res
    
    def backtrack(row):
        if row == n:
            ans.append(make_board())
            return
        
        for col in range(n):
            diag = row - col
            anti_diag = row + col
            
            # check if placement works
            if (col in cols or
                diag in diags or
                anti_diag in anti_diags
            ): continue
            
            board[row][col] = "Q"
            cols.add(col)
            diags.add(diag)
            anti_diags.add(anti_diag)
            
            backtrack(row + 1)
            
            board[row][col] = "."
            cols.remove(col)
            diags.remove(diag)
            anti_diags.remove(anti_diag)
            
    backtrack(0)
    return ans


def solve_sudoku(board: List[List[str]]) -> None:
    """Modify board in-place to solve the 9x9 Sudoku. Empty cells are '.'"""
    n = 3
    N = n * n
    solved = False
    
    box_idx = lambda r, c: (r // n) * n + (c // n)
    rows = [set() for _ in range(N)]
    cols = [set() for _ in range(N)]
    boxes = [set() for _ in range(N)]
    
    def can_place(r, c, d):
        return not (
            str(d) in rows[r] or
            str(d) in cols[c] or
            str(d) in boxes[box_idx(r, c)]
        )
        
    def place_digit(r, c, d):
        rows[r].add(str(d))
        cols[c].add(str(d))
        boxes[box_idx(r, c)].add(str(d))
        board[r][c] = str(d)
        
    def remove_digit(r, c, d):
        rows[r].remove(str(d))
        cols[c].remove(str(d))
        boxes[box_idx(r, c)].remove(str(d))
        board[r][c] = "."
        
    def move_to_next(r, c):
        nonlocal solved
        if r == N - 1 and c == N - 1:
            solved = True
            return
        if c == N - 1: backtrack(r + 1, 0)  # go to next row's start
        else: backtrack(r, c + 1)  # go to next column
    
    for i in range(N):
        for j in range(N):
            if board[i][j] != ".":
                d = int(board[i][j])
                place_digit(i, j, d)
    
    def backtrack(row, col):
        nonlocal solved
        if board[row][col] == ".":  # place one of the digits
            for d in range(1, N + 1):
                if can_place(row, col, d):
                    place_digit(row, col, d)
                    move_to_next(row, col)  # move onto the next index
                    if solved: return
                    remove_digit(row, col, d)
        else:  # move onto the next index
            move_to_next(row, col)
            
    backtrack(0, 0)
    return board


# ---------------------------------
# Test Utilities (order-insensitive compares)
# ---------------------------------

def _normalize_lists_of_lists(coll: List[List[int]]) -> List[List[int]]:
    return sorted([sorted(x) for x in coll])


def _normalize_boards(boards: List[List[str]]) -> List[List[str]]:
    # sort string boards lexicographically for deterministic compare
    return sorted(boards)


# ---------------------------------
# Unit Tests
# ---------------------------------
class TestBacktrackingEasy(unittest.TestCase):
    def test_subsets(self):
        nums = [1, 2, 3]
        out = subsets(nums)
        expected = [
            [], [1], [2], [3],
            [1,2], [1,3], [2,3],
            [1,2,3]
        ]
        self.assertEqual(_normalize_lists_of_lists(out), _normalize_lists_of_lists(expected))

    def test_permutations(self):
        nums = [1, 2, 3]
        out = permutations(nums)
        expected = [
            [1,2,3],[1,3,2],
            [2,1,3],[2,3,1],
            [3,1,2],[3,2,1]
        ]
        self.assertEqual(sorted(out), sorted(expected))


class TestBacktrackingMedium(unittest.TestCase):
    def test_combination_sum(self):
        candidates = [2,3,6,7]
        target = 7
        out = combination_sum(candidates, target)
        expected = [[7],[2,2,3]]
        self.assertEqual(_normalize_lists_of_lists(out), _normalize_lists_of_lists(expected))

        candidates2 = [2,3,5]
        target2 = 8
        out2 = combination_sum(candidates2, target2)
        expected2 = [[2,2,2,2],[2,3,3],[3,5]]
        self.assertEqual(_normalize_lists_of_lists(out2), _normalize_lists_of_lists(expected2))

    def test_letter_combinations(self):
        out = letter_combinations("23")
        expected = [
            "ad","ae","af",
            "bd","be","bf",
            "cd","ce","cf",
        ]
        self.assertEqual(sorted(out), sorted(expected))
        self.assertEqual(letter_combinations(""), [])

    def test_word_search(self):
        board = [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ]
        self.assertTrue(word_search([row[:] for row in board], "ABCCED"))
        self.assertTrue(word_search([row[:] for row in board], "SEE"))
        self.assertFalse(word_search([row[:] for row in board], "ABCB"))


class TestBacktrackingHard(unittest.TestCase):
    def test_solve_n_queens(self):
        # n=1 -> 1 solution
        sols1 = solve_n_queens(1)
        self.assertEqual(_normalize_boards(sols1), _normalize_boards([["Q"]]))
        # n=4 -> 2 solutions
        sols4 = solve_n_queens(4)
        expected4 = [
            [".Q..","...Q","Q...","..Q."],
            ["..Q.","Q...","...Q",".Q.."],
        ]
        self.assertEqual(_normalize_boards(sols4), _normalize_boards(expected4))

    def test_solve_sudoku(self):
        board = [
            list("53..7...."),
            list("6..195..."),
            list(".98....6."),
            list("8...6...3"),
            list("4..8.3..1"),
            list("7...2...6"),
            list(".6....28."),
            list("...419..5"),
            list("....8..79"),
        ]
        solved = [
            list("534678912"),
            list("672195348"),
            list("198342567"),
            list("859761423"),
            list("426853791"),
            list("713924856"),
            list("961537284"),
            list("287419635"),
            list("345286179"),
        ]
        solve_sudoku(board)
        self.assertEqual(board, solved)


if __name__ == "__main__":
    unittest.main()
