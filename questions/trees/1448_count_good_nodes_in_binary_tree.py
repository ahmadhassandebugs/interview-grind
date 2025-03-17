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

# 

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node: TreeNode, prefix_path=[]):
            
            if not node: return 0
            
            if not prefix_path or node.val >= max(prefix_path): good = 1
            else: good = 0
            
            l_good_nodes = r_good_nodes = 0
            if node.left: l_good_nodes = dfs(node.left, prefix_path + [node.val])
            if node.right: r_good_nodes = dfs(node.right, prefix_path + [node.val])
            
            return good + l_good_nodes + r_good_nodes
            
        return dfs(root, [])

if __name__=="__main__":
    sol = Solution()
    tc1 = build_tree_from_list([3,1,4,3,None,1,5])
    tc2 = build_tree_from_list([3,3,None,4,2])
    tc3 = build_tree_from_list([1])
    print(sol.goodNodes(tc1))
    print(sol.goodNodes(tc2))
    print(sol.goodNodes(tc3))
