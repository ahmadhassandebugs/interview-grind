##### Double ended queue #####
# Functions:
# 1. enqueue(x) O(1) 
# 2. dequeue() O(1)
# 3. peek() O(1)
# 4. size, isEmpty 

### Takeaways ###
# if rear is null, the queue is empty

# we can use a singly linked list with two pointers (front and rear)
#   to handle this
# enqueue adds to the rear of the queue, dequeue removes from the front
# peek returns front element without dequeuing it

class Node:
  def __init__(self, x):
    self.data = x
    self.next = None
    
class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.n = 0
    
  def enqueue(self, x):
    node = Node(x)
    if not self.rear:
      self.front = self.rear = node
    else:
      self.rear.next = node
      self.rear = node
    self.n += 1
  
  def dequeue(self):
    if self.is_empty():
      raise KeyError("Empty Queue")
    node = self.front
    self.front = self.front.next
    self.n -= 1
    if not self.front:
      self.rear = None
    return node.data
  
  def peek(self):
    if self.is_empty():
      raise KeyError("Empty Queue")
    return self.front.data
  
  def size(self):
    return self.n
  
  def is_empty(self):
    return self.n == 0


if __name__=="__main__":
  q = Queue()
  
  # Test is_empty on an empty queue
  assert q.is_empty() == True, "Test failed: Queue should be empty"
  
  # Test enqueue
  q.enqueue(1)
  assert q.is_empty() == False, "Test failed: Queue should not be empty"
  assert q.size() == 1, "Test failed: Queue size should be 1"
  assert q.peek() == 1, "Test failed: Front element should be 1"
  
  q.enqueue(2)
  assert q.size() == 2, "Test failed: Queue size should be 2"
  assert q.peek() == 1, "Test failed: Front element should still be 1"
  
  # Test dequeue
  assert q.dequeue() == 1, "Test failed: Dequeued element should be 1"
  assert q.size() == 1, "Test failed: Queue size should be 1 after dequeue"
  assert q.peek() == 2, "Test failed: Front element should be 2"
  
  assert q.dequeue() == 2, "Test failed: Dequeued element should be 2"
  assert q.is_empty() == True, "Test failed: Queue should be empty after dequeue"
  
  # Test dequeue on empty queue
  try:
    q.dequeue()
  except KeyError:
    pass
  else:
    assert False, "Test failed: Dequeue on empty queue should raise KeyError"
  
  print("All tests passed!")
