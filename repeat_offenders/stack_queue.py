# ====================================================================
# STACK AND QUEUE PRACTICE SET (8 Core Problems)
# ====================================================================

"""
Monotonic Stack (MS) Summary:
- MDS (Decreasing): Finds NGE (Next Greater Element). Pop when Current > Stack Top.
- MIS (Increasing): Finds NSE (Nearest Smaller Element). Pop when Current < Stack Top.
- Tips (Always O(N)):
    - Store Indices (not values) for assignment and distance calculations.
    - Use a Sentinel (e.g., [-1]) for boundary conditions (NSE Left).
    - Handle Circular Arrays by iterating 2N times and using i % N.
"""

# --------------------------------------------------------------------
# 1. Valid Parentheses (Basic Stack)
# --------------------------------------------------------------------

def valid_parentheses(s: str) -> bool:
    """
    Determines if an input string containing '(', ')', '{', '}', '[' and ']' 
    is valid. Brackets must close in the correct order.
    """
    from collections import deque
    stack  = deque([])
    paran = { "[": "]", "{": "}", "(": ")" }
    
    for ch in s:
        if ch in paran.values():  # closing
            if len(stack) == 0: return False
            if ch != paran[stack.pop()]: return False
        else:  # opening
            stack.append(ch)
    
    return len(stack) == 0  # empty stack
    # --------------------------------

# --------------------------------------------------------------------
# 2. Next Greater Element II (Monotonic Stack - Circular Array)
# --------------------------------------------------------------------

def next_greater_element_circular(nums: list[int]) -> list[int]:
    """
    Finds the next greater element for every element in a circular array.
    """
    n = len(nums)
    stack = []
    res = [-1] * n
    
    for i in range(2 * n):
        while len(stack) > 0 and nums[i % n] > nums[stack[-1]]:
            res[stack[-1]] = nums[i % n]
            stack.pop()
        if i < n: stack.append(i % n)
    return res
    # --------------------------------

# --------------------------------------------------------------------
# 3. Largest Rectangle in Histogram (Monotonic Stack - Area)
# --------------------------------------------------------------------

def largest_rectangle_in_histogram(heights: list[int]) -> int:
    """
    Finds the area of the largest rectangle in a histogram.
    """
    n = len(heights)
    stack = [-1]
    max_area = 0
    
    for i in range(n):
        while len(stack) > 1 and heights[i] < heights[stack[-1]]:
            l, c, r = stack[-2], stack[-1], i
            area = (r - l - 1) * heights[c]
            if area > max_area: max_area = area
            stack.pop()
        stack.append(i)
    
    while len(stack) > 1:
        l, c, r = stack[-2], stack[-1], n
        area = (r - l - 1) * heights[c]
        if area > max_area: max_area = area
        stack.pop()
    
    return max_area
    # --------------------------------

# --------------------------------------------------------------------
# 4. Implement Stack using Queues (Queue Constraint)
# --------------------------------------------------------------------

from collections import deque

class MyStack:
    """
    Implements a LIFO stack using only FIFO queues.
    fns: push, pop, top, empty
    """
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        if not self.q:
            raise IndexError("pop from empty stack")
        return self.q.popleft()

    def top(self) -> int:
        if not self.q:
            raise IndexError("top from empty stack")
        return self.q[0]

    def empty(self) -> bool:
        return not self.q

class MyStackExpensivePop:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.top_val = None

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.top_val = x

    def pop(self) -> int:
        if self.empty():
            raise IndexError("pop from empty stack")

        while len(self.q1) > 1:
            self.top_val = self.q1.popleft()
            self.q2.append(self.top_val)
        
        popped = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1

        if not self.q1:
             self.top_val = None
        
        return popped

    def top(self) -> int:
        if self.empty():
            raise IndexError("top from empty stack")
        return self.top_val
        
    def empty(self) -> bool:
        return not self.q1
    # --------------------------------

# --------------------------------------------------------------------
# 5. Implement Queue using Stacks (Stack Constraint)
# --------------------------------------------------------------------

class MyQueue:
    """
    Implements a FIFO queue using only LIFO stacks.
    fns: push, pop, peek, empty
    """
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _transfer(self):
        # Transfers all elements from in_stack to out_stack, reversing order
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def push(self, x: int) -> None:
        # O(1) push: New elements always go to the input stack
        self.in_stack.append(x)

    def pop(self) -> int:
        # Amortized O(1) pop: 
        # If out_stack is empty, initiate the transfer (reversal)
        if not self.out_stack:
            self._transfer()
        
        if not self.out_stack:
             raise IndexError("pop from empty queue")
             
        return self.out_stack.pop()

    def peek(self) -> int:
        # Amortized O(1) peek:
        if not self.out_stack:
            self._transfer()

        if not self.out_stack:
             raise IndexError("peek from empty queue")
             
        return self.out_stack[-1]

    def empty(self) -> bool:
        # The queue is empty only if both stacks are empty
        return not self.in_stack and not self.out_stack
    # --------------------------------

