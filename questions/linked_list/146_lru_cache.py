# capacity is fixed
# get(key)->value
# put(key,value)
#   update the value if it exists, otherwise add the key and value
#   check if adding will exceed the capacity, if yes evict least recently
#   used key
# we could use a hash_map but keeping track of lru is not easy
# queue (list) can give us lru but removing first element is O(n)
# queue (linked list) can give us lru and removing adding is O(1)
#   but we do not know how to get a node with key. we could use 
#   a hashmap(key->node) and linked list
#   to remove from the from the front, we need head. to add to the
#   back we need tail
# 1. remove node: requires knowing previous so use doubly linked list
# 2. add node to the end
# 3. get(key) => get node, remove node, then add to the end, and ret value
# 4. put(key,value) => if exists, get node, remove node. create new node,
#    add to the hashmap, add to the end.
#    if capacity exceeded, remove from the front.
# 5. handling empty queue, 1 capacity is too much code so use sentinel nodes

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.cap = capacity
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next, self.tail.prev = self.tail, self.head

    def _enque(self, node: Node) -> None:
        self.tail.prev.next, node.prev = node, self.tail.prev
        self.tail.prev, node.next = node, self.tail
    
    def _remove(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev
        
    def _deque(self) -> Node:
        node = self.head.next
        self._remove(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.map: return -1
        
        node = self.map[key]
        self._remove(node)
        self._enque(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            old_node = self.map[key]
            self._remove(old_node)
            
        self.map[key] = Node(key, value)
        self._enque(self.map[key])
        
        if len(self.map) > self.cap:
            node = self._deque()
            del self.map[node.key]
        
    
if __name__ == "__main__":
    # Test put and get
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1, "Test case 1 failed"
    cache.put(3, 3)
    assert cache.get(2) == -1, "Test case 2 failed"
    cache.put(4, 4)
    assert cache.get(1) == -1, "Test case 3 failed"
    assert cache.get(3) == 3, "Test case 4 failed"
    assert cache.get(4) == 4, "Test case 5 failed"
    print("test_put_and_get passed")

    # Test update existing key
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)
    assert cache.get(1) == 10, "Test case 1 failed"
    assert cache.get(2) == 2, "Test case 2 failed"
    print("test_update_existing_key passed")

    # Test capacity limit
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == -1, "Test case 1 failed"
    assert cache.get(2) == 2, "Test case 2 failed"
    print("test_capacity_limit passed")
