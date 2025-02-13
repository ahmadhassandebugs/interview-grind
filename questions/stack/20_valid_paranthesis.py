# s = "()[]{}" => True
# s = "(]" => False

# use a stack (LIFO) to validate
# if it's opening, add to the stack
# if it's closing, pop from the stack 
#   and see if there's a match. if no, false
# at the end, return true if stack is empty
# stack: deque => append, pop
# queue: deque => append, pop(0)
# TIP: always check if popping from empty

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = deque()
        for cha in s:
            if cha in mappings.keys():
                if not len(stack): return False
                last_cha = stack.pop()
                if last_cha != mappings[cha]: return False
            else:
                stack.append(cha)
        return not stack

if __name__=="__main__":
    pass    
