##### Binary Search Trees #####
# Functions:
# 1. insert(value) log(n)
# 2. search(value) log(n)
# 3. delete(value) log(n)
# 4. traversals: inorder, preorder, postorder
# 5. size, depth

### Takeaways ###
# you don't know how to delete a node
#   2 children case is tricky (inorder predecessor)
#   queue: append() and pop(0), stack: append() and pop()
# for dfs with stack, add the right node first (LIFO) so
#   that left node is popped first

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = TreeNode(value)
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = TreeNode(value)
      else:
        self.right.insert(value)
  
  def search(self, value):
    if value < self.value:
      if not self.left:
        return False
      else:
        return self.left.search(value)
    elif value > self.value:
      if not self.right:
        return False
      else:
        return self.right.search(value)
    else:
      return True
  
  def inorder(self):
    if self.left:
      self.left.inorder()
    print(self.value, sep=",")
    if self.right:
      self.right.inorder()
  
  def preorder(self):
    print(self.value, sep=",")
    if self.left:
      self.left.preorder()
    if self.right:
      self.right.preorder()
  
  def postorder(self):
    if self.left:
      self.left.postorder()
    if self.right:
      self.right.postorder()
    print(self.value, sep=",")

  def size(self):
    l_size, r_size = 0, 0
    if self.left:
      l_size = self.left.size()
    if self.right:
      r_size = self.right.size()
    return l_size + r_size + 1
  
  def depth(self):
    l_depth, r_depth = 0, 0
    if self.left:
      l_depth = self.left.depth()
    if self.right:
      r_depth = self.right.depth()
    return 1 + max(l_depth, r_depth)

def bfs(node):
  queue = []
  queue.append(node)
  while len(queue) > 0:
    current = queue.pop(0)
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
    print(f"{current.value}->")

def dfs(node):
  stack = []
  stack.append(node)
  while len(stack) > 0:
    current = stack.pop()
    print(f"{current.value}->")
    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)

if __name__=="__main__":
  # Create a binary search tree and insert values
  bst = TreeNode(10)
  bst.insert(5)
  bst.insert(15)
  bst.insert(3)
  bst.insert(7)
  bst.insert(12)
  bst.insert(18)
  bst.insert(1)
  bst.insert(4)
  bst.insert(6)

  # Test search function
  print("Search 7:", bst.search(7))  # Should return True
  print("Search 20:", bst.search(20))  # Should return False

  # Test inorder traversal
  print("Inorder traversal:")
  bst.inorder()  # Should print 1, 3, 4, 5, 6, 7, 10, 12, 15, 18

  # Test preorder traversal
  print("Preorder traversal:")
  bst.preorder()  # Should print 10, 5, 3, 1, 4, 7, 6, 15, 12, 18

  # Test postorder traversal
  print("Postorder traversal:")
  bst.postorder()  # Should print 1, 4, 3, 6, 7, 5, 12, 18, 15, 10

  # Test size function
  print("Size of the tree:", bst.size())  # Should return 10

  # Test depth function
  print("Depth of the tree:", bst.depth())  # Should return 4
  
  # Test BFS traversal
  print("BFS traversal:")
  bfs(bst)  # Should print 10->5->15->3->7->12->18->1->4->6->

  # Test DFS traversal
  print("DFS traversal:")
  dfs(bst)  # Should print 10->5->3->1->4->7->6->15->12->18->
