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
# - Stop before the node when inserting at pos (use cur.next.next loop)
# - Pay attention to empty and single node cases
# - When traversing, use cur.next in loop 

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
    
  def insertAtBegin(self, x):
    node = Node(x)
    node.next = self.head
    self.head = node
  
  def insertAtEnd(self, x):
    node = Node(x)
    if self.head is None:
      self.insertAtBegin(x)
      return
  
    cur = self.head
    while cur.next:
      cur = cur.next
    cur.next = node
  
  def insertAtIndex(self, x, pos):
    node = Node(x)

    if self.head is None:
      if pos == 0:
        self.insertAtBegin(x)
      else:
        print("Pos not found")
      return

    # [Mistake] tend to make mistakes with counter (stop before the pos)
    cur, pos = self.head, pos-1  
    while cur.next and pos > 0:
      cur, pos = cur.next, pos-1
    if pos == 0:
      node_after_pos = cur.next
      cur.next = node
      node.next = node_after_pos
    else:
      print("Pos not found", pos)
  
  def deleteFirst(self):
    if self.head is None: return
    self.head = self.head.next
  
  def deleteLast(self):
    if self.head is None: return
    if self.head.next is None: self.deleteFirst()
    
    cur = self.head
    while cur.next and cur.next.next:
      cur = cur.next
    cur.next = None
  
  def deleteElement(self, x):
    if self.head is None: return
    if self.head.next is None and self.head.data == x: self.deleteFirst()
    
    cur = self.head
    while cur.next and cur.next.next and cur.next.data != x:
      cur = cur.next
    if cur.next.data == x:
      cur.next = cur.next.next
    else:
      print("ele not found")
  
  def __len__(self):
    if self.head is None: return 0
    cur, count = self.head, 0
    while cur.next:
      cur, count = cur.next, count+1
    return count
  
  def __str__(self):
    result = ""
    if self.head is None: return ""
    cur = self.head
    while cur.next:
      result += f"{cur.data}->"
      cur = cur.next
    result += f"{cur.data}->"
    return f"{result}NULL"


if __name__=="__main__":
  llist = LinkedList()
  # add nodes to the linked list
  llist.insertAtEnd('a')
  llist.insertAtEnd('b')
  llist.insertAtBegin('c')
  llist.insertAtEnd('d')
  llist.insertAtIndex('g', 2)
  print("c->a->g->b->d->NULL vs.", llist)
  # remove nodes
  llist.deleteLast()
  print("c->a->g->b->NULL vs.", llist)
  llist.deleteElement("g")
  print("c->a->b->NULL vs.", llist)
  llist.deleteFirst()
  print("a->b->NULL vs.", llist)