# --------------------------------------------------------------------
# 6. Sliding Window Maximum (Deque)
# --------------------------------------------------------------------

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    """
    Finds the maximum element in every contiguous subarray (window) of size k.
    """
    n = len(nums)
    max_deque = deque() # Stores indices
    result = []
    
    for i in range(n):
        # 1. Purge index outside the window
        if max_deque and max_deque[0] == i - k:
            max_deque.popleft()
            
        # 2. Maintain Monotonicity (remove smaller, redundant elements from the back)
        while max_deque and nums[i] >= nums[max_deque[-1]]:
            max_deque.pop()
            
        # 3. Add current index
        max_deque.append(i)
        
        # 4. Record result after the window is formed
        if i >= k - 1:
            result.append(nums[max_deque[0]])
            
    return result
    # --------------------------------

# --------------------------------------------------------------------
# 7. Evaluate Reverse Polish Notation (RPN) (Stack for Evaluation)
# --------------------------------------------------------------------

def eval_rpn(tokens: list[str]) -> int:
    """
    Evaluates the value of an arithmetic expression in Reverse Polish Notation.
    """
    stack = []
    opeartors = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b
    }
    for ch in tokens:
        if ch in opeartors.keys():
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(opeartors[ch](a, b))
        else: stack.append(ch)
    return stack.pop()
    # --------------------------------

# --------------------------------------------------------------------
# 8. Decode String (Stack for State Management)
# --------------------------------------------------------------------

def decode_string(s: str) -> str:
    """
    Decodes a string encoded as k[encoded_string], where the encoded_string
    inside the square brackets is repeated k times.
    """
    stack = []
    current_str, current_num = "", 0
    for ch in s:
        if ch.isdigit():
            current_num = (current_num * 10) + int(ch)
        elif ch == "[":
            stack.append((current_str, current_num))
            current_str, current_num = "", 0
        elif ch == "]":
            prev_str, prev_num = stack.pop()
            current_str = prev_str + current_str * prev_num
        else:
            current_str += ch
    return current_str
    # --------------------------------

# ====================================================================
# RUNNING TEST CASES
# ====================================================================

print("--- 1. Valid Parentheses ---")
print(f"()[]{{}}: {valid_parentheses('()[]{}')}")  # Expected: True
print(f"([{{}}]): {valid_parentheses('([{}]){}')}") # Expected: True
print(f"((({{}}): {valid_parentheses('((({})')}") # Expected: False
print(f"{{[}}]: {valid_parentheses('{[]}}')}")    # Expected: False
print(f"Empty: {valid_parentheses('')}")           # Expected: True

print("\n--- 2. Next Greater Element II (Circular) ---")
print(f"[1,2,1]: {next_greater_element_circular([1, 2, 1])}") # Expected: [2, -1, 2]
print(f"[5,4,3,2,1]: {next_greater_element_circular([5, 4, 3, 2, 1])}") # Expected: [-1, 5, 5, 5, 5]
print(f"[1,8,2,6,3]: {next_greater_element_circular([1, 8, 2, 6, 3])}") # Expected: [8, -1, 6, 8, 8]

print("\n--- 3. Largest Rectangle in Histogram ---")
print(f"[2,1,5,6,2,3]: {largest_rectangle_in_histogram([2, 1, 5, 6, 2, 3])}") # Expected: 10
print(f"[6,7,5,2,4,5,9,3]: {largest_rectangle_in_histogram([6, 7, 5, 2, 4, 5, 9, 3])}") # Expected: 16
print(f"[1]: {largest_rectangle_in_histogram([1])}")                             # Expected: 1
print(f"[0, 9]: {largest_rectangle_in_histogram([0, 9])}")                     # Expected: 9

print("\n--- 4. Implement Stack using Queues ---")
stack_q = MyStack()
stack_q.push(1)
stack_q.push(2)
print(f"Top: {stack_q.top()}")   # Expected: 2
print(f"Pop: {stack_q.pop()}")   # Expected: 2
print(f"Empty: {stack_q.empty()}") # Expected: False

print("\n--- 5. Implement Queue using Stacks ---")
queue_s = MyQueue()
queue_s.push(10)
queue_s.push(20)
print(f"Peek: {queue_s.peek()}") # Expected: 10
print(f"Pop: {queue_s.pop()}")   # Expected: 10
queue_s.push(30)
print(f"Pop: {queue_s.pop()}")   # Expected: 20

print("\n--- 6. Sliding Window Maximum ---")
print(f"[1,3,-1,-3,5,3,6,7], k=3: {sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)}") # Expected: [3, 3, 5, 5, 6, 7]
print(f"[1], k=1: {sliding_window_maximum([1], 1)}")                                         # Expected: [1]
print(f"[9,11], k=2: {sliding_window_maximum([9, 11], 2)}")                                 # Expected: [11]

print("\n--- 7. Evaluate Reverse Polish Notation ---")
rpn1 = ["2", "1", "+", "3", "*"]
rpn2 = ["4", "13", "5", "/", "+"]
rpn3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(f"{rpn1}: {eval_rpn(rpn1)}") # Expected: 9 ((2+1)*3)
print(f"{rpn2}: {eval_rpn(rpn2)}") # Expected: 6 (4 + (13/5))
print(f"{rpn3}: {eval_rpn(rpn3)}") # Expected: 22

print("\n--- 8. Decode String ---")
print(f"3[a]2[bc]: {decode_string('3[a]2[bc]')}")       # Expected: aaabcbc
print(f"3[a2[c]]: {decode_string('3[a2[c]]')}")         # Expected: accaccacc
print(f"2[abc]3[cd]ef: {decode_string('2[abc]3[cd]ef')}") # Expected: abcabccdcdedef
