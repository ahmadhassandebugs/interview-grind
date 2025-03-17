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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node: return False
            if is_same(node, subRoot): return True
            return dfs(node.left) or dfs(node.right)
        
        def is_same(node1, node2):
            if (not node1) ^ (not node2): return False
            if (not node1) and (not node2): return True
            
            return (node1.val == node2.val and
                    is_same(node1.left, node2.left) and
                    is_same(node1.right, node2.right))
                       
        return dfs(root)


if __name__ == "__main__":    
    sol = Solution()
    tc1 = build_tree_from_list([3,4,5,1,2]), build_tree_from_list([4,1,2])
    tc2 = build_tree_from_list([3,4,5,1,2,None,None,None,None,0]), build_tree_from_list([4,1,2])
    tc3 = build_tree_from_list([1,1]), build_tree_from_list([1])
    print(sol.isSubtree(*tc1))
    print(sol.isSubtree(*tc2))
    print(sol.isSubtree(*tc3))
