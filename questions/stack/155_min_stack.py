# stack: deque => append(x) at the end, pop() from the end
# [-2, 0, -3, 4]
# nothing below an element in stack changes so maintain
#   each elements min for below elements
# could also use my 2 stack approach (visualize it better)

# (value, min_below)
# [(-2, -2)]
# [(-2, -2), (0, -2)] container[-1][1] to see previous and compare
# [(-2, -2), (0, -2), (-3, -3)]
# [(-2, -2), (0, -2), (-3, -3), (4, -3)]

class MinStack:

    def __init__(self):
        self.container = []
        self.n = 0

    def push(self, val: int) -> None:
        if self.n == 0:
            min_val = val
        else:
            min_val = self.container[self.n-1][1]
            min_val = min(min_val, val)
        self.container.append((val, min_val))
        self.n += 1

    def pop(self) -> None:
        del self.container[self.n-1]
        self.n -= 1

    def top(self) -> int:
        return self.container[self.n-1][0]

    def getMin(self) -> int:
        return self.container[self.n-1][1]
    
if __name__=="__main__":
    pass
