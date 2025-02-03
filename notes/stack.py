##### Stack #####
# 1. push(x) O(1)
# 2. pop() O(1)
# 3. peek() O(1)
# 4. size, isEmpty

# we can use a singly linked list with a signle
#   front pointer
# push adds element to the front and pop removes
#   from the front

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.front = None
    self.n = 0
    
  def push(self, x):
    if not self.front:
      self.front = Node(x)
    else:
      node = Node(x)
      node.next = self.front
      self.front = node
    self.n += 1
  
  def pop(self):
    if self.is_empty():
      return KeyError("Empty Stack")
    node = self.front
    self.front = self.front.next
    self.n -= 1
    return node.data
  
  def peek(self):
    if self.is_empty():
      return KeyError("Empty Stack")
    return self.front.data
  
  def size(self):
    return self.n
  
  def is_empty(self):
    return self.n == 0

if __name__=="__main__":
  # Test cases for Stack class

  stack = Stack()

  # Test is_empty on an empty stack
  assert stack.is_empty() == True

  # Test push
  stack.push(1)
  assert stack.peek() == 1
  assert stack.size() == 1
  assert stack.is_empty() == False

  stack.push(2)
  assert stack.peek() == 2
  assert stack.size() == 2

  # Test pop
  assert stack.pop() == 2
  assert stack.size() == 1
  assert stack.peek() == 1

  assert stack.pop() == 1
  assert stack.size() == 0
  assert stack.is_empty() == True

  # Test pop on an empty stack
  try:
    stack.pop()
  except KeyError as e:
    assert str(e) == "'Empty Stack'"

  # Test peek on an empty stack
  try:
    stack.peek()
  except KeyError as e:
    assert str(e) == "'Empty Stack'"

  print("All test cases passed!")
