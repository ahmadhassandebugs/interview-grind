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

# ---------------------------------
# Backtracking – Function Stubs ONLY
# ---------------------------------

def subsets(nums: List[int]) -> List[List[int]]:
    """Return all subsets (the power set) of nums. Order of subsets doesn't matter."""
    pass


def permutations(nums: List[int]) -> List[List[int]]:
    """Return all permutations of nums. Order of permutations doesn't matter."""
    pass


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """Return all unique combinations where candidates can be used unlimited times to sum to target."""
    pass


def letter_combinations(digits: str) -> List[str]:
    """Return all possible letter combinations for a phone number string (2-9)."""
    pass


def word_search(board: List[List[str]], word: str) -> bool:
    """Return True if word exists in the 2D grid via adjacent cells (no reuse), else False."""
    pass


def solve_n_queens(n: int) -> List[List[str]]:
    """Return all distinct solutions where 'Q' and '.' represent queens and empty.
    Each solution is a list of strings (board rows)."""
    pass


def solve_sudoku(board: List[List[str]]) -> None:
    """Modify board in-place to solve the 9x9 Sudoku. Empty cells are '.'"""
    pass


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
