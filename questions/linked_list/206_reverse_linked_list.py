# [1,2,3,4,5]
# 1->2->3->4->5->NULL
# ^ (head)
# 1. Iterative solution: traverse each node and change the dir of arrows
#   for node 2, 1 becomes next
#   need a temp ptr to store rest of the linked list
#   start from cur=head, rest=head.next
#   while rest is not None
#   temp = rest.next # 3
#   rest.next = cur  # 1<-2
#   cur = rest  # 2
#   rest = temp # 3
# 2. recursive solution: we can have two ptrs (one for reversed head, one for original head)
#   at the start, reversed head is NULL, and original is head (rev=NULL,org=head)
#   store next node of org_head (org_rest)
#   make org.next = rev
#   rev head is now org
#   then call the function recursively (org, org_rest) is org_rest is not none

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def recurse(rev=None, org=None):
            org_rest = org.next
            org.next = rev
            if org_rest:
                return recurse(rev=org, org=org_rest)
            else:
                return org
            
        if head is None: return None

        return recurse(rev=None, org=head)


        # if head is None: return None

        # cur, rest = head, head.next

        # while rest:
        #     temp = rest.next
        #     rest.next = cur
        #     cur = rest
        #     rest = temp

        # head.next = None
        # return cur



if __name__=="__main__":
    tc1 = create_linked_list([])
    sol = Solution()
    tc1 = sol.reverseList(tc1)
    print_linked_list(tc1)
