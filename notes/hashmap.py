##### Hash Map (Table) #####
# Functions:
# 1. insert(key,value) O(1)
# 2. remove(key) O(1)
# 3. access(key) O(1)
# 4. search(value) O(n)
# 5. print() O(n)
# 6. length() O(n)

### Takeaways ###
# It's better to traverse using current not (i.e., while cur:)
# If some node is to be removed, just maintain a second
#   previous pointer.

# we can maintain a dynamic array of linked list for this
#   any decent hash function should work
#   the dynamic array will contain head of the llist
# while inserting, find the index using hash fn and insert at the end
#   of that linked list if element is not there already
# when removing, find the index and check the keys in linked list
#   raise error if not there and set is empty
# when accessing, simply find index and return value from the linked list
# when searching, find the index and check the value field of nodes
#    in the linked list and return value

class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None

class HashMap:
  def __init__(self, capacity=8):
    self.capacity = capacity
    self.n = 0
    self.container = [None] * self.capacity
    
  def insert(self, key, value):
    key_hash = self.__hash(key)
    if self.container[key_hash] is None:
      self.container[key_hash] = Node(key, value)
      self.n += 1
      return
    
    cur = self.container[key_hash]
    while cur:
      if cur.key == key:
        cur.value = value
        return
      cur = cur.next
    
    node = Node(key, value)
    node.next = self.container[key_hash]
    self.container[key_hash] = node
    self.n += 1
      
  def remove(self, key):
    key_hash = self.__hash(key)      
    prev = None
    cur = self.container[key_hash]
        
    while cur:
      if cur.key == key:
        if prev:          
          prev.next = cur.next
        else:
          self.container[key_hash] = cur.next
        self.n -= 1
        return
      prev = cur
      cur = cur.next
    
    return None
  
  def access(self, key):
    key_hash = self.__hash(key)
    cur = self.container[key_hash]
    while cur:
      if cur.key == key:
        return cur.value
      cur = cur.next
    
    return None
  
  def search(self, value):
    for _, node in enumerate(self.container):
      while node:
        if node.value == value:
          return node.key
        node = node.next
    return None
  
  def __hash(self, key):
    return key % self.capacity
  
  def __len__(self):
    return self.n
  
  def __str__(self):
    result = ""
    for i, node in enumerate(self.container):
      if node is None:
        continue
      result += f"Bucket {i}: "
      cur = node
      while cur:
        result += f"({cur.key}, {cur.value})->"
        cur = cur.next
      result += f"NULL "
    return result


if __name__=="__main__":
  hash_map = HashMap()
  
  # Test insert
  hash_map.insert(1, 'one')
  hash_map.insert(2, 'two')
  hash_map.insert(3, 'three')
  print(hash_map)  # Expected: 1:one-> 2:two-> 3:three->
  
  # Test access
  print(hash_map.access(1))  # Expected: 'one'
  print(hash_map.access(4))  # Expected: None
  
  # Test remove
  hash_map.remove(2)
  print(hash_map)  # Expected: 1:one-> 3:three->
  
  # Test search
  print(hash_map.search('three'))  # Expected: 3
  print(hash_map.search('four'))  # Expected: None
  
  # Test length
  print(len(hash_map))  # Expected: 2
