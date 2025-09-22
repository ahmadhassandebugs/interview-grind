"""
Recursion Practice - Scaffold (no implementations) + Unit Tests

Rules:
- Do NOT implement the functions; fill them in yourself later.
- Run tests with:  python -m unittest recursion_scaffold_and_tests.py
"""
from __future__ import annotations
import unittest
from typing import List, Optional, Tuple

"""
# 🌀 Recursion Cheat Sheet

## 🔑 Tips for Solving Recursion Problems
- **Identify the base case** → the simplest input that stops recursion.  
- **Define the recursive step in words** before coding.  
- **Avoid recomputing** → use memoization (cache results).  
- **Think divide & conquer** → split the problem into smaller independent subproblems.  
- **Use helper functions** when you need extra state (e.g., indices, accumulators).  
- **Visualize with small inputs** → draw recursion trees for clarity.  
- **Convert to iterative if needed** → tail recursion → loop, DP for overlapping subproblems.  

---

## 📂 Common Recursion Patterns

### Divide & Conquer
- Binary Search  
- Merge Sort / Quick Sort  

### Tree Recursion (multiple recursive calls)
- Fibonacci sequence  
- Binary tree traversals (preorder, inorder, postorder)  

### Choice Recursion (explore all options → bridge to backtracking)
- Generate subsets (power set)  
- Generate permutations  

### Recursion + Memoization
- Fibonacci optimized  
- Word Break  
- Unique BSTs (Catalan problems)  

"""

