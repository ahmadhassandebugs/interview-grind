# [4,2,7,1,3,6,9]
# recursive solution is easier to think about
#   given a node as input, return if it's None
#   call the function recursively on children
#   invert left and right after

from typing import Optional

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

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def recurse(node: Optional[TreeNode]):
            if not node: return
            
            if node.left: recurse(node.left)
            if node.right: recurse(node.right)
            
            node.left, node.right = node.right, node.left
            
        recurse(root)
        return root

if __name__=="__main__":
    sol = Solution()
    tc1 = build_tree_from_list([])
    print_tree(tc1)
    print_tree(sol.invertTree(tc1))
