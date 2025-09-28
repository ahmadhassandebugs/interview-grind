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
    prev, curr, = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def reverse_list_recursive(head):
    if head is None or head.next is None: return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

def find_middle(head):
    if head is None: return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def has_cycle(head):
    if head is None: return False
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False

def remove_nth_from_end_iterative(head, n):
    if head is None: return head
    dummy = ListNode(0, head)
    left = right = dummy
    while right and n >= 0:
        right = right.next
        n -= 1
    if n == -1:
        while right:
            left, right = left.next, right.next
        left.next = left.next.next
    return dummy.next

def remove_nth_from_end_recursive(head, n):
    if head is None: return None
    dummy = ListNode(0, head)

    def recurse(node):
        if node is None: return 0
        curr_depth = recurse(node.next) + 1
        if curr_depth == n + 1: node.next = node.next.next
        return curr_depth
    
    recurse(dummy)
    return dummy.next

def merge_two_sorted_lists(l1, l2):
    curr = dummy = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val: curr.next, l1 = l1, l1.next
        else: curr.next, l2 = l2, l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next

def merge_alternate(l1, l2):
    if l1 is None: return l2
    if l2 is None: return l1
    head = l1
    while l1 and l2:
        next_l1 = l1.next
        next_l2 = l2.next
        l1.next = l2
        l2.next = next_l1
        l1 = next_l1
        l2 = next_l2
    if l2:
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = l2
    return head

def add_node_at_beginning(head, val):
    node = ListNode(val)
    node.next = head
    return node

def add_node_at_end(head, val):
    node = ListNode(val)
    if head is None: return node
    curr = head
    while curr.next: curr = curr.next
    curr.next = node
    return head

def remove_node_from_beginning(head):
    if head is None: return None
    return head.next

def remove_node_from_end(head):
    if head is None or head.next is None: return None
    curr = head
    while curr.next and curr.next.next:
        curr = curr.next
    curr.next = curr.next.next
    return head

# ----- Test Cases -----

def test_reverse_list_iterative():
    head = build_list([1, 2, 3, 4, 5])
    new_head = reverse_list_iterative(head)
    print_list(new_head)
    head = build_list([1, 2])
    new_head = reverse_list_iterative(head)
    print_list(new_head)
    head = build_list([1])
    new_head = reverse_list_iterative(head)
    print_list(new_head)
    head = build_list([])
    new_head = reverse_list_iterative(head)
    print_list(new_head)

def test_reverse_list_recursive():
    head = build_list([1, 2, 3, 4, 5])
    new_head = reverse_list_recursive(head)
    print_list(new_head)
    head = build_list([1, 2])
    new_head = reverse_list_recursive(head)
    print_list(new_head)
    head = build_list([1])
    new_head = reverse_list_recursive(head)
    print_list(new_head)
    head = build_list([])
    new_head = reverse_list_recursive(head)
    print_list(new_head)

def test_find_middle():
    head = build_list([1, 2, 3, 4, 5])
    mid = find_middle(head)
    print(mid.val if mid else None)
    head = build_list([1, 2, 3, 4])
    mid = find_middle(head)
    print(mid.val if mid else None)
    head = build_list([1, 2])
    mid = find_middle(head)
    print(mid.val if mid else None)
    head = build_list([1])
    mid = find_middle(head)
    print(mid.val if mid else None)
    head = build_list([])
    mid = find_middle(head)
    print(mid.val if mid else None)

def test_has_cycle():
    head = build_list([1, 2, 3, 4])
    head.next.next.next.next = head.next  # Create cycle
    print(has_cycle(head))
    head = build_list([1, 2, 3, 4])
    print(has_cycle(head))
    head = build_list([1])
    head.next = head  # Create cycle
    print(has_cycle(head))
    head = build_list([])
    print(has_cycle(head))

