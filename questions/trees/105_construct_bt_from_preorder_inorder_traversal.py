from typing import List, Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        p_idx = 0
        
        def get_left_right_tree(root: int, inorder: List[int]) -> Tuple[List[int], List[int]]:
            idx = inorder.index(root)
            return inorder[:idx], inorder[idx+1:]
            
        def build_recursive(inorder: List[int]):
            if not inorder: return None
            nonlocal p_idx
            root = TreeNode(preorder[p_idx])
            left, right = get_left_right_tree(preorder[p_idx], inorder)
            p_idx += 1
            root.left = build_recursive(left)
            root.right = build_recursive(right)
            return root
                        
        return build_recursive(inorder)
    

if __name__=="__main__":
    sol = Solution()
    
    # Test case 1
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = sol.buildTree(preorder, inorder)
    print_tree(root)  # Expected output: 3 9 20 None None 15 7 None None None None
    
    # Test case 2
    preorder = [1, 2, 3]
    inorder = [2, 1, 3]
    root = sol.buildTree(preorder, inorder)
    print_tree(root)  # Expected output: 1 2 3 None None None None
    
    # Test case 3
    preorder = [1, 2, 4, 5, 3]
    inorder = [4, 2, 5, 1, 3]
    root = sol.buildTree(preorder, inorder)
    print_tree(root)  # Expected output: 1 2 3 4 5 None None None None None None
    
    # Test case 4
    preorder = [-1]
    inorder = [-1]
    root = sol.buildTree(preorder, inorder)
    print_tree(root)  # Expected output: [-1]
