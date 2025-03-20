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

# we could sort stones but that's O(NLOGN) and we will have to do
#   that N times
# heap is an easier way to do it since adding is O(LOGN) and removal
#   is O(LOGN) and peek is O(1)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MinHeap()
        for stone in stones: heap.push(-stone)
        
        # remove two stones each time (return when one left)
        while True:
            if not heap.size(): return 0
            stone1 = -heap.pop()
            if not heap.size(): return stone1
            stone2 = -heap.pop()
            diff  = stone1 - stone2  # must be non-negative
            if diff: heap.push(-diff)
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.lastStoneWeight([2,7,4,1,8,1]))
    print(sol.lastStoneWeight([1]))
    print(sol.lastStoneWeight([10, 4, 2, 10]))
    print(sol.lastStoneWeight([3, 3, 3, 3]))
    print(sol.lastStoneWeight([9, 3, 2, 10, 7]))
    print(sol.lastStoneWeight([1, 1, 1, 1, 1, 1]))
    print(sol.lastStoneWeight([5, 5, 5, 5, 5, 5, 5]))
