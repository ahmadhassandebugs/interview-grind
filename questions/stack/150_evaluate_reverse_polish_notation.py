# keep adding numbers to stack
# if an operator is seen, get last two numbers,
#   evaluate them, and push the result onto stack
# there should be only one number in stack at the end
#   return that
# tokens = ["4","13","5","/","+"]
# TIPS: just store tokens as ints; verify returns and ops

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "/": lambda a,b: a/b,
            "*": lambda a,b: a*b
        }
        stack = []
        
        for tok in tokens:
            if tok not in operators.keys():
                stack.append(int(tok))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(operators[tok](a, b)))
        return stack.pop()
    
if __name__=="__main__":
    tc1 = ["4","13","5","/","+"]
    tc2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    sol = Solution()
    print(sol.evalRPN(tc1))
    print(sol.evalRPN(tc2))
