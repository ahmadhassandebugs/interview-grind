
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
        if self.n <= 0: raise ValueError("Empty Heap")
        # replace root with last element
        return_val = self.container[0]
        self._swap(0, self.n-1)
        self.container.pop()
        self.n -= 1
        # heapify down to restore heap property
        self._heapify_down(0)
        return return_val
    
    def peek(self) -> int:
        if self.n <= 0: raise ValueError("Empty Heap")
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
    
if __name__ == "__main__":
    # Test initialization
    heap = MinHeap()
    print(heap)
    assert heap.size() == 0, f"Expected size 0, got {heap.size()}"
    assert str(heap) == "[]:0", f"Expected '[]:0', got {str(heap)}"
    
    # Test push
    heap.push(5)
    print(heap)
    assert heap.size() == 1, f"Expected size 1, got {heap.size()}"
    assert heap.peek() == 5, f"Expected peek 5, got {heap.peek()}"
    
    heap.push(3)
    print(heap)
    assert heap.size() == 2, f"Expected size 2, got {heap.size()}"
    assert heap.peek() == 3, f"Expected peek 3, got {heap.peek()}"
    
    heap.push(8)
    print(heap)
    assert heap.size() == 3, f"Expected size 3, got {heap.size()}"
    assert heap.peek() == 3, f"Expected peek 3, got {heap.peek()}"
    
    heap.push(1)
    print(heap)
    assert heap.size() == 4, f"Expected size 4, got {heap.size()}"
    assert heap.peek() == 1, f"Expected peek 1, got {heap.peek()}"
    
    heap.push(6)
    print(heap)
    assert heap.size() == 5, f"Expected size 5, got {heap.size()}"
    assert heap.peek() == 1, f"Expected peek 1, got {heap.peek()}"
    
    heap.push(0)
    print(heap)
    assert heap.size() == 6, f"Expected size 6, got {heap.size()}"
    assert heap.peek() == 0, f"Expected peek 0, got {heap.peek()}"
    
    heap.push(10)
    print(heap)
    assert heap.size() == 7, f"Expected size 7, got {heap.size()}"
    assert heap.peek() == 0, f"Expected peek 0, got {heap.peek()}"
    
    # Test pop
    heap.pop()
    print(heap)
    assert heap.size() == 6, f"Expected size 6, got {heap.size()}"
    assert heap.peek() == 1, f"Expected peek 1, got {heap.peek()}"
    
    heap.pop()
    print(heap)
    assert heap.size() == 5, f"Expected size 5, got {heap.size()}"
    assert heap.peek() == 3, f"Expected peek 3, got {heap.peek()}"
    
    heap.pop()
    print(heap)
    assert heap.size() == 4, f"Expected size 4, got {heap.size()}"
    assert heap.peek() == 5, f"Expected peek 5, got {heap.peek()}"
    
    heap.pop()
    print(heap)
    assert heap.size() == 3, f"Expected size 3, got {heap.size()}"
    assert heap.peek() == 6, f"Expected peek 6, got {heap.peek()}"
    
    heap.pop()
    print(heap)
    assert heap.size() == 2, f"Expected size 2, got {heap.size()}"
    assert heap.peek() == 8, f"Expected peek 8, got {heap.peek()}"
    
    heap.pop()
    print(heap)
    assert heap.size() == 1, f"Expected size 1, got {heap.size()}"
    assert heap.peek() == 10, f"Expected peek 10, got {heap.peek()}"
    
    heap.pop()
    print(heap)
    assert heap.size() == 0, f"Expected size 0, got {heap.size()}"
    try:
        heap.peek()
    except ValueError as e:
        assert str(e) == "Empty Heap"
    else: assert False, "Some other error"
    
    heap = MinHeap()
    nums = [5, 3, 8, 1, 6, 0, 10]
    heap.heapify(nums)
    print(heap)
