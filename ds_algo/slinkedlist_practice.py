"""
- head -> Optional[nodes]

- insert: make new node, make its next head, make head this node: head -> new_node -> [old_head]
"""

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __len__(self):
        curr, n = self.head, 0
        while curr:
            n += 1
            curr = curr.next
        return n
    
    def __str__(self):
        curr, result = self.head, ""
        while curr:
            result += f"{curr.data}->"
            curr = curr.next
        return f"{result}None"
        
    def insert_at_begin(self, x):
        pass
    
    def insert_at_end(self, x):
        pass
    
    def insert_at_index(self, x, pos):
        pass
    
    def delete_first(self):
        pass
    
    def delete_last(self):
        pass
    
    def delete_at_index(self, pos):
        pass
    
    def delete_element(self, x):
        pass
            

if __name__ == "__main__":
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
    
    # Test delete_at_index
    ll.insert_at_begin(50)
    ll.insert_at_begin(40)
    print(ll)  # Expected: ->40->50->10->30->None
    ll.delete_at_index(0)
    print(ll)  # Expected: ->50->10->30->None
    ll.delete_at_index(1)
    print(ll)  # Expected: ->50->30->None
    ll.delete_at_index(1)
    print(ll)  # Expected: ->50->None
    ll.delete_at_index(0)
    print(ll)  # Expected: ->None
