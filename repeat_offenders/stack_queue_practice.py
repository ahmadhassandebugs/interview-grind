# ====================================================================
# STACK AND QUEUE PRACTICE SET (8 Core Problems)
# ====================================================================

# --------------------------------------------------------------------
# 1. Valid Parentheses (Basic Stack)
# --------------------------------------------------------------------

def valid_parentheses(s: str) -> bool:
    """
    Determines if an input string containing '(', ')', '{', '}', '[' and ']' 
    is valid. Brackets must close in the correct order.
    """
    pass
    # --------------------------------

# --------------------------------------------------------------------
# 2. Next Greater Element II
# --------------------------------------------------------------------

def next_greater_element_circular(nums: list[int]) -> list[int]:
    """
    Finds the next greater element for every element in a circular array.
    """
    pass
    # --------------------------------

# --------------------------------------------------------------------
# 3. Largest Rectangle in Histogram
# --------------------------------------------------------------------

def largest_rectangle_in_histogram(heights: list[int]) -> int:
    """
    Finds the area of the largest rectangle in a histogram.
    """
    pass
    # --------------------------------

# --------------------------------------------------------------------
# 4. Implement Stack using Queues
# --------------------------------------------------------------------

from collections import deque

class MyStack:
    """
    Implements a LIFO stack using only FIFO queues.
    fns: push, pop, top, empty
    """
    pass
    # --------------------------------

# --------------------------------------------------------------------
# 5. Implement Queue using Stacks
# --------------------------------------------------------------------

class MyQueue:
    """
    Implements a FIFO queue using only LIFO stacks.
    fns: push, pop, peek, empty
    """
    pass
    # --------------------------------

# --------------------------------------------------------------------
# 6. Sliding Window Maximum
# --------------------------------------------------------------------

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    """
    Finds the maximum element in every contiguous subarray (window) of size k.
    """
    pass
    # --------------------------------

# --------------------------------------------------------------------
# 7. Evaluate Reverse Polish Notation (RPN)
# --------------------------------------------------------------------

def eval_rpn(tokens: list[str]) -> int:
    """
    Evaluates the value of an arithmetic expression in Reverse Polish Notation.
    """
    pass
    # --------------------------------

# --------------------------------------------------------------------
# 8. Decode String
# --------------------------------------------------------------------

def decode_string(s: str) -> str:
    """
    Decodes a string encoded as k[encoded_string], where the encoded_string
    inside the square brackets is repeated k times.
    """
    pass
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
