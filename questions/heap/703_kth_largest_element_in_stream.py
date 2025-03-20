from typing import List

class MinHeap:
    def __init__(self):
        self.container = []
        self.n = 0
    
    def __str__(self):
        return f"{self.container}:{self.n}"
    
    def size(self):
        return self.n
    
    def push(self, val: int):
        # insert at the end
        self.container.append(val)
        self.n += 1
        # heapify up to restore heap property
        self._heapify_up(self.n - 1)
    
    def pop(self) -> int:
        if self.n <= 0: return None
        # replace root with last element
        return_val = self.container[0]
        self._swap(0, self.n-1)
        self.container.pop()
        self.n -= 1
        # heapify down to restore heap property
        self._heapify_down(0)
        return return_val
    
    def peek(self) -> int:
        if self.n <= 0: return None
        return self.container[0]
    
    def heapify(self, nums):
        for num in nums: self.push(num)
        i  = (self.n - 1) // 2
        while i > 0:
            self._heapify_down(i)
            i = self._parent(i)
    
    def _parent(self, i, check=True):
        idx = (i-1) // 2
        if check:
            assert 0 <= idx < self.n, f"parent of {i}: {idx} not in range"
        return idx
    
    def _left_child(self, i,check=True):
        idx = (2*i) + 1
        if check:
            assert 0 <= idx < self.n, f"left child of {i}: {idx} not in range"
        return idx
    
    def _right_child(self, i, check=True):
        idx = (2*i) + 2
        if check:
            assert 0 <= idx < self.n, f"right child of {i}: {idx} not in range"
        return idx
    
    def _swap(self, i, j):
        self.container[i], self.container[j] = self.container[j], self.container[i]
    
    def _heapify_up(self, i):
        while i > 0 and self.container[i] < self.container[self._parent(i)]:
            self._swap(i, self._parent(i))
            i = self._parent(i)
    
    def _heapify_down(self, i):
        while True:
            min, l, r = i, self._left_child(i, check=False), self._right_child(i, check=False)
            
            if l < self.n and self.container[l] < self.container[min]:
                min = l
            if r < self.n and self.container[r] < self.container[min]:
                min = r
                
            if min == i: break
            
            self._swap(i, min)
            i = min

# a new number appears
#   if smaller than kth largest (root), ignore
#   if larger than or eq to kth largest, add to the end and heapify up
# if n > k, pop (and heapify down)
# return peek (root)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = MinHeap()
        self.k = k
        for num in nums: self.add(num)

    def add(self, val: int) -> int:
        if self.heap.size() <= self.k or val >= self.heap.peek():
            self.heap.push(val)
        if self.heap.size() > self.k:
            self.heap.pop()
        return self.heap.peek() 


if __name__ == "__main__":
    # Test cases
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))  # returns 4
    print(kthLargest.add(5))  # returns 5
    print(kthLargest.add(10)) # returns 5
    print(kthLargest.add(9))  # returns 8
    print(kthLargest.add(4))  # returns 8
    
    
  
    