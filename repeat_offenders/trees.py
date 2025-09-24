"""
Tree Practice - Scaffold (no implementations) + Unit Tests

Run tests with:
    python -m unittest tree_scaffold_and_tests.py

Guidelines:
- Do NOT implement the functions below; fill them in yourself later.
- Helpers are provided for building and inspecting trees in tests.
"""
from __future__ import annotations
import unittest
from typing import List, Optional, Deque
from collections import deque


# -----------------------------
# Data structure & helpers
# -----------------------------
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def build_tree_from_level(level: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from a level-order list with None as missing nodes."""
    if not level:
        return None
    it = iter(level)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q: Deque[TreeNode] = deque([root])
    for a, b in zip(it, it):
        node = q.popleft()
        if a is not None:
            node.left = TreeNode(a)
            q.append(node.left)
        if b is not None:
            node.right = TreeNode(b)
            q.append(node.right)
    return root


def tree_to_level_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Serialize a tree to level-order with trailing Nones trimmed (for testing)."""
    if not root:
        return []
    out: List[Optional[int]] = []
    q: Deque[Optional[TreeNode]] = deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
    # trim trailing None values
    while out and out[-1] is None:
        out.pop()
    return out


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


# -----------------------------
# Easy
# -----------------------------

def max_depth(root: Optional[TreeNode]) -> int:
    """Return maximum depth of a binary tree."""
    if root is None: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Invert a binary tree (mirror it) and return the root."""
    if root is None: return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def is_symmetric(root: Optional[TreeNode]) -> bool:
    """Return True if a binary tree is a mirror of itself around its center."""
    
    def recurse(left: Optional[TreeNode], right: Optional[TreeNode]):
        if left is None and right is None: return True
        if left is None or right is None: return False
        
        return (left.val == right.val
            and recurse(left.left, right.right)
            and recurse(left.right, right.left)
        )
    
    if root is None: return True
    return recurse(root.left, root.right)


# -----------------------------
# Medium
# -----------------------------

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """Return level-order traversal of node values."""
    # if root is None: return []
    # from collections import deque
    # queue = deque([root])
    # res = []
    
    # while queue:
    #     size = len(queue)
    #     level = []
    #     for _ in range(size):
    #         node = queue.popleft()
    #         level.append(node.val)
    #         if node.left: queue.append(node.left)
    #         if node.right: queue.append(node.right)
    #     res.append(level)
    
    # return res
    
    res = []
    
    def recurse(node, level):
        if level >= len(res): res.append([])
        res[level].append(node.val)
        if node.left: recurse(node.left, level + 1)
        if node.right: recurse(node.right, level + 1)
        
    if root is None: return []
    recurse(root, 0)
    return res    


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """Return the diameter (longest path length in edges) of the tree."""
    
    diameter = 0
    
    def depth(node):
        nonlocal diameter
        if node is None: return 0
        L = depth(node.left)
        R = depth(node.right)
        diameter = max(diameter, L + R)
        return 1 + max(L, R)

    depth(root)
    return diameter


def lowest_common_ancestor_bst(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """Return LCA of nodes p and q in a BST."""
    if root is None: return None
    
    if p.val < root.val and q.val < root.val: return lowest_common_ancestor_bst(root.left, p, q)
    if p.val > root.val and q.val > root.val: return lowest_common_ancestor_bst(root.right, p, q)
    
    return root


def lowest_common_ancestor_bt(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """Return LCA of nodes p and q in a general binary tree (not necessarily BST)."""
    if root is None: return None
    if p.val == root.val or q.val == root.val: return root
    
    left = lowest_common_ancestor_bt(root.left, p, q)
    right = lowest_common_ancestor_bt(root.right, p, q)
    
    if left and right: return root
    return left if left else right


def build_tree_pre_in(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """Build a binary tree from preorder and inorder traversals."""
    # use preorder to create nodes in sequence D&C and inorder to infer children
    if len(preorder) == 0: return None
    n = len(inorder)
    pos = {inorder[i]: i for i in range(n)}
    curr_pos = 0
    
    def build(lo, hi) -> Optional[TreeNode]:
        nonlocal curr_pos
        if lo > hi: return None
        
        root = TreeNode(preorder[curr_pos])
        mid = pos[preorder[curr_pos]]
        curr_pos += 1
        
        root.left = build(lo, mid - 1)
        root.right = build(mid + 1, hi)
        return root
    
    return build(0, n - 1)


# -----------------------------
# Hard
# -----------------------------

def max_path_sum(root: Optional[TreeNode]) -> int:
    """Return the maximum path sum for any path (may start/end anywhere)."""
    max_sum = float("-inf")

    def dfs(node: Optional[TreeNode]):
        nonlocal max_sum
        if node is None: return 0

        left_max_sum = dfs(node.left)
        right_max_sum = dfs(node.right)
        curr_path_sum = node.val + max(0, left_max_sum) + max(0, right_max_sum)

        if curr_path_sum > max_sum: max_sum = curr_path_sum

        # only one side can continue up; it can be negative
        return node.val + max(left_max_sum, right_max_sum)
    
    dfs(root)
    return max_sum


def distance_k(root: Optional[TreeNode], target: TreeNode, k: int) -> List[int]:
    """Return values of all nodes at distance k from target (order not important)."""
    res = []

    def collect_down(node: Optional[TreeNode], d: int):
        if node is None: return
        if d == 0:
            res.append(node.val)
            return
        collect_down(node.left, d - 1)
        collect_down(node.right, d - 1)

    def dfs(node: Optional[TreeNode]):  # returns distance from target
        if node is None: return -1
        if node == target:
            collect_down(node, k)
            return 0  # when this returns, we check bends
        
        L = dfs(node.left)
        if L != -1:
            if L + 1 == k:
                res.append(node.val)
            else:
                collect_down(node.right, k - L - 2)  # one edge up to node and one edge down to right
                return L + 1

        R = dfs(node.right)
        if R != -1:
            if R + 1 == k: res.append(node.val)
            else:
                collect_down(node.left, k - R - 2)
                return R + 1
        
        return -1
    
    dfs(root)
    return res


# -----------------------------
# Unit Tests
# -----------------------------
class TestTreesEasy(unittest.TestCase):
    def test_max_depth(self):
        root = build_tree_from_level([3,9,20,None,None,15,7])
        self.assertEqual(max_depth(root), 3)
        self.assertEqual(max_depth(None), 0)

    def test_invert_tree(self):
        root = build_tree_from_level([4,2,7,1,3,6,9])
        inv = invert_tree(root)
        self.assertEqual(tree_to_level_list(inv), [4,7,2,9,6,3,1])

    def test_is_symmetric(self):
        sym = build_tree_from_level([1,2,2,3,4,4,3])
        asym = build_tree_from_level([1,2,2,None,3,None,3])
        self.assertTrue(is_symmetric(sym))
        self.assertFalse(is_symmetric(asym))


class TestTreesMedium(unittest.TestCase):
    def test_level_order(self):
        root = build_tree_from_level([3,9,20,None,None,15,7])
        self.assertEqual(level_order(root), [[3],[9,20],[15,7]])
        self.assertEqual(level_order(None), [])

    def test_diameter_of_binary_tree(self):
        root = build_tree_from_level([1,2,3,4,5])
        # Longest path is 4-2-1-3 or 4-2-5 → edges = 3
        self.assertEqual(diameter_of_binary_tree(root), 3)

    def test_lca_bst(self):
        # BST:      6
        #         /   \
        #        2     8
        #       / \   / \
        #      0   4 7   9
        #         / \
        #        3   5
        root = build_tree_from_level([6,2,8,0,4,7,9,None,None,3,5])
        p = find_node(root, 2)
        q = find_node(root, 8)
        r = lowest_common_ancestor_bst(root, p, q)
        self.assertIsNotNone(r)
        self.assertEqual(r.val, 6)
        p = find_node(root, 2); q = find_node(root, 4)
        r = lowest_common_ancestor_bst(root, p, q)
        self.assertIsNotNone(r)
        self.assertEqual(r.val, 2)

    def test_lca_bt(self):
        root = build_tree_from_level([3,5,1,6,2,0,8,None,None,7,4])
        p = find_node(root, 5)
        q = find_node(root, 1)
        r = lowest_common_ancestor_bt(root, p, q)
        self.assertIsNotNone(r)
        self.assertEqual(r.val, 3)
        p = find_node(root, 5); q = find_node(root, 4)
        r = lowest_common_ancestor_bt(root, p, q)
        self.assertIsNotNone(r)
        self.assertEqual(r.val, 5)

    def test_build_tree_pre_in(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        root = build_tree_pre_in(preorder, inorder)
        self.assertEqual(tree_to_level_list(root), [3,9,20,None,None,15,7])


class TestTreesHard(unittest.TestCase):
    def test_max_path_sum(self):
        root = build_tree_from_level([-10,9,20,None,None,15,7])
        # Best path: 15 -> 20 -> 7 = 42
        self.assertEqual(max_path_sum(root), 42)
        self.assertEqual(max_path_sum(TreeNode(1)), 1)

    def test_distance_k(self):
        # Tree:      3
        #          /   \
        #         5     1
        #        / \   / \
        #       6   2 0   8
        #          / \
        #         7   4
        root = build_tree_from_level([3,5,1,6,2,0,8,None,None,7,4])
        target = find_node(root, 5)
        out = distance_k(root, target, 2)
        self.assertEqual(sorted(out), sorted([7,4,1]))
        out = distance_k(root, target, 3)
        self.assertEqual(sorted(out), sorted([0,8]))


if __name__ == "__main__":
    unittest.main()
