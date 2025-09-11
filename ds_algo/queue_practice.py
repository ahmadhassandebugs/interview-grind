class Node:
  def __init__(self, x):
    self.data = x
    self.next = None
    
class Queue:
  def __init__(self):
    pass
        
  def enqueue(self, x):
    pass
  
  def dequeue(self):
    pass
  
  def peek(self):
    pass
  
  def size(self):
    pass
  
  def is_empty(self):
    pass


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