def test_remove_nth_from_end_iterative():
    head = build_list([1, 2, 3, 4, 5])
    new_head = remove_nth_from_end_iterative(head, 2)
    print_list(new_head)
    head = build_list([1, 2, 3, 4, 5])
    new_head = remove_nth_from_end_iterative(head, 1)
    print_list(new_head)
    head = build_list([1, 2, 3, 4, 5])
    new_head = remove_nth_from_end_iterative(head, 5)
    print_list(new_head)
    head = build_list([1, 2])
    new_head = remove_nth_from_end_iterative(head, 1)
    print_list(new_head)
    head = build_list([1, 2])
    new_head = remove_nth_from_end_iterative(head, 2)
    print_list(new_head)
    head = build_list([1])
    new_head = remove_nth_from_end_iterative(head, 1)
    print_list(new_head)
    head = build_list([])
    new_head = remove_nth_from_end_iterative(head, 0)
    print_list(new_head)

def test_remove_nth_from_end_recursive():
    head = build_list([1, 2, 3, 4, 5])
    new_head = remove_nth_from_end_recursive(head, 2)
    print_list(new_head)
    head = build_list([1, 2, 3, 4, 5])
    new_head = remove_nth_from_end_recursive(head, 1)
    print_list(new_head)
    head = build_list([1, 2, 3, 4, 5])
    new_head = remove_nth_from_end_recursive(head, 5)
    print_list(new_head)
    head = build_list([1, 2])
    new_head = remove_nth_from_end_recursive(head, 1)
    print_list(new_head)
    head = build_list([1, 2])
    new_head = remove_nth_from_end_recursive(head, 2)
    print_list(new_head)
    head = build_list([1])
    new_head = remove_nth_from_end_recursive(head, 1)
    print_list(new_head)
    head = build_list([])
    new_head = remove_nth_from_end_recursive(head, 0)
    print_list(new_head)

def test_merge_two_sorted_lists():
    l1 = build_list([1, 3, 5])
    l2 = build_list([2, 4, 6])
    new_head = merge_two_sorted_lists(l1, l2)
    print_list(new_head)
    l1 = build_list([])
    l2 = build_list([2, 4, 6])
    new_head = merge_two_sorted_lists(l1, l2)
    print_list(new_head)
    l1 = build_list([1, 3, 5])
    l2 = build_list([])
    new_head = merge_two_sorted_lists(l1, l2)
    print_list(new_head)
    l1 = build_list([])
    l2 = build_list([])
    new_head = merge_two_sorted_lists(l1, l2)
    print_list(new_head)

def test_merge_alternate():
    l1 = build_list([1, 3, 5])
    l2 = build_list([2, 4, 6])
    new_head = merge_alternate(l1, l2)
    print_list(new_head)
    l1 = build_list([1, 3, 5, 7])
    l2 = build_list([2, 4, 6])
    new_head = merge_alternate(l1, l2)
    print_list(new_head)
    l1 = build_list([1, 3, 5])
    l2 = build_list([2, 4, 6, 8])
    new_head = merge_alternate(l1, l2)
    print_list(new_head)
    l1 = build_list([1, 3, 5])
    l2 = build_list([])
    new_head = merge_alternate(l1, l2)
    print_list(new_head)
    l1 = build_list([])
    l2 = build_list([2, 4, 6, 8])
    new_head = merge_alternate(l1, l2)
    print_list(new_head)
    l1 = build_list([])
    l2 = build_list([])
    new_head = merge_alternate(l1, l2)
    print_list(new_head)

def test_add_remove_operations():
    head = build_list([1, 2, 3])
    head = add_node_at_beginning(head, 0)
    print_list(head)  # 0 -> 1 -> 2 -> 3
    head = add_node_at_end(head, 4)
    print_list(head)  # 0 -> 1 -> 2 -> 3 -> 4
    head = remove_node_from_beginning(head)
    print_list(head)  # 1 -> 2 -> 3 -> 4
    head = remove_node_from_end(head)
    print_list(head)  # 1 -> 2 -> 3

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
    print("\nTest Add/Remove Operations:")
    test_add_remove_operations()
