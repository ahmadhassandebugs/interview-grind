# Binary Search Questions Scaffold

# Definition for a BST node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1. Binary Search in a BST Iteratively
def bst_search_iterative(root: TreeNode, target: int) -> bool:
    node = root
    while node:  # will stop when reached child and didn't find anything
        if target == node.val: return True
        node = node.left if target < node.val else node.right
    return False

# 2. Binary Search in a BST Recursively
def bst_search_recursive(root: TreeNode, target: int) -> bool:
    if not root: return False
    if target == root.val: return True
    if target < root.val: return bst_search_iterative(root.left, target)
    else: return bst_search_iterative(root.right, target)

# 3. Binary Search in a Sorted Array Iteratively
def binary_search_iterative(arr: list[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    while l <= r:
       mid = (l + r) // 2
       if arr[mid] == target: return mid
       elif arr[mid] < target: l = mid + 1
       else: r = mid - 1
    return -1

# 4. Binary Search in a Sorted Array Recursively
def binary_search_recursive(arr: list[int], target: int, left: int, right: int) -> int:
    if left > right: return -1
    mid = (left + right) // 2
    if arr[mid] == target: return mid
    elif arr[mid] < target: return binary_search_recursive(arr, target, mid + 1, right)
    else: return binary_search_recursive(arr, target, left, mid - 1)

# 5. Binary Search in a Rotated Sorted Array Iteratively
# 2 [2,3,4,0,1] l=0,r=4,mid=2
# given l and r, arr can be rotated or not
# if it is not, use regular search
# if it is, use mid to decide
def rotated_binary_search_iterative(arr: list[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target: return mid
        
        if arr[l] <= arr[mid]:  # left half is sorted
            if arr[l] <= target < arr[mid]: r = mid - 1
            else: l = mid + 1
        else:  # right half is sorted
            if arr[mid] < target <= arr[r]: l = mid + 1
            else: r = mid - 1
    return -1
    

# 6. Binary Search in a Rotated Sorted Array with Duplicates Iteratively
def rotated_binary_search_duplicates_iterative(arr: list[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target: return mid
        
        # Handle duplicates: shrink boundaries to bypass ambiguity
        if arr[l] == arr[mid] == arr[r]:
            l += 1
            r -= 1
            continue
        
        if arr[l] <= arr[mid]:  # left half is sorted
            if arr[l] <= target < arr[mid]: r = mid - 1
            else: l = mid + 1
        else:  # right half is sorted
            if arr[mid] < target <= arr[r]: l = mid + 1
            else: r = mid - 1
    return -1


# Test Cases
if __name__ == "__main__":

    # BST example:
    #        10
    #       /  \
    #      5   15
    #     / \   \
    #    3   7   18
    root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))

    # Test for BST iterative
    assert bst_search_iterative(root, 7) == True  # True
    assert bst_search_iterative(root, 6) == False  # False

    # Test for BST recursive
    assert bst_search_recursive(root, 15) == True  # True
    assert bst_search_recursive(root, 4) == False  # False

    # Sorted Array
    sorted_array = [1, 3, 5, 7, 9, 11, 13]

    # Test for sorted array iterative
    assert binary_search_iterative(sorted_array, 7) == 3  # Expected index: 3
    assert binary_search_iterative(sorted_array, 8) == -1  # Expected index: -1

    # Test for sorted array recursive
    assert binary_search_recursive(sorted_array, 3, 0, len(sorted_array)-1) == 1  # Expected index: 1
    assert binary_search_recursive(sorted_array, 14, 0, len(sorted_array)-1) == -1  # Expected index: -1

    # Rotated Sorted Array (without duplicates)
    rotated_array = [4, 5, 6, 7, 0, 1, 2]

    # Test for rotated sorted array iterative
    assert rotated_binary_search_iterative(rotated_array, 0) == 4  # Expected index: 4
    assert rotated_binary_search_iterative(rotated_array, 1) == 5  # Expected index: 4
    assert rotated_binary_search_iterative(rotated_array, 4) == 0  # Expected index: 4
    assert rotated_binary_search_iterative(rotated_array, 3) == -1  # Expected index: -1
    assert rotated_binary_search_iterative([1], 1) == 0  # Expected index: 0
    assert rotated_binary_search_iterative([1], 2) == -1  # Expected index: -1
    assert rotated_binary_search_iterative([1,2], 1) == 0  # Expected index: 0
    assert rotated_binary_search_iterative([2,1], 1) == 1  # Expected index: 0
    assert rotated_binary_search_iterative([2,1], 2) == 0  # Expected index: 0
    assert rotated_binary_search_iterative([1,2], 2) == 1  # Expected index: 1
    assert rotated_binary_search_iterative([1,2], 3) == -1  # Expected index: 1

    # Rotated Sorted Array with duplicates
    rotated_array_duplicates = [2, 5, 6, 0, 0, 1, 2]

    # Test for rotated sorted array with duplicates iterative
    assert rotated_binary_search_duplicates_iterative(rotated_array_duplicates, 0) == 3  # True
    assert rotated_binary_search_duplicates_iterative(rotated_array_duplicates, 3) == -1  # False