# [2,4,3] [5,6,4]
#  342
# +465
#  807
# [2,4,3,5] [5,6,4]
#  5342
# + 465
#  5807
# traverse the lists and add numbers + carry
# new node value is sum // 10 and carry is sum % 10
# if one of the node is null their value is zero
# stop when both the nodes are null

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1: return l2
        if not l2: return l1
        
        carry = 0
        val = carry + l1.val + l2.val
        val, carry = val % 10, val // 10 
        head = cur = ListNode(val=val)
        
        while l1.next and l2.next:
            l1, l2 = l1.next, l2.next
            val = carry + l1.val + l2.val
            val, carry = val % 10, val // 10 
            cur.next = ListNode(val=val)
            cur = cur.next
            
        while l1.next:
            l1 = l1.next
            val = carry + l1.val
            val, carry = val % 10, val // 10 
            cur.next = ListNode(val=val)
            cur = cur.next
        
        while l2.next:
            l2 = l2.next
            val = carry + l2.val
            val, carry = val % 10, val // 10 
            cur.next = ListNode(val=val)
            cur = cur.next
            
        if carry: cur.next = ListNode(val=carry)
            
        return head
            

if __name__=="__main__":
    tc1 = create_linked_list([9,9,9,9,9,9,9]), create_linked_list([9,9,9,9])
    sol = Solution()
    print_linked_list(sol.addTwoNumbers(*tc1))

        