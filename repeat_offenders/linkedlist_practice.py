# ===== Linked List Patterns Practice =====

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----- Utility Functions -----

def build_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def print_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

# ----- Scaffolds to Implement -----

def reverse_list_iterative(head):
    # TODO: Reverse using three pointers
    return head

def reverse_list_recursive(head):
    # TODO: Reverse recursively
    return head

def find_middle(head):
    # TODO: Use slow and fast pointer
    return head

def has_cycle(head):
    # TODO: Detect cycle using slow and fast pointer
    return False

def remove_nth_from_end_iterative(head, n):
    # TODO: Remove nth node from end using two pointers
    return head

def remove_nth_from_end_recursive(head, n):
    # TODO: Remove nth node from end using recursion
    return head

def merge_two_sorted_lists(l1, l2):
    # TODO: Merge two sorted lists
    return l1

def merge_alternate(l1, l2):
    # TODO: Merge two lists at alternate positions
    return l1

# ----- Test Cases -----

def test_reverse_list_iterative():
    head = build_list([1, 2, 3, 4, 5])
    new_head = reverse_list_iterative(head)
    print_list(new_head)

def test_reverse_list_recursive():
    head = build_list([1, 2, 3])
    new_head = reverse_list_recursive(head)
    print_list(new_head)

def test_find_middle():
    head = build_list([1, 2, 3, 4, 5])
    mid = find_middle(head)
    print(mid.val if mid else None)

def test_has_cycle():
    head = build_list([1, 2, 3, 4])
    head.next.next.next.next = head.next  # Create cycle
    print(has_cycle(head))

def test_remove_nth_from_end_iterative():
    head = build_list([1, 2, 3, 4, 5])
    new_head = remove_nth_from_end_iterative(head, 2)
    print_list(new_head)

def test_remove_nth_from_end_recursive():
    head = build_list([1, 2, 3, 4, 5])
    new_head = remove_nth_from_end_recursive(head, 1)
    print_list(new_head)

def test_merge_two_sorted_lists():
    l1 = build_list([1, 3, 5])
    l2 = build_list([2, 4, 6])
    new_head = merge_two_sorted_lists(l1, l2)
    print_list(new_head)

def test_merge_alternate():
    l1 = build_list([1, 3, 5])
    l2 = build_list([2, 4, 6, 8])
    new_head = merge_alternate(l1, l2)
    print_list(new_head)

# ----- Run All Tests -----

if __name__ == "__main__":
    print("Test Reverse Iterative:")
    test_reverse_list_iterative()
    print("\nTest Reverse Recursive:")
    test_reverse_list_recursive()
    print("\nTest Find Middle:")
    test_find_middle()
    print("\nTest Has Cycle:")
    test_has_cycle()
    print("\nTest Remove N-th from End (Iterative):")
    test_remove_nth_from_end_iterative()
    print("\nTest Remove N-th from End (Recursive):")
    test_remove_nth_from_end_recursive()
    print("\nTest Merge Two Sorted Lists:")
    test_merge_two_sorted_lists()
    print("\nTest Merge Alternate:")
    test_merge_alternate()