# -----------------------------
# Data structures & utilities
# -----------------------------
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    head = None
    cur = None
    for v in values:
        node = ListNode(v)
        if not head:
            head = node
            cur = node
        else:
            cur.next = node
            cur = node
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def serialize_tree_preorder(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Helper for tests: serialize a tree by preorder with None markers."""
    res: List[Optional[int]] = []

    def dfs(node: Optional[TreeNode]):
        if not node:
            res.append(None)
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res


# -----------------------------
# Recursion – Easy
# -----------------------------

def factorial(n: int) -> int:
    """Return n! using recursion. Assume n >= 0."""
    if n <= 1: return 1
    return n * factorial(n - 1)


def reverse_string(s: str) -> str:
    """Return the reversed string using recursion."""
    if len(s) <= 1: return s
    return reverse_string(s[1:]) + s[0]


def sum_array(arr: List[int]) -> int:
    """Return sum(arr) using recursion (no loops)."""
    if len(arr) == 0: return 0
    if len(arr) == 1: return arr[0]
    return arr[0] + sum_array(arr[1:])


# -----------------------------
# Recursion – Medium
# -----------------------------

def binary_search_recursive(arr: List[int], target: int, left: int = 0, right: Optional[int] = None) -> int:
    """Return index of target in sorted arr or -1 if not found."""
    if right is None: right = len(arr) - 1
    if left > right: return -1
    mid = (left + right) // 2
    if target > arr[mid]: return binary_search_recursive(arr, target, mid + 1, right)
    elif target < arr[mid]: return binary_search_recursive(arr, target, left, mid - 1)
    else: return mid


def max_depth(root: Optional[TreeNode]) -> int:
    """Return the maximum depth of a binary tree."""
    if root is None: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def is_palindrome_list_recursive(head: Optional[ListNode]) -> bool:
    """Return True if linked list is a palindrome using recursion."""
    front = head
    def check(node: Optional[ListNode]):
        nonlocal front
        if node is None: return True
        if not check(node.next): return False
        ok = front.val == node.val
        front = front.next
        return ok
    return check(head)


def merge_two_sorted_lists_recursive(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted linked lists using recursion and return head of merged list."""
    if l1 is None: return l2
    if l2 is None: return l1
    if l1.val <= l2.val:
        l1.next = merge_two_sorted_lists_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_sorted_lists_recursive(l1, l2.next)
        return l2


def tower_of_hanoi(n: int, src: str = 'A', aux: str = 'B', dst: str = 'C') -> List[Tuple[str, str]]:
    """Return the sequence of moves to solve Tower of Hanoi with n disks as (from_peg, to_peg)."""
    moves: List[Tuple[str, str]] = []

    def solve(k, s, a, d):
        nonlocal moves
        if k == 0: return
        # move k-1 disks from src -> aux
        solve(k - 1, s, d, a)
        # move largest disk from src -> dst
        moves.append((s, d))
        # move k-1 disks from aux -> dst
        solve(k - 1, a, s, d)
    
    solve(n, src, aux, dst)
    return moves


# -----------------------------
# Recursion – Hard
# -----------------------------

def generate_unique_bsts(n: int) -> List[Optional[TreeNode]]:
    """Generate all structurally unique BSTs storing values 1..n and return their roots."""
    pass


def word_break_all(s: str, wordDict: List[str]) -> List[str]:
    """Return all sentences formed by breaking s into words from wordDict (order of sentences doesn't matter)."""
    pass


# -----------------------------
# Unit Tests (kept small but comprehensive)
# -----------------------------
class TestRecursionEasy(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

    def test_reverse_string(self):
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("recursion"), "noisrucer")

    def test_sum_array(self):
        self.assertEqual(sum_array([]), 0)
        self.assertEqual(sum_array([5]), 5)
        self.assertEqual(sum_array([1, 2, 3, 4]), 10)


class TestRecursionMedium(unittest.TestCase):
    def test_binary_search_recursive(self):
        arr = [1, 3, 5, 7, 9, 11]
        self.assertEqual(binary_search_recursive(arr, 1), 0)
        self.assertEqual(binary_search_recursive(arr, 7), 3)
        self.assertEqual(binary_search_recursive(arr, 11), 5)
        self.assertEqual(binary_search_recursive(arr, 6), -1)
        self.assertEqual(binary_search_recursive([], 10), -1)

    def test_max_depth(self):
        # Tree:   1
        #        / \
        #       2   3
        #      / \
        #     4   5
        root = TreeNode(1,
                        TreeNode(2, TreeNode(4), TreeNode(5)),
                        TreeNode(3))
        self.assertEqual(max_depth(root), 3)
        self.assertEqual(max_depth(None), 0)

    def test_is_palindrome_list_recursive(self):
        self.assertTrue(is_palindrome_list_recursive(build_linked_list([1, 2, 2, 1])))
        self.assertTrue(is_palindrome_list_recursive(build_linked_list([1])))
        self.assertFalse(is_palindrome_list_recursive(build_linked_list([1, 2])))
        self.assertTrue(is_palindrome_list_recursive(build_linked_list([])))

    def test_merge_two_sorted_lists_recursive(self):
        l1 = build_linked_list([1, 2, 4])
        l2 = build_linked_list([1, 3, 4])
        merged = merge_two_sorted_lists_recursive(l1, l2)
        self.assertEqual(linked_list_to_list(merged), [1, 1, 2, 3, 4, 4])

    def test_tower_of_hanoi(self):
        # For n=2, optimal moves: A->B, A->C, B->C
        moves = tower_of_hanoi(2, 'A', 'B', 'C')
        self.assertEqual(moves, [('A', 'B'), ('A', 'C'), ('B', 'C')])


class TestRecursionHard(unittest.TestCase):
    def test_generate_unique_bsts(self):
        # n=0 -> edge case: often defined as [None]
        trees0 = generate_unique_bsts(0)
        self.assertIsInstance(trees0, list)
        # n=1 -> one tree: [1]
        trees1 = generate_unique_bsts(1)
        self.assertEqual(len(trees1), 1)
        self.assertEqual(serialize_tree_preorder(trees1[0]), [1, None, None])
        # n=3 -> 5 unique BSTs (Catalan number C3 = 5)
        trees3 = generate_unique_bsts(3)
        self.assertEqual(len(trees3), 5)
        # Verify all serialize to distinct shapes/values
        serials = {tuple(serialize_tree_preorder(t)) for t in trees3}
        self.assertEqual(len(serials), 5)

    def test_word_break_all(self):
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        out = word_break_all(s, wordDict)
        self.assertIsInstance(out, list)
        self.assertEqual(set(out), {"cats and dog", "cat sand dog"})
        # No solution case
        self.assertEqual(word_break_all("leetcode", ["leetcod"]), [])


if __name__ == "__main__":
    unittest.main()
