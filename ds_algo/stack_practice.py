class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    pass
    
  def push(self, x):
    pass
  
  def pop(self):
    pass
  
  def peek(self):
    pass
  
  def size(self):
    pass
  
  def is_empty(self):
    pass

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
