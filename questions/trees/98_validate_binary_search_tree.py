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


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int, bool]:
            
            l_low = r_low = float('inf')
            l_high = r_high = float('-inf')
            l_valid = r_valid = True
            
            if node.left:
                l_low, l_high, l_valid = dfs(node.left)
                
            if node.right:
                r_low, r_high, r_valid = dfs(node.right)
                
            lowest = min(node.val, l_low, r_low)
            highest = max(node.val, l_high, r_high)
            valid = l_high < node.val < r_low
            
            return lowest, highest, valid and l_valid and r_valid           

        
        if not root: return True
        _, _, valid = dfs(root)
        return valid
            


if __name__=="__main__":
    sol = Solution()
    tc1 = build_tree_from_list([2,1,3])
    tc2 = build_tree_from_list([5,1,4,None,None,3,6])
    tc3 = build_tree_from_list([1])
    print(sol.isValidBST(tc1))
    print(sol.isValidBST(tc2))
    print(sol.isValidBST(tc3))
