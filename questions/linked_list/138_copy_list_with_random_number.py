# [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Deep copy of linked list is easy. The problem is
#   to point to a random node when
#   1. it hasn't been created
#   2. it has been created but we gotta find the index in original
# So we can go iteratively and create nodes in one pass
# Do another pass and point randoms to their nodes
# To avoid searching in O(n), we can use hashmaps


from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random  # points to nth node
        
def create_linked_list(arr):
    if not arr:
        return None
    head = Node(x=arr[0][0], random=arr[0][1])
    current = head
    for val in arr[1:]:
        current.next = Node(x=val[0], random=val[1])
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(f"[{current.val},{current.random}]", end=" -> " if current.next else "\n")
        current = current.next

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        
        cur_idx = 0
        n_head = n_cur = Node(x=head.val)
        n_hash_map = {cur_idx: n_cur}  # idx,node
        cur = head
        hash_map = {cur: cur_idx}  # node,idx
        while cur.next:
            cur_idx += 1
            cur = cur.next
            hash_map[cur] = cur_idx
            n_cur.next = Node(x=cur.val)
            n_cur = n_cur.next
            n_hash_map[cur_idx] = n_cur
            
        cur = head
        r_indices = []  # random_idx
        while cur:
            if cur.random: r_indices.append(hash_map[cur.random])
            else: r_indices.append(None)
            cur = cur.next
            
        n_cur = n_head
        cur_idx = 0
        while n_cur:
            if r_indices[cur_idx]: n_cur.random = n_hash_map[r_indices[cur_idx]]
            else: n_cur.random = None
            n_cur = n_cur.next
            cur_idx += 1
            
        return n_head
    
if __name__=="__main__":
    tc1 = create_linked_list([[7,None],[13,0],[11,4],[10,2],[1,0]])
    sol = Solution()
    sol1 = sol.copyRandomList(tc1)
    print_linked_list(sol1)
