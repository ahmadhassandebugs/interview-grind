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
    
# for each node, get depth of left and right nodes
# see if they differ by more than 1

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def recurse(node):
            
            if not node: return 0, True
            
            l_depth = r_depth = 0
            l_balanced = r_balanced = True
            
            if node.left: l_depth, l_balanced = recurse(node.left)
            if node.right: r_depth, r_balanced = recurse(node.right)
            
            balanced = abs(l_depth - r_depth) <= 1
            balanced = balanced and l_balanced and r_balanced
            
            return max(l_depth, r_depth) + 1, balanced
        
        _, balanced = recurse(root)
        return balanced

if __name__=="__main__":
    sol = Solution()
    tc1 = build_tree_from_list([3,9,20,None,None,15,7])
    tc2 = build_tree_from_list([1,2,2,3,3,None,None,4,4])
    tc3 = build_tree_from_list([1,2])
    print(sol.diameterOfBinaryTree(tc1))
    print(sol.diameterOfBinaryTree(tc2))
    print(sol.diameterOfBinaryTree(tc3))
