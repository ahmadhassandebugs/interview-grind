# [1,2,3,4,5] -> [1,5,2,4,3]
# first, last, second, second-last, third, third last, ...
# 1. break down the problem
#   get second half of the linked list
#   reverse the second half
#   now we have left and right
#   alternate elements from two linked lists: left and right


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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def find_middle(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse(head):
            if head is None: return None

            cur, rest = head, head.next

            while rest:
                temp = rest.next
                rest.next = cur
                cur = rest
                rest = temp

            head.next = None
            return cur
        
        def merge(left, right):
            """
            in each iteration join left and right together
            """
            while right.next:
                next_left = left.next
                left.next = right
                left = next_left

                next_right = right.next
                right.next = left
                right = next_right

        
        if head and head.next:
            
            right = find_middle(head=head)
            left, right = head, reverse(right)

            print_linked_list(left)
            print_linked_list(right)

            merge(left, right)


if __name__=="__main__":
    tc1 = create_linked_list([1,2,3,4,5,6])
    sol = Solution()
    sol.reorderList(tc1)
    print_linked_list(tc1)
