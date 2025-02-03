##### Singly Linked List #####
# Functions:
# 1. insertAtBegin(x) O(1)
# 2. insertAtEnd(x) O(n)
# 3. insertAtIndex(pos,x) O(n) if pos not found return without adding
# 4. deleteFirst() O(1)
# 5. deleteLast() O(n)
# 6. deleteElement(x) O(n)
# 7. length() O(n)
# 8. print() O(n)

#### Takeaways ####
# still struggling with insert at index and delete at index/element
#   since you're using cur.next condition, you should check for first
#   node separately or use cur condition and a prev node pointer

# create a Node class to take care of each node and keep track of
#   head bc the actual head node can change between objects
# always check for empty (head is null), one node cases
# start with an empty linked list where head is pointing to NULL

class Node:
  def __init__(self, x):
    self.data = x
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    
  def insert_at_begin(self, x):
    node = Node(x)
    node.next = self.head
    self.head = node
  
  def insert_at_end(self, x):
    if not self.head:
      self.head = Node(x)
    cur = self.head
    while cur.next:
      cur = cur.next
    cur.next = Node(x)
  
  def insert_at_index(self, x, pos):
    if not self.head:
      if pos == 0:
        self.head = Node(x)
        return
      else:
        return KeyError("Pos not found")
    if pos == 0:
      self.insert_at_begin(x)
      return
    cur, pos = self.head, pos-1
    while cur.next and pos > 0:
      cur, pos = cur.next, pos-1
    if pos == 0:
      node = Node(x)
      node.next = cur.next
      cur.next = node
    else:
      return KeyError("Pos not found")

  def delete_first(self):
    if self.head:
      self.head = self.head.next
  
  def delete_last(self):
    if not self.head:
      return KeyError("Cannot delete from empty list")
    if not self.head.next:
      self.head = None
    cur = self.head
    while cur.next.next:
      cur = cur.next
    cur.next = None
  
  def delete_element(self, x):
    if not self.head:
      return KeyError("Cannot delete from empty list")
    if not self.head.next:
      if x == self.head.data:
        self.head = None
      else:
        return KeyError("Cannot find the element")
      
    if x == self.head.data:
      self.delete_first()
      return
      
    cur = self.head
    while cur.next:
      if x == cur.next.data:
        cur.next = cur.next.next
        return
      cur = cur.next
    
    return KeyError("Cannot find the element")
  
  def __len__(self):
    cur, count = self.head, 0
    while cur:
      cur, count = cur.next, count+1
    return count
  
  def __str__(self):
    cur, result = self.head, ""
    while cur:
      cur, result = cur.next, f"{result}->{cur.data}"
    return f"{result}->None"

if __name__=="__main__":
  ll = LinkedList()
  
  # Test insert_at_begin
  ll.insert_at_begin(10)
  print(ll)  # Expected: ->10->None
  ll.insert_at_begin(20)
  print(ll)  # Expected: ->20->10->None
  
  # Test insert_at_end
  ll.insert_at_end(30)
  print(ll)  # Expected: ->20->10->30->None
  ll.insert_at_end(40)
  print(ll)  # Expected: ->20->10->30->40->None
  
  # Test insert_at_index
  ll.insert_at_index(25, 2)
  print(ll)  # Expected: ->20->10->25->30->40->None
  ll.insert_at_index(5, 0)
  print(ll)  # Expected: ->5->20->10->25->30->40->None
  
  # Test delete_first
  ll.delete_first()
  print(ll)  # Expected: ->20->10->25->30->40->None
  
  # Test delete_last
  ll.delete_last()
  print(ll)  # Expected: ->20->10->25->30->None
  
  # Test delete_element
  ll.delete_element(25)
  print(ll)  # Expected: ->20->10->30->None
  ll.delete_element(20)
  print(ll)  # Expected: ->10->30->None
  
  # Test __len__
  print(len(ll))  # Expected: 2
  
  # Test __str__
  print(ll)  # Expected: ->10->30->None
