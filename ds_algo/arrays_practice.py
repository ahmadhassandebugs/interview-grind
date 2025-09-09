
import ctypes  # used for c arrays

class CustomList:
    
    def __init__(self):
        self.cap = 1
        self.n = 0
        self.container = self.__make_array(self.cap)
    
    def __make_array(self, cap):
        return (cap * ctypes.py_object)()
    
    def __resize_array(self, cap):
        new_container = self.__make_array(cap)
        for i in range(self.n):
            new_container[i] = self.container[i]
        self.container = new_container
        self.cap = cap
    
    def __str__(self):
        result = ""
        for i in range(self.n):
            result += f"{self.container[i]},"
        return f"capacity:{self.cap} size:{self.n} [{result}]"
    
    def append(self, x):
        self.container[self.n] = x
        self.n += 1
        if self.n == self.cap: self.__resize_array(self.cap * 2)
    
    def index(self, x):
        for i in range(self.n):
            if self.container[i] == x: return i
        return None
    
    def delete(self, x):
        pos = self.index(x)
        if not pos: return
        for i in range(pos, self.n - 1): self.container[i] = self.container[i + 1]
        self.n -= 1
        # make sure we maintain the property that there's space for at least one element without resizing
        # therefore, we use > instead of >= since we check for resizing in append after insertion
        if self.cap // 2 > self.n: self.__resize_array(self.cap // 2)

if __name__ == "__main__":
    my_list = CustomList()
    # Append elements
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    print("After appending 10, 20, 30:", my_list)
    # Find an element
    print("Index of 20:", my_list.index(20))
    print("Index of 15:", my_list.index(15))
    # Remove an element
    my_list.delete(20)
    print("After removing 20:", my_list)
    my_list.delete(15)
    print("After removing 15:", my_list)
    # Append elements
    my_list.append(40)
    print("After appending 40:", my_list)
