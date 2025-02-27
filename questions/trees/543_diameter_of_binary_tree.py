from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def build_tree_from_list(values):
    if not values:
        return None

    def inner(index):
        if index < len(values) and values[index] is not None:
            node = TreeNode(values[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node
        return None

    return inner(0)

def print_tree(root):
    if not root:
        print("Empty tree")
        return

    def bfs(node):
        queue = [node]
        while queue:
            current = queue.pop(0)
            if current:
                print(current.val, end=" ")
                queue.append(current.left)
                queue.append(current.right)
            else:
                print("None", end=" ")
        print()

    bfs(root)

# [1,2,3,4,5]
# for each node, we have to get diameter and depth
# depth = max(l_depth, r_depth) + 1
# max_diameter = max(l_dia, r_dia, l_depth + r_depth + 2)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def recurse(node: Optional[TreeNode]) -> Tuple[int, int]:
            l_depth = r_depth = l_dia = r_dia = dia = 0
            
            if node.left:
                l_depth, l_dia = recurse(node.left)
                dia += l_depth
            if node.right:
                r_depth, r_dia = recurse(node.right)
                dia += r_depth
            
            depth = max(l_depth, r_depth) + 1
            dia = max(l_dia, r_dia, dia)
            return depth, dia
        
        _, dia = recurse(root)
        return dia

if __name__=="__main__":
    sol = Solution()
    tc1 = build_tree_from_list([1])
    print_tree(tc1)
    print(sol.diameterOfBinaryTree(tc1))
