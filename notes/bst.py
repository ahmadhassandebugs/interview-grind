##### Binary Search Trees #####
# Functions:
# 1. insert(value) log(n)
# 2. search(value) log(n)
# 3. delete(value) log(n)
# 4. traversals: inorder, preorder, postorder


class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
